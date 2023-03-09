from inventory_report.importer.importer import Importer

import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if '.json' not in path:
            raise ValueError('Arquivo inválido')

        try:
            with open(path, 'r') as file:
                return [row for row in json.load(file)]
        except FileNotFoundError:
            raise ("File not found")
