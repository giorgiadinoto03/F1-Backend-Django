from django.core.management.base import BaseCommand
from api.models import Session, Driver, Result
import requests

class Command(BaseCommand):
    help = "Importa i risultati delle sessioni da OpenF1"

    def handle(self, *args, **kwargs):
        sessions = Session.objects.filter(session_type__in=["Race", "Qualifying", "Sprint"])

        for session in sessions:
            print(f"Importando risultati per sessione {session.session_key} ({session.session_name})")

            url = f"https://api.openf1.org/v1/results?session_key={session.session_key}"
            #va modificato con questo url:
            # from urllib.request import urlopen
            #import json

            #response = urlopen('https://api.openf1.org/v1/session_result')
            #data = json.loads(response.read().decode('utf-8'))
            #print(data)

            # If you want, you can import the results in a DataFrame (you need to install the `pandas` package first)
            # import pandas as pd
            # df = pd.DataFrame(data)
            try:
                response = requests.get(url)
                data = response.json()
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Errore fetch session {session.session_key}: {e}"))
                continue
            #aggiungere url per la posizione dei piloti nel risultato (incrociare in base alla meeting_key, session_key e driver_number)
            #from urllib.request import urlopen
            #import json

            #response = urlopen(f'https://api.openf1.org/v1/position?meeting_key={session.meeting_key}&session_key={session.session_key}&driver_number={item["driver_number"]}')
            #data = json.loads(response.read().decode('utf-8'))
            #print(data)

            print(f"  -> {len(data)} risultati trovati")

            if not isinstance(data, list) or not data:
                continue

            for item in data:
                driver, _ = Driver.objects.get_or_create(
                    number=item["driver_number"],
                    defaults={
                        "full_name": item.get("full_name", f"Driver {item['driver_number']}"),
                        "broadcast_name": item.get("broadcast_name", ""),
                        "acronym": item.get("name_acronym", ""),
                        "first_name": item.get("first_name", ""),
                        "last_name": item.get("last_name", ""),
                    },
                )

                Result.objects.update_or_create(
                    session=session,
                    driver=driver,
                    defaults={
                        "position": item.get("position", 0),
                        "time": item.get("time", None),
                        "gap_to_leader": item.get("gap_to_leader", None),
                        "q1": item.get("q1", None),
                        "q2": item.get("q2", None),
                        "q3": item.get("q3", None),
                    },
                )

        total = Result.objects.count()
        self.stdout.write(self.style.SUCCESS(f"✅ Risultati importati con successo ({total} totali)"))
