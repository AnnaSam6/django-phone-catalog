import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV'
    
    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for row in reader:
                phone = Phone(
                    id=int(row['id']),
                    name=row['name'],
                    image=row['image'],
                    price=int(row['price']),
                    release_date=parse_date(row['release_date']),
                    lte_exists=row['lte_exists'] == 'True',
                )
                phone.save()
                
        self.stdout.write(self.style.SUCCESS('All phones imported!'))
