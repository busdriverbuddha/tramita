-- ### 3.1.16. Informes legislativos

%%sql
ALTER TABLE informes_legislativos_senado
    ALTER COLUMN id_informe_legislativo TYPE BIGINT;

ALTER TABLE informes_legislativos_senado
    ADD CONSTRAINT pk_informe_legislativo PRIMARY KEY (id_informe_legislativo);