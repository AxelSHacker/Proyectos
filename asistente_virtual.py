import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchafr nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    #almacenar el reconocedor en variable

    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion
        print("Ya puedes hablar")

        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio, language="es-es")

            #prueba de que pudo ingresar
            print("Dijiste: "+ pedido)

            #devolver pedido
            return pedido
        #en caso de no reconocer el audio
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print("ups, no hay servicio")

            #devolver error
            return "Sigo Esperando"

        #en caso de no devolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups, no entendi")

            # devolver error
            return "Sigo Esperando"

        #error inesperado
        except:
            # prueba de que no comprendio el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "Sigo Esperando"

#funcion para que el asistente sea escuchado
def hablar(mensaje):

    #encender el motor de pyttsx3
    engine = pyttsx3.init()

    #pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()

#informar dia de la semana
def pedir_dia():

    #crear variables con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #variable dia de la semana
    dia_semana= dia.weekday()
    print(dia_semana)

    #diccionario con nombres
    calendario = {0: "Lunes",1: "Martes",2: "Miercoles",3: "Jueves",4: "Viernes", 5: "Sabado",6: "Domingo"}
    hablar(f"Hoy es{calendario[dia_semana]}")

#informar de la hora
def pedir_hora():

    #variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son {hora.hour} hora con {hora.minute} minutos y {hora.second} segundos"

    #decir la hora
    hablar(hora)

#funcion saludo inicial
def saludo_inicial():

    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buenos dias"
    else:
        momento = "Buenas tardes"

    #decir el saludo
    hablar(f"{momento}, soy Patata, en que te puedo ayudar")

#Funcion central del asistente
def pedir_cosas():

    #activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop central
    while comenzar:

        #activar el micro y guardar el pedido
        pedido = transformar_audio_en_texto().lower()

        if "abrir youtube" in pedido:
            hablar("Con gusto, voy a abrir youtube")
            webbrowser.open("https://www.youtube.com")
        elif "abrir navegador" in pedido:
            hablar("Me pongo a ello")
            webbrowser.open("https://www.google.com")
            continue
        elif "Que dia es hoy" in pedido:
            pedir_dia()
            continue
        elif"Que hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando en wikipedia, espere")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("En wikipedia pone:")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("Me pongo a ello")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("a ver que tal suena")
            pywhatkit.playonyt(pedido)
            continue
        elif "chiste" in pedido:
            hablar(pyjokes.get_joke("es"))
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple":"APPL",
                       "amazon":"AMZN",
                       "google":"GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"El precion de {accion} es de {precio_actual}")
                continue
            except:
                hablar("Perdon pero no la he econtrado")
        elif "hasta luego" in pedido:
            hablar("Hasta luego cabesa")
            break

pedir_cosas()