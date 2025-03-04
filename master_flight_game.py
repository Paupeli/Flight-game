#
# !!!!! MUISTA TEHDÄ OMA BRANCH !!!!!!!! ENNEN KUIN MUOKKAAT !!!!! (ohjeet discordissa #repo)
#
# Pushataan tänne vain valmista (tai melkein valmista) koodia, testata voi vapaasti
# Aluksi saattaa olla ettei mikään vielä toimi, ok tehtä "raakile"

# Muista kommentoida koodiasi !!!


# PELIN RAKENNE

# 0 A ) SQL-connector (yhteinen salasana)
# 0 B ) IMPORTIT TÄHÄN (import.random, jne)
# 0 C ) FUNKTIOT / DEF TAITAA TULLA TÄNNE AINAKIN LOPUKSI

# 1) ALOITUSRUUTU (Grafiikka, ääni?) (**JOHANNA**)

# 2) MAIN MENU, SCOREBOARD (**OUTI**) JA UUDEN PELIN LUONTI (**RONI**)
    # > Aloita peli
        # >> Valitse hahmo (huom. game.location pitää päivittää)
        # >> Luo uusi hahmo
            # >>> Valitse, kuinka pitkä peli (**RONI**)
                # Tässä kohtaa "tallennetaan" arvotut Euroopan maat ja kentät alkavaa peliä varten ! (Ronin koodi)
    # > Katso scoreboard
    # > Ohjeet
    # > Lopeta peli

# 3) PELIN PERUSKULKU: LIIKKUMINEN, KYSYMYKSET JA TEHTÄVÄT
    # Pelaaja aloittaa Helsingistä: Peli ilmoittaa sijainnin (grafiikka, ääni?)

    # Peli kysyy vihjekysymyksen (**PAULIINA**)
            #VÄÄRÄ VASTAUS
                # -50 pistettä
                # Ilmoitus väärästä vastauksesta, siirtyminen vastauksen mukaiselle kentälle
                # Uusi vihjekysymys oikeasta kentästä / kaupungista
                # 3 kentän jälkeen peli loppuu >> Kohta 4, pelin päättyminen

            #OIKEA VASTAUS
                # +100 pistettä
                # Ilmoitus oikeasta vastauksesta, siirtyminen oikealle mukaiselle kentälle

    # Tehtävä kohteessa (**PAULIINA**)
        # Oikea vastaus +50, väärä vastaus -25
        # Ilmoitus käyttäjälle vastauksesta ja pisteistä
        # >>> Peli kysyy vihjekysymyksen uudesta kohteesta (edellinen osio)

# 4) PELIN PÄÄTTYMINEN



    # Pelaaja