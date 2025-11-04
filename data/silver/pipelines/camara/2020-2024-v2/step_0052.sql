-- ### 3.1.4 Eventos

%%sql
CREATE TABLE eventos_camara_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_evento ORDER BY year_snapshot DESC) AS rn
    FROM eventos_camara
)
WHERE rn = 1;

DROP TABLE eventos_camara;
ALTER TABLE eventos_camara_dedup RENAME TO eventos_camara;