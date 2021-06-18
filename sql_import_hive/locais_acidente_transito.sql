USE trabalhoFinal;

CREATE EXTERNAL TABLE IF NOT EXISTS locais_acidente_transito (
	n_boletim					String,
	data_boletim				String,
	n_municipio					Integer,
	nome_municipio				String,
	seq_logradouros				Integer,
	n_logradouro				Integer,
	tipo_logradouro				String,
	nome_logradouro				String,
	tipo_logradouro_anterior	String,
	nome_logradouro_anterior	String,
	n_bairro					Integer,
	nome_bairro					String,
	tipo_bairro					String,
	descricao_tipo_bairro		String,
	n_imovel					Integer,
	n_imovel_proximo			Integer
)
COMMENT 'Relação de logradouros dos locais de acidentes de trânsito'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ';'
STORED AS TEXTFILE
location '/user/vagrant/trabFinal/Logradouros_acidenteTransito';

LOAD DATA LOCAL INPATH '/vagrant/trabalho_final/CSV/Logradouros_acidenteTransito.csv' OVERWRITE INTO TABLE locais_acidente_transito;