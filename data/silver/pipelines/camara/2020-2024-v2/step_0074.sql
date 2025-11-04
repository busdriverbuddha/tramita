-- ### 3.1.20 Partidos e líderes

%%sql
ALTER TABLE partidos_lideres_camara
    ALTER COLUMN id_partido_lider TYPE BIGINT;

ALTER TABLE partidos_lideres_camara
    ADD CONSTRAINT pk_partido_lider
    PRIMARY KEY (id_partido_lider);