# F1-Backend-Django

Progetto backend in Django per gestire dati di Formula 1. Semplice e in fase di sviluppo (Work in Progress).

## Stato
⚠️ In sviluppo — molte funzionalità non sono ancora complete.

## Descrizione
Backend REST API costruito con Django e Django REST Framework per gestire entità come piloti, team, gare e risultati. Questo repository ospita il codice server; l'interfaccia client (se presente) è separata.

## Requisiti
- Python 3.10+ (o versione compatibile)
- pip
- virtualenv (opzionale)
- Django
- djangorestframework

## Installazione rapida (locale)
1. Clona il repository:
   git clone https://github.com/giorgiadinoto03/F1-Backend-Django.git
2. Entra nella cartella del progetto:
   cd F1-Backend-Django
3. Crea e attiva un virtualenv (consigliato):
   python -m venv .venv
   - macOS / Linux: source .venv/bin/activate
   - Windows: .venv\Scripts\activate
4. Installa le dipendenze:
   pip install -r requirements.txt
   (Se non c'è requirements.txt, installa manualmente Django e djangorestframework)
5. Applica le migrazioni:
   python manage.py migrate
6. Crea un superuser per l'admin:
   python manage.py createsuperuser
7. Avvia il server di sviluppo:
   python manage.py runserver

## Esempio di endpoint (segnaposto)
- GET /api/drivers/ — lista di piloti
- GET /api/teams/ — lista di team
- GET /api/races/ — calendario gare
- POST /api/results/ — invio risultati

(NB: gli endpoint reali possono cambiare man mano che sviluppo procede)

## Come contribuire
- Apri un'issue per segnalare bug o proporre funzionalità.
- Apri una pull request per inviare modifiche (preferibile: una PR piccola e ben documentata).
- Aggiungi test per nuove funzionalità quando possibile.

## Note per lo sviluppo
- Tenere aggiornate le migrazioni.
- Aggiungere file requirements.txt se non presente.
- Considerare l'uso di Docker per standardizzare l'ambiente.

## License
Da decidere (TBD)

## Contatti
Repository: https://github.com/giorgiadinoto03/F1-Backend-Django
Autore: @giorgiadinoto03
Svolto durante il corso: ITS Prodigi - Full Stack Developers
