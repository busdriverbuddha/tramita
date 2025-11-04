-- ### 3.1.2. Parlamentar

%%sql
CREATE TABLE parlamentares_senado_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY codigo_parlamentar ORDER BY year_snapshot DESC) AS rn
    FROM parlamentar_senado
)
WHERE rn = 1;

DROP TABLE parlamentar_senado;
ALTER TABLE parlamentares_senado_dedup RENAME TO parlamentar_senado;
