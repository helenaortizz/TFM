# Predicción de Parto Pretérmino con Machine Learning

## Presentación del Proyecto

Este repositorio contiene el código y los recursos utilizados en el Trabajo de Fin de Máster (TFM) titulado:  
**"Desarrollo de un Modelo Predictivo de parto pretérmino utilizando Machine Learning: Aplicación en obstetricia desde la perspectiva de la Matrona"**  
Autora: **Helena Ortiz Rivero**  
Máster Universitario en Bioinformática y Bioestadística (UOC)

El objetivo es desarrollar un modelo de Machine Learning interpretable y aplicable en la práctica clínica para estimar el riesgo de parto pretérmino, empleando el conjunto de datos público **Natality Public Use File 2023** del CDC. Se ha creado también una **aplicación web interactiva** para su uso por matronas y profesionales sanitarios.

- Aplicación online: [Hugging Face Space](https://huggingface.co/spaces/helenaortizz/Calculadora_Riesgo_Parto_Pretermino)

---

## Requisitos y entorno

### Requisitos mínimos

Python ≥ 3.11

Instalación básica con `pip`:

```bash
pip install -r requirements.txt
```

### Opción 2: Crear entorno con Conda (opcional)

```bash
conda env create -f environment.yml
conda activate parto-pretérmino
```
---

## Bibliotecas utilizadas

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`
- `xgboost`
- `gradio`
- `joblib`

---

## Documentación

- [Dataset CDC Natality 2023](https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm)

---

## Licencia

Este proyecto está bajo derechos de autor de la autora (© Helena Ortiz Rivero). Requiere autorización para uso no académico. Reproducción o uso comercial prohibidos.

---
