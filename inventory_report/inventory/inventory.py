from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def json_converter(path):
        try:
            with open(path, 'r') as file:
                return [row for row in json.load(file)]
        except FileNotFoundError:
            raise ("File not found")

    @staticmethod
    def csv_converter(path):
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return [row for row in
                        csv.DictReader(file, delimiter=',', quotechar='"')]
        except FileNotFoundError:
            raise ("File not found")

    @staticmethod
    def xml_converter(path):
        try:
            with open(path) as file:
                return xmltodict.parse(file.read())['dataset']['record']
        except FileNotFoundError:
            raise ("File not found")

    @classmethod
    def extensions_type(cls, path):
        if '.csv' in path:
            return cls.csv_converter(path)
        if '.json' in path:
            return cls.json_converter(path)
        if '.xml' in path:
            return cls.xml_converter(path)

    @classmethod
    def import_data(cls, path, type):
        file_content = cls.extensions_type(path=path)
        if type == 'simples':
            return SimpleReport.generate(file_content)

        return CompleteReport.generate(file_content)
