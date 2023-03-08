from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(relatory_date):
        simple_report = SimpleReport.generate(relatory_date)

        comps = {}

        for company in relatory_date:
            if company['nome_da_empresa'] in comps:
                comps[company['nome_da_empresa']] += 1
            else:
                comps[company['nome_da_empresa']] = 1

        total_products_company = ""

        for cp in relatory_date:
            total_products_company += \
                f"- {cp['nome_da_empresa']}: {comps[cp['nome_da_empresa']]}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{total_products_company}"
        )
