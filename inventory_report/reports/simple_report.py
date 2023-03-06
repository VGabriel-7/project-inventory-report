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

        return f"""
          Data de fabricação mais antiga: {min(oldest_date)}
          Data de validade mais próxima: {closest_date}
          Empresa com mais produtos: NOME DA EMPRESA
        """


print(SimpleReport.generate([
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
   ])
  )
