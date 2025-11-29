# Asunto vs vuokra -simulaattori - Projektiohjeet

## Projektin nimi
"Asunto vs vuokra -simulaattori"

## Stack
Python 3.10+, Streamlit, pandas, matplotlib. Ei muita riippuvuuksia ilman erillistä lupaa.

## Hakemistorakenne

* `simulaatio.py` = pelkkä laskentamoottori (ei Streamlitiä, ei I/O:ta).

* `app.py` = Streamlit-käyttöliittymä, joka käyttää `simulate_detailed`-funktiota.

* `requirements.txt` = `streamlit`, `pandas`, `matplotlib`.

## `simulaatio.py`

* Säilytä funktiot `annuity_payment` ja `simulate_detailed`.

* Älä muuta funktioiden parametreja ilman että päivität vastaavasti `app.py`:n kutsun.

* Pidä koodi deterministisenä, ei globaaleja sivuvaikutuksia.

## `app.py`

* Käytä `from simulaatio import simulate_detailed`.

* UI rakennetaan Streamlit-komponenteilla:

  * Vasemmassa sivupalkissa perusparametrit (vuodet, asunnon hinta, oma pääoma, korko, laina-aika).

  * Pääalueella kolme saraketta:

    1. Omistusasunnon juoksevat kulut (vastike, kiinteistövero, remonttivara €/v, omistajan muut kulut, arvonnousu).

    2. Vuokra (vuokra €/kk, vuokrankorotus, vuokralaisen muut kulut).

    3. Sijoitukset (alkusijoitus, osaketuotto, varainsiirtovero %, myyntikulut %, checkbox negatiiviselle säästölle).

* Kutsu `simulate_detailed` suoraan UI-parametreista, muista muuntaa prosentit desimaaleiksi (`/100`).

* Näytä:

  * Tekstiyhteenveto 10/20/… vuoden nettovarallisuudesta.

  * Matplotlib-kuvaaja nettovarallisuuskäyristä (omistus vs vuokra+sijoitukset).

  * `st.dataframe(df.tail())` viimeisistä riveistä.

## Testaus

* Paikallisesti komento `streamlit run app.py`.

* Koodi ei saa kaatua sliderien ääriarvoilla (esim. 0 € remonttivara, 0 % korko, 0 € vuokra).

## Koodityyli

* Selkeät suomenkieliset docstringit / kommentit liiketoimintalogiikasta.

* Ei tarpeetonta monimutkaisuutta, pidä funktiot lyhyinä ja luettavina.

## Deploy

* Huolehdi, että `requirements.txt`, `app.py` ja `simulaatio.py` ovat repossa juuritasolla, jotta Streamlit Cloud osaa käynnistää sovelluksen komennolla `streamlit run app.py`.

