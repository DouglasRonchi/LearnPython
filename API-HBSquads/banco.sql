CREATE TABLE linguagens(
	cd_linguagem int not null AUTO_INCREMENT,
	PRIMARY KEY(cd_linguagem),
	nm_linguagem varchar(100)
);

CREATE TABLE bancos_de_dados(
	cd_banco_de_dados int not null AUTO_INCREMENT,
	PRIMARY KEY(cd_banco_de_dados),
	nm_banco_de_dados varchar(100)
);


CREATE TABLE frontends(
	cd_frontend int not null AUTO_INCREMENT,
	PRIMARY KEY (cd_frontend),
	nm_frontend varchar(100)
);

CREATE TABLE desenvolvedores(
	cd_desenvolvedor int not null AUTO_INCREMENT,
	PRIMARY KEY(cd_desenvolvedor),
	nm_desenvolvedor varchar(100)
);

CREATE TABLE vagas(
	cd_vaga int not null AUTO_INCREMENT,
	PRIMARY KEY(cd_vaga),
	fk_desenvolvedor int not null UNIQUE,
	fk_linguagem int not null UNIQUE,
	fk_banco_de_dados int not null UNIQUE,
	fk_frontend int not NULL UNIQUE,
	FOREIGN KEY (fk_desenvolvedor) REFERENCES desenvolvedores(cd_desenvolvedor),
	FOREIGN KEY (fk_linguagem) REFERENCES linguagens(cd_linguagem),
	FOREIGN KEY (fk_banco_de_dados) REFERENCES bancos_de_dados(cd_banco_de_dados),
	FOREIGN KEY (fk_frontend) REFERENCES frontends(cd_frontend)
);

