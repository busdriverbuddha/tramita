-- ### 3.1.6 Legislaturas

%%sql
CREATE TABLE legislaturas_camara_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_legislatura ORDER BY year_snapshot DESC) AS rn
    FROM legislaturas_camara
)
WHERE rn = 1;

DROP TABLE legislaturas_camara;
ALTER TABLE legislaturas_camara_dedup RENAME TO legislaturas_camara;