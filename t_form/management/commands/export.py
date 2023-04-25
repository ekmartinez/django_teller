import csv
from django.core.management.base import BaseCommand
from t_form.models import Report

class Command(BaseCommand):
    help = 'Export Report data to CSV'

    def handle(self, *args, **options):
        filename = 'reports.csv'
        fields = ['location', 'name', 'date', 'cash_reported', 
                    'pennies', 'nickels', 'dimes', 'quarters', 
                    'one_dollar', 'five_dollar', 'ten_dollar', 
                    'twenty_dollar', 'fifty_dollar', 'one_hundred']
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
            
            for report in Report.objects.all():
                writer.writerow([getattr(report, field) for field in fields])
        

        self.stdout.write(self.style.SUCCESS(f'Successfully exported Report data to {filename}'))
