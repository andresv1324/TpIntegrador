import streamlit as st
from PIL import Image
from pathlib import Path

# Ruta absoluta de la carpeta principal del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent

# Carpeta de imágenes
RUTA_IMG = RUTA_PROYECTO / "assets" / "picaro" / "img"

# Carpeta de GIF
RUTA_GIF = RUTA_PROYECTO / "assets" / "picaro" / "gif"

# Cargar imágenes
picaroEnTunel = Image.open(RUTA_IMG / "picaroTunel.png")
tunelCamino = Image.open(RUTA_IMG / "tunelCaminos.png")
picaCandado = Image.open(RUTA_IMG / "picaCandado.png")
picaMontaña = Image.open(RUTA_IMG / "picaMontaña.png")


def textoCruce():
    #CAMINO TUNEL
    if st.session_state.destino == "Tunel" and st.session_state.cruce =="Trepar tunel":
        if st.session_state.mostrarTextoComo==1:
            st.write("Al entrar al túnel, distingues a tu derecha una escalera que se extiende por toda su longitud, ascendiendo hasta el techo y continuando en línea recta por su interior. Parece una opción perfecta para atravesarlo sin depender de ningún otro elemento. Sin embargo, no puedes evitar pensar que será arriesgado: tendrás que mantenerte en posición vertical durante un tiempo indeterminado. A pesar de tus dudas, decides seguir ese camino. Comienzas a avanzar y, poco a poco, el ambiente se vuelve cada vez más pesado.")
            st.write("Escuchas ruidos a tu alrededor, pero no logras distinguir de dónde provienen. De repente, algo aparece frente a ti. A primera vista, crees que se trata de una rata asquerosa, pero, a medida que se acerca, comienzas a distinguir mejor su silueta. Hay algo extraño en esa criatura: su cuerpo emite un tenue brillo que apenas ilumina la oscuridad del túnel…")
            st.image(RUTA_GIF/"tunelArriba.gif")
            if st.button("Continuar", key="textoPicaroTunTrepar"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("¡Es una ardilla! ¿Una ardilla? ¿Aquí? La situación te resulta bastante extraña, pero la pequeña criatura se acerca y te observa con curiosidad. Luego, te hace una seña para que la sigas, indicándote el mismo camino que ya estabas recorriendo. Curiosamente, poco a poco comienzas a sentirte mejor: el ambiente se vuelve más ligero y recuperas tu velocidad habitual. Finalmente, distingues tu próximo desafío justo frente a ti…")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            st.image(RUTA_GIF / "tunelArdilla.gif")
            if st.button("Continuar", key="textoPicaroTunTrepar2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()
    elif st.session_state.destino == "Tunel" and st.session_state.cruce =="Cruzar el tunel":
        if st.session_state.mostrarTextoComo==1:
            st.write("Eres un pícaro, maestro del engaño y las trampas. Antes de continuar, decides analizar cuidadosamente el camino, prestando atención a cada detalle que logras distinguir en la penumbra. Nunca está de más ser precavido. Al examinar tu entorno, comienzas a notar ciertas irregularidades: piedras que sobresalen más de lo habitual, pequeños huecos sospechosamente bien distribuidos en las paredes y otras peculiaridades que difícilmente parecen producto de la casualidad…")
            st.image(RUTA_GIF/"trampasCueva.gif")
            st.write("Has visto este tipo de trampas millones de veces, así que sabes perfectamente cómo actuar. Confiado en tu experiencia, decides avanzar con cautela: esquivas una, luego otra y continúas sorteando cada obstáculo que encuentras en el camino. Así, poco a poco, consigues llegar hasta la mitad del recorrido. Desde allí ya logras divisar la salida, aunque la escasa visibilidad te impide distinguir con claridad qué te espera más adelante…")
            if st.button("Continuar", key="textoPicaroTunCruzar"):
                st.session_state.mostrarTextoComo = 2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Un suave tintineo comienza a resonar desde la parte más oscura del túnel. Entre las sombras distingues pequeños destellos dorados que aparecen y desaparecen rápidamente, hasta que finalmente revelan la figura de un gato tricolor. La criatura se acerca tranquilamente y pasa entre tus piernas. Al hacerlo, una tenue luz ilumina tus pasos y revela el camino que tienes por delante. Decides seguirlo, aprovechando su misteriosa compañía para continuar avanzando. Poco después, consigues llegar al final del recorrido…")
            st.write("¡Felicidades! tienes un nuevo amigo de aventuras")
            st.image(RUTA_GIF/"gato.gif")
            if st.button("Continuar", key="textoPicaroTunCruzar2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    #CAMINO DEL MONTAÑA
    elif st.session_state.destino =="Montaña Con Laberintos" and st.session_state.cruce =="Trepar montaña":
        if st.session_state.mostrarTextoComo==1:
            st.write("Decides trepar a un árbol y avanzar saltando de una rama a otra. Confías plenamente en tu agilidad y en el sigilo que has perfeccionado durante años, convencido de que podrás cruzar la montaña de esta manera. Sin embargo, las horas comienzan a pasar y, sin comida ni agua, el agotamiento empieza a hacerse notar. Tus manos resbalan cada vez más de los troncos y tu agarre pierde firmeza, pero aun así decides continuar. La tarde comienza a caer y, junto con ella, el viento aumenta su intensidad, haciendo que cada movimiento se vuelva más complicado…")
            st.image(RUTA_GIF / "ladronBosquito.gif")
            st.write("Comienzas a sentirte en peligro, pero tu terquedad puede más y decides continuar. Te preparas para saltar hacia un árbol que se encuentra a una distancia considerablemente mayor que los anteriores. Sin embargo, justo en el momento del salto, una fuerte ráfaga de viento te empuja y terminas cayendo al suelo. Por suerte, sigues con vida, aunque el golpe y el agotamiento te dejan bastante debilitado. Comprendes que necesitas descansar y recuperar energías, así que decides buscar algo para comer, lo que sea que encuentres. Te recuestas contra el tronco de un árbol y observas tu alrededor. No escuchas ningún ruido, todo parece tranquilo y poco a poco comienzas a relajarte. Pero, de repente…")
          

            if st.button("Continuar", key="textoPicaroMonTrepar"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Un suave tintineo comienza a escucharse entre la oscuridad. A lo lejos, distingues pequeños destellos dorados que aparecen y desaparecen fugazmente, hasta que finalmente revelan la figura de un gato tricolor. Este se acerca tranquilamente y pasa entre tus piernas. Al hacerlo, una tenue luz comienza a iluminar tu entorno, revelando tanto tus pasos como el camino que tienes por delante. Decides seguirlo, confiando en aquella misteriosa compañía. Poco a poco, consigues atravesar el resto del recorrido y finalmente llegas al final…")
            st.write("Felicidades! tienes un nuevo amigo de aventuras")
            st.image(RUTA_GIF/"gato.gif")
            if st.button("Continuar", key="textoPicaroMonTrepar2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    elif st.session_state.destino =="Montaña Con Laberintos" and st.session_state.cruce =="Cruzar La Montaña":
        if st.session_state.mostrarTextoComo==1:
            st.write("Decides que tu mejor opción es afrontar el riesgo y te adentras de lleno en el bosque que se extiende frente a ti. Al principio avanzas con determinación, pero pronto comienzas a notar que algo no está bien: el camino parece no llevar a ninguna parte y no haces más que dar vueltas una y otra vez. Ruidos extraños te acechan entre los árboles, mientras voces que no logras identificar comienzan a resonar en tu cabeza. La confusión y el miedo se apoderan de ti, hasta que, casi sin darte cuenta, la noche cae repentinamente. Ahora estás completamente perdido, desorientado y asustado…")
            st.write("Un ruido repentino te saca de tus pensamientos. Sientes que algo se aproxima a gran velocidad, moviéndose de una manera extraña entre la oscuridad. Tu pulso se acelera, pero la curiosidad puede más que tu instinto de supervivencia. Decides quedarte quieto y observar, intentando distinguir qué se acerca. A lo lejos, apenas alcanzas a ver unos destellos dorados y pequeñas patitas que avanzan en tu dirección. Entrecierra los ojos y concentras la mirada hasta que, finalmente, logras distinguir de qué se trata…")
            st.image(RUTA_GIF / "picaLuciernagas.gif")
            if st.button("Continuar", key="textoPicaroMonCruzar"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("¡Es una ardilla! ¿Una ardilla? ¿Aquí? La situación te resulta bastante extraña, pero la pequeña criatura se acerca y te observa con curiosidad. Luego, te hace una seña para que la sigas, indicándote el mismo camino que ya estabas recorriendo. Curiosamente, comienzas a sentirte mejor: el ambiente se vuelve más ligero y recuperas tu velocidad habitual. Con las energías renovadas, levantas la mirada y distingues tu próximo desafío justo frente a ti…")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            st.image(RUTA_GIF / "ultimo.gif")
            if st.button("Continuar", key="textoPicaroMonCruzar2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()


def informacion_explorador():
    st.text(
    "Eres un pícaro explorador en busca de su propio camino. Has engañado a personas,"
    "mentido y robado para sobrevivir, pero jamás te han descubierto. Eres ágil, astuto"
    "y posees un encanto envidiable; tienes la capacidad de convencer hasta a la persona"
    "más desconfiada del planeta. Tu fortaleza mental es admirable y tus habilidades de supervivencia, excepcionales."

    "En tu día a día, hay una frase que siempre ronda tus pensamientos: «Cuantos más obstáculos"
    "superes, mayor será tu sabiduría». Después de todo, eres un aprendiz de la vida misma."

    "Un día, mientras recorrías tu camino, encontraste un cartel que anunciaba tu próximo desafío:"
    "escapar de una mazmorra. Lo observaste por un momento y pensaste… ¿Por qué no?"
    )
    st.image(RUTA_GIF / "elPicaPica.gif")
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
            "Te encuentras frente a un túnel de dimensiones colosales, especialmente para alguien de tu tamaño. Te detienes a observarlo mientras analizas tus posibilidades. Piensas y piensas, pero, después de darle varias vueltas al asunto, solo consigues imaginar dos maneras de atravesarlo…"
            "¿Cuál eliges?"
        )
        st.image(picaroEnTunel)
        cruce = st.radio(
            "",
            ["Trepar tunel", "Cruzar el tunel"],
            key="cruce_explorador_tunel"
        )

    elif st.session_state.destino == "Montaña Con Laberintos":
        st.subheader(
            "Comienzas tu recorrido por la montaña. La inmensidad del paisaje te abruma por un instante, pero no tardas en recuperar la compostura. Recuerdas todo lo que has superado hasta ahora y te convences de que eres capaz de afrontar cualquier desafío. Después de todo, nada podrá detenerte…"
            "¿Cuál eliges?"
        )
        st.image(picaMontaña)
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
        st.session_state.mascota = "Ardilla"

    elif st.session_state.cruce in [
        "Cruzar el tunel",
        "Trepar montaña"
    ]:
        st.write("Encontraste un Gato Tricolor mascota en el camino.")
        st.session_state.mascota = "Gato Tricolor"

    st.session_state.etapa = "MAZMORRA"
    st.rerun()


def etapa_5_explorador():
    if st.session_state.mascota == "Ardilla":
        st.write("Llegas a la entrada de la mazmorra y te encuentras con dos caminos, uno encima del otro. El pasillo inferior desprende un olor nauseabundo y repulsivo, aunque la oscuridad no te permite distinguir qué se esconde en su interior. Por otro lado, el pasillo superior no presenta ningún olor extraño, pero puedes escuchar cómo el viento se desliza entre sus paredes, produciendo un inquietante silbido…")
        st.write("¿por donde eliges ir?")
        st.image(tunelCamino)
        sala = st.radio(
            "",
            ["Entrada Superior", "Entrada Inferior"],
            key="sala_explorador_ardilla"
        )

    elif st.session_state.mascota == "Gato Tricolor":
        st.write("Llegas a la entrada de la mazmorra y te encuentras con dos caminos, uno sobre el otro. El pasillo inferior desprende un olor nauseabundo y repulsivo, aunque no logras distinguir qué se esconde en su interior. Por otro lado, el pasillo superior no presenta ningún olor extraño, pero puedes escuchar cómo el viento roza sus paredes, produciendo un suave y constante silbido…")
        st.write("¿por donde eliges ir?")
        st.image(tunelCamino)
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
    sala = st.session_state.salaInicial

    if sala == "Entrada Superior":
        st.write("Decides adentrarte por el pasillo superior; por alguna razón, tienes un buen presentimiento. Sin embargo, apenas avanzas, una repentina corriente de aire proveniente de los niveles inferiores te envuelve y te impulsa violentamente hacia arriba, haciéndote volar hasta uno de los pisos más altos de la mazmorra. Al recuperar el equilibrio, te encuentras cara a cara con un enorme enjambre de murciélagos y ratas que no dejan de moverse por todas partes. El caos es absoluto… ¡parece el mismísimo infierno!")
        st.write("Pero, antes de dejarte llevar por el pánico, lo primero que haces es buscar a tu pequeño amigo roedor, asegurándote de que no le haya sucedido nada. Mientras corres entre los pocos sectores que parecen ofrecer cierta estabilidad, intentas mantener el equilibrio y encontrar una salida. Tu mente trabaja a toda velocidad, buscando alguna solución entre tanto caos. Piensas: ¿Qué hago?…")
        st.image(RUTA_GIF /"excapeRuinas.gif")
        opcion = st.radio(
            "",
            ["¡Snif Snif!","¡Flish, flash flish!"]
        )


    elif sala == "Entrada Inferior":
        st.write("Te adentras por el pasillo inferior y avanzas unos pocos pasos, intentando distinguir qué se esconde entre la oscuridad. De repente, una potente corriente de aire descendente te empuja con una fuerza descomunal, haciéndote perder el equilibrio. El impacto es tan intenso que el suelo cede bajo tus pies, provocando que caigas junto con los escombros y quedes atrapado bajo ellos…")
        st.write("¿Resistiras?")
        st.image(RUTA_GIF / "caidaMazmorra.gif")
        opcion = st.radio(
            "",
            ["¡Snif Snif!","Crack crack"]
        )

    elif sala == "Pasillo Abajo":
        st.write("Entras con total confianza por el pasillo inferior, convencido de que, a veces, el camino que parece peor esconde la mejor oportunidad. Tras avanzar un poco, descubres que el túnel se divide en dos direcciones y decides tomar el camino de la izquierda. Sin embargo, tu recorrido termina frente a una antigua reja de hierro oxidado, cerrada con un candado tan viejo como el lugar mismo…")
        st.image(RUTA_GIF / "ruinas.gif")       
        st.write("A tus pies, el agua estancada comienza a burbujear, liberando un gas verdoso e inflamable que irrita tus ojos. De repente, el gato tricolor comienza a bufar en dirección al techo, erizando su pelaje mientras un tenue resplandor protector los envuelve a ambos. Su misterioso brillo parece neutralizar parte de la toxicidad del ambiente, permitiéndote respirar con algo más de tranquilidad…")
        opcion = st.radio(
            "",
            ["Forzar Cerrojo", "Explotar Bisagra"]
        )
        

    elif sala == "Pasillo Arriba":
        st.write("Decides tomar el camino de la derecha, atravesando una galería estrecha donde el barro te llega hasta los tobillos. Avanzas con cautela, pero, de repente, pisas una losa suelta que cede bajo tu peso con un estridente chasquido metálico. Antes de que puedas reaccionar, el suelo bajo tus botas comienza a resquebrajarse y termina cediendo, revelando una fosa repleta de agua turbia y escombros…")
        st.write("Desde las grietas de los muros laterales comienzan a escucharse unos chillidos inquietantes. Poco a poco, aparecen enormes roedores subterráneos, atraídos por el olor a carroña que impregna el lugar. Sus movimientos son inquietos y sus ojos parecen estar fijos en ti. En cuestión de segundos, te encuentras rodeado por una plaga hambrienta que no parece tener intención de dejarte pasar… Piensas: ¿Qué hago?…")
        st.image(RUTA_GIF / "tunelRata.gif")
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

def etapa_7_explorador():
    if st.session_state.salaInicial =="Entrada Superior" and st.session_state.opcionBatalla=="¡Snif Snif!":
        st.write("Tu pequeño amigo roedor llama tu atención y te hace una seña para que toques su nariz, que comienza a emitir un tenue resplandor. Con curiosidad, acercas tu mano y rozas su pequeña naricita. En ese instante, una luz ilumina el camino frente a ti, revelando una posible ruta hacia la salida. Aprovechas el impulso de energía que acabas de recibir y, haciendo uso de tu agilidad, te apresuras a seguir el sendero iluminado. Poco a poco, consigues abrirte paso hasta alcanzar el final del recorrido…")
        st.image(RUTA_GIF /"salidaRuina.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Entrada Superior" and st.session_state.opcionBatalla=="¡Flish, flash flish!":
        st.write("Llegas al lugar hasta donde aquella corriente de viento te había arrastrado y, al aterrizar, tus ojos no pueden creer lo que ven. Frente a ti se extienden enormes enjambres de murciélagos y ratas, todos corrompidos por una fuerza desconocida que los ha vuelto completamente frenéticos y peligrosos. La escena te deja momentáneamente paralizado, sin saber cómo reaccionar. Sin embargo, un chillido de dolor de tu pequeño amigo roedor te devuelve a la realidad: ¡una de las ratas lo ha mordido!…")
        st.write("Lo recoges rápidamente y lo proteges entre tus brazos para evitar que vuelva a lastimarse. Presa de la desesperación, comienzas a correr mientras apartas y empujas a los animales con todas tus fuerzas, intentando abrirte paso entre aquel enjambre. Sin embargo, pronto recuerdas que la fuerza bruta nunca ha sido tu especialidad… y cada vez te resulta más difícil avanzar.")
        st.image(RUTA_GIF /"excapeRuinasFallado.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Entrada Inferior" and st.session_state.opcionBatalla=="¡Snif Snif!":
        st.write("Tu pequeño amigo roedor se acerca a ti con sus patitas envueltas en un brillo intenso, invitándote a tocarlas. Al hacerlo, una luz lo envuelve por completo y su cuerpo comienza a crecer hasta alcanzar cinco veces su tamaño original. ¡Su transformación es increíble! Ahora, convertido en un roedor gigantesco, comienza a cavar a una velocidad extraordinaria, incluso más rápido de lo que el viento los aplasta. Su ritmo de excavación aumenta cada vez más, abriéndoles paso hacia un lugar seguro…")
        st.image(RUTA_GIF/"excapeCalabaza.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Entrada Inferior" and st.session_state.opcionBatalla=="Crack crack":
        st.write("El pelaje de tu pequeño amigo roedor comienza a desprender destellos dorados. ¡Lo que habías presenciado antes no había sido una ilusión! Su misterioso poder es real. La criatura se acerca a tu pierna, intentando alcanzar tu altura, y, a medida que su brillo se intensifica, comienzas a sentir que algo a tu alrededor está cambiando…")
        st.image(RUTA_GIF /"excapeALuz.gif")
        st.write("De repente, sientes cómo una nueva energía recorre tu cuerpo. El dolor disminuye y recuperas parte de tus fuerzas, como si aquel misterioso brillo te hubiera devuelto la vitalidad. Sin perder ni un segundo, comienzas a cavar con renovado entusiasmo y avanzas todo lo rápido que puedes, decidido a salir de allí…")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Abajo" and st.session_state.opcionBatalla=="Forzar Cerrojo":
        st.write("Decides utilizar tus ganzúas para forzar el cerrojo lo más rápido posible. Cada segundo cuenta y la presión aumenta: el poder protector de tu amigo felino todavía no está lo suficientemente desarrollado como para mantenerte a salvo de aquel gas tóxico. Te ves obligado a soportar sus efectos mientras concentras toda tu atención en la cerradura, intentando abrirla antes de que sea demasiado tarde…")
        st.image(picaCandado)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Abajo" and st.session_state.opcionBatalla=="Explotar Bisagra":
        st.write("Durante uno de tus tantos viajes, un viejo sabio te enseñó a llevar siempre un pedernal en una pequeña bolsa, por precaución. Al recordar aquel consejo, decides buscarlo entre tus pertenencias y rápidamente encuentras la bolsita. Sin embargo, al revisar tus herramientas, te das cuenta de que no tienes absolutamente nada que pueda ayudarte a generar una llama: solo cuentas con el gas acumulado y tu pedernal. ¡Pero necesitas fuego! ¡Aunque sea una pequeña chispa!…")
        st.write("Tu amigo tricolor parece darse cuenta de lo que intentas conseguir. De repente, frunce el rostro y su pelaje comienza a erizarse, desprendiendo pequeñas chispas. ¡BOOM! Una fuerte explosión hace saltar la reja de golpe, mientras el humo acumulado comienza a disiparse. ¡Las chispas de tu compañero felino fueron la clave para abrirte paso hacia la salida!…")
        st.image(RUTA_GIF / "boom.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Arriba" and st.session_state.opcionBatalla=="Salto":
        st.write("Justo antes de caer, tu instinto de supervivencia se activa y reaccionas rápidamente: saltas hacia una de las paredes y clavas tu daga para conseguir sujetarte. Apenas un instante después, tu amigo felino también salta en tu dirección, aferrándose a ti antes de trepar hasta una viga cercana. Ambos consiguen mantenerse a salvo, evitando caer al vacío…")
        st.image(RUTA_GIF / "rescateGato.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Arriba" and st.session_state.opcionBatalla=="Uso De La Capa":
        st.write("Decides cubrirte con tu capa para protegerte de aquella plaga, pero el miedo te paraliza y no consigues moverte. Recibes varios golpes mientras permaneces inmóvil, hasta que, de un momento a otro, dejas de sentir cualquier molestia. Algo extraño acaba de suceder…")
        st.write("¡Sorpresa! ¡Tu amigo felino también tiene poderes! Con tan solo hacer sonar su pequeña campanita dos veces, consigue que ambos comiencen a levitar, elevándolos suavemente por encima del suelo y alejándolos del peligro…")
        st.image(RUTA_GIF / "elGatoVolador.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()

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
    if st.session_state.salaInicial =="Entrada Superior" and st.session_state.opcionBatalla=="¡Snif Snif!":
        st.session_state.etapa = 9
        st.rerun()
    elif st.session_state.salaInicial =="Entrada Superior" and st.session_state.opcionBatalla=="¡Flish, flash flish!":
        st.write("Tu cuerpo comienza a resentirse ante la cantidad de golpes y rasguños recibidos. Son demasiadas criaturas atacando al mismo tiempo y, por más que intentes resistir, tu resistencia tiene un límite. Poco a poco, te resulta cada vez más difícil soportar el embate de aquella plaga…")
        st.image(RUTA_GIF /"ruinaSinExcape.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Entrada Inferior" and st.session_state.opcionBatalla=="¡Snif Snif!":
        st.write("Entre los montones de tierra comienzas a distinguir pequeños haces de luz que se filtran desde el exterior. ¡La salida está cerca! Gracias a la ayuda de tu pequeño amigo roedor, consigues abrirte paso entre la tierra acumulada y finalmente logras escapar de la mazmorra…")
        st.image(RUTA_GIF /"salidaTunel.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Entrada Inferior" and st.session_state.opcionBatalla=="Crack crack":
        st.write("Parece que tu plan está funcionando y consigues acercarte cada vez más a la salida. Sin embargo, el viento sopla con tanta fuerza que avanzar se vuelve cada vez más complicado. Por más que intentas continuar, cada paso requiere un esfuerzo enorme…")
        st.image(RUTA_GIF/"sinEscape.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Abajo" and st.session_state.opcionBatalla=="Forzar Cerrojo":
        st.write("Finalmente consigues abrir el cerrojo. Con las pocas fuerzas que te quedan, atraviesas la reja y alcanzas el otro lado. Por fin puedes respirar aire fresco, pero el alivio dura poco: el agotamiento y los efectos del gas terminan pasándote factura y, apenas das unos pasos, pierdes el conocimiento…")
        st.image(RUTA_GIF / "gasVeneno.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Abajo" and st.session_state.opcionBatalla=="Explotar Bisagra":
        st.write("Tú y tu amigo felino se apresuran a atravesar el hueco que ha quedado en la reja, logrando escapar hacia un pasadizo oculto que conduce a una salida secreta de la mazmorra…")
        st.image(RUTA_GIF /"escapeluz.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Arriba" and st.session_state.opcionBatalla=="Salto":
        st.write("Deciden saltar juntos hacia el siguiente nivel y, tras un arriesgado impulso, consiguen llegar al otro lado. Sin embargo, en medio de la emoción por haber superado el obstáculo, olvidaron considerar una posibilidad: ¡todavía podrían aparecer más roedores subterráneos!…")
        st.image(RUTA_GIF / "spiderman.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Arriba" and st.session_state.opcionBatalla=="Uso De La Capa":
        st.write("…hasta conseguir llevarlos a un lugar seguro, donde ambos puedan recuperarse y continuar su camino.")
        st.image(RUTA_GIF / "escapeTunelVuela.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 9
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
    elif etapa == 7:
        etapa_7_explorador()
    elif etapa == 8:
        finalAventura()
    elif etapa ==9:
        infoSalia()

#python -m streamlit run practica.py
