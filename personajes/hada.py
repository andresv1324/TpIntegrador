import streamlit as st
from PIL import Image
from pathlib import Path

# Ruta absoluta de la carpeta principal del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent

# Carpeta de imágenes
RUTA_IMG = RUTA_PROYECTO / "assets" / "hada" / "img"

# Carpeta de GIF
RUTA_GIF = RUTA_PROYECTO / "assets" / "hada" / "gif"

# Cargar imágenes
imgRioBravo = Image.open(RUTA_IMG / "hadaAnteElRioTempestuoso.png")
hadaGatAntCam = Image.open(RUTA_IMG / "hadaGatoAnteCamino.png")
hadaBajLlu = Image.open(RUTA_IMG / "gataBajoLaLluvia.png")
hadaCalva = Image.open(RUTA_IMG / "hadaCorte.png")
hadaSubSue = Image.open(RUTA_IMG / "hadaEnSubSuelo.png")
hadaCampana = Image.open(RUTA_IMG / "hadaCampanaGato.png")
hadaArdAntCam = Image.open(RUTA_IMG /"hadaArdiAnteCamino.png")
hadaFloresMag = Image.open(RUTA_IMG /"hadaEncuentroFlores.png")


def textoCruce():
    #CAMINO RIO BRAVO
    if st.session_state.destino == "Rio Bravo" and st.session_state.cruce =="Bordear el rio":
        if st.session_state.mostrarTextoComo==1:
            st.write("Elijes bordear el rio, dices que es mejor un trabajo duro que uno arriesgado, tu camino empieza complicado, te sientes observada y ansiosa, lo cual te hace tropezar y lastimarte, llegas a mitad de camino y sientes que no puedes más, de repente una manada de perros aparece en frente tuyo, gruñéndote y enfrentandote, tu miedo te ciega y tu cansancio actual no ayuda, pero")
            st.write("Desde lo más alto de los árboles a tu lado finos balines empiezan a dirigirse hacia los perros haciendo que se asusten y no sepan que hacer más que correr hacia diferentes direcciones, se olvidan de ti, pero debido a todo lo ocurrido te desmayas, momentos después te despiertas y sin entender mucho sigues el camino")
            st.image(RUTA_GIF / "hadaBordearRio.gif")

            if st.button("Continuar", key="textHadaBalsBorde"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Estás llegando al final de tu camino… Pero… espera un momento, ¿qué es ese ruido? *escuchas ruido de madera, empiezas a tener miedo…* de la nada te cae una nuez en la cabeza")
            st.write("Lejos de asustarte mirás hacia la dirección donde la viste venir, unos ojos redondos y brillosos te miran desde esa dirección, es una ardilla!! pero no cualquier ardilla, destellos dorados salen de su nariz y orejas cuando te ven, acaso esta será una conexión…?")
            st.image(RUTA_GIF / "hadaArdilla.gif")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            if st.button("Continuar", key="textHadaBalsBorde2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()
    elif st.session_state.destino == "Rio Bravo" and st.session_state.cruce =="Balsa por dentro":
        if st.session_state.mostrarTextoComo==1:
            st.write("Eliges cruzar el río por dentro, tu instinto de venganza y de ira te hace ir por el lugar más peligroso a simple vista, donde estabas había una balsa medianamente decente, que en tu cabeza era buena idea, y de hecho, sí… El primer trayecto fue un poco turbulento, pero luego el rio desemboca y se calma haciendo de tu viaje hasta la mazmorra tranquilo. Pero de repente, casi llegando al final, el río se alborota y se vuelve incontrolable, intentas mantenerte a flote hasta llegar pero tu balsa se vuelca…")
            st.image(RUTA_GIF / "hadaPelirrojaEnLosRapidos.gif")

            if st.button("Continuar", key="textHadaBalsDentr3"):
                st.session_state.mostrarTextoComo = 2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Justo antes de caer un gato tricolor callejero rondaba por ahí, vio la situación e hizo sonar su campana, no entiendes bien que pasó pero saliste ilesa y tu cuerpo no dolía, cuando logras despertar estabas en el suelo y sobre ti había un amigo felino tricolor mirándote fijo, crees ver destellos dorados salir de su collar pero dudas")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            st.image(RUTA_GIF / "encuentroGatito.gif")
            if st.button("Continuar", key="textHadaBalsDentr4"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    #CAMINO DEL BOSQUE
    elif st.session_state.destino =="Bosque Brumoso" and st.session_state.cruce =="Volar Sobre el bosque":
        if st.session_state.mostrarTextoComo==1:
            st.write("Creíste que pasar por fuera del bosque sería lo más lógico, pensaste que el cielo sería tranquilo, pero estuviste equivocada, empezaste a volar y de primera un grupo de pájaros te chocó desestabilizandote un poco, un trayecto de silencio inquietante te hizo poner nerviosa, no estabas equivocada, ese bosque es tierra de nadie, pero hadas de diferentes reinos constantemente luchan por esos cielos")
            st.write("te vieron y creyeron que eras un hada exploradora investigando terreno para posibles complicaciones en el futuro (para ellos, por supuesto) logran hacerte caer, pero fuiste tan rápida que tu caída fue cerca del final, aunque antes de caer te desmayas")

            if st.button("Continuar", key="textHadaBalsBorde"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("justo antes de caer un gato tricolor callejero rondaba por ahí, vio la situación e hizo sonar su campana, no entiendes bien que pasó pero saliste ilesa y tu cuerpo no dolía, cuando logras despertar estabas en el suelo y sobre ti había un amigo felino tricolor mirándote fijo, crees ver destellos dorados salir de su collar pero dudas")
            st.write("Felicidades! tienes un nuevo amigo que te acompañará en esta travesía")
            if st.button("Continuar", key="textHadaBalsBorde2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    elif st.session_state.destino =="Bosque Brumoso" and st.session_state.cruce =="Cruzar Por Dentro":
        if st.session_state.mostrarTextoComo==1:
            st.write("Elegiste la mejor opción para cruzar este camino, el bosque es horrible, oscuro, tenebroso, pero no tiene peligro alguno, con tal de que no pises mal, ni te caigas, tu viaje es tranquilo, consejo: evita mirar hacia arriba")
            if st.button("Continuar", key="textHadaBosqueDentro"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Estás llegando al final de tu camino… Pero… espera un momento, ¿qué es ese ruido? *escuchas ruido de madera, empiezas a tener miedo…* de la nada te cae una nuez en la cabeza")
            st.write("Lejos de asustarte mirás hacia la dirección donde la viste venir, unos ojos redondos y brillosos te miran desde esa dirección, es una ardilla!! pero no cualquier ardilla, destellos dorados salen de su nariz y orejas cuando te ven, acaso esta será una conexión…?")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            if st.button("Continuar", key="textHadaBosqueDentro"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

def informacion_hada():
    st.image(RUTA_GIF / "hadaDesterrada.gif")
    st.text(
        "Eres un hada que fue exiliada de su lugar, de su casa, de su familia, "
        "luchaste por quedarte y te defendiste, pero la reina no te creyó a pesar "
        "de que todo haya sido una confusión y el culpable sea otro, tu exiliación "
        "solo puede ser redimida enfrentando esta aventura. Si logras superar, "
        "serás inocente y podrás volver a tu aldea; si no, tu peor destino será "
        "no salir de la mazmorra. Te deseamos suerte."
    )

    if st.button("Continuar", key="continuar_historia_hada"):
        st.session_state.informacion = 0
        st.rerun()


def elegir_camino_hada():
    st.subheader(
        "Hiciste la elección de personaje, tu rumbo ha comenzado, elige tu camino"
    )

    destino = st.radio(
        "¿A dónde quieres ir?",
        ["Rio Bravo", "Bosque Brumoso"],
        key="destino_hada"
    )

    if st.button("Continuar", key="continuar_camino_hada"):
        st.session_state.destino = destino
        st.session_state.etapa = 3
        st.rerun()

#OPCION CRUZAR CAMINO
def etapa_3_hada():
    if st.session_state.destino == "Rio Bravo":
        st.header(
            "Empiezas tu recorrido por un río turbulento que intimida, "
            "rompe olas contra piedras filosas y hay muchísimo viento. "
            "¿Por dónde eliges ir?"
        )
        st.image(imgRioBravo, width=500)
        cruce = st.radio(
            "",
            ["Balsa por dentro", "Bordear el rio"],
            key="cruce_hada_rio"
        )

    elif st.session_state.destino == "Bosque Brumoso":
        st.subheader(
            "Inicias tu recorrido por el bosque brumoso, está todo lleno de "
            "niebla y hay un ambiente tenso y sombrío."
        )
        cruce = st.radio(
            "",
            ["Volar Sobre el bosque", "Cruzar Por Dentro"],
            key="cruce_hada_bosque"
        )
    else:
        return

    if st.button("Continuar", key="continuar_cruce_hada"):
        st.session_state.cruce = cruce
        st.session_state.etapa = 4
        st.rerun()

#OPCION TENER MASCOTA
def etapa_4_hada():
    if st.session_state.cruce in [
        "Bordear el rio",
        "Cruzar Por Dentro"
    ]:
        st.session_state.mascota = "Ardilla"

    elif st.session_state.cruce in [
        "Balsa por dentro",
        "Volar Sobre el bosque"
    ]:
        st.session_state.mascota = "Gato Tricolor"

    st.session_state.etapa = "MAZMORRA"
    st.rerun()


def etapa_5_hada():
    if st.session_state.mascota == "Ardilla":
        st.write("Encuentras y entras a la mazmorra")
        st.write("pasas por un tunel que te dirige hacia el este (izquierda) y te encuentras con dos opciones de camino, el primero tiene un aspecto tranquilo, calmo e inquietante, el segundo se ve más familiar, como tu hogar, algunas flores salen de la puerta y se ve vida…")
        st.image(hadaArdAntCam)
        sala = st.radio(
            "¿Con quién vas a luchar?",
            ["Pasillo Tranquilo", "Pasillo Familiar"],
            key="sala_hada_ardilla"
        )

    elif st.session_state.mascota == "Gato Tricolor":
        st.write("Llegas a la entrada de la mazmorra pasas por un túnel que te dirige hacia el este")
        st.write("Está oscuro y hay muchos ruidos, pero crees que es la mejor entrada y que es un engaño el aspecto para que los exploradores como vos no pasen, más adelante te encuentras con dos pasillos ¿cuál eliges?")
        st.image(hadaGatAntCam)
        sala = st.radio(
            "",
            ["Pasillo Izquierdo", "Pasillo Derecho"],
            key="sala_hada_gato"
        )
    else:
        return

    if st.button("Continuar", key="continuar_sala_hada"):
        st.session_state.salaInicial = sala
        st.session_state.etapa = 6
        st.rerun()


def etapa_6_hada():
    sala = st.session_state.salaInicial

    if sala == "Pasillo Tranquilo":
        st.write("Entras a una habitación en penumbras, tras pasar la entrada tus ojos no pueden creer lo que ven, entidades, personas, espíritus, toda clase de fantasmas que te puedas imaginar, deambulando por todo el lugar… te encuentras frente a fantasmas que buscan oro y cosas brillantes, sino te raptan y no te dejan salir")
        st.image(RUTA_GIF /"hadaSalaFantasma.gif")
        opcion = st.radio(
            "¿qué hacés?",
            ["Polvo De Hadas", "¡snif snif!"],
            key="opcionPasilloTranquilo"
        )

    elif sala == "Pasillo Familiar":
        st.write("Entras a la puerta de tu eleccion y te encuentras con un campo de flores hermoso, las flores más bellas que jamás hayas visto, tu amigo roedor se emociona porque jamás creyó que existiera algo así, empiezas tu camino pero a medida que avanzas te das cuenta que las flores largan un olor extraño, casi nauseabundo, malas noticias… las flores son venenosas, largan un hedor parecido al ácido y te asfixian")
        st.image(RUTA_GIF / "hadaFlores.gif")
        opcion = st.radio(
            "¿qué hacés?",
            ["Polvo De Hadas", "¡snif snif!"],
            key="opcionPasilloFamiliar"
        )

    elif sala == "Pasillo Izquierdo":
        st.write("Entras a una habitación llena de humedad.")
        st.write("Es un espacio donde cae agua por doquier y su piso está inundado de barro, sientes como tus alas empiezan a pesar por el agua que cae y no te permite seguir volando, inevitablemente debes caminar, el barro te llegaba hasta por debajo de la rodilla, pero de repente sientes que este te tira un poco, frente a ti se eleva una montaña de barro, es un espiritu que usa el barro como cuerpo")
        st.image(RUTA_GIF / "hadaAnteBarro.gif")
        opcion = st.radio(
            "¿qué haces?",
            ["Tintineo De Campana", "Cortar Mechon Del Cabello"],
            key="opcionPasilloIzquierdo"
        )

    elif sala == "Pasillo Derecho":
        st.write("Este pasillo está oscuro, haces 5 pasos y el piso se pierde… caes por un túnel y al caer te encuentras con una habitación completamente a oscuras donde hay mucho ruido, sabes que si sigues 5 minutos así no resistiras ¿qué haces?")
        st.image(hadaSubSue)
        opcion = st.radio(
            "¿que haces?",
            ["Tintineo De Campana", "Correr"],
            key="opcionPasilloDerecho"
        )

    else:
        return

    if st.button("Continuar", key="continuarBatallaHada"):
        st.session_state.opcionBatalla = opcion
        st.session_state.etapa = 7
        st.rerun()

def etapa_7_hada():

    if st.session_state.salaInicial =="Pasillo Derecho" and st.session_state.opcionBatalla=="Tintineo De Campana":
        st.write("Tu compañero te llama, empieza a moverse inquieto y ves una lucecita tenue, recuerdas la caída en el bosque y los destellos dorados, intentas enfocar la vista y te das cuenta que es el collar de tu compañero, acercas tu mano para tocar la campana")
        st.image(hadaCampana)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Derecho" and st.session_state.opcionBatalla=="Correr":
        st.write("Los ruidos no te dejan escuchar nada, no ves nada, dos de tus sentidos están totalmente bloqueados, tu corazón se empieza a acelerar y tu cabeza se empieza a nublar, solo logras sentir como tu gato compañero se altera y te pones aún más nerviosa")
        st.image(RUTA_GIF / "hadaGatitoLocos.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Izquierdo" and st.session_state.opcionBatalla=="Tintineo De Campana":
        st.write("De repente escuchas un tintineo, el mismo que escuchaste antes, es tu amigo felino que está a tu lado intentando llamar tu atención moviendo su campana en su collarcito, esta empieza a brillar y te inclinas para tocarla, en ese momento el brillo de su campan ")
        st.image(hadaBajLlu)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Izquierdo" and st.session_state.opcionBatalla=="Cortar Mechon Del Cabello":
        st.write("En tus épocas de estudio formaste parte de un grupo secreto que estudiaba magia prohibida que requiere partes de ti, agarras un mechón de tu largo cabello y lo cortas, El hechizo dice que cuando un hada hace esto, el cabello brilla esparciendo la luz encerrada en sí. ")
        st.image(hadaCalva)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Tranquilo" and st.session_state.opcionBatalla=="Polvo De Hadas":
        st.write("Eliges el polvo de hada, lo lanzas como lluvia y este crea un humo que hace pequeñas explosiones, logran cegar a los fantasmas y permiten perderte entre el lugar para que los fantasmas no te perciban")
        st.write("Lamentablemente tu hechizo no estaba bien estudiado, ni bien practicado, funciona hasta la mitad del lugar, pero luego se disipa, llegas a la puerta, pero antes de cruzar un fantasma te agarra de los pies arrastrándose por dentro")
        st.image(RUTA_GIF /"hadaFantasmaMal.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Tranquilo" and st.session_state.opcionBatalla=="¡snif snif!":
        st.write("Te acuerdas de tu Ardilla y sus destellos dorados que salían de ella, pues… tiene poderes! permite que ella se suba en tu cabeza y te hará invisible para pasar entre los fantasmas…")
        st.image(RUTA_GIF/"hadaInvisible.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Familiar" and st.session_state.opcionBatalla=="Polvo De Hadas":
        st.write("Empiezas a buscar soluciones y te acuerdas de tus clases de magia antes de ser exiliada, un hechizo se te viene a la memoria y junto a tu polvo de hadas apaga todo el veneno que te libera sigues avanzando lo más rápido posible para lograr salir")
        st.image(RUTA_GIF / "hadaSinNiebla.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Familiar" and st.session_state.opcionBatalla=="¡snif snif!":
        st.write("Ante la desesperación tu amigo roedor llama tu atención y ves como su pelaje empieza a brillar, no era mentira lo que viste en el bosque, él también tiene poderes!!")
        st.write(hadaFloresMag)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    else:
        st.error("No se encontró una combinación válida")
        st.write("Sala recibida:", repr(st.session_state.salaInicial))
        st.write("Opción recibida:", repr(st.session_state.opcionBatalla))

def infoSalia():
    if st.session_state.condicionSalida == 2:
        st.error("No lograste Escapar De La Mazmorra")
        if st.button("Continuar"):
            st.session_state.etapa = 10
            st.rerun()
    elif st.session_state.condicionSalida == 1:
        st.success("Felicidades! lograste Escapar De La Mazmorra")
        if st.button("Continuar"):
            st.session_state.etapa = 10
            st.rerun()

def finalAventura():
    if st.session_state.salaInicial =="Pasillo Izquierdo" and st.session_state.opcionBatalla=="Tintineo De Campana":
        st.write("Se fusiona con el tuyo y de ahí nace una luz que encandila al espíritu y lo seca en un segundo, dejando el barro seco y al espíritu encerrado.")
        st.image(RUTA_GIF / "hadaEscapaBarro.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Izquierdo" and st.session_state.opcionBatalla=="Cortar Mechon Del Cabello":
        st.write("lamentablemente este brillo no es suficiente para secarlo a él y todo alrededor, el poder se consume rápido y el espíritu recupera su fuerza")
        st.image(RUTA_GIF/ "hadaMostroFallo.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Derecho" and st.session_state.opcionBatalla=="Tintineo De Campana":
        st.write("Y al instante la campana brilla e ilumina todo el lugar mostrando que los ruidos no son más que unos cuantos bichos chocando contra metales")
        st.write("estos son insectos comunes sumidos en una locura extraña, tu amigo felino y tú deciden avanzar empujandolos, no te generan daño alguno y al estar iluminados se calman.")
        st.image(RUTA_GIF/ "hadaGatitoLuz.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Derecho" and st.session_state.opcionBatalla=="Correr":
        st.write("Lo agarras y empiezas a correr para lo que sea que haya en ese lugar, para escapar, pero en la desesperación chocas contra una pared ")
        st.image(RUTA_GIF / "hadaContraPared.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Tranquilo" and st.session_state.opcionBatalla=="Polvo De Hadas":
        st.session_state.etapa = 9
        st.rerun()
    elif st.session_state.salaInicial =="Pasillo Tranquilo" and st.session_state.opcionBatalla=="¡snif snif!":
        st.write("Bien! tienes que ser cuidadosa, no hacer ruido y seguir, eres un hada así que vuelas despacio para hacer el menor ruido posible y no tocar a ningún fantasma.")
        st.image(RUTA_GIF / "hadaArdillaEscape.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Familiar" and st.session_state.opcionBatalla=="Polvo De Hadas":
        st.write("Pero hay un detalle que no viste, las plantas sin ese veneno que liberan, son agresivas, logras salvarte de su veneno pero no de sus rasguños")
        st.write("Sus rasguños te dañan, te raspan y te vuelven más débil a medida que quieras salir")
        st.image(RUTA_GIF / "hadaEspinas.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Familiar" and st.session_state.opcionBatalla=="¡snif snif!":
        st.write("Tu ardilla empieza a trepar por tu cuerpo hasta lograr subir sobre tu cabeza")
        st.write("Empieza a brillar cada vez más y genera una burbuja protectora que te repele de todos los gases venenosos, al no combatirlos ni apagar estos gases las flores se mantienen dormidas, pasas sigilosa y tranquila Las flores no se despertaron y llegaste al final")
        st.image(RUTA_GIF / "hadaEscudo.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()

def main_hada():
    etapa = st.session_state.etapa

    if etapa == 2:
        if st.session_state.informacion == 1:
            informacion_hada()
        else:
            elegir_camino_hada()
    elif etapa == 3:
        etapa_3_hada()
    elif etapa == 4:
        if st.session_state.mostrarTextoComo==1 or st.session_state.mostrarTextoComo==2:
            textoCruce()
        else:
            etapa_4_hada()
    elif etapa == 5:
        etapa_5_hada()
    elif etapa == 6:
        etapa_6_hada()
    elif etapa == 7:
        etapa_7_hada()
    elif etapa == 8:
        finalAventura()
    elif etapa ==9:
        infoSalia()


#python -m streamlit run practica.py