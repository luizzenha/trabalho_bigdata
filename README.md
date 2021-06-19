# trabalho_bigdata
Trabalho em grupo big data - MBA

# Informações de pastas
 - CSV: arquivos originais
 - sql_import_hive: comandos sql para importar os arquivos originais para o hive
 - pyspark: scripts criados para tratamento dos dados
 - csv_clean: arquivos csv gerados após processo no pyspark para tratamento dos dados 
 - pandas: scripts gerados para geração dos gráficos
 - charts: gráficos em png gerados via pandas e um pdf consolidado, os dados usados para geração desses gráficos foram gerados pelo pyspark

# Passos para executar o projeto:

- Dentro do ambiente da VM (hive, hadoop e spark)
  - Criar uma pasta com o nome trabalho_final dentro de /vagrant/
  - Colocar a pasta CSV dentro da pasta trabalho_final
  - Colocar os arquivos da pasta sql_import_hive dentro do /vagrant e executar o import para o hive na seguinte sequencia
    1) criando_database.sql
    2) locais_acidente_transito.sql  
    3) ocorrencia_transito.sql
    4) pessoas_acidente_transito.sql

    ex: 
    `$ hive –f <caminho>\criando_database.sql`

- Exportar os dados via pyspark, adicionar os arquivos da pasta pyspark dentro do /vagrant e executar todos os arquivos .py

  ex:
  `$ spark-submit atividade_01.py`

- Extrair os arquivos gerados, importar no colab ou em um ambiente python com pandas e executar os códigos que estão dentro da pasta pandas para geração dos gráficos



GRUPO:
- Arthur Almeida
- Karina Padua de Oliveira Pinto
- Kleber Luiz Tomazi
- Luiz Othávio Heitzmann Zenha
- Rafaela dos Santos Silva
- Verônica Batista
- Wagner Soares da Silva

