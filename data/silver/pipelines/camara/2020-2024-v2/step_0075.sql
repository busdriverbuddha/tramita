-- ### 3.1.21 Partidos e membros

%%sql
ALTER TABLE partidos_membros_camara
    ALTER COLUMN id_partido_membro TYPE BIGINT;

ALTER TABLE partidos_membros_camara
    ADD CONSTRAINT pk_partido_membro
    PRIMARY KEY (id_partido_membro);