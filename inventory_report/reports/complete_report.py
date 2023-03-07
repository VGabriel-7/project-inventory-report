from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(relatory_date):
        simple_report = SimpleReport.generate(relatory_date)

        companies = {}

        for company in relatory_date:
            if company['nome_da_empresa'] in companies:
                companies[company['nome_da_empresa']] += 1
            else:
                companies[company['nome_da_empresa']] = 1

        total_products = ""

        for company in relatory_date:
            total_products += f"- {company['nome_da_empresa']}: {companies[company['nome_da_empresa']]}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{total_products}"
        )