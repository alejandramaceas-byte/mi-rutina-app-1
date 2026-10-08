
import streamlit as st
import json
from pathlib import Path
from datetime import date

# ============================================================
# CONFIGURACIÓN
# ============================================================
st.set_page_config(
    page_title="Mi Rutina de Hipertrofia",
    page_icon="💪",
    layout="wide"
)

HISTORIAL_FILE = Path("historial_pesos.json")

# ============================================================
# RUTINA PRINCIPAL
# ============================================================
rutina = {
    "Lunes: Pierna A 🍑": {
        "objetivo": "Énfasis Glúteo Máximo & Isquios",
        "ejercicios": [
            {
                "ejercicio": "Hip Thrust con Barra",
                "series": "4 x 8-10",
                "tempo": "2-2-1-0",
                "carga": "20-30 kg",
                "nota": "Fuerza pura de glúteo. Pausa de 2 s arriba apretando. Mentón al pecho."
                 "imagen": "Hip Thrust con Barra.png"
            },
            {
                "ejercicio": "Peso Muerto Rumano con Mancuernas",
                "series": "4 x 10-12",
                "tempo": "3-1-1-0",
                "carga": "12-14 kg / mano",
                "nota": "Empujar cadera hacia atrás. Estiramiento de isquio/glúteo."
            },
            {
                "ejercicio": "Step-Up en Banco",
                "series": "3 x 10-12 c/p",
                "tempo": "3-0-1-0",
                "carga": "8 kg / mano",
                "nota": "Torso inclinado 45°. Subir empujando el talón, sin impulso de la pierna trasera."
            },
            {
                "ejercicio": "Curl de Femoral Sentado",
                "series": "4 x 12-15",
                "tempo": "3-1-1-1",
                "carga": "50 kg",
                "nota": "Pelvis pegada al respaldo. Sostener 1 s la contracción."
            },
            {
                "ejercicio": "Abducción de Cadera en Máquina",
                "series": "3 x 15-20",
                "tempo": "2-2-1-0",
                "carga": "50 kg",
                "nota": "Tronco inclinado adelante. Pausa de 2 s al abrir."
            }
        ]
    },

    "Martes: Torso A 💪": {
        "objetivo": "Fuerza de Empuje y Tracción",
        "ejercicios": [
            {
                "ejercicio": "Press Inclinado con Mancuernas",
                "series": "4 x 8-10",
                "tempo": "3-1-1-0",
                "carga": "12 kg / mano",
                "nota": "Apertura de tórax. Bajada controlada de 3 s."
            },
            {
                "ejercicio": "Jalón al Pecho (Agarre Neutro)",
                "series": "4 x 8-10",
                "tempo": "3-1-1-1",
                "carga": "36 kg",
                "nota": "Tracción con los codos. Pausa de 1 s en la contracción."
            },
            {
                "ejercicio": "Press Militar Sentado con Mancuernas",
                "series": "3 x 10-12",
                "tempo": "2-1-1-0",
                "carga": "10 kg / mano",
                "nota": "Estabilidad de core, sin arquear la espalda baja."
            },
            {
                "ejercicio": "Remo en Polea Baja (Agarre Giratorio)",
                "series": "3 x 10-12",
                "tempo": "3-0-1-1",
                "carga": "32-36 kg",
                "nota": "Estirar escápulas al frente y apretar atrás en la contracción."
            },
            {
                "ejercicio": "Aperturas en Polea (Cruce)",
                "series": "3 x 12-15",
                "tempo": "2-1-1-1",
                "carga": "5 kg / lado",
                "nota": "Aislamiento pectoral, foco en el pico de contracción."
            }
        ]
    },

    "Miércoles: Pierna B 🦵": {
        "objetivo": "Énfasis Cuádriceps - Protocolo Rodilla",
        "ejercicios": [
            {
                "ejercicio": "Extensión de Cuádriceps",
                "series": "4 x 12-15",
                "tempo": "3-1-1-1",
                "carga": "23 kg",
                "nota": "Pre-exhaustación. Sostener 1 s arriba, bajar en 3 s. No bloquear."
            },
            {
                "ejercicio": "Sentadilla Trasera (Talones Elevados)",
                "series": "3 x 8-10",
                "tempo": "3-1-1-0",
                "carga": "7.5-10 kg / lado",
                "nota": "Disco delgado bajo talones. Bajar en 3 s sin rebote abajo."
            },
            {
                "ejercicio": "Prensa de Piernas",
                "series": "3 x 10-12",
                "tempo": "3-0-1-0",
                "carga": "30 kg / lado",
                "nota": "Pies a anchura de hombros en zona media-baja. Frenar antes del bloqueo."
            },
            {
                "ejercicio": "Zancadas Estáticas (Fijas)",
                "series": "3 x 12 c/p",
                "tempo": "2-1-1-0",
                "carga": "5-7.5 kg / mano",
                "nota": "Descenso vertical estricto para evitar desviaciones de la rótula."
            },
            {
                "ejercicio": "Elevación de Gemelos de Pie",
                "series": "4 x 15-20",
                "tempo": "2-2-1-1",
                "carga": "Peso corporal",
                "nota": "Pausa de 2 s abajo en estiramiento total."
            }
        ]
    },

    "Jueves: Torso B 💪": {
        "objetivo": "Brazos, Hombro Lateral & Core",
        "ejercicios": [
            {
                "ejercicio": "Elevaciones Laterales con Mancuernas",
                "series": "4 x 12-15",
                "tempo": "2-1-1-0",
                "carga": "6 kg / mano",
                "nota": "Codos ligeramente flexionados. Elevación en plano escapular."
            },
            {
                "ejercicio": "Press Francés con Barra Z",
                "series": "3 x 10-12",
                "tempo": "3-0-1-0",
                "carga": "15-20 kg",
                "nota": "Codos cerrados mirando al techo. Bajar barra hacia la coronilla."
            },
            {
                "ejercicio": "Curl Martillo con Mancuernas",
                "series": "3 x 10-12",
                "tempo": "3-0-1-0",
                "carga": "8 kg / mano",
                "nota": "Trabajo para braquial y antebrazo. Movimiento estricto."
            },
            {
                "ejercicio": "Extensiones de Tríceps en Polea",
                "series": "3 x 12-15",
                "tempo": "2-1-1-1",
                "carga": "23-27 kg",
                "nota": "Abrir la cuerda abajo y apretar el tríceps."
            },
            {
                "ejercicio": "Curl de Bíceps en Banco Inclinado",
                "series": "3 x 10-12",
                "tempo": "3-0-1-0",
                "carga": "8 kg / mano",
                "nota": "Estiramiento profundo de la cabeza larga del bíceps."
            },
            {
                "ejercicio": "Rueda Abdominal o Plancha Dinámica",
                "series": "3 x 10-12",
                "tempo": "2-1-1-0",
                "carga": "Peso corporal",
                "nota": "Movimiento desde la cadera y abdomen, no desde los hombros."
            }
        ]
    },

    "Viernes: Pierna C 🍑": {
        "objetivo": "Énfasis Glúteo Hipertrofia & Modelado",
        "ejercicios": [
            {
                "ejercicio": "Sentadilla Búlgara (Enfoque Glúteo)",
                "series": "4 x 10-12 c/p",
                "tempo": "3-1-1-0",
                "carga": "8-10 kg / mano",
                "nota": "Pie delantero alejado del banco, torso inclinado 45°. Llevar cadera atrás."
            },
            {
                "ejercicio": "Hip Thrust Bóster / Polea en Patada",
                "series": "3 x 12-15",
                "tempo": "2-1-1-1",
                "carga": "15-20 kg",
                "nota": "Aislamiento sin carga axial en columna. Apriete máximo de 1 s arriba."
            },
            {
                "ejercicio": "Prensa de Piernas (Pies Altos y Anchos)",
                "series": "3 x 10-12",
                "tempo": "3-0-1-0",
                "carga": "35-40 kg / lado",
                "nota": "Pies arriba para transferir el esfuerzo a glúteo e isquios."
            },
            {
                "ejercicio": "Patada de Glúteo en Polea",
                "series": "3 x 15",
                "tempo": "2-1-1-1",
                "carga": "10-15 kg",
                "nota": "Pierna ligeramente en diagonal (45°) para activar la fibra superior del glúteo."
            },
            {
                "ejercicio": "Hiperextensiones 45°",
                "series": "3 x 12-15",
                "tempo": "2-1-1-1",
                "carga": "Disco de 10 kg",
                "nota": "Encorvar espalda alta y subir enfocando el movimiento en glúteos."
            }
        ]
    }
}

# ============================================================
# FUNCIONES DE HISTORIAL
# ============================================================
def cargar_historial():
    if not HISTORIAL_FILE.exists():
        return []
    try:
        with open(HISTORIAL_FILE, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return datos if isinstance(datos, list) else []
    except Exception:
        return []

def guardar_historial(historial):
    with open(HISTORIAL_FILE, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)

def obtener_ejercicios():
    resultado = []
    for dia, info in rutina.items():
        for item in info["ejercicios"]:
            resultado.append({
                "dia": dia,
                "ejercicio": item["ejercicio"],
                "carga_referencia": item["carga"],
                "series": item["series"]
            })
    return resultado

def buscar_ultimo_registro(historial, ejercicio):
    registros = [r for r in historial if r["ejercicio"] == ejercicio]
    if not registros:
        return None
    return sorted(registros, key=lambda x: (x["semana"], x["fecha"]))[-1]

def calcular_peso_objetivo(ultimo, incremento, cumplio_rango):
    """Sugiere el peso de la siguiente semana.
    Solo aumenta la carga cuando se completó el rango de repeticiones.
    """
    if not ultimo or not cumplio_rango:
        return float(ultimo["peso"]) if ultimo else None
    if float(ultimo["peso"]) <= 0 or incremento <= 0:
        return float(ultimo["peso"])
    return round(float(ultimo["peso"]) + float(incremento), 2)

# ============================================================
# ESTADO
# ============================================================
if "historial" not in st.session_state:
    st.session_state.historial = cargar_historial()

# ============================================================
# ENCABEZADO
# ============================================================
st.title("💪 Mi Plan de Transformación Corporal")
st.markdown("### Hipertrofia Glútea & Salud Articular")
st.caption("Horario de entrenamiento: 7:00 AM - 9:00 AM")
st.markdown("---")

with st.expander("📈 ¿Cómo funcionará la progresión semanal?"):
    st.markdown("""
    1. Registramos el **peso realmente utilizado**.
    2. Indicamos si completaste **todas las series dentro del rango y con buena técnica**.
    3. Si cumpliste el rango, la app propone el incremento que seleccionaste.
    4. Si no cumpliste el rango, la app recomienda **mantener el mismo peso**.
    5. El historial conserva todas las semanas para poder ver la evolución de cada ejercicio.
    """)

# ============================================================
# PESTAÑAS
# ============================================================
tab_rutina, tab_registro, tab_progreso = st.tabs([
    "🏋️ Rutina",
    "📝 Registrar pesos",
    "📈 Progreso"
])

# ============================================================
# TAB 1 - RUTINA
# ============================================================
with tab_rutina:
    dia = st.selectbox(
        "📅 Selecciona el día de entrenamiento:",
        list(rutina.keys())
    )

    info_dia = rutina[dia]

    st.subheader(f"{dia}")
    st.info(f"🎯 **Objetivo:** {info_dia['objetivo']}")

    for i, item in enumerate(info_dia["ejercicios"], start=1):
        with st.expander(
            f"{i}. {item['ejercicio']}  |  {item['series']}"
        ):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**Series / repeticiones:** {item['series']}")
            with col2:
                st.write(f"**Tempo:** {item['tempo']}")
            with col3:
                st.write(f"**Carga de referencia:** {item['carga']}")

            st.write(f"📝 **Técnica:** {item['nota']}")

            ultimo = buscar_ultimo_registro(
                st.session_state.historial,
                item["ejercicio"]
            )
            if ultimo:
                st.success(
                    f"Último registro: **{ultimo['peso']} kg** "
                    f"(semana {ultimo['semana']})"
                )
            else:
                st.caption("Aún no hay un peso registrado para este ejercicio.")

# ============================================================
# TAB 2 - REGISTRO SEMANAL
# ============================================================
with tab_registro:
    st.subheader("📝 Registro semanal de pesos")
    st.write(
        "Registra el peso realmente utilizado. La aplicación lo comparará "
        "con la semana anterior para que podamos controlar la progresión."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        semana = st.number_input(
            "Semana",
            min_value=1,
            max_value=52,
            value=1,
            step=1
        )

    with col2:
        fecha_entrenamiento = st.date_input(
            "Fecha",
            value=date.today()
        )

    with col3:
        dia_registro = st.selectbox(
            "Día",
            list(rutina.keys()),
            key="dia_registro"
        )

    ejercicios_dia = rutina[dia_registro]["ejercicios"]

    ejercicio_registro = st.selectbox(
        "Ejercicio",
        [x["ejercicio"] for x in ejercicios_dia],
        key="ejercicio_registro"
    )

    ejercicio_info = next(
        x for x in ejercicios_dia
        if x["ejercicio"] == ejercicio_registro
    )

    ultimo = buscar_ultimo_registro(
        st.session_state.historial,
        ejercicio_registro
    )

    if ultimo:
        st.info(
            f"📌 Último peso registrado: **{ultimo['peso']} kg** "
            f"en la semana **{ultimo['semana']}**."
        )

    col1, col2 = st.columns(2)

    with col1:
        peso = st.number_input(
            "Peso utilizado (kg)",
            min_value=0.0,
            max_value=500.0,
            value=float(ultimo["peso"]) if ultimo else 0.0,
            step=0.5,
            format="%.1f"
        )

    with col2:
        reps_realizadas = st.text_input(
            "Repeticiones realizadas",
            value=ejercicio_info["series"]
        )

    cumplio_rango = st.checkbox(
        "✅ Completé el rango de repeticiones con buena técnica",
        value=False,
        help="Solo si completaste todas las series dentro del rango indicado y con buena técnica."
    )

    incremento_planeado = st.selectbox(
        "Incremento sugerido para la próxima semana",
        [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 5.0],
        index=3 if "Mancuernas" in ejercicio_registro else 4,
        format_func=lambda x: "Mantener peso" if x == 0 else f"+{x:g} kg"
    )

    notas = st.text_area(
        "Notas de la sesión",
        placeholder="Ej.: completé todas las series, se sintió pesado, buena técnica, molestias, etc."
    )

    peso_objetivo = calcular_peso_objetivo(
        ultimo,
        incremento_planeado,
        cumplio_rango
    )

    if peso_objetivo is not None:
        if cumplio_rango and ultimo and incremento_planeado > 0:
            st.success(
                f"🎯 **Peso objetivo para la próxima semana: {peso_objetivo:g} kg** "
                f"(actual {peso:.1f} kg + {incremento_planeado:g} kg)"
            )
        elif ultimo:
            st.info(
                f"🎯 **Sugerencia: mantener {ultimo['peso']:g} kg** la próxima semana "
                f"y buscar completar el rango con buena técnica."
            )

    if st.button("💾 Guardar registro de esta semana", type="primary"):
        registro = {
            "semana": int(semana),
            "fecha": fecha_entrenamiento.isoformat(),
            "dia": dia_registro,
            "ejercicio": ejercicio_registro,
            "peso": float(peso),
            "repeticiones": reps_realizadas,
            "cumplio_rango": bool(cumplio_rango),
            "incremento_planeado": float(incremento_planeado),
            "peso_objetivo_siguiente": peso_objetivo,
            "notas": notas
        }

        # Si ya existe un registro del mismo ejercicio y semana, lo reemplaza.
        st.session_state.historial = [
            r for r in st.session_state.historial
            if not (
                r["ejercicio"] == ejercicio_registro
                and int(r["semana"]) == int(semana)
            )
        ]

        st.session_state.historial.append(registro)
        st.session_state.historial.sort(
            key=lambda x: (int(x["semana"]), x["fecha"])
        )
        guardar_historial(st.session_state.historial)

        st.success(
            f"✅ Guardado: {ejercicio_registro} — "
            f"{peso:.1f} kg — Semana {int(semana)}"
        )

        if ultimo:
            diferencia = float(peso) - float(ultimo["peso"])
            if diferencia > 0:
                st.success(f"📈 Aumento respecto al último registro: +{diferencia:.1f} kg")
            elif diferencia < 0:
                st.warning(f"📉 Disminución respecto al último registro: {diferencia:.1f} kg")
            else:
                st.info("➡️ Mismo peso que el último registro.")

# ============================================================
# TAB 3 - PROGRESO
# ============================================================
with tab_progreso:
    st.subheader("📈 Seguimiento de progresión")

    if not st.session_state.historial:
        st.info("Todavía no hay registros. Comienza guardando el peso de la primera semana.")
    else:
        ejercicios_registrados = sorted(
            set(r["ejercicio"] for r in st.session_state.historial)
        )

        ejercicio_grafica = st.selectbox(
            "Selecciona el ejercicio para ver su evolución:",
            ejercicios_registrados
        )

        registros_ejercicio = sorted(
            [
                r for r in st.session_state.historial
                if r["ejercicio"] == ejercicio_grafica
            ],
            key=lambda x: int(x["semana"])
        )

        if registros_ejercicio:
            ultimo_registro = registros_ejercicio[-1]
            objetivo = ultimo_registro.get("peso_objetivo_siguiente")

            if objetivo is not None:
                st.success(
                    f"🎯 **Próximo objetivo para {ejercicio_grafica}: {float(objetivo):g} kg**"
                )

            import pandas as pd

            datos = pd.DataFrame([
                {
                    "Semana": int(r["semana"]),
                    "Peso (kg)": float(r["peso"])
                }
                for r in registros_ejercicio
            ])

            st.line_chart(
                datos.set_index("Semana"),
                y="Peso (kg)"
            )

            st.dataframe(
                datos,
                use_container_width=True,
                hide_index=True
            )

            if len(registros_ejercicio) >= 2:
                primero = float(registros_ejercicio[0]["peso"])
                ultimo_peso = float(registros_ejercicio[-1]["peso"])
                diferencia = ultimo_peso - primero

                if diferencia > 0:
                    st.success(
                        f"📈 Progreso acumulado: **+{diferencia:.1f} kg** "
                        f"desde la semana {registros_ejercicio[0]['semana']}."
                    )
                elif diferencia < 0:
                    st.warning(
                        f"📉 Variación acumulada: **{diferencia:.1f} kg**."
                    )
                else:
                    st.info("➡️ El peso se mantiene igual desde el primer registro.")

        st.markdown("---")
        st.subheader("📋 Historial completo")

        import pandas as pd

        historial_df = pd.DataFrame(st.session_state.historial)

        if not historial_df.empty:
            historial_df = historial_df.sort_values(
                ["semana", "dia", "ejercicio"]
            )

            st.dataframe(
                historial_df,
                use_container_width=True,
                hide_index=True
            )

            csv = historial_df.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                "⬇️ Descargar historial en Excel/CSV",
                data=csv,
                file_name="historial_entrenamiento.csv",
                mime="text/csv"
            )

# ============================================================
# PIE
# ============================================================
st.markdown("---")
st.caption(
    "💡 La idea es registrar el peso real de cada semana y utilizar el historial "
    "para decidir los siguientes incrementos, sin perder los registros anteriores."
)
