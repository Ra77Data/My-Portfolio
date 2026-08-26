"""
Comparación de modelos de abandono de empleados
================================================

Misma representación de features (Pipeline + ColumnTransformer) y el MISMO
split train/test (random_state=42, stratify) para comparar de forma justa:

  1. Regresión Logística
  2. Random Forest
  3. Gradient Boosting

Para cada modelo se hace GridSearchCV (cv=5, scoring='roc_auc') y se reportan:
  - ROC AUC (CV, media)
  - ROC AUC (test)
  - PR-AUC / Average Precision (test)
"""

import time
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

RANDOM_STATE = 42
TEST_SIZE = 0.30

# ----------------------------------------------------------------------------
# 1. Carga y definición de features (idéntica a la versión corregida)
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
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)
print(f"Train: {train_x.shape[0]} | Test: {test_x.shape[0]} "
      f"(prevalencia test: {test_y.mean()*100:.2f}%)\n")

preprocesador = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAS),
        ("num", StandardScaler(), NUMERICAS),
    ]
)

# ----------------------------------------------------------------------------
# 2. Función de evaluación con GridSearchCV
# ----------------------------------------------------------------------------
def evaluar(nombre, estimador, param_grid):
    t0 = time.time()
    pipe = Pipeline([("prep", preprocesador), ("clf", estimador)])
    grid = GridSearchCV(
        pipe, param_grid, cv=5, scoring="roc_auc", n_jobs=-1, return_train_score=False
    )
    grid.fit(train_x, train_y)
    proba = grid.best_estimator_.predict_proba(test_x)[:, 1]
    roc = roc_auc_score(test_y, proba)
    pr = average_precision_score(test_y, proba)
    dt = time.time() - t0
    print(f"[{nombre}] {dt:.0f}s | mejores params: {grid.best_params_}")
    return {
        "modelo": nombre,
        "roc_cv": grid.best_score_,
        "roc_test": roc,
        "pr_test": pr,
        "params": grid.best_params_,
    }

# ----------------------------------------------------------------------------
# 3. Los tres modelos
# ----------------------------------------------------------------------------
resultados = []

# 3.1 Regresión Logística
resultados.append(evaluar(
    "Regresión Logística",
    LogisticRegression(max_iter=2000, solver="lbfgs", random_state=RANDOM_STATE),
    {
        "clf__C": [0.01, 0.1, 0.5, 1, 10],
        "clf__class_weight": [None, "balanced"],
    },
))

# 3.2 Random Forest
resultados.append(evaluar(
    "Random Forest",
    RandomForestClassifier(random_state=RANDOM_STATE, n_jobs=1),
    {
        "clf__n_estimators": [400],
        "clf__max_depth": [None, 8, 16, 24],
        "clf__min_samples_leaf": [1, 4],
        "clf__class_weight": [None, "balanced"],
    },
))

# 3.3 Gradient Boosting
resultados.append(evaluar(
    "Gradient Boosting",
    GradientBoostingClassifier(random_state=RANDOM_STATE),
    {
        "clf__n_estimators": [300],
        "clf__learning_rate": [0.03, 0.1],
        "clf__max_depth": [2, 3],
        "clf__subsample": [0.8, 1.0],
    },
))

# ----------------------------------------------------------------------------
# 4. Tabla comparativa
# ----------------------------------------------------------------------------
base = test_y.mean()
print("\n" + "=" * 74)
print("TABLA COMPARATIVA (mismo split, mismo pipeline)")
print("=" * 74)
print(f"{'Modelo':<22} {'ROC CV':>8} {'ROC test':>9} {'PR-AUC test':>12} {'lift vs base':>12}")
print("-" * 74)
for r in resultados:
    print(f"{r['modelo']:<22} {r['roc_cv']:>8.4f} {r['roc_test']:>9.4f} "
          f"{r['pr_test']:>12.4f} {r['pr_test']/base:>12.2f}x")
print("-" * 74)
print(f"{'PR-AUC baseline (prevalencia)':<22} {'':>8} {'':>9} {base:>12.4f}")
print()

mejor = max(resultados, key=lambda r: r["roc_test"])
print(f"Mejor modelo por ROC AUC en test: {mejor['modelo']} "
      f"({mejor['roc_test']:.4f})")
