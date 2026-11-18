import streamlit as st
from pathlib import Path

# Ruta absoluta de la carpeta principal del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent

# Carpetas de recursos
RUTA_IMG = RUTA_PROYECTO / "assets" / "picaro" / "img"
RUTA_GIF = RUTA_PROYECTO / "assets" / "picaro" / "gif"


def mostrar_escena(parrafos, media, botones, clave_prefix=""):
    """Dibuja la imagen a la izquierda y la historia con botones directos a la derecha."""
    col_izq, col_der = st.columns([1, 1.15], gap="large")

    with col_izq:
        st.image(str(media), use_container_width=True)

    with col_der:
        with st.container(border=True):
            for p in parrafos:
                st.write(p)

            st.markdown("---")
            cols = st.columns(len(botones))
            for i, texto_btn in enumerate(botones):
                if cols[i].button(texto_btn, key=f"{clave_prefix}_{i}", use_container_width=True):
                    return texto_btn

    return None


def textoCruce():
    # CAMINO TUNEL
    if st.session_state.destino == "Tunel" and st.session_state.cruce == "Trepar tunel":
        if st.session_state.mostrarTextoComo == 1:
            if mostrar_escena(
                parrafos=[
                    "Al entrar al túnel, distingues a tu derecha una escalera que se extiende por toda su longitud, ascendiendo hasta el techo y continuando en línea recta por su interior. Parece una opción perfecta para atravesarlo sin depender de ningún otro elemento. Sin embargo, no puedes evitar pensar que será arriesgado: tendrás que mantenerte en posición vertical durante un tiempo indeterminado. A pesar de tus dudas, decides seguir ese camino. Comienzas a avanzar y, poco a poco, el ambiente se vuelve cada vez más pesado.",
                    "Escuchas ruidos a tu alrededor, pero no logras distinguir de dónde provienen. De repente, algo aparece frente a ti. A primera vista, crees que se trata de una rata asquerosa, pero, a medida que se acerca, comienzas a distinguir mejor su silueta. Hay algo extraño en esa criatura: su cuerpo emite un tenue brillo que apenas ilumina la oscuridad del túnel…"
                ],
                media=RUTA_GIF / "tunelArriba.gif",
                botones=["Continuar"],
                clave_prefix="textoPicaroTunTrepar"
            ):
                st.session_state.mostrarTextoComo = 2
                st.rerun()

        elif st.session_state.mostrarTextoComo == 2:
            if mostrar_escena(
                parrafos=[
                    "¡Es una ardilla! ¿Una ardilla? ¿Aquí? La situación te resulta bastante extraña, pero la pequeña criatura se acerca y te observa con curiosidad. Luego, te hace una seña para que la sigas, indicándote el mismo camino que ya estabas recorriendo. Curiosamente, poco a poco comienzas a sentirte mejor: el ambiente se vuelve más ligero y recuperas tu velocidad habitual. Finalmente, distingues tu próximo desafío justo frente a ti…",
                    "✨ ¡Felicidades! Un compañero te eligió para acompañarte en tu aventura."
                ],
                media=RUTA_GIF / "tunelArdilla.gif",
                botones=["Continuar"],
                clave_prefix="textoPicaroTunTrepar2"
            ):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    elif st.session_state.destino == "Tunel" and st.session_state.cruce == "Cruzar el tunel":
        if st.session_state.mostrarTextoComo == 1:
            if mostrar_escena(
                parrafos=[
                    "Eres un pícaro, maestro del engaño y las trampas. Antes de continuar, decides analizar cuidadosamente el camino, prestando atención a cada detalle que logras distinguir en la penumbra. Nunca está de más ser precavido. Al examinar tu entorno, comienzas a notar ciertas irregularidades: piedras que sobresalen más de lo habitual, pequeños huecos sospechosamente bien distribuidos en las paredes y otras peculiaridades que difícilmente parecen producto de la casualidad…",
                    "Has visto este tipo de trampas millones de veces, así que sabes perfectamente cómo actuar. Confiado en tu experiencia, decides avanzar con cautela: esquivas una, luego otra y continúas sorteando cada obstáculo que encuentras en el camino. Así, poco a poco, consigues llegar hasta la mitad del recorrido. Desde allí ya logras visualizar la salida, aunque la escasa visibilidad te impide distinguir con claridad qué te espera más adelante…"
                ],
                media=RUTA_GIF / "trampasCueva.gif",
                botones=["Continuar"],
                clave_prefix="textoPicaroTunCruzar"
            ):
                st.session_state.mostrarTextoComo = 2
                st.rerun()

        elif st.session_state.mostrarTextoComo == 2:
            if mostrar_escena(
                parrafos=[
                    "Un suave tintineo comienza a resonar desde la parte más oscura del túnel. Entre las sombras distingues pequeños destellos dorados que aparecen y desaparecen rápidamente, hasta que finalmente revelan la figura de un gato tricolor. La criatura se acerca tranquilamente y pasa entre tus piernas. Al hacerlo, una tenue luz ilumina tus pasos y revela el camino que tienes por delante. Decides seguirlo, aprovechando su misteriosa compañía para continuar avanzando. Poco después, consigues llegar al final del recorrido…",
                    "✨ ¡Felicidades! Tienes un nuevo amigo de aventuras."
                ],
                media=RUTA_GIF / "gato.gif",
                botones=["Continuar"],
                clave_prefix="textoPicaroTunCruzar2"
            ):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    # CAMINO DE LA MONTAÑA
    elif st.session_state.destino == "Montaña Con Laberintos" and st.session_state.cruce == "Trepar montaña":
        if st.session_state.mostrarTextoComo == 1:
            if mostrar_escena(
                parrafos=[
                    "Decides trepar a un árbol y avanzar saltando de una rama a otra. Confías plenamente en tu agilidad y en el sigilo que has perfeccionado durante años, convencido de que podrás cruzar la montaña de esta manera. Sin embargo, las horas comienzan a pasar y, sin comida ni agua, el agotamiento empieza a hacerse notar. Tus manos resbalan cada vez más de los troncos y tu agarre pierde firmeza, pero aun así decides continuar. La tarde comienza a caer y, junto con ella, el viento aumenta su intensidad…",
                    "Comienzas a sentirte en peligro, pero tu terquedad puede más y decides continuar. Te preparas para saltar hacia un árbol lejano, pero una fuerte ráfaga de viento te empuja y terminas cayendo al suelo. Por suerte, sigues con vida, aunque el golpe y el agotamiento te dejan bastante debilitado. Te recuestas contra el tronco de un árbol y observas tu alrededor. Todo parece tranquilo… Pero, de repente…"
                ],
                media=RUTA_GIF / "ladronBosquito.gif",
                botones=["Continuar"],
                clave_prefix="textoPicaroMonTrepar"
            ):
                st.session_state.mostrarTextoComo = 2
                st.rerun()

        elif st.session_state.mostrarTextoComo == 2:
            if mostrar_escena(
                parrafos=[
                    "Un suave tintineo comienza a escucharse entre la oscuridad. A lo lejos, distingues pequeños destellos dorados que aparecen y desaparecen fugazmente, hasta que finalmente revelan la figura de un gato tricolor. Este se acerca tranquilamente y pasa entre tus piernas. Al hacerlo, una tenue luz comienza a iluminar tu entorno, revelando tanto tus pasos como el camino que tienes por delante. Decides seguirlo, confiando en aquella misteriosa compañía. Poco a poco, consigues atravesar el resto del recorrido y finalmente llegas al final…",
                    "✨ ¡Felicidades! Tienes un nuevo amigo de aventuras."
                ],
                media=RUTA_GIF / "gato.gif",
                botones=["Continuar"],
                clave_prefix="textoPicaroMonTrepar2"
            ):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    elif st.session_state.destino == "Montaña Con Laberintos" and st.session_state.cruce == "Cruzar La Montaña":
        if st.session_state.mostrarTextoComo == 1:
            if mostrar_escena(
                parrafos=[
                    "Decides que tu mejor opción es afrontar el riesgo y te adentras de lleno en el bosque que se extiende frente a ti. Al principio avanzas con determinación, pero pronto comienzas a notar que algo no está bien: el camino parece no llevar a ninguna parte y no haces más que dar vueltas una y otra vez. Ruidos extraños te acechan entre los árboles, mientras voces que no logras identificar comienzan a resonar en tu cabeza. La noche cae repentinamente y estás completamente perdido…",
                    "Un ruido repentino te saca de tus pensamientos. Sientes que algo se aproxima a gran velocidad entre la oscuridad. Decides quedarte quieto y observar. A lo lejos, apenas alcanzas a ver unos destellos dorados y pequeñas patitas que avanzan en tu dirección. Concentras la mirada hasta que logras distinguir de qué se trata…"
                ],
                media=RUTA_GIF / "picaLuciernagas.gif",
                botones=["Continuar"],
                clave_prefix="textoPicaroMonCruzar"
            ):
                st.session_state.mostrarTextoComo = 2
                st.rerun()

        elif st.session_state.mostrarTextoComo == 2:
            if mostrar_escena(
                parrafos=[
                    "¡Es una ardilla! ¿Una ardilla? ¿Aquí? La situación te resulta bastante extraña, pero la pequeña criatura se acerca y te observa con curiosidad. Luego, te hace una seña para que la sigas, indicándote el mismo camino que ya estabas recorriendo. Curiosamente, comienzas a sentirte mejor: el ambiente se vuelve más ligero y recuperas tu velocidad habitual. Con las energías renovadas, levantas la mirada y distingues tu próximo desafío justo frente a ti…",
                    "✨ ¡Felicidades! Un compañero te eligió para acompañarte en tu aventura."
                ],
                media=RUTA_GIF / "ultimo.gif",
                botones=["Continuar"],
                clave_prefix="textoPicaroMonCruzar2"
            ):
                st.session_state.mostrarTextoComo = 0
                st.rerun()


def informacion_explorador():
    if mostrar_escena(
        parrafos=[
            "Eres un pícaro explorador en busca de su propio camino. Has engañado a personas, mentido y robado para sobrevivir, pero jamás te han descubierto. Eres ágil, astuto y posees un encanto envidiable; tienes la capacidad de convencer hasta a la persona más desconfiada del planeta. Tu fortaleza mental es admirable y tus habilidades de supervivencia, excepcionales.",
            "En tu día a día, hay una frase que siempre ronda tus pensamientos: «Cuantos más obstáculos superes, mayor será tu sabiduría». Después de todo, eres un aprendiz de la vida misma.",
            "Un día, mientras recorrías tu camino, encontraste un cartel que anunciaba tu próximo desafío: escapar de una mazmorra. Lo observaste por un momento y pensaste… ¿Por qué no?"
        ],
        media=RUTA_GIF / "elPicaPica.gif",
        botones=["Comenzar mi travesía"],
        clave_prefix="continuar_historia_explorador"
    ):
        st.session_state.informacion = 0
        st.rerun()


def elegir_camino_explorador():
    st.markdown("<h3 style='text-align: center;'>Hiciste la elección de personaje, tu rumbo ha comenzado</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>¿A dónde quieres ir?</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        with st.container(border=True):
            st.image(str(RUTA_IMG / "picaroTunel.png"), use_container_width=True)
            if st.button("🕳️ Tunel", key="btn_destino_tunel", use_container_width=True):
                st.session_state.destino = "Tunel"
                st.session_state.etapa = 3
                st.rerun()

    with col2:
        with st.container(border=True):
            st.image(str(RUTA_IMG / "picaMontaña.png"), use_container_width=True)
            if st.button("⛰️ Montaña Con Laberintos", key="btn_destino_montana", use_container_width=True):
                st.session_state.destino = "Montaña Con Laberintos"
                st.session_state.etapa = 3
                st.rerun()


def etapa_3_explorador():
    if st.session_state.destino == "Tunel":
        eleccion = mostrar_escena(
            parrafos=[
                "Te encuentras frente a un túnel de dimensiones colosales, especialmente para alguien de tu tamaño. Te detienes a observarlo mientras analizas tus posibilidades.",
                "Después de darle varias vueltas al asunto, solo consigues imaginar dos maneras de atravesarlo… ¿Cuál eliges?"
            ],
            media=RUTA_IMG / "picaroTunel.png",
            botones=["Trepar tunel", "Cruzar el tunel"],
            clave_prefix="cruce_explorador_tunel"
        )
    elif st.session_state.destino == "Montaña Con Laberintos":
        eleccion = mostrar_escena(
            parrafos=[
                "Comienzas tu recorrido por la montaña. La inmensidad del paisaje te abruma por un instante, pero no tardas en recuperar la compostura. Recuerdas todo lo que has superado hasta ahora y te convences de que eres capaz de afrontar cualquier desafío.",
                "Después de todo, nada podrá detenerte… ¿Cuál eliges?"
            ],
            media=RUTA_IMG / "picaMontaña.png",
            botones=["Trepar montaña", "Cruzar La Montaña"],
            clave_prefix="cruce_explorador_montana"
        )
    else:
        return

    if eleccion:
        st.session_state.cruce = eleccion
        st.session_state.etapa = 4
        st.rerun()


def etapa_4_explorador():
    if st.session_state.cruce in ["Trepar tunel", "Cruzar La Montaña"]:
        st.session_state.mascota = "Ardilla"
    elif st.session_state.cruce in ["Cruzar el tunel", "Trepar montaña"]:
        st.session_state.mascota = "Gato Tricolor"

    st.session_state.etapa = "MAZMORRA"
    st.rerun()


def etapa_5_explorador():
    if st.session_state.mascota == "Ardilla":
        eleccion = mostrar_escena(
            parrafos=[
                "Llegas a la entrada de la mazmorra y te encuentras con dos caminos, uno encima del otro. El pasillo inferior desprende un olor nauseabundo y repulsivo, aunque la oscuridad no te permite distinguir qué se esconde en su interior.",
                "Por otro lado, el pasillo superior no presenta ningún olor extraño, pero puedes escuchar cómo el viento se desliza entre sus paredes, produciendo un inquietante silbido… ¿Por dónde eliges ir?"
            ],
            media=RUTA_IMG / "tunelCaminos.png",
            botones=["Entrada Superior", "Entrada Inferior"],
            clave_prefix="sala_explorador_ardilla"
        )
    elif st.session_state.mascota == "Gato Tricolor":
        eleccion = mostrar_escena(
            parrafos=[
                "Llegas a la entrada de la mazmorra y te encuentras con dos caminos, uno sobre el otro. El pasillo inferior desprende un olor nauseabundo y repulsivo, aunque no logras distinguir qué se esconde en su interior.",
                "Por otro lado, el pasillo superior no presenta ningún olor extraño, pero puedes escuchar cómo el viento roza sus paredes, produciendo un suave y constante silbido… ¿Por dónde eliges ir?"
            ],
            media=RUTA_IMG / "tunelCaminos.png",
            botones=["Pasillo Abajo", "Pasillo Arriba"],
            clave_prefix="sala_explorador_gato"
        )
    else:
        return

    if eleccion:
        st.session_state.salaInicial = eleccion
        st.session_state.etapa = 6
        st.rerun()


def etapa_6_explorador():
    sala = st.session_state.salaInicial

    if sala == "Entrada Superior":
        eleccion = mostrar_escena(
            parrafos=[
                "Decides adentrarte por el pasillo superior; por alguna razón, tienes un buen presentimiento. Sin embargo, apenas avanzas, una repentina corriente de aire proveniente de los niveles inferiores te envuelve y te impulsa violentamente hacia arriba, haciéndote volar hasta uno de los pisos más altos de la mazmorra. Al recuperar el equilibrio, te encuentras cara a cara con un enorme enjambre de murciélagos y ratas.",
                "Antes de dejarte llevar por el pánico, te aseguras de que tu pequeño amigo roedor esté a salvo. Tu mente trabaja a toda velocidad buscando una solución entre tanto caos. Piensas: ¿Qué hago?…"
            ],
            media=RUTA_GIF / "excapeRuinas.gif",
            botones=["¡Snif Snif!", "¡Flish, flash flish!"],
            clave_prefix="bat_exp_sup"
        )
    elif sala == "Entrada Inferior":
        eleccion = mostrar_escena(
            parrafos=[
                "Te adentras por el pasillo inferior y avanzas unos pocos pasos, intentando distinguir qué se esconde entre la oscuridad. De repente, una potente corriente de aire descendente te empuja con una fuerza descomunal, haciéndote perder el equilibrio.",
                "El impacto es tan intenso que el suelo cede bajo tus pies, provocando que caigas junto con los escombros y quedes atrapado bajo ellos… ¿Resistirás?"
            ],
            media=RUTA_GIF / "caidaMazmorra.gif",
            botones=["¡Snif Snif!", "Crack crack"],
            clave_prefix="bat_exp_inf"
        )
    elif sala == "Pasillo Abajo":
        eleccion = mostrar_escena(
            parrafos=[
                "Entras con total confianza por el pasillo inferior. Tras avanzar un poco, tomas el camino de la izquierda, pero tu recorrido termina frente a una antigua reja de hierro oxidado, cerrada con un candado tan viejo como el lugar mismo…",
                "A tus pies, el agua estancada libera un gas verdoso e inflamable que irrita tus ojos. De repente, el gato tricolor comienza a bufar en dirección al techo, erizando su pelaje mientras un tenue resplandor protector los envuelve a ambos. ¿Qué haces?"
            ],
            media=RUTA_GIF / "ruinas.gif",
            botones=["Forzar Cerrojo", "Explotar Bisagra"],
            clave_prefix="bat_exp_abajo"
        )
    elif sala == "Pasillo Arriba":
        eleccion = mostrar_escena(
            parrafos=[
                "Decides tomar el camino de la derecha, atravesando una galería estrecha donde el barro te llega hasta los tobillos. De repente, pisas una losa suelta que cede bajo tu peso y revela una fosa repleta de agua turbia y escombros…",
                "Desde las grietas de los muros laterales comienzan a escucharse chillidos inquietantes: enormes roedores subterráneos aparecen atraídos por el olor. En cuestión de segundos te encuentras rodeado por una plaga hambrienta… Piensas: ¿Qué hago?…"
            ],
            media=RUTA_GIF / "tunelRata.gif",
            botones=["Salto", "Uso De La Capa"],
            clave_prefix="bat_exp_arriba"
        )
    else:
        return

    if eleccion:
        st.session_state.opcionBatalla = eleccion
        st.session_state.etapa = 7
        st.rerun()


def etapa_7_explorador():
    sala = st.session_state.salaInicial
    opcion = st.session_state.opcionBatalla

    if sala == "Entrada Superior" and opcion == "¡Snif Snif!":
        if mostrar_escena(
            parrafos=[
                "Tu pequeño amigo roedor llama tu atención y te hace una seña para que toques su nariz, que comienza a emitir un tenue resplandor. Con curiosidad, acercas tu mano y rozas su pequeña naricita. En ese instante, una luz ilumina el camino frente a ti, revelando una posible ruta hacia la salida. Aprovechas el impulso de energía y te apresuras a seguir el sendero iluminado…"
            ],
            media=RUTA_GIF / "salidaRuina.gif",
            botones=["Continuar"],
            clave_prefix="et7_exp_1"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Entrada Superior" and opcion == "¡Flish, flash flish!":
        if mostrar_escena(
            parrafos=[
                "Llegas al lugar hasta donde aquella corriente de viento te había arrastrado y te topas con enormes enjambres de murciélagos y ratas frenéticos. Un chillido de dolor de tu pequeño amigo roedor te devuelve a la realidad: ¡una de las ratas lo ha mordido!…",
                "Lo recoges rápidamente y lo proteges entre tus brazos mientras intentas abrirte paso a empujones. Sin embargo, pronto recuerdas que la fuerza bruta nunca ha sido tu especialidad… y cada vez te resulta más difícil avanzar."
            ],
            media=RUTA_GIF / "excapeRuinasFallado.gif",
            botones=["Continuar"],
            clave_prefix="et7_exp_2"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Entrada Inferior" and opcion == "¡Snif Snif!":
        if mostrar_escena(
            parrafos=[
                "Tu pequeño amigo roedor se acerca a ti con sus patitas envueltas en un brillo intenso, invitándote a tocarlas. Al hacerlo, una luz lo envuelve por completo y su cuerpo comienza a crecer hasta alcanzar cinco veces su tamaño original. ¡Su transformación es increíble! Ahora, convertido en un roedor gigantesco, comienza a cavar a una velocidad extraordinaria, abriéndoles paso hacia un lugar seguro…"
            ],
            media=RUTA_GIF / "excapeCalabaza.gif",
            botones=["Continuar"],
            clave_prefix="et7_exp_3"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Entrada Inferior" and opcion == "Crack crack":
        if mostrar_escena(
            parrafos=[
                "El pelaje de tu pequeño amigo roedor comienza a desprender destellos dorados. ¡Su misterioso poder es real! A medida que su brillo se intensifica, sientes cómo una nueva energía recorre tu cuerpo.",
                "El dolor disminuye y recuperas parte de tus fuerzas, como si aquel misterioso brillo te hubiera devuelto la vitalidad. Sin perder ni un segundo, comienzas a cavar con renovado entusiasmo y avanzas todo lo rápido que puedes…"
            ],
            media=RUTA_GIF / "excapeALuz.gif",
            botones=["Continuar"],
            clave_prefix="et7_exp_4"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Abajo" and opcion == "Forzar Cerrojo":
        if mostrar_escena(
            parrafos=[
                "Decides utilizar tus ganzúas para forzar el cerrojo lo más rápido posible. Cada segundo cuenta y la presión aumenta: el poder protector de tu amigo felino todavía no está lo suficientemente desarrollado como para mantenerte a salvo de aquel gas tóxico. Te ves obligado a soportar sus efectos mientras concentras toda tu atención en la cerradura…"
            ],
            media=RUTA_IMG / "picaCandado.png",
            botones=["Continuar"],
            clave_prefix="et7_exp_5"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Abajo" and opcion == "Explotar Bisagra":
        if mostrar_escena(
            parrafos=[
                "Recuerdas el consejo de un viejo sabio y buscas en tu bolsa un pedernal que guardabas por precaución. Solo cuentas con el gas acumulado y tu pedernal, pero necesitas una chispa…",
                "Tu amigo tricolor parece darse cuenta de lo que intentas conseguir. De repente, su pelaje comienza a erizarse, desprendiendo pequeñas chispas. ¡BOOM! Una fuerte explosión hace saltar la reja de golpe. ¡Las chispas de tu compañero felino fueron la clave para abrirte paso!"
            ],
            media=RUTA_GIF / "boom.gif",
            botones=["Continuar"],
            clave_prefix="et7_exp_6"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Arriba" and opcion == "Salto":
        if mostrar_escena(
            parrafos=[
                "Justo antes de caer, tu instinto de supervivencia se activa y reaccionas rápidamente: saltas hacia una de las paredes y clavas tu daga para conseguir sujetarte. Apenas un instante después, tu amigo felino también salta en tu dirección, aferrándose a ti antes de trepar hasta una viga cercana. Ambos consiguen mantenerse a salvo…"
            ],
            media=RUTA_GIF / "rescateGato.gif",
            botones=["Continuar"],
            clave_prefix="et7_exp_7"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Arriba" and opcion == "Uso De La Capa":
        if mostrar_escena(
            parrafos=[
                "Decides cubrirte con tu capa para protegerte de aquella plaga, pero el miedo te paraliza y no consigues moverte. Recibes varios golpes mientras permaneces inmóvil, hasta que, de un momento a otro, dejas de sentir cualquier molestia.",
                "¡Sorpresa! ¡Tu amigo felino también tiene poderes! Con tan solo hacer sonar su pequeña campanita dos veces, consigue que ambos comiencen a levitar, elevándolos suavemente por encima del suelo y alejándolos del peligro…"
            ],
            media=RUTA_GIF / "elGatoVolador.gif",
            botones=["Continuar"],
            clave_prefix="et7_exp_8"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()


def infoSalia():
    if st.session_state.condicionSalida == 2:
        st.error("💀 No lograste escapar de la mazmorra")
        if st.button("Continuar", key="fin_malo_exp"):
            st.session_state.etapa = 10
            st.rerun()
    elif st.session_state.condicionSalida == 1:
        st.success("🏆 ¡Felicidades! Lograste escapar de la mazmorra")
        if st.button("Continuar", key="fin_bueno_exp"):
            st.session_state.etapa = 10
            st.rerun()


def finalAventura():
    sala = st.session_state.salaInicial
    opcion = st.session_state.opcionBatalla

    if sala == "Entrada Superior" and opcion == "¡Snif Snif!":
        st.session_state.etapa = 9
        st.rerun()

    elif sala == "Entrada Superior" and opcion == "¡Flish, flash flish!":
        if mostrar_escena(
            parrafos=[
                "Tu cuerpo comienza a resentirse ante la cantidad de golpes y rasguños recibidos. Son demasiadas criaturas atacando al mismo tiempo y, por más que intentes resistir, tu resistencia tiene un límite. Poco a poco, te resulta cada vez más difícil soportar el embate de aquella plaga…"
            ],
            media=RUTA_GIF / "ruinaSinExcape.gif",
            botones=["Continuar"],
            clave_prefix="fin_exp_1"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Entrada Inferior" and opcion == "¡Snif Snif!":
        if mostrar_escena(
            parrafos=[
                "Entre los montones de tierra comienzas a distinguir pequeños rayos de luz que se filtran desde el exterior. ¡La salida está cerca! Gracias a la ayuda de tu pequeño amigo roedor, consigues abrirte paso entre la tierra acumulada y finalmente logras escapar de la mazmorra…"
            ],
            media=RUTA_GIF / "salidaTunel.gif",
            botones=["Continuar"],
            clave_prefix="fin_exp_2"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Entrada Inferior" and opcion == "Crack crack":
        if mostrar_escena(
            parrafos=[
                "Parece que tu plan está funcionando y consigues acercarte cada vez más a la salida. Sin embargo, el viento sopla con tanta fuerza que avanzar se vuelve cada vez más complicado. Por más que intentas continuar, cada paso requiere un esfuerzo enorme…"
            ],
            media=RUTA_GIF / "sinEscape.gif",
            botones=["Continuar"],
            clave_prefix="fin_exp_3"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Abajo" and opcion == "Forzar Cerrojo":
        if mostrar_escena(
            parrafos=[
                "Finalmente consigues abrir el cerrojo. Con las pocas fuerzas que te quedan, atraviesas la reja y alcanzas el otro lado. Por fin puedes respirar aire fresco, pero el alivio dura poco: el agotamiento y los efectos del gas terminan pasándote factura y, apenas das unos pasos, pierdes el conocimiento…"
            ],
            media=RUTA_GIF / "gasVeneno.gif",
            botones=["Continuar"],
            clave_prefix="fin_exp_4"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Abajo" and opcion == "Explotar Bisagra":
        if mostrar_escena(
            parrafos=[
                "Tú y tu amigo felino se apresuran a atravesar el hueco que ha quedado en la reja, logrando escapar hacia un pasadizo oculto que conduce a una salida secreta de la mazmorra…"
            ],
            media=RUTA_GIF / "escapeluz.gif",
            botones=["Continuar"],
            clave_prefix="fin_exp_5"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Arriba" and opcion == "Salto":
        if mostrar_escena(
            parrafos=[
                "Deciden saltar juntos hacia el siguiente nivel y, tras un arriesgado impulso, consiguen llegar al otro lado. Sin embargo, en medio de la emoción por haber superado el obstáculo, olvidaron considerar una posibilidad: ¡todavía podrían aparecer más roedores subterráneos!…"
            ],
            media=RUTA_GIF / "spiderman.gif",
            botones=["Continuar"],
            clave_prefix="fin_exp_6"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Arriba" and opcion == "Uso De La Capa":
        if mostrar_escena(
            parrafos=[
                "…hasta conseguir llevarlos a un lugar seguro, donde ambos puedan recuperarse y continuar su camino."
            ],
            media=RUTA_GIF / "escapeTunelVuela.gif",
            botones=["Continuar"],
            clave_prefix="fin_exp_7"
        ):
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
        if st.session_state.mostrarTextoComo in [1, 2]:
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
    elif etapa == 9:
        infoSalia()
