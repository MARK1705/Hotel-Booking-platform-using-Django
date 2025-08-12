import csv
from django.core.management.base import BaseCommand
from hotel.models import Hotel

class Command(BaseCommand):
    help = 'Import hotel data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csvfile = options['csvfile']
        count = 0
        with open(csvfile, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Hotel.objects.create(
                    name=row['Name'],              # Adjust this if needed
                    city=row['CityName'],
                    address=row['Address'],
                    price=float(row['Price']) if row['Price'] else None,
                    rating=float(row['Rating']) if row['Rating'] else None,
                    amenities=row.get('Amenities', '')
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(
            f"Imported {count} hotels from {csvfile}"
        ))
