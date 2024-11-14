import streamlit as st
from groq import Groq

st.set_page_config(page_title="Astrología con Val", page_icon= "😜", layout="centered")
st.title("Aprende de Astrología para conocerte más")

nombre = st.text_input("Ingrese su signo")
if st.button("Buscar"):
    st.write(f'Hola {nombre} bienvenido/a a mi plataforma astrológica')



modelos = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']

def configurar_pagina():
    st.title("Las AstroLocas")
    st.sidebar.title("Tipo de Diseño")
    elegirModelo = st.sidebar.selectbox("Elegir un modelo", options= modelos, index= 0)
    return elegirModelo

# modelo = configurar_pagina ()

#CLASE 07
#Creacion de un usuario

def crear_usuario_groq():
    claveSecreta = st.secrets["CLAVE_API"]
    return Groq(api_key=claveSecreta)

def configurar_modelo(cliente,modelo,mensajeDeEntrada):
    return cliente.chat.completions.create(
        model=modelo,
        messages = [{"role":"user", "content":mensajeDeEntrada}],
        stream=True
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

#Clase 8 - Actualizar y mostrar historial, area del chat 

def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content":contenido, "avatar": avatar})

#Mostrar historial
def mostrar_historial():
    for mensaje in st.session_state.mensajes:
     with st.chat_message(mensaje["role"], avatar= mensaje["avatar"]):
         st.markdown(mensaje["content"])

#area_chat
def area_chat():
    contenedorDelChat = st.container(height=300, border=True)
    with contenedorDelChat:
        mostrar_historial()

#clase 9

def generar_respuesta(chat_completo):
    respuesta_completa = ""
    for frase in chat_completo:
        if frase.choices[0].delta.content:
            respuesta_completa += frase.choices[0].delta.content
            yield frase.choices[0].delta.content
    return respuesta_completa

def main():
    modelo = configurar_pagina()
    clienteUsuario = crear_usuario_groq()
    inicializar_estado() #Captura el mensaje del usuario
    area_chat()
    mensaje = st.chat_input("Escribí tu mensaje:")
    if mensaje:
        actualizar_historial("user",mensaje,"🧐")
        chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)
        if chat_completo:
            with st.chat_message("assistant"):
                respuesta_completa = st.write_stream(generar_respuesta(chat_completo))
                actualizar_historial("assistent", respuesta_completa,"🤖")
        st.rerun()


if __name__ == "__main__":
    main()





