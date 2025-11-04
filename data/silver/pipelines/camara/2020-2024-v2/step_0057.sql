

%%sql
ALTER TABLE legislaturas_camara
    ALTER COLUMN id_legislatura TYPE BIGINT;

ALTER TABLE legislaturas_camara
    ADD CONSTRAINT pk_legislaturas PRIMARY KEY (id_legislatura);