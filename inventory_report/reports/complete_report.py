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
            name_company = f"- {company['nome_da_empresa']}: "
            quantity_products = f"{companies[company['nome_da_empresa']]}\n"
            total_products += name_company + quantity_products

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{total_products}"
        )
