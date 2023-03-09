from inventory_report.importer.importer import Importer

import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if '.xml' not in path:
            raise ValueError('Arquivo inválido')

        try:
            with open(path) as file:
                return xmltodict.parse(file.read())['dataset']['record']
        except FileNotFoundError:
            raise ("File not found")
