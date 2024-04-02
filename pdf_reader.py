import fitz  # PyMuPDF
import camelot
import os
from typing import List
import pandas as pd


def pegar_caminhos_pdf(diretorio: str) -> List[str]:
    return [
        os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith(".pdf")
    ]


def encontrar_paginas_com_tabelas(
    caminho_pdf: str, texto_chave: str, estado: str
) -> List[int]:
    paginas_com_tabela: List[int] = []
    with fitz.open(caminho_pdf) as doc:
        for num_pagina, pagina in enumerate(doc, start=1):
            texto_pagina: str = pagina.get_text()
            if texto_chave in texto_pagina and estado in texto_pagina:
                paginas_com_tabela.append(num_pagina)
    return paginas_com_tabela


def extrair_tabelas(caminho_pdf: str, paginas: List[int]) -> str:
    for num_pagina in paginas:
        tabelas = camelot.io.read_pdf(  
            caminho_pdf, pages=str(num_pagina), flavor="stream"
        )
        for tabela in tabelas:
            df = tabela.df
            linha_material = df[
                df[0].str.contains("10. Material de construção", na=False)
            ]
            if not linha_material.empty:
                valor = linha_material.iloc[0, 3].strip()
                return valor
    return ""


def mes_ano_do_nome_arquivo(nome_arquivo: str) -> str:
    partes = nome_arquivo.split("_")
    ano = partes[1]
    mes = partes[2].split(".")[0]
    return f"{mes}/{ano}"


caminhos_pdf = pegar_caminhos_pdf(
    r"C:\Users\vitor\OneDrive - Balaroti Comércio de Materiais de Construção SA\Documentos - Planejamento Financeiro\PMC\PDF'S"
)

lista_valores = []
for caminho_pdf in caminhos_pdf:
    texto_chave = "Tabela 4 - Indicadores do Volume de Vendas do Comércio Varejista e Comércio Varejista Ampliado"
    estado = "Santa Catarina"
    paginas_com_tabela = encontrar_paginas_com_tabelas(caminho_pdf, texto_chave, estado)
    valor = extrair_tabelas(caminho_pdf, paginas_com_tabela)
    if valor:
        valor = float(valor.replace(",", "."))
        mes_ano = mes_ano_do_nome_arquivo(os.path.basename(caminho_pdf))
        lista_valores.append({"Mês/Ano": mes_ano, "Valor": valor})

df_valores = pd.DataFrame(lista_valores)

df_valores.to_csv("variacao_pmc_santa_catarina.csv", index=False, sep=';')
