-- ### 3.1.15 Blocos e partidos

%%sql
ALTER TABLE blocos_partidos_camara
    ALTER COLUMN id_bloco_partido TYPE BIGINT;

ALTER TABLE blocos_partidos_camara
    ADD CONSTRAINT pk_bloco_partido
    PRIMARY KEY (id_bloco_partido);