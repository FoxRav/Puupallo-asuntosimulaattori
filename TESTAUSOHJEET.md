# Testausohjeet - Asunto vs vuokra -simulaattori

## Projektin rakenne

Projektin juuritasolla pitäisi olla:
- `app.py` - Streamlit-käyttöliittymä
- `simulaatio.py` - Laskentamoottori
- `requirements.txt` - Riippuvuudet
- `INSTRUCTIONS.md` - Projektiohjeet

**HUOM:** `.venv`-kansiossa ei pitäisi olla projektitiedostoja, vain Python-paketit.

## Asennus

1. Aktivoi virtuaaliympäristö (jos ei ole aktiivinen):
   ```bash
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   
   # Windows CMD
   .venv\Scripts\activate.bat
   
   # Linux/Mac
   source .venv/bin/activate
   ```

2. Asenna riippuvuudet (jos ei ole asennettu):
   ```bash
   pip install -r requirements.txt
   ```

## Perustestaus

1. Käynnistä Streamlit-sovellus:
   ```bash
   streamlit run app.py
   ```

2. Avaa selaimessa osoite, joka näkyy terminaalissa (yleensä `http://localhost:8501`)

3. Tarkista että:
   - Sivupalkissa näkyvät perusparametrit
   - Pääalueella on kolme saraketta (Omistusasunto, Vuokra, Sijoitukset)
   - Yhteenveto näkyy oikein
   - Kuvaaja piirtyy
   - Viimeiset datarivit näkyvät

## Ääriarvojen testaus

Testaa että koodi ei kaadu seuraavilla ääriarvoilla:

### Testi 1: Nollakorko
- Aseta "Lainan korko %/v" = 0.0
- Tarkista että laskenta toimii (ei jakoa nollalla)

### Testi 2: Nollaremonttivara
- Aseta "Remonttivara €/v" = 0
- Tarkista että laskenta toimii

### Testi 3: Nollavuokra
- Aseta "Vuokra €/kk" = 0
- Tarkista että laskenta toimii

### Testi 4: Negatiivinen arvonnousu
- Aseta "Asunnon arvonnousu %/v" = -5.0
- Tarkista että laskenta toimii

### Testi 5: Negatiivinen osaketuotto
- Aseta "Osaketuotto %/v (netto)" = -5.0
- Tarkista että laskenta toimii

### Testi 6: Oma pääoma = asunnon hinta
- Aseta "Oma pääoma (€)" = "Asunnon hinta (€)"
- Tarkista että laskenta toimii (ei lainaa)

### Testi 7: Oma pääoma > asunnon hinta
- Aseta "Oma pääoma (€)" suuremmaksi kuin "Asunnon hinta (€)"
- Tarkista että laskenta toimii

### Testi 8: Minimiajat
- Aseta "Vuodet" = 5
- Aseta "Laina-aika (v)" = 5
- Tarkista että laskenta toimii

### Testi 9: Maksimiajat
- Aseta "Vuodet" = 40
- Aseta "Laina-aika (v)" = 40
- Tarkista että laskenta toimii

### Testi 10: Negatiivinen säästö
- Aseta checkbox "Sallitaanko negatiivinen säästö" = True
- Aseta parametrit niin että omistusasunnon kulut < vuokra
- Tarkista että laskenta toimii ja säästö voi olla negatiivinen

## Toiminnallisuustestaus

### Testi 11: Perusskenaario
- Käytä oletusarvoja
- Tarkista että:
  - Nettovarallisuudet ovat järkeviä
  - Kuukausittaiset kulut ovat positiivisia
  - Kuvaaja näyttää kaksi käyrää

### Testi 12: Parametrien muutos
- Muuta parametreja sliderien avulla
- Tarkista että laskenta päivittyy reaaliajassa
- Tarkista että kaikki arvot muuttuvat järkevästi

### Testi 13: Datarivien tarkistus
- Tarkista että `df.tail()` näyttää viimeiset 5 riviä
- Tarkista että sarakkeet ovat oikein:
  - `month`, `year`
  - `loan_balance`, `house_value`, `rent`
  - `owner_total_monthly_cost`, `renter_total_monthly_cost`
  - `monthly_saving_renter`, `portfolio`
  - `networth_owner`, `networth_renter`

## Yksikkötestaus (vapaaehtoinen)

Voit testata `simulaatio.py`-moduulia suoraan Pythonissa:

```python
from simulaatio import annuity_payment, simulate_detailed

# Testi: nollakorko
result = annuity_payment(100000, 0.0, 25)
print(f"Nollakorko: {result}")

# Testi: perusskenaario
df = simulate_detailed(
    years=10,
    house_price=650000,
    down_payment=300000,
    loan_interest_annual=0.03,
    loan_years=25,
    maintenance_fee=418,
    house_appreciation_annual=0.02,
    rent_initial=1800,
    rent_increase_annual=0.03,
    initial_investment=300000,
    stock_return_annual=0.06,
    transfer_tax_rate=0.015,
    sale_cost_rate=0.02,
    property_tax_rate_annual=0.0,
    renovation_yearly_eur=3000,
    owner_other_monthly=40,
    renter_other_monthly=30,
    allow_negative_saving=False,
)
print(f"Rivejä: {len(df)}")
print(f"Viimeinen nettovarallisuus (omistus): {df.iloc[-1]['networth_owner']:.2f} €")
print(f"Viimeinen nettovarallisuus (vuokra): {df.iloc[-1]['networth_renter']:.2f} €")
```

## Tunnettuja rajoituksia

- Jos `down_payment >= house_price`, lainaa ei ole (tämä on ok)
- Negatiiviset tuotot (arvonnousu, osaketuotto) ovat sallittuja
- Koodi ei tarkista että parametrit ovat järkeviä (esim. oma pääoma voi olla suurempi kuin asunnon hinta)

## Ongelmien raportointi

Jos löydät ongelman:
1. Kirjaa ylös mitä parametreja käytit
2. Kirjaa ylös mitä virhettä tuli
3. Tarkista että tiedostot ovat oikeassa paikassa (ei `.venv`-kansiossa)

