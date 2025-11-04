-- ### 3.1.17. Documentos associados a informes

%%sql
ALTER TABLE informes_documentos_associados_senado
    ALTER COLUMN id_documento_associado TYPE BIGINT;

ALTER TABLE informes_documentos_associados_senado
    ADD CONSTRAINT pk_documento_associado PRIMARY KEY (id_documento_associado);