{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;\f2\fnil\fcharset0 LucidaGrande;
}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import gradio as gr\
import pandas as pd\
import joblib\
\
# Carga del modelo\
file_path = 'mejor_modelo_xgboost.pkl'  \
modelo_xgb = joblib.load(file_path)\
\
# Mapeos originales del modelo\
age_map = \{\
    '<15 a\'f1os': '<15', '15-19 a\'f1os': '15-19', '20-24 a\'f1os': '20-24',\
    '25-29 a\'f1os': '25-29', '30-34 a\'f1os': '30-34', '35-39 a\'f1os': '35-39',\
    '40-44 a\'f1os': '40-44', '45-49 a\'f1os': '45-49', '50-54 a\'f1os': '50-54'\
\}\
race_map = \{\
    'Blanca': 'White', 'Negra': 'Black',\
    'Ind\'edgena Americano/Nativo de Alaska': 'AIAN',\
    'Asi\'e1tica': 'Asian', 'Isle\'f1a del Pac\'edfico': 'NHOPI',\
    'Multiracial': 'Multiracial'\
\}\
edu_map = \{\
    'Educaci\'f3n Primaria': '\uc0\u8804 8th',\
    'Educaci\'f3n Secundaria': '9-12_no_diploma',\
    'Bachillerato': 'HS_diploma',\
    'Estudios Pre-Universitarios': 'Some_college',\
    'Grado Superior': 'Assoc_degree',\
    'Graduado Universitario': 'Bachelor',\
    'M\'e1ster Universitario': 'Master',\
    'Doctorado': 'Doctorate',\
    'Desconocido': 'Unknown'\
\}\
bmi_map = \{\
    'Infrapeso': 'Underweight',\
    'Normal': 'Normal',\
    'Sobrepeso': 'Overweight',\
    'Obesidad I': 'Obesity_I',\
    'Obesidad II': 'Obesity_II',\
    'Obesidad Extrema': 'Extreme_Obesity',\
    'Desconocido': 'Unknown'\
\}\
presentation_map = \{\
    'Cef\'e1lica': 1,\
    'Pod\'e1lica': 2,\
    'Transversa': 3,\
    'Otros': 9\
\}\
plurality_map = \{\
    '\'danico': 1,\
    'Gemelar': 2,\
    'Trillizos': 3,\
    'Orden Superior': 4\
\}\
prenatal_map = \{\
    '1\'ba-3\'ba mes (1-12 semanas)': 1,\
    '4\'ba-6\'ba mes (13-24 semanas)': 2,\
    '7\'ba mes o m\'e1s (25+ semanas)': 3,\
    'Sin control prenatal': 4,\
    'Desconocido': 5\
\}\
\
# Funci\'f3n de predicci\'f3n de parto pret\'e9rmino\
def predecir_parto_pretermino(\
    age, race, education, birth_order, interval, prenatal_start, smoking,\
    bmi, diabetes, hypertension, preterm, cesarean, no_risk, no_infect,\
    chorio, presentation, plurality\
):\
    entrada = pd.DataFrame([\{\
        "Mother_Age": age_map[age],\
        "Mother_Race": race_map[race],\
        "Mother_Education": edu_map[education],\
        "Total_Birth_Order": birth_order,\
        "Interval_Last_Pregnancy": interval,\
        "Prenatal_Care_Start": prenatal_map[prenatal_start],\
        "Smoking_Before_Pregnancy": smoking,\
        "BMI": bmi_map[bmi],\
        "Gestational_Diabetes": binario(diabetes),\
        "Gestational_Hypertension": binario(hypertension),\
        "Previous_Preterm_Birth": binario(preterm),\
        "Previous_Cesarean": binario(cesarean),\
        "No_Risk_Factors": binario(no_risk),\
        "No_Infections": binario(no_infect),\
        "Chorioamnionitis": binario(chorio),\
        "Fetal_Presentation": presentation_map[presentation],\
        "Plurality": plurality_map[plurality]\
    \}])\
\
    proba = modelo_xgb.predict_proba(entrada)[0][1]\
    pred = modelo_xgb.predict(entrada)[0]\
    nivel = "ALTO" if pred == 1 else "BAJO"\
    emoji = "
\f1 \uc0\u55357 \u56628 
\f0 " if pred == 1 else "
\f1 \uc0\u55357 \u57314 
\f0 "\
    texto = f"\{emoji\} Riesgo estimado de parto pret\'e9rmino: \{proba:.1%\} 
\f2 \uc0\u8594 
\f0  \{nivel\}"\
\
    porcentaje = round(proba * 100)\
    return texto, porcentaje\
\
# Funci\'f3n auxiliar para respuestas binarias\
def binario(valor):\
    return 1 if valor == "S\'ed" else 0\
\
# Opciones para los controles\
age_opts = ['<15 a\'f1os', '15-19 a\'f1os', '20-24 a\'f1os', '25-29 a\'f1os', '30-34 a\'f1os', '35-39 a\'f1os', '40-44 a\'f1os', '45-49 a\'f1os', '50-54 a\'f1os']\
race_opts = ['Blanca', 'Negra', 'Ind\'edgena Americano/Nativo de Alaska', 'Asi\'e1tica', 'Isle\'f1a del Pac\'edfico', 'Multiracial']\
edu_opts = ['Educaci\'f3n Primaria', 'Educaci\'f3n Secundaria', 'Bachillerato', 'Estudios Pre-Universitarios', 'Grado Superior', 'Graduado Universitario', 'M\'e1ster Universitario', 'Doctorado', 'Desconocido']\
bmi_opts = ['Infrapeso', 'Normal', 'Sobrepeso', 'Obesidad I', 'Obesidad II', 'Obesidad Extrema', 'Desconocido']\
pres_opts = ['Cef\'e1lica', 'Pod\'e1lica', 'Transversa', 'Otros']\
plural_opts = ['\'danico', 'Gemelar', 'Trillizos', 'Orden Superior']\
birth_order_opts = list(range(1, 10))\
prenatal_opts = list(prenatal_map.keys())\
\
# Interfaz Gradio\
with gr.Blocks(theme=gr.themes.Base()) as demo:\
    gr.Markdown(\
        "<h2 style='text-align:center; color:#2c3e50;'>Calculadora de Riesgo de Parto Pret\'e9rmino</h2>"\
    )\
    with gr.Row():\
        age = gr.Dropdown(age_opts, label="Edad de la madre")\
        race = gr.Dropdown(race_opts, label="Raza")\
        education = gr.Dropdown(edu_opts, label="Nivel educativo")\
\
    with gr.Row():\
        birth_order = gr.Dropdown(birth_order_opts, label="N\'famero de embarazos (contando actual)")\
        interval = gr.Slider(0, 99, label="Meses desde el \'faltimo embarazo", step=1)\
        prenatal_start = gr.Dropdown(prenatal_opts, label="Inicio del cuidado prenatal (mes)")\
\
    with gr.Row():\
        smoking = gr.Slider(0, 20, label="Cigarrillos por d\'eda antes del embarazo", step=1)\
        bmi = gr.Dropdown(bmi_opts, label="\'cdndice de Masa Corporal (IMC)")\
        presentation = gr.Dropdown(pres_opts, label="Presentaci\'f3n fetal")\
\
    with gr.Row():\
        plurality = gr.Dropdown(plural_opts, label="N\'famero de fetos")\
        diabetes = gr.Radio(["No", "S\'ed"], label="\'bfDiabetes gestacional?")\
        hypertension = gr.Radio(["No", "S\'ed"], label="\'bfHipertensi\'f3n gestacional?")\
\
    with gr.Row():\
        preterm = gr.Radio(["No", "S\'ed"], label="\'bfParto prematuro previo?")\
        cesarean = gr.Radio(["No", "S\'ed"], label="\'bfCes\'e1rea previa?")\
        no_risk = gr.Radio(["No", "S\'ed"], label="\'bfSin factores de riesgo?")\
\
    with gr.Row():\
        no_infect = gr.Radio(["No", "S\'ed"], label="\'bfSin infecciones?")\
        chorio = gr.Radio(["No", "S\'ed"], label="\'bfCorioamnionitis?")\
\
    gr.Markdown("---")\
    btn = gr.Button("
\f1 \uc0\u55357 \u56590 
\f0  Calcular riesgo", variant="primary")\
    salida_texto = gr.Textbox(label="Resultado", lines=2, elem_classes="text-center")\
    barra_riesgo = gr.Slider(0, 100, step=1, label="Visualizaci\'f3n del riesgo (%)", interactive=False)\
\
    btn.click(fn=predecir_parto_pretermino,\
              inputs=[age, race, education, birth_order, interval, prenatal_start, smoking,\
                      bmi, diabetes, hypertension, preterm, cesarean, no_risk, no_infect,\
                      chorio, presentation, plurality],\
              outputs=[salida_texto, barra_riesgo])\
\
demo.launch()}