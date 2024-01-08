from utilidades_cve import dados, moeda

preco = dados.leiaDinheiro('Digite um preço: R$')

moeda.resumo(preco, 10, 50)