# Puupallo-asuntosimulaattori

Puopololle simulaattori - Vertaile omistusasumisen ja vuokra-asumisen + osakesijoittamisen taloudellisia vaikutuksia ajan kuluessa.

🌐 **Julkaistu sovellus:** https://puupallo-asuntosimulaattori.streamlit.app/

## Ominaisuudet

- Simuloi nettovarallisuuden kehitystä 5-40 vuoden ajanjaksolla
- Vertaile omistusasunnon ja vuokra-asumisen + osakesijoittamisen kustannuksia
- Ota huomioon kaikki merkittävät kulut: vastike, kiinteistövero, remonttivara, varainsiirtovero, myyntikulut, jne.
- Visualisoi tulokset kuvaajalla

## Paikallinen käyttö

1. Asenna riippuvuudet:
   ```bash
   pip install -r requirements.txt
   ```

2. Käynnistä sovellus:
   ```bash
   streamlit run app.py
   ```

3. Avaa selaimessa osoite, joka näkyy terminaalissa (yleensä `http://localhost:8501`)

## Tiedostorakenne

- `app.py` - Streamlit-käyttöliittymä
- `simulaatio.py` - Laskentamoottori (ei Streamlitiä, ei I/O:ta)
- `requirements.txt` - Python-riippuvuudet
- `INSTRUCTIONS.md` - Projektiohjeet kehittäjille
- `TESTAUSOHJEET.md` - Testausohjeet

## Teknologiat

- Python 3.10+
- Streamlit
- pandas
- matplotlib
