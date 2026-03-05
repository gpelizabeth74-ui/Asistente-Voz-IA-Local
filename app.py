import streamlit as st
import pyttsx3
import speech_recognition as sr
import ollama

st.title("Asistente-Voz-IA-Local")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# memoria de conversación
if "chat" not in st.session_state:
    st.session_state.chat = [
        {"role": "system", "content": "Eres un tutor experto en Ingeniería de Ciencia de Datos e IA de Senati. Ayudas a Elizabeth Guerrero con conceptos técnicos de Python, SQL y Machine Learning de forma clara y profesional."}
    ]

if st.button("Hablar"):

    with sr.Microphone() as source:
        st.write("Escuchando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")

        st.success("Dijiste:")
        st.write(text)

        # guardar mensaje del usuario
        st.session_state.chat.append({"role": "user", "content": text})

        # respuesta de IA
        response = ollama.chat(
            model="tinyllama",
            messages=st.session_state.chat
        )

        respuesta = response["message"]["content"]

        # guardar respuesta
        st.session_state.chat.append({"role": "assistant", "content": respuesta})

        st.write("Asistente:")
        st.write(respuesta)

        engine.save_to_file(respuesta, "respuesta.mp3")
        engine.runAndWait()

        audio_file = open("respuesta.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

    except:
        st.error("No entendí lo que dijiste")