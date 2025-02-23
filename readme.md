# PharmaPriceTracker

## Introduktion
PharmaPriceTracker er et projekt designet til at spore priser på farmaceutiske produkter. Denne README-fil vil guide dig gennem opsætningen af projektet.

## Krav
Før du begynder, skal du sikre dig, at du har følgende installeret:
- [Python](https://www.python.org/) (version 3.8 eller nyere)
- [pip](https://pip.pypa.io/en/stable/) (Python Package Installer)
- [virtualenv](https://virtualenv.pypa.io/en/stable/) (anbefales)

## Installation
Følg disse trin for at sætte projektet op:

1. Klon repository:
    ```sh
    git clone https://github.com/mglavind/PharmaPriceTracker.git
    ```

2. Naviger til projektmappen:
    ```sh
    cd PharmaPriceTracker
    ```

3. Opret og aktiver et virtuelt miljø:
    ```sh
    python -m venv env
    source env/bin/activate  # På Windows brug: .\env\Scripts\activate
    ```

4. Installer afhængigheder:
    ```sh
    pip install -r requirements.txt
    ```

5. Anvend migrationer:
    ```sh
    python manage.py migrate
    ```

## Brug
For at starte applikationen, kør følgende kommando:
```sh
python manage.py runserver
```

## Test
For at køre testene, brug følgende kommando:
```sh
python manage.py test
```

## Bidrag
Hvis du ønsker at bidrage til projektet, bedes du følge disse trin:
1. Fork projektet
2. Opret en ny branch (`git checkout -b feature/dit-feature-navn`)
3. Commit dine ændringer (`git commit -m 'Tilføj feature'`)
4. Push til branchen (`git push origin feature/dit-feature-navn`)
5. Opret en Pull Request

