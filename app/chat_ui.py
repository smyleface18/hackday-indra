import datetime

import requests
import streamlit as st


# ---------- Configuración básica de la página ----------
st.set_page_config(
    page_title="Asistente Energético UPTC",
    page_icon="💡",
    layout="centered",
)

st.title("Asistente de Consumo Energético UPTC")
st.caption("Demo visual para IAMinds 2026 - Chat de consulta y recomendaciones")


# ---------- Inicializar historial de chat en sesión ----------
if "messages" not in st.session_state:
    # Cada mensaje será un dict: {"role": "user"/"assistant", "content": "texto"}
    st.session_state.messages = []


# ---------- Mostrar historial ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---------- Controles de contexto (sede y sector) ----------
col1, col2 = st.columns(2)

with col1:
    sede = st.selectbox(
        "Sede",
        ["Tunja", "Duitama", "Sogamoso", "Chiquinquirá"],
        index=0,
    )

with col2:
    sector = st.selectbox(
        "Sector",
        ["Comedores", "Salones", "Laboratorios", "Auditorios", "Oficinas"],
        index=0,
    )


# ---------- Entrada de usuario ----------
prompt = st.chat_input("Escribe tu pregunta sobre consumo energético...")

if prompt:
    # 1. Guardar mensaje del usuario en el historial
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Construir el JSON que enviarías al backend
    payload = {
        "user_id": "demo_user",
        "timestamp": datetime.datetime.now().isoformat(),
        "question": prompt,
        "context": {
            "sede": sede,
            "sector": sector,
        },
    }

    # Mostrar el JSON para ti y tu equipo
    with st.expander("Ver JSON enviado al backend"):
        st.json(payload)

    # 3. (Futuro) Llamar a la API del modelo
    # try:
    #     response = requests.post("http://localhost:8000/predict", json=payload)
    #     response.raise_for_status()
    #     result_json = response.json()
    #     answer = result_json.get("answer", "No se recibió una respuesta válida del modelo.")
    # except Exception as e:
    #     answer = f"Ocurrió un error al consultar el modelo: {e}"

    # Por ahora, simulamos la respuesta:
    answer = (
        f"Recibí tu pregunta: '{prompt}'.\n\n"
        f"Sede: {sede}, Sector: {sector}.\n\n"
        "Aquí iría la respuesta del modelo con recomendaciones de ahorro energético."
    )

    # 4. Guardar respuesta del asistente en el historial
    st.session_state.messages.append({"role": "assistant", "content": answer})

    # 5. Forzar refresco para que se vea el nuevo mensaje
    st.rerun()
