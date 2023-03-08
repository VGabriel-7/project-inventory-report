from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(file, type):
        with open(file, encoding='utf-8') as file:
            file_content = csv.DictReader(file, delimiter=',', quotechar='"')

            if type == 'simples':
                return SimpleReport.generate(file_content)

            return CompleteReport.generate(file_content)
