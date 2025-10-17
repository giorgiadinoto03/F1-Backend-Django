from django.core.management.base import BaseCommand
from api.models import Race
import requests

class Command(BaseCommand):
    help = "Importa i Gran Premi da OpenF1"

    def handle(self, *args, **kwargs):
        url = "https://api.openf1.org/v1/meetings?year=2025"
        data = requests.get(url).json()

        for item in data:
            race, created = Race.objects.update_or_create(
            meeting_key=item["meeting_key"],
            defaults={
                "meeting_name": item.get("meeting_official_name", ""),
                "country_code": item.get("country_code", ""),
                "country_name": item.get("country_name", ""),
                "location": item.get("location", ""),
                "year": item.get("year", 2025),
                "circuit_image": item.get("circuit_image", "")
            }
        )
        race.circuit_image = f"/media/circuit_images/{race.circuit_image}.png"
        race.save()

        
        self.stdout.write(self.style.SUCCESS("✅ Gran Premi importati"))
