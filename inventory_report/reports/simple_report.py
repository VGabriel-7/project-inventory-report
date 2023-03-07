from datetime import date, datetime


class SimpleReport:
    @staticmethod
    def generate(relatory_date):
        oldest_date = [
            relatory['data_de_fabricacao'] for relatory in relatory_date
            ]

        closest_dates = [
            relatory['data_de_validade'] for relatory in relatory_date
            ]

        today = date.today()

        closest_date = min(closest_dates, key=lambda x: abs(
            datetime.strptime(x, '%Y-%m-%d').date() - today
          ))

        companies = {}

        for company in relatory_date:
            if company['nome_da_empresa'] in companies:
                companies[company['nome_da_empresa']] += 1
            else:
                companies[company['nome_da_empresa']] = 1

        return (
            f"Data de fabricação mais antiga: {min(oldest_date)}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {max(companies, key=companies.get)}"
        )
