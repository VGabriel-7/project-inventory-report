from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1234,
        nome_do_produto='Produto de teste',
        nome_da_empresa='Empresa de teste',
        data_de_fabricacao='03/03/23',
        data_de_validade='03/03/25',
        numero_de_serie='256',
        instrucoes_de_armazenamento='Instrucao de teste'
    )

    assert product.id == 1234
    assert product.nome_do_produto == 'Produto de teste'
    assert product.nome_da_empresa == 'Empresa de teste'
    assert product.data_de_fabricacao == '03/03/23'
    assert product.data_de_validade == '03/03/25'
    assert product.numero_de_serie == '256'
    assert product.instrucoes_de_armazenamento == 'Instrucao de teste'
