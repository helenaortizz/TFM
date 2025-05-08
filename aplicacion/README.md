---
title: Calculadora Riesgo Parto Pretérmino
emoji: 👶
colorFrom: indigo
colorTo: yellow
sdk: gradio
sdk_version: 5.29.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Calculadora de riesgo de parto pretérmino.
---
# Calculadora de Riesgo de Parto Pretérmino

Esta aplicación tiene como objetivo la predicción del riesgo de parto pretérmino mediante el uso de un modelo de aprendizaje automático entrenado con el dataset público del CDC (Natality Public Use File 2023). Está pensada para ser usada con fines educativos, de investigación o como herramienta de ayuda a la toma de decisiones clínicas.

## Variables utilizadas

- Edad, raza y nivel educativo de la madre.  
- Orden de nacimiento y tiempo desde el último embarazo.  
- Inicio del cuidado prenatal (clasificado por trimestre).  
- Consumo de tabaco.  
- IMC pregestacional.  
- Antecedentes obstétricos: cesárea, parto prematuro previo.  
- Comorbilidades: diabetes, hipertensión.  
- Factores infecciosos y presentación fetal.  
- Embarazos múltiples.

## ¿Cómo se interpreta?

- El modelo estima la **probabilidad de parto pretérmino**.  
- Un umbral de decisión convierte esa probabilidad en una predicción binaria (`Alto` / `Bajo` riesgo).  
- Se incluye una visualización interactiva del riesgo porcentual.

> Esta herramienta no sustituye el juicio clínico. Su uso debe ser validado en entornos sanitarios por profesionales cualificados.