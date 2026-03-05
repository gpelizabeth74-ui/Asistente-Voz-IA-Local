
# Asistente de Voz con IA Local (TinyLlama & Ollama)

Este proyecto implementa un asistente de voz inteligente que opera de manera 100% local. Utiliza modelos de lenguaje de última generación para procesar consultas de voz y responder de forma auditiva, sin depender de servicios en la nube.

## Funcionalidades

- Reconocimiento de Voz (STT): Captura de audio mediante micrófono y conversión a texto usando SpeechRecognition.
- Procesamiento de IA Local: Integración con Ollama para ejecutar el modelo TinyLlama localmente.
- Respuesta de Voz (TTS): Generación de respuestas auditivas automatizadas mediante pyttsx3.
- Interfaz de Usuario: Panel de control interactivo desarrollado en Streamlit.

## Tecnologías Utilizadas

- Lenguaje: Python 3.12
- IA Engine: Ollama (Modelo: TinyLlama)
- Librerías Clave:
  - streamlit: Interfaz web y gestión de estado.
  - speech_recognition: Procesamiento de señales de audio.
  - ollama: Conexión con el servidor de IA local.
  - pyttsx3: Motor de síntesis de voz.

## Estructura del Proyecto

- app.py: Lógica principal de la aplicación y flujo de datos.
- .gitignore: Protección de archivos temporales y entornos virtuales.
- respuesta.mp3: Archivo generado dinámicamente para la salida de voz.

## Autor

Elizabeth Guerrero
Estudiante de Ingeniería de Ciencia de Datos e IA - Senati
