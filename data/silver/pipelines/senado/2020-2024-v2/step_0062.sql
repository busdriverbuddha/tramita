

%%sql
CREATE TABLE encontro_legislativo_senado_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_encontro_legislativo ORDER BY year_snapshot DESC) AS rn
    FROM encontro_legislativo_senado
)
WHERE rn = 1;

DROP TABLE encontro_legislativo_senado;
ALTER TABLE encontro_legislativo_senado_dedup RENAME TO encontro_legislativo_senado;
