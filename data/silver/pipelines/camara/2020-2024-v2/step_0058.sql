-- ### 3.1.7 Órgãos

%%sql
CREATE TABLE orgaos_camara_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_orgao ORDER BY year_snapshot DESC) AS rn
    FROM orgaos_camara
)
WHERE rn = 1;

DROP TABLE orgaos_camara;
ALTER TABLE orgaos_camara_dedup RENAME TO orgaos_camara;