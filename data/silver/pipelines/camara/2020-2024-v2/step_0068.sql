-- ### 3.1.14 Votações

%%sql
CREATE TABLE votacoes_camara_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_votacao ORDER BY year_snapshot DESC) AS rn
    FROM votacoes_camara
)
WHERE rn = 1;

DROP TABLE votacoes_camara;
ALTER TABLE votacoes_camara_dedup RENAME TO votacoes_camara;

ALTER TABLE votacoes_camara
    ALTER COLUMN id_votacao TYPE TEXT;

ALTER TABLE votacoes_camara
    ADD CONSTRAINT pk_votacoes
    PRIMARY KEY (id_votacao);