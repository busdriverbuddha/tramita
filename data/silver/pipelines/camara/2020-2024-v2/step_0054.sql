-- ### 3.1.5 Frentes

%%sql
CREATE TABLE frentes_camara_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_frente ORDER BY year_snapshot DESC) AS rn
    FROM frentes_camara
)
WHERE rn = 1;

DROP TABLE frentes_camara;
ALTER TABLE frentes_camara_dedup RENAME TO frentes_camara;