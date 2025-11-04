

%%sql

DROP TABLE IF EXISTS tipo_emendas_senado;

CREATE TABLE tipo_emendas_senado AS
WITH base AS (
    SELECT
        tipo_emenda,
        year_snapshot
    FROM emendas_senado
    WHERE tipo_emenda IS NOT NULL
)
SELECT
    tipo_emenda,
    max(year_snapshot) AS year_snapshot
FROM base
GROUP BY tipo_emenda;
