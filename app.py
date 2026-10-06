import streamlit as st
import json
import os

st.set_page_config(page_title="Mi Rutina App", page_icon="💪", layout="wide")

DATA_FILE = "rutina_progreso.json"

# Estructura base por defecto de los 5 dias
def_rutina = {
    "Lunes: Tren Inferior (Cuadriceps / Gluteos)": [
        {
            "ejercicio": "Prensa Inclinada",
            "musculo": "Cuadriceps",
            "series": 4,
            "repeticiones": "8-10",
            "peso_anterior_kg": 160.0,
            "peso_actual_kg": 160.0,
            "reemplazo_activo": "(Mantener actual)",
            "imagen": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400",
            "alternativas": ["Sentadilla Hack", "Zancadas Bulgaras", "Extension de Cuadriceps"]
        },
        {
            "ejercicio": "Sentadilla Goblet",
            "musculo": "Cuadriceps / Core",
            "series": 3,
            "repeticiones": "10-12",
            "peso_anterior_kg": 16.0,
            "peso_actual_kg": 16.0,
            "reemplazo_activo": "(Mantener actual)",
            "imagen": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400",
            "alternativas": ["Sentadilla Libre", "Prensa Horizontal"]
        }
    ],
    "Martes: Espalda y Hombros": [
        {
            "ejercicio": "Jalon al Pecho",
            "musculo": "Espalda (Dorsales)",
            "series": 4,
            "repeticiones": "10-12",
            "peso_anterior_kg": 35.0,
            "peso_actual_kg": 35.0,
            "reemplazo_activo": "(Mantener actual)",
            "imagen": "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=400",
            "alternativas": ["Dominadas asistidas", "Remo en polea baja"]
        }
    ],
    "Miercoles: Cadena Posterior (Gluteos / Isquios)": [
        {
            "ejercicio": "Hip Thrust",
            "musculo": "Gluteos",
            "series": 4,
            "repeticiones": "8-10",
            "peso_anterior_kg": 80.0,
            "peso_actual_kg": 80.0,
            "reemplazo_activo": "(Mantener actual)",
            "imagen": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400",
            "alternativas": ["Puente de gluteos", "Peso muerto rumano"]
        }
    ],
    "Jueves: Torso Superior (Pecho y Biceps)": [
        {
            "ejercicio": "Press de Banca con Mancuernas",
            "musculo": "Pecho",
            "series": 4,
            "repeticiones": "8-10",
            "peso_anterior_kg": 12.0,
            "peso_actual_kg": 12.0,
            "reemplazo_activo": "(Mantener actual)",
            "imagen": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400",
            "alternativas": ["Flexiones", "Press en maquina"]
        }
    ],
    "Viernes: Gluteos, Core y Triceps": [
        {
            "ejercicio": "Patada de Gluteo en Polea",
            "musculo": "Gluteos",
            "series": 4,
            "repeticiones": "12-15",
            "peso_anterior_kg": 15.0,
            "peso_actual_kg": 15.0,
            "reemplazo_activo": "(Mantener actual)",
            "imagen": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=400",
            "alternativas": ["Sentadilla Bulgara", "Hip Thrust"]
        }
    ]
}

# Cargar o inicializar datos persistentes
def cargar_datos():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return def_rutina
    return def_rutina

def guardar_datos(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

rutina_data = cargar_datos()

# Sidebar de perfil
st.sidebar.header("Perfil de Usuario")
nombre = st.sidebar.text_input("Nombre", "Ingeniera")
edad = st.sidebar.number_input("Edad", value=45)
peso_actual_user = st.sidebar.number_input("Peso Corporal (kg)", value=71.0)
meta = st.sidebar.text_input("Meta", "Hipertrofia en deficit calorico")

st.title("Sistema de Entrenamiento Personalizado")
st.write("Control de cargas, series, repeticiones y persistencia local.")

dia_seleccionado = st.selectbox("Selecciona el dia de entrenamiento:", list(rutina_data.keys()))
st.subheader(f"Rutina para: {dia_seleccionado}")

modificado = False

for i, item in enumerate(rutina_data[dia_seleccionado]):
    col1, col2, col3 = st.columns([1, 2, 2])
    
    with col1:
        st.image(item["imagen"], width=140, caption=item["ejercicio"])
        
    with col2:
        st.markdown(f"### {item['ejercicio']}")
        st.write(f"**Musculo principal:** {item['musculo']}")
        st.write(f"**Objetivo:** {item['series']} series x {item['repeticiones']} reps")
        
        # Opciones de reemplazo
        opciones_reemplazo = ["(Mantener actual)"] + item["alternativas"]
        idx_actual = 0
        if item["reemplazo_activo"] in opciones_reemplazo:
            idx_actual = opciones_reemplazo.index(item["reemplazo_activo"])
            
        reemplazo = st.selectbox("Reemplazar ejercicio", opciones_reemplazo, index=idx_actual, key=f"reemplazo_{i}_{dia_seleccionado}")
        
        if reemplazo != item["reemplazo_activo"]:
            item["reemplazo_activo"] = reemplazo
            modificado = True
            
        if item["reemplazo_activo"] != "(Mantener actual)":
            st.warning(f"En uso: {item['reemplazo_activo']}")

    with col3:
        st.markdown("#### Progresion de Carga")
        st.text(f"Peso anterior: {item['peso_anterior_kg']} kg")
        
        nuevo_peso = st.number_input("Peso actual (kg)", value=float(item['peso_actual_kg']), key=f"peso_{i}_{dia_seleccionado}")
        
        if nuevo_peso != item['peso_actual_kg']:
            item['peso_anterior_kg'] = item['peso_actual_kg']
            item['peso_actual_kg'] = nuevo_peso
            modificado = True

        if item['peso_actual_kg'] > item['peso_anterior_kg']:
            st.success(f"¡Subiste de peso!")
            
    st.divider()

if modificado:
    guardar_datos(rutina_data)
    st.toast("¡Cambios guardados con exito en la base de datos local!", icon="💾")