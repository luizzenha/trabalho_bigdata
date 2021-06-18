# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark.sql import Row


spark = SparkSession \
    .builder \
    .appName("Total de acidentes com vitima por bairro em acidentes com embriaguez") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("USE trabalhoFinal")

df = spark.sql("SELECT log.nome_bairro, count(*) AS num_vitimas FROM " +
                "pessoas_acidente_transito AS env " +
                "INNER JOIN locais_acidente_transito AS log " + 
                "ON env.num_boletim = log.n_boletim WHERE env.Embreagues = 'SIM'" +
                "GROUP BY log.nome_bairro")

#df.show(200)

df.coalesce(1).write.option('header', 'true').format("csv") \
    .save("/user/vagrant/trabFinal/atividade1.csv")

 
