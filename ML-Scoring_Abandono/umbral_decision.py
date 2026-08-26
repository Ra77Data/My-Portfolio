"""
Definición del UMBRAL DE DECISIÓN para activar planes de retención
===================================================================

Marco de decisión coste-beneficio:

  * p_i            = probabilidad de abandono predicha para el empleado i
  * impacto_i      = coste de rotación si el empleado i se va (impacto_abandono)
  * C_accion       = coste de la acción de retención por empleado
  * r              = efectividad de la acción (fracción de los que se irían
                     que realmente logramos retener)

  Beneficio esperado de intervenir sobre i = p_i * r * impacto_i
  Coste de intervenir sobre i              = C_accion

  => Intervenir si  p_i * r * impacto_i  >  C_accion
  => umbral individual:  p_i  >  C_accion / (r * impacto_i)

Aquí hacemos un barrido de un UMBRAL GLOBAL t sobre el conjunto de TEST
(fuera de muestra) y calculamos el ahorro esperado para distintas
combinaciones de (C_accion, r). Además mostramos el equivalente por empleado.
"""

import argparse

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

RANDOM_STATE = 42

parser = argparse.ArgumentParser(description="Umbral de decisión de retención")
parser.add_argument("--C", type=float, default=1000.0,
                    help="Coste de la acción de retención por empleado (USD)")
parser.add_argument("--r", type=float, default=0.4,
                    help="Efectividad de la acción de retención (0-1)")
args = parser.parse_args()

# ----------------------------------------------------------------------------
# 1. Carga y modelo (mismo pipeline, mejores params del paso anterior)
# ----------------------------------------------------------------------------
df = pd.read_csv("df_abandono.csv")
TARGET = "abandono"

CATEGORICAS = [
    "viajes", "departamento", "educacion", "carrera",
    "satisfaccion_entorno", "implicacion", "puesto",
    "satisfaccion_trabajo", "estado_civil", "horas_extra",
    "evaluacion", "satisfaccion_companeros",
]
NUMERICAS = [
    "edad", "distancia_casa", "nivel_laboral", "salario_mes",
    "num_empresas_anteriores", "incremento_salario_porc",
    "nivel_acciones", "anos_experiencia", "num_formaciones_ult_ano",
    "anos_compania", "anos_desde_ult_promocion", "anos_con_manager_actual",
]
FEATURES = CATEGORICAS + NUMERICAS

X = df[FEATURES]
y = df[TARGET]

train_x, test_x, train_y, test_y = train_test_split(
    X, y, test_size=0.30, random_state=RANDOM_STATE, stratify=y
)

pipe = Pipeline([
    ("prep", ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAS),
        ("num", StandardScaler(), NUMERICAS),
    ])),
    ("clf", LogisticRegression(C=0.5, max_iter=2000, solver="lbfgs", random_state=RANDOM_STATE)),
])
pipe.fit(train_x, train_y)

# scores fuera de muestra (test) para evaluar de forma honesta
test_scores = pipe.predict_proba(test_x)[:, 1]
test_impacto = test_x.join(df[["impacto_abandono", "abandono"]]).loc[test_x.index, "impacto_abandono"].values
test_y_arr = test_y.values

print(f"ROC AUC test      : {roc_auc_score(test_y, test_scores):.4f}")
print(f"PR-AUC test       : {average_precision_score(test_y, test_scores):.4f}")
n_leav = int(test_y_arr.sum())
print(f"Test: {len(test_y)} empleados, {n_leav} leavers "
      f"({test_y.mean()*100:.1f}%)\n")

# contexto económico
coste_rotacion_test = float(df.loc[test_x.index][df.loc[test_x.index, 'abandono'] == 1]['impacto_abandono'].sum())
print(f"Coste total de rotación en test (si todos los leavers se van): ${coste_rotacion_test:,.0f}")
print(f"  (techo de ahorro con r=1 y C=0)\n")

# ----------------------------------------------------------------------------
# 2. Barrido de umbral global
# ----------------------------------------------------------------------------
def barrido_umbral(scores, y, impacto, C_accion, r):
    """Devuelve DataFrame con métricas por umbral y el umbral óptimo."""
    filas = []
    for t in np.arange(0.05, 0.90, 0.01):
        flag = scores >= t
        n_flag = int(flag.sum())
        if n_flag == 0:
            continue
        leavers_capt = int((flag & (y == 1)).sum())
        precision = leavers_capt / n_flag
        # ahorro esperado (forward-looking, usa p_i)
        ahorro_esperado = (scores[flag] * r * impacto[flag]).sum() - n_flag * C_accion
        # ahorro realizado (retrospectivo, usa el abandono real)
        ahorro_realizado = (r * impacto[flag & (y == 1)].sum()) - n_flag * C_accion
        filas.append({
            "umbral": round(t, 2),
            "n_flag": n_flag,
            "leavers_capt": leavers_capt,
            "recall": leavers_capt / y.sum(),
            "precision": precision,
            "ahorro_esperado": ahorro_esperado,
            "ahorro_realizado": ahorro_realizado,
        })
    res = pd.DataFrame(filas)
    return res

print("=" * 100)
print("UMBRAL ÓPTIMO POR ESCENARIO (barrido sobre test)")
print("=" * 100)
print(f"{'C_acción':>9} {'r':>4} {'umbral*':>8} {'n_flag':>7} {'recall':>7} "
      f"{'precisión':>9} {'ahorro esperado':>16} {'ahorro realizado':>17}")
print("-" * 100)

escenarios = []
for C_accion in [1000, 3000, 5000]:
    for r in [0.3, 0.5]:
        res = barrido_umbral(test_scores, test_y_arr, test_impacto, C_accion, r)
        best = res.loc[res["ahorro_esperado"].idxmax()]
        escenarios.append((C_accion, r, best, res))
        print(f"{C_accion:>9,} {r:>4.1f} {best['umbral']:>8.2f} "
              f"{int(best['n_flag']):>7} {best['recall']:>7.2%} {best['precision']:>9.2%} "
              f"${best['ahorro_esperado']:>14,.0f} ${best['ahorro_realizado']:>15,.0f}")

print()
print("umbral* = umbral global que maximiza el ahorro esperado (forward-looking).")
print("recall  = % de leavers reales que el umbral captura (cobertura).")
print("precisión = % de los señalados que realmente se van.\n")

# ----------------------------------------------------------------------------
# 3. Detalle del escenario recomendado
# ----------------------------------------------------------------------------
C_REC, R_REC = args.C, args.r
res_rec = barrido_umbral(test_scores, test_y_arr, test_impacto, C_REC, R_REC)
best_rec = res_rec.loc[res_rec["ahorro_esperado"].idxmax()]

print("=" * 100)
print(f"DETALLE DEL ESCENARIO RECOMENDADO: C_acción=${C_REC:,} | r={R_REC}")
print("=" * 100)
print(res_rec[["umbral", "n_flag", "leavers_capt", "recall", "precision",
               "ahorro_esperado", "ahorro_realizado"]].head(25).to_string(index=False))

t_opt = best_rec["umbral"]
print(f"\n=> Umbral óptimo: {t_opt:.2f} "
      f"(señalar a {int(best_rec['n_flag'])} de {len(test_y)} empleados = "
      f"{best_rec['n_flag']/len(test_y):.1%} de la plantilla)")

# ----------------------------------------------------------------------------
# 4. Equivalente por empleado (umbral individual, teóricamente óptimo)
# ----------------------------------------------------------------------------
print("\n" + "=" * 100)
print("REFINAMIENTO: umbral individual (el óptimo real es por empleado)")
print("=" * 100)
print("Intervenir si  p_i  >  C_accion / (r * impacto_i)")
print(f"Con C=${C_REC:,} y r={R_REC}:  p_i  >  {C_REC/(R_REC):,.0f} / impacto_i")
print()
print("  impacto_i = $5,000  -> umbral = {:.0%}".format(C_REC/(R_REC*5000)))
print("  impacto_i = $10,000 -> umbral = {:.0%}".format(C_REC/(R_REC*10000)))
print("  impacto_i = $20,000 -> umbral = {:.0%}".format(C_REC/(R_REC*20000)))
print("  impacto_i = $30,000 -> umbral = {:.0%}".format(C_REC/(R_REC*30000)))
print("\n  Interpretación: cuanto más caro es reemplazar a un empleado (salario alto),")
print("  menor es el umbral: conviene intervenir antes (con menor probabilidad predicha).")

# ----------------------------------------------------------------------------
# 5. Aplicar el umbral a TODA la plantilla y guardar la lista de acción
# ----------------------------------------------------------------------------
df_full = pd.read_csv("df_abandono.csv")
df_full["scoring_abandono"] = pipe.predict_proba(df_full[FEATURES])[:, 1]
df_full["accion_retencion"] = np.where(df_full["scoring_abandono"] >= t_opt, "SÍ", "No")

n_accion = int((df_full["accion_retencion"] == "SÍ").sum())
print("\n" + "=" * 100)
print(f"PLAN DE RETENCIÓN SOBRE TODA LA PLANTILLA (umbral {t_opt:.2f}, "
      f"C=${C_REC:,}, r={R_REC})")
print("=" * 100)
print(f"Empleados a los que intervenir: {n_accion} / {len(df_full)} "
      f"({n_accion/len(df_full):.1%})")
presupuesto = n_accion * C_REC
print(f"Presupuesto en acciones: ${presupuesto:,}")

# estimación de ahorro esperado sobre toda la plantilla (forward-looking)
flag_full = df_full["accion_retencion"] == "SÍ"
ahorro_esperado_full = (df_full.loc[flag_full, "scoring_abandono"] *
                        R_REC * df_full.loc[flag_full, "impacto_abandono"]).sum() - presupuesto
print(f"Ahorro esperado (forward-looking): ${ahorro_esperado_full:,.0f}")

salida = "plan_retencion.xlsx"
df_full.to_excel(salida, index=False)
print(f"\nPlan guardado en: {salida}")
