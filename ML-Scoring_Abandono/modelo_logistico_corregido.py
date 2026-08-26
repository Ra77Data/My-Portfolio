"""
Modelo de abandono de empleados - REGRESIÓN LOGÍSTICA (versión corregida)
=======================================================================

Corrige 3 problemas del proyecto original:

1. BUG de escalado: el score se calculaba sobre datos SIN escalar con un
   modelo entrenado sobre datos escalados -> todos los scores daban 1.0.
   Ahora todo el preprocesamiento vive dentro de un Pipeline, de modo que
   es imposible olvidar el escalado (ni que se fugue entre train/test).

2. Features redundantes/derivadas: se EXCLUYEN 'salario_ano' (== salario_mes
   x 12) e 'impacto_abandono' (coste derivado del salario, no un driver de
   abandono).

3. Reproducibilidad: random_state fijado en el split y en el modelo.

Métricas reportadas: ROC AUC (test) y PR-AUC / Average Precision (test),
más el baseline (prevalencia de abandono) para interpretar el PR-AUC.
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

RANDOM_STATE = 42
TEST_SIZE = 0.30

# ----------------------------------------------------------------------------
# 1. Carga
# ----------------------------------------------------------------------------
df = pd.read_csv("df_abandono.csv")  # CSV separado por comas (default)
print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
print(f"Prevalencia de abandono: {df['abandono'].mean()*100:.2f}%\n")

TARGET = "abandono"
ID_COL = "id"

# Variables EXCLUIDAS a propósito: salario_ano (duplicado de salario_mes)
# e impacto_abandono (coste, no driver).
EXCLUIDAS = ["id", "salario_ano", "impacto_abandono"]

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
print(f"Features usadas: {len(FEATURES)} "
      f"({len(CATEGORICAS)} categóricas + {len(NUMERICAS)} numéricas)")
print(f"Excluidas: {EXCLUIDAS}\n")

# ----------------------------------------------------------------------------
# 2. Pipeline de preprocesamiento + modelo
# ----------------------------------------------------------------------------
preprocesador = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAS),
        ("num", StandardScaler(), NUMERICAS),
    ]
)

pipeline = Pipeline(
    steps=[
        ("prep", preprocesador),
        ("clf", LogisticRegression(max_iter=2000, solver="lbfgs", random_state=RANDOM_STATE)),
    ]
)

# ----------------------------------------------------------------------------
# 3. Split reproducible
# ----------------------------------------------------------------------------
X = df[FEATURES]
y = df[TARGET]

train_x, test_x, train_y, test_y = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)
print(f"Train: {train_x.shape[0]} | Test: {test_x.shape[0]} "
      f"(prevalencia test: {test_y.mean()*100:.2f}%)\n")

# ----------------------------------------------------------------------------
# 4. Optimización de hiperparámetros (GridSearchCV sobre el Pipeline)
# ----------------------------------------------------------------------------
param_grid = {
    "clf__C": [0.01, 0.1, 0.5, 1, 5, 10],
    "clf__class_weight": [None, "balanced"],
}

grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="roc_auc",
    n_jobs=-1,
    return_train_score=False,
)
grid.fit(train_x, train_y)

print("Mejores hiperparámetros:", grid.best_params_)
print(f"ROC AUC (CV, media 5-fold): {grid.best_score_:.4f}\n")

# ----------------------------------------------------------------------------
# 5. Evaluación sobre TEST (fuera de muestra)
# ----------------------------------------------------------------------------
best_model = grid.best_estimator_
proba_test = best_model.predict_proba(test_x)[:, 1]

roc_auc = roc_auc_score(test_y, proba_test)
pr_auc = average_precision_score(test_y, proba_test)
baseline_pr = test_y.mean()

print("=" * 60)
print("EVALUACIÓN SOBRE TEST (fuera de muestra)")
print("=" * 60)
print(f"ROC AUC          : {roc_auc:.4f}")
print(f"PR-AUC (avg prec): {pr_auc:.4f}")
print(f"PR-AUC baseline  : {baseline_pr:.4f}  (prevalencia, modelo aleatorio)")
print(f"Lift PR-AUC/base : {pr_auc/baseline_pr:.2f}x")
print()

# ----------------------------------------------------------------------------
# 6. Scoring sobre TODOS los empleados (ahora con el Pipeline correcto)
# ----------------------------------------------------------------------------
df = pd.read_csv("df_abandono.csv")  # recargar para partir del original
df["scoring_abandono"] = best_model.predict_proba(df[FEATURES])[:, 1]

scores = df["scoring_abandono"]
print("=" * 60)
print("DISTRIBUCIÓN DEL SCORE CORREGIDO")
print("=" * 60)
print(scores.describe().round(4).to_string())
print()
print(f"  min={scores.min():.4f}  max={scores.max():.4f}")
print(f"  filas con score == 1.0 : {(scores == 1.0).sum()} / {len(scores)}")
print(f"  filas con score  < 0.05: {(scores < 0.05).sum()} / {len(scores)}")

# Sanity check: los que se van deberían tener score medio más alto
leavers = df.loc[df[TARGET] == 1, "scoring_abandono"]
stayers = df.loc[df[TARGET] == 0, "scoring_abandono"]
print(f"\n  score medio de los que SÍ abandonan : {leavers.mean():.4f}")
print(f"  score medio de los que NO abandonan : {stayers.mean():.4f}")

# ----------------------------------------------------------------------------
# 7. Top 10 empleados en mayor riesgo
# ----------------------------------------------------------------------------
print("\nTop 10 empleados con mayor probabilidad de abandono:")
cols_top = ["id", "puesto", "departamento", "salario_mes",
            "horas_extra", "estado_civil", "abandono", "scoring_abandono"]
print(df.sort_values("scoring_abandono", ascending=False)[cols_top].head(10).to_string(index=False))

# ----------------------------------------------------------------------------
# 8. Guardar resultado
# ----------------------------------------------------------------------------
salida = "abandono_con_scoring_corregido.xlsx"
df.to_excel(salida, index=False)
print(f"\nResultado guardado en: {salida}")

# Verificación final explícita
assert scores.max() < 0.999999, "¡ALERTA: el score sigue saturado en 1.0!"
print("Verificación OK: el score ya NO da todo 1.0.")
