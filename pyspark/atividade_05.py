# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark.sql import Row


spark = SparkSession \
    .builder \
    .appName("Total de acidentes com vitima por bairro em acidentes com embriaguez") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("USE trabalhoFinal")

df = spark.sql("SELECT Embreagues, AVG(Idade) AS media_idade FROM pessoas_acidente_transito GROUP BY Embreagues")

df.coalesce(1).write.option('header', 'true').format("csv") \
    .save("/user/vagrant/trabFinal/atividade5.csv")

 
