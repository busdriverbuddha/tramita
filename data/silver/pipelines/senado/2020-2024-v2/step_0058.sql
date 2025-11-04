-- ### 3.1.18. Providências

%%sql
ALTER TABLE providencias_senado
    ALTER COLUMN id_providencia TYPE BIGINT;

ALTER TABLE providencias_senado
    ADD CONSTRAINT pk_providencia PRIMARY KEY (
        id_processo,
        id_despacho,
        id_providencia
    );