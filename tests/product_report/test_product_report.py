from inventory_report.inventory.product import Product


def test_relatorio_produto():
    expect_string = """O produto test fabricado em \
2022-03-22 por empresa test com \
validade até 2023-03-22 precisa ser \
armazenado Armazenamento test."""

    report = Product(
                1,
                'test',
                'empresa test',
                '2022-03-22',
                '2023-03-22',
                'PKG87',
                'Armazenamento test',
            )

    assert str(report) == expect_string
