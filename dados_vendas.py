import polars as pl
import numpy as np
from datetime import datetime, timedelta
import os
from pathlib import Path

def gerar_dados_vendas(numero_linhas: int, nome_arquivo: str):
    if numero_linhas <= 0:
        raise ValueError("O número de linhas deve ser positivo")

    caminho_arquivo = Path(nome_arquivo)
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)

    nomes_produtos = np.asarray(
        [
            "Laptop",
            "Smartphone",
            "Mesa",
            "Cadeira",
            "Monitor",
            "Impressora",
            "Papel",
            "Caneta",
            "Caderno",
            "Cafeteira",
            "Armário",
            "Copos Plásticos",
        ]
    )
    categorias = np.asarray(
        [
            "Eletrônicos",
            "Eletrônicos",
            "Escritório",
            "Escritório",
            "Eletrônicos",
            "Eletrônicos",
            "Papelaria",
            "Papelaria",
            "Papelaria",
            "Eletrônicos",
            "Escritório",
            "Diversos",
        ]
    )

    indices_produtos = np.random.randint(len(nomes_produtos), size=numero_linhas)
    quantidades = np.random.randint(1, 11, size=numero_linhas)
    precos = np.random.randint(199, 10000, size=numero_linhas) / 100

    data_inicio = datetime(2010, 1, 1)
    data_fim = datetime(2023, 12, 31)
    intervalo_dias = (data_fim - data_inicio).days

    datas_pedidos = np.array([
        (data_inicio + timedelta(days=np.random.randint(0, intervalo_dias))).strftime('%Y-%m-%d') 
        for _ in range(numero_linhas)
    ])

    colunas = {
        "order_id": np.arange(numero_linhas),
        "order_date": datas_pedidos,
        "customer_id": np.random.randint(100, 1000, size=numero_linhas),
        "customer_name": [f"Cliente_{i}" for i in np.random.randint(2**15, size=numero_linhas)],
        "product_id": indices_produtos + 200,
        "product_names": nomes_produtos[indices_produtos],
        "categories": categorias[indices_produtos],
        "quantity": quantidades,
        "price": precos,
        "revenue": precos * quantidades,
    }

    df = pl.DataFrame(colunas)
    df.write_csv(nome_arquivo, separator=',', include_header=True)

    print(f"Arquivo gerado com sucesso: {nome_arquivo}")
    print(f"Total de registros: {numero_linhas:,}")
    print(f"Tamanho do arquivo: {os.path.getsize(nome_arquivo) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    caminho_saida = r"C:\Users\ferna\WORK\Projetos_Python\Dashboard_Taipy\dados_vendas.csv"
    gerar_dados_vendas(100_000, caminho_saida)
