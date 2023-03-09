from inventory_report.importer.importer import Importer

import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if '.csv' not in path:
            raise ValueError('Arquivo inválido')

        try:
            with open(path, 'r', encoding='utf-8') as file:
                return [row for row in
                        csv.DictReader(file, delimiter=',', quotechar='"')]
        except FileNotFoundError:
            raise ("File not found")
