import streamlit as st

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="optimizate ñaño",
    layout="centered"
)

# =====================================================
# COLORES PERSONALIZADOS
# =====================================================

st.markdown("""
<style>

/* ATAQUE */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Ataque"]{
    background-color: orange !important;
}

/* PRECISION */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Precision"]{
    background-color: #ff9500 !important;
}

/* CRITICA */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Critica"]{
    background-color: red !important;
}

/* DAÑO CRITICO */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="DañoCritico"]{
    background-color: #ff2b2b !important;
}

/* ARMADURA */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Armadura"]{
    background-color: gray !important;
}

/* ESQUIVA */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Esquiva"]{
    background-color: #8a8a8a !important;
}

/* SALUD */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Salud"]{
    background-color: darkgreen !important;
}

/* BOTIN */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Botin"]{
    background-color: limegreen !important;
}

/* HAMBRE */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Hambre"]{
    background-color: #7b1e3a !important;
}

/* EMPRENDIMIENTO */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Emprendimiento"]{
    background-color: hotpink !important;
}

/* ENERGIA */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Energia"]{
    background-color: navy !important;
}

/* PRODUCCION */
div[data-testid="stProgressBar"] div[role="progressbar"][aria-label="Produccion"]{
    background-color: gold !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITULO
# =========================================================

st.title("🇪🇨 optimizate ñaño")

st.write("Sistema automático de builds")

# =========================================================
# ENTRADAS
# =========================================================

modo = st.selectbox(
    "Selecciona el modo",
    ["war", "eco"]
)

nivel_jugador = st.number_input(
    "Nivel del jugador",
    min_value=1,
    value=28
)

empresas_deseadas = st.number_input(
    "Cantidad de empresas",
    min_value=2,
    max_value=12,
    value=9
)

# =========================================================
# BOTON
# =========================================================

if st.button("🇪🇨 CALCULAR BUILD"):

    # =====================================================
    # PUNTOS
    # =====================================================

    puntos_totales = nivel_jugador * 4

    # =====================================================
    # COSTO EMPRESAS
    # =====================================================

    niveles_empresas = empresas_deseadas - 2

    costo_empresas = 0

    for i in range(1, niveles_empresas + 1):

        costo_empresas += i

    puntos = puntos_totales - costo_empresas

    # =====================================================
    # INFO
    # =====================================================

    st.subheader("📊 INFORMACIÓN")

    st.write(f"Nivel jugador: {nivel_jugador}")

    st.write(f"Puntos totales: {puntos_totales}")

    st.write(f"Empresas: {empresas_deseadas}")

    st.write(f"Costo empresas: {costo_empresas}")

    st.write(f"Puntos restantes: {puntos}")

    # =====================================================
    # VALIDACION
    # =====================================================

    if puntos <= 0:

        st.error("No tienes suficientes puntos")

    else:

        # =================================================
        # WAR MODE
        # =================================================

        if modo == "war":

            stats = {

                "Ataque": {
                    "valor": 100,
                    "incremento": 25,
                    "maximo": 350,
                    "nivel": 0
                },

                "Precision": {
                    "valor": 50,
                    "incremento": 5,
                    "maximo": 100,
                    "nivel": 0
                },

                "Critica": {
                    "valor": 10,
                    "incremento": 5,
                    "maximo": 60,
                    "nivel": 0
                },

                "DañoCritico": {
                    "valor": 100,
                    "incremento": 20,
                    "maximo": 300,
                    "nivel": 0
                },

                "Armadura": {
                    "valor": 0,
                    "incremento": 6,
                    "maximo": 60,
                    "nivel": 0
                },

                "Esquiva": {
                    "valor": 0,
                    "incremento": 4,
                    "maximo": 40,
                    "nivel": 0
                },

                "Salud": {
                    "valor": 100,
                    "incremento": 10,
                    "maximo": 200,
                    "nivel": 0
                },

                "Botin": {
                    "valor": 5,
                    "incremento": 2,
                    "maximo": 25,
                    "nivel": 0
                },

                "Hambre": {
                    "valor": 4,
                    "incremento": 1,
                    "maximo": 14,
                    "nivel": 0
                }
            }

        # =================================================
        # ECO MODE
        # =================================================

        else:

            stats = {

                "Emprendimiento": {
                    "valor": 30,
                    "incremento": 5,
                    "maximo": 80,
                    "nivel": 0
                },

                "Energia": {
                    "valor": 30,
                    "incremento": 10,
                    "maximo": 130,
                    "nivel": 0
                },

                "Produccion": {
                    "valor": 10,
                    "incremento": 3,
                    "maximo": 40,
                    "nivel": 0
                }
            }

        # =================================================
        # FUNCION WAR
        # =================================================

        def calcular_war(build):

            ataque = build["Ataque"]["valor"]

            precision = (
                build["Precision"]["valor"] / 100
            )

            critica = (
                build["Critica"]["valor"] / 100
            )

            daño_critico = (
                build["DañoCritico"]["valor"] / 100
            )

            armadura = build["Armadura"]["valor"]

            esquiva = build["Esquiva"]["valor"]

            salud = build["Salud"]["valor"]

            botin = build["Botin"]["valor"]

            hambre = build["Hambre"]["valor"]

            # =============================================
            # DAÑO
            # =============================================

            daño_base = ataque * precision

            bonus_critico = (
                daño_base *
                critica *
                daño_critico
            )

            daño_total = (
                daño_base +
                bonus_critico
            )

            # =============================================
            # DEFENSA
            # =============================================

            defensa = (
                armadura * 2.4 +
                esquiva * 3.2 +
                salud * 1.2
            )

            # =============================================
            # UTILIDAD
            # =============================================

            utilidad = (
                hambre * 14 +
                botin * 5
            )

            # =============================================
            # PRIORIDADES
            # =============================================

            prioridad_precision = (
                precision * 170
            )

            prioridad_critica = (
                critica * 145
            )

            prioridad_salud = (
                salud * 0.8
            )

            prioridad_hambre = (
                hambre * 10
            )

            # =============================================
            # SINERGIA
            # =============================================

            sinergia = (
                precision *
                critica *
                daño_critico *
                120
            )

            # =============================================
            # BALANCE
            # =============================================

            diferencia = max(
                ataque / 3,
                precision * 100,
                critica * 100,
                daño_critico / 2,
                salud / 2
            ) - min(
                ataque / 3,
                precision * 100,
                critica * 100,
                daño_critico / 2,
                salud / 2
            )

            penalizacion = diferencia * 0.7

            return (

                daño_total +

                defensa +

                utilidad +

                prioridad_precision +

                prioridad_critica +

                prioridad_salud +

                prioridad_hambre +

                sinergia -

                penalizacion
            )

        # =================================================
        # FUNCION ECO
        # =================================================

        def calcular_eco(build):

            emprendimiento = (
                build["Emprendimiento"]["valor"]
            )

            energia = (
                build["Energia"]["valor"]
            )


            produccion = (
                build["Produccion"]["valor"]
            )

            economia = produccion * 12

            economia += emprendimiento * 2

            economia += energia * 1.5

            economia *= (
                1 + empresas_deseadas * 0.12
            )

            return economia

        # =================================================
        # OPTIMIZADOR
        # =================================================

        while puntos > 0:

            mejor_stat = None

            mejor_ratio = -999999

            for nombre, datos in stats.items():

                if datos["valor"] >= datos["maximo"]:
                    continue

                costo = datos["nivel"] + 1

                if costo > puntos:
                    continue

                temp = {}

                for n, d in stats.items():

                    temp[n] = d.copy()

                temp[nombre]["valor"] += (
                    datos["incremento"]
                )

                temp[nombre]["nivel"] += 1

                if modo == "war":

                    actual = calcular_war(stats)

                    nuevo = calcular_war(temp)

                else:

                    actual = calcular_eco(stats)

                    nuevo = calcular_eco(temp)

                mejora = nuevo - actual

                ratio = mejora / costo

                if ratio > mejor_ratio:

                    mejor_ratio = ratio

                    mejor_stat = nombre

            if mejor_stat is None:
                break

            costo = (
                stats[mejor_stat]["nivel"] + 1
            )

            stats[mejor_stat]["nivel"] += 1

            stats[mejor_stat]["valor"] += (
                stats[mejor_stat]["incremento"]
            )

            puntos -= costo

        # =================================================
        # RESULTADOS
        # =================================================

        st.subheader("🇪🇨 BUILD ÓPTIMA 🇪🇨")

        st.write(f"Modo: {modo.upper()}")

        st.write("---")

        for nombre, datos in stats.items():

            progreso = (
                datos["valor"] /
                datos["maximo"]
            )

            st.write(
                f"✅ {nombre}: "
                f"{datos['valor']} "
                f"(Lvl {datos['nivel']})"
            )

            st.progress(
                min(progreso, 1.0),
                text=nombre
            )

        st.write("---")

        st.success(
            f"🪙 Puntos sobrantes: {puntos}"
        )

   
            
# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<hr style="border:1px solid #30363d; margin-top:40px;">

<div style="
text-align:center;
color:#8b949e;
font-size:14px;
padding:20px;
">

Developed by <b>Antonio Pluas</b><br>
War Era Ecuadorian company© 2026

</div>
""", unsafe_allow_html=True)

