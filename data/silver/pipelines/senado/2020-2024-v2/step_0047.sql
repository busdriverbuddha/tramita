-- ### 3.1.8. Votos

%%sql
ALTER TABLE votos_senado
    ALTER COLUMN id_voto TYPE BIGINT;

ALTER TABLE votos_senado
    ADD CONSTRAINT pk_voto PRIMARY KEY (id_voto);