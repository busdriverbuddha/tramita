-- ### 3.1.3 Deputados

%%sql
CREATE TABLE deputados_camara_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_deputado ORDER BY year_snapshot DESC) AS rn
    FROM deputados_camara
)
WHERE rn = 1;

DROP TABLE deputados_camara;
ALTER TABLE deputados_camara_dedup RENAME TO deputados_camara;
