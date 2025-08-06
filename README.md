# Examen ML: Regresie Liniară pe Boston Housing

## Obiectiv

Antrenează și evaluează un model de regresie liniară care prezice prețul mediu al unei locuințe în funcție de mai mulți factori socio-economici și structurali.

---

## Fișiere disponibile

- `boston.csv`
- `examen_student.py` – fișierul pe care trebuie să îl completezi

---

## Ce trebuie să faci

1. Încarcă datele din `dataset/boston.csv`
2. Normalizează datele de intrare cu `StandardScaler`
3. Antrenează un model de regresie liniară (`LinearRegression`)
4. Evaluează performanța cu următoarele metrici:
   - R² (r2_score)
   - MSE (mean_squared_error)
   - RMSE (squared=False)
   - MAE (mean_absolute_error)
5. Selectează cele mai bune 5 coloane folosind `SelectKBest`
6. Antrenează un nou model doar cu aceste 5 coloane și compară scorurile
7. Antrenează și un model `Ridge(alpha=1.0)` și compară performanța
8. Creează două grafice:
   - Scatter: `RM` (nr. camere) vs `target`
   - Histogramă: distribuția erorii `(y_test - y_pred)`

---

##  Bonus (opțional)

- Încearcă și `Lasso(alpha=0.1)` și compară scorul
- Folosește `PolynomialFeatures` grad 2 pe 2-3 coloane

---

##  Livrabil

- Modifică și salvează tot codul în `code/examen_student.py`
- Comentează fiecare secțiune importantă
- La final, scrie o concluzie despre ce ai învățat și ce ai observat

---

Succes!
