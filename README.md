# pdf_table_reader
Este script Python realiza a extração automática de dados específicos de tabelas em documentos PDF e compila esses dados em um arquivo CSV. Utiliza as bibliotecas PyMuPDF (fitz), Camelot, os, e pandas para efetuar as seguintes operações:

### Identificação de Arquivos PDF:
    Busca todos os arquivos PDF em um diretório especificado.
### Localização de Páginas com Tabelas Relevantes:
    Analisa cada página dos documentos PDF para encontrar tabelas que contenham um texto-chave e referências a um estado específico.
    Isso é útil para filtrar informações relevantes de um grande volume de dados.
### Extração de Dados das Tabelas:
    Extrai valores específicos de tabelas encontradas nas páginas identificadas.
    O foco é em linhas que contêm materiais de construção, obtendo valores quantitativos relevantes.
### Organização dos Dados Extraídos:
    Compila os dados extraídos, incluindo o valor e a data (mês/ano) extraída do nome do arquivo, em um DataFrame pandas.
