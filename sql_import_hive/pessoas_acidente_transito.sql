USE trabalhoFinal;

CREATE EXTERNAL TABLE IF NOT EXISTS pessoas_acidente_transito(
	num_boletim 			String,
	data_hora_boletim		String,
	n_envolvido				Integer,
	condutor				String, 
	cod_severidade			Integer,
	desc_severidade			String,
	sexo					String,
	cinto_seguranca			String,
	Embreagues				String,
	Idade					Integer,
	nascimento				String,
	categoria_habilitacao	String,
	descricao_habilitacao	String,
	declaracao_obito		Integer,
	cod_severidade_antiga	Integer,
	especie_veiculo			String,
	pedestre				String,
	passageiro				String
)
COMMENT 'Relação de pessoas envolvidas em acidentes de trânsito'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ';'
STORED AS TEXTFILE
location '/user/vagrant/trabFinal/Pessoas_acidenteTransito-2019';

LOAD DATA LOCAL INPATH '/vagrant/trabalho_final/CSV/pessoas_acidente_transito.csv' OVERWRITE INTO TABLE pessoas_acidente_transito;
