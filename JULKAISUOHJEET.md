# Julkaisuohjeet - Streamlit Cloud

## Vaihe 1: GitHub-repositorio

1. Luo uusi repository GitHubissa (tai käytä olemassa olevaa)
   - Nimi: esim. `asunto-vuokra-simulaattori`
   - Julkinen tai yksityinen (Streamlit Cloud tukee molempia)

2. Alusta git-repositorio (jos ei ole jo tehty):
   ```bash
   git init
   ```

3. Lisää kaikki projektitiedostot:
   ```bash
   git add app.py simulaatio.py requirements.txt README.md .gitignore
   git commit -m "Initial commit: Asunto vs vuokra -simulaattori"
   ```

4. Yhdistä GitHub-repositorioon:
   ```bash
   git remote add origin https://github.com/KAYTTAJANIMI/asunto-vuokra-simulaattori.git
   git branch -M main
   git push -u origin main
   ```

## Vaihe 2: Streamlit Cloud -julkaisu

1. Mene osoitteeseen: https://share.streamlit.io/

2. Kirjaudu sisään GitHub-tililläsi

3. Klikkaa "New app"

4. Täytä lomake:
   - **Repository**: Valitse GitHub-repositoriosi
   - **Branch**: `main` (tai mikä branch haluat käyttää)
   - **Main file path**: `app.py`
   - **App URL**: Voit antaa oman URL:n tai käyttää automaattista

5. Klikkaa "Deploy!"

## Vaihe 3: Tarkistus

1. Streamlit Cloud käynnistää sovelluksen automaattisesti
   - Ensimmäinen käynnistys voi kestää 1-2 minuuttia
   - Streamlit asentaa automaattisesti `requirements.txt`-tiedostossa olevat paketit

2. Tarkista että:
   - Sovellus käynnistyy ilman virheitä
   - Kaikki parametrit toimivat
   - Kuvaaja piirtyy oikein
   - Datarivit näkyvät

## Vaihe 4: Päivitykset

Kun teet muutoksia koodiin:

1. Commitoi muutokset:
   ```bash
   git add .
   git commit -m "Päivityksen kuvaus"
   git push
   ```

2. Streamlit Cloud päivittää sovelluksen automaattisesti
   - Päivitys näkyy yleensä muutamassa minuutissa
   - Voit seurata päivitystä Streamlit Cloud -dashboardissa

## Tärkeät huomiot

### Tiedostojen sijainti
- **VAIN** juuritasolla olevat tiedostot näkyvät Streamlit Cloudille
- Varmista että `app.py`, `simulaatio.py` ja `requirements.txt` ovat repositorion juuressa
- Älä commitoi `.venv`-kansiota (se on `.gitignore`-tiedostossa)

### Requirements.txt
- Varmista että `requirements.txt` sisältää kaikki tarvittavat paketit
- Älä sisällytä versioita ellei ole pakollista (Streamlit Cloud asentaa uusimmat yhteensopivat versiot)

### Yksityisyys
- Jos repository on yksityinen, Streamlit Cloud vaatii että annat sille oikeudet repositoryyn
- Julkiset repositoryt toimivat suoraan

### Kustannukset
- Streamlit Cloud on ilmainen julkisille repositoryille
- Yksityisille repositoryille on maksullinen versio (tai voit käyttää julkista)

## Vaihtoehtoiset julkaisutavat

### Heroku
- Vaatii `Procfile` ja mahdollisesti muita konfiguraatiotiedostoja
- Maksullinen (ilmainen tier poistettu)

### Railway
- Vaatii `Procfile` tai `railway.json`
- Maksullinen (rajoitettu ilmainen tier)

### Streamlit Community Cloud (suositus)
- Helpoin tapa Streamlit-sovelluksille
- Ilmainen julkisille repositoryille
- Automaattinen päivitys

## Ongelmien ratkaisu

### Sovellus ei käynnisty
1. Tarkista että `app.py` on repositorion juuressa
2. Tarkista että `requirements.txt` on oikein
3. Tarkista Streamlit Cloud -logit virheistä

### Paketit eivät asennu
1. Tarkista että `requirements.txt` on oikeassa muodossa
2. Poista versiotiedot jos ne aiheuttavat ongelmia
3. Tarkista että pakettien nimet ovat oikein

### Sovellus on hidas
1. Streamlit Cloud jakaa resursseja ilmaisten käyttäjien kesken
2. Maksullinen versio tarjoaa paremmat resurssit

