-- ### 3.1.5. Emendas

%%sql
ALTER TABLE emendas_senado
    ALTER COLUMN id_emenda TYPE BIGINT;

ALTER TABLE emendas_senado
    ADD CONSTRAINT pk_emenda PRIMARY KEY (id_emenda);