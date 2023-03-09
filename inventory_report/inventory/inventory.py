from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(file, type):
        with open(file, encoding='utf-8') as file:
            file_content = csv.DictReader(file, delimiter=',', quotechar='"')
            file_content_edited = [row for row in file_content]
            if type == 'simples':
                report_simple = SimpleReport.generate(file_content_edited)
                return report_simple
            elif type == 'completo':
                report_coomplete = CompleteReport.generate(file_content_edited)
                return report_coomplete
