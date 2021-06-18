# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark.sql import Row


spark = SparkSession \
    .builder \
    .appName("Total de acidentes com vitima por bairro em acidentes com embriaguez") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("USE trabalhoFinal")

df = spark.sql("SELECT env.especie_veiculo, bol.pavimento, COUNT(*) AS num_vitimas FROM " +
                "ocorrencia_transito AS bol " +
                "INNER JOIN pessoas_acidente_transito AS env ON bol.n_boletim = env.num_boletim " +
                "GROUP BY env.especie_veiculo, bol.pavimento")

#df.show(200)

df.coalesce(1).write.option('header', 'true').format("csv") \
    .save("/user/vagrant/trabFinal/atividade3.csv")

 
