-- ### 3.1.13. Autoria do documento

%%sql
ALTER TABLE documento_autoria_senado
    ALTER COLUMN id_documento_autoria TYPE BIGINT;

ALTER TABLE documento_autoria_senado
    ADD CONSTRAINT pk_documento_autoria PRIMARY KEY (id_documento_autoria);