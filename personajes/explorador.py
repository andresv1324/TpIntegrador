import streamlit as st

def textoCruce():
    #CAMINO TUNEL
    if st.session_state.destino == "Tunel" and st.session_state.cruce =="Trepar tunel":
        if st.session_state.mostrarTextoComo==1:
            st.write("Entras al túnel y a tu derecha visualizas una escalera que recorre el túnel hasta llegar al techo y sigue por dentro, recto, perfecto para cruzar el túnel sin depender de nada, crees que es arriesgado ya que tendrás que estar en posición vertical pero no sabes por cuánto tiempo, sin embargo sigues por esa opción a pesar de tus dudas, empiezas tu camino y el ambiente se vuelve pesado")
            st.write("hay ruidos pero no logras visualizar que es lo que escuchas, de repente ves algo enfrente tuyo, crees que es una rata asquerosa, pero medianamente se va acercando empiezas a ver con claridad extrañamente este ser brilla levemente…")

            if st.button("Continuar", key="textoPicaroTunTrepar"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("¡Es una ardilla! ¿una ardilla? ¿por acá?, se te hace extraño pero ella se acerca y te ve con curiosidad, te indica que la sigas, claramente por el mismo camino que vos estabas ya recorriendo, pero de repente te empiezas a sentir mejor, el ambiente se aligera y tu velocidad se normaliza, ves tu próximo desafío en frente tuyo…")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            if st.button("Continuar", key="textoPicaroTunTrepar2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()
    elif st.session_state.destino == "Tunel" and st.session_state.cruce =="Cruzar el tunel":
        if st.session_state.mostrarTextoComo==1:
            st.write("Eres un pícaro, maestro de las trampas y la mentira, analizas tu trayecto, lo poco que se ve, pero mejor precavido que distraído… al hacer tu análisis notas ciertas características, piedras sobresalidas más de lo debido, pequeños huecos extrañamente bien posicionados en las paredes y demás")
            st.write("Ya has visto millones de veces este tipo de trampas, así que decides avanzar, esquivas una, esquivas otra, así hasta llegar a mitad de camino, logras ver la salida pero es difícil ver e identificar qué hay más adelante")
            if st.button("Continuar", key="textoPicaroTunCruzar"):
                st.session_state.mostrarTextoComo = 2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("un tintineo se acerca de lo más oscuro, ves pequeños destellos dorados pero se desvanecen rápidamente revelando la figura de un gato tricolor, este se dirige hacia ti, pasando entre tus piernas hace iluminar tus pasos y el camino siguiente, decides seguirlo… logras llegar al final")
            st.write("¡Felicidades! tienes un nuevo amigo de aventuras")
            if st.button("Continuar", key="textoPicaroTunCruzar2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    #CAMINO DEL MONTAÑA
    elif st.session_state.destino =="Montaña Con Laberintos" and st.session_state.cruce =="Trepar montaña":
        if st.session_state.mostrarTextoComo==1:
            st.write("Decides escalar un árbol y saltar de punta en punta, confías en tu agilidad y sigilo aprendido hace años y crees poder cruzar la montaña finalmente, el día transcurre y sin comida ni agua te agotas, tus manos se empiezan a resbalar de los troncos y tu agarre ya no es seguro, pero sigues. La tarde empieza a caer, y con ella el viento aumenta")
            st.write("te sientes en peligro pero sigues por testarudo, te preparas para saltar a un árbol que está a una distancia más larga, pero al momento de brincar un viento fuerte te empuja y te hace caer al suelo, de suerte sigues vivo, pero te sientes débil así que decides descansar y comer encuentres lo que encuentres, te recuestas sobre un árbol y miras a tu alrededor, no escuchas nada y te relajas, pero de pronto…")

            if st.button("Continuar", key="textoPicaroMonTrepar"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Un tintineo se acerca de lo más oscuro, ves pequeños destellos dorados pero se desvanecen rápidamente revelando la figura de un gato tricolor, este se dirige hacia ti, pasando entre tus piernas hace iluminar tus pasos y el camino siguiente, decides seguirlo… logras llegar al final")
            st.write("Felicidades! tienes un nuevo amigo de aventuras")
            if st.button("Continuar", key="textoPicaroMonTrepar2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    elif st.session_state.destino =="Montaña Con Laberintos" and st.session_state.cruce =="Cruzar La Montaña":
        if st.session_state.mostrarTextoComo==1:
            st.write("Decides que tu mejor opción es enfrentarte al riesgo y te metes de lleno al bosque frente a tí, empiezas tu camino pero te das cuenta que no hay más que vueltas y vueltas, ruidos extraños te acechan y voces imaginarias empiezan a estar en tu cabeza, te empiezas a volver loco y la noche cae de repente, te sientes perdido y asustado, crack")
            st.write("Un ruido te saca de tus pensamientos y sientes que algo se aproxima a ti con una velocidad diferente, te empiezas a acelerar pero la curiosidad puede más que tu ingenio, te quedas quieto observando si logras ver algo y lo máximo que llegas a ver son destellos dorados y unas patitas aproximándose, enfocas tu vista y logras ver que.")
            if st.button("Continuar", key="textoPicaroMonCruzar"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("¡Es una ardilla! ¿una ardilla? ¿por acá?, se te hace extraño pero ella se acerca y te ve con curiosidad, te indica que la sigas, claramente por el mismo camino que vos estabas ya recorriendo, pero de repente te empiezas a sentir mejor, el ambiente se aligera y tu velocidad se normaliza, ves tu próximo desafío en frente tuyo ")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            if st.button("Continuar", key="textoPicaroMonCruzar2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()


def informacion_explorador():
    st.text(
        "Eres un pícaro explorador, en busca de su camino… engañaste a gente, "
        "mentiste y robaste para sobrevivir, pero jamás te descubrieron. Eres ágil "
        "y con encantos de envidiar; convences hasta a la persona más desconfiada "
        "del planeta. Posees una fuerza mental increíble y una supervivencia "
        "irrevocable. En tu cotidianidad tus pensamientos dicen: “entre más "
        "obstáculos superados, más sabiduría”. Obviamente eres un aprendiz de "
        "la vida misma. Un día viste en un cartel tu siguiente obstáculo: salir "
        "de una mazmorra, y pensaste… ¿por qué no?"
    )

    if st.button("Continuar", key="continuar_historia_explorador"):
        st.session_state.informacion = 0
        st.rerun()

#OPCION DE CAMINO
def elegir_camino_explorador():
    st.subheader(
        "Hiciste la elección de personaje, tu rumbo ha comenzado, elige tu camino"
    )

    destino = st.radio(
        "¿A dónde quieres ir?",
        ["Tunel","Montaña Con Laberintos"],
        key="destino_explorador"
    )

    if st.button("Continuar", key="continuar_camino_explorador"):
        st.session_state.destino = destino
        st.session_state.etapa = 3
        st.rerun()

#OPCION DE CRUZAR PRIMER CAMINO
def etapa_3_explorador():
    if st.session_state.destino == "Tunel":
        st.subheader(
            " te encuentras con un túnel, bastante gigante para tu tamaño, piensas y piensas, solo se te ocurren dos formas de cruzar…"
            "¿Cuál eliges?"
        )
        cruce = st.radio(
            "",
            ["Trepar tunel", "Cruzar el tunel"],
            key="cruce_explorador_tunel"
        )

    elif st.session_state.destino == "Montaña Con Laberintos":
        st.subheader(
            "Inicias tu recorrido por la montaña. La inmensidad del paisaje te abruma por un instante, pero rápidamente recuperas la calma. Recuerdas que eres capaz de superar cualquier desafío y que nada podrá detenerte."
            "¿Cuál eliges?"
        )
        cruce = st.radio(
            "",
            ["Trepar montaña", "Cruzar La Montaña"],
            key="cruce_explorador_montana"
        )
    else:
        return

    if st.button("Continuar", key="continuar_cruce_explorador"):
        st.session_state.cruce = cruce
        st.session_state.etapa = 4
        st.rerun()


def etapa_4_explorador():

    if st.session_state.cruce in [
        "Trepar tunel",
        "Cruzar La Montaña"
    ]:
        st.write("Encuentras una Ardilla mascota en el camino.")
        st.session_state.mascota = "Ardilla"

    elif st.session_state.cruce in [
        "Cruzar el tunel",
        "Trepar montaña"
    ]:
        st.write("Encontraste un Gato Tricolor mascota en el camino.")
        st.session_state.mascota = "Gato Tricolor"

    if st.button("Continuar", key="continuar_mascota_explorador"):
        st.session_state.etapa = "MAZMORRA"
        st.rerun()


def etapa_5_explorador():
    if st.session_state.mascota == "Ardilla":
        st.write("llegas a la entrada de la mazmorra, te encuentras con dos caminos, uno arriba del otro, el de abajo irradia un olor nauseabundo y asqueroso, pero no logras llegar a ver nada más, del pasillo de arriba no hay ningun tipo de olor, pero el viento se escucha como roza las paredes…")
        st.write("¿por donde eliges ir?")
        sala = st.radio(
            "",
            ["Entrada Superior", "Entrada Inferior"],
            key="sala_explorador_ardilla"
        )

    elif st.session_state.mascota == "Gato Tricolor":
        st.write("llegas a la entrada de la mazmorra, te encuentras con dos caminos, uno arriba del otro, el de abajo irradia un olor nauseabundo y asqueroso, pero no logras llegar a ver nada más, del pasillo de arriba no hay ningun tipo de olor, pero el viento se escucha como roza las paredes…")
        st.write("¿por donde eliges ir?")
        sala = st.radio(
            "",
            ["Pasillo Abajo", "Pasillo Arriba"],
            key="sala_explorador_gato"
        )
    else:
        return

    if st.button("Continuar", key="continuar_sala_explorador"):
        st.session_state.salaInicial = sala
        st.session_state.etapa = 6
        st.rerun()


def etapa_6_explorador():
    st.subheader(f"El camino del {st.session_state.personaje}")
    sala = st.session_state.salaInicial

    if sala == "Entrada Superior":
        st.write("Entras a la entrada de arriba, por alguna razón tienes un buen presentimiento, de repente un viento desde abajo te hacen volar hasta uno de los últimos pisos de la mazmorra y te encuentras frente a frente con un enjambre de murciélagos y ratas que no se quedan quietas, parece el mismo infierno. ")
        st.write("Pero antes de entrar en pánico buscas a tu amigo roedor para que no le suceda nada, mientras corres por lugares medianamente estables piensas ¿Qué hago?")
        opcion = st.radio(
            "",
            ["¡Snif Snif!","¡Flish, flash flish!"]
        )


    elif sala == "Entrada Inferior":
        st.write("entras por la entrada de abajo, das unos pasos intentando ver el camino y un viento en dirección hacia abajo te obliga a caer y su fuerza hace perforar el piso, y a su vez aplastarte")
        st.write("¿Resistiras?")
        opcion = st.radio(
            "",
            ["¡Snif Snif!","Crack crack"]
        )

    elif sala == "Pasillo Abajo":
        st.write("Entras con toda tu confianza por la entrada de abajo, ya que piensan que la peor entrada será el mejor camino, este túnel esta dividido en dos y tu decides ir por la izquierda, tu camino desemboca en una reja de hierro oxidada bloqueada con un candado viejo.")
        st.write("A tus pies, el agua estancada burbujea despidiendo un gas verdoso e inflamable que hace arder los ojos. el gato tricolor empieza a bufar hacia el techo, erizando su lomo tricolor mientras un tenue brillo protector rodea a ambos, neutralizando parte del aire tóxico")
        opcion = st.radio(
            "",
            ["Forzar Cerrojo", "Explotar Bisagra"]
        )
        

    elif sala == "Pasillo Arriba":
        st.write("Eliges ir por la derecha cruzando una galería angosta con barro hasta los tobillos, pisas una losa floja que cede con un chasquido metálico. El suelo bajo tus botas se quiebra sobre una fosa llena de agua turbia y escombros.")
        st.write("De las grietas de los muros laterales asoman chillidos hambrientos: una plaga de roedores subterraneos de gran tamaño atraídos por el olor a carroña ¿que haces?")
        opcion = st.radio(
            "",
            ["Salto", "Uso De La Capa"]
        )
        
    else:
        return

    if st.button("Continuar", key="continuar_batalla_explorador"):
        st.session_state.opcionBatalla = opcion
        st.session_state.etapa = 7
        st.rerun()


def main_explorador():
    etapa = st.session_state.etapa

    if etapa == 2:
        if st.session_state.informacion == 1:
            informacion_explorador()
        else:
            elegir_camino_explorador()
    elif etapa == 3:
        etapa_3_explorador()
    elif etapa == 4:
        if st.session_state.mostrarTextoComo==1 or st.session_state.mostrarTextoComo==2:
            textoCruce()
        else:
            etapa_4_explorador()
    elif etapa == 5:
        etapa_5_explorador()
    elif etapa == 6:
        etapa_6_explorador()

#python -m streamlit run practica.py