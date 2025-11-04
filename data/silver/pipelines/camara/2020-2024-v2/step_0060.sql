-- ### 3.1.8 Partidos



%%sql
CREATE TABLE partidos_camara_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_partido ORDER BY year_snapshot DESC) AS rn
    FROM partidos_camara
)
WHERE rn = 1;

DROP TABLE partidos_camara;
ALTER TABLE partidos_camara_dedup RENAME TO partidos_camara;