-- ### 3.1.9. Autoria-iniciativa

%%sql
ALTER TABLE autoria_iniciativa_senado
    ALTER COLUMN id_autoria_iniciativa TYPE BIGINT;

ALTER TABLE autoria_iniciativa_senado
    ADD CONSTRAINT pk_autoria_iniciativa PRIMARY KEY (id_autoria_iniciativa);