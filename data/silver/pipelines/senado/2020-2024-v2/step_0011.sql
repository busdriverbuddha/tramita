


%%sql
DROP TABLE IF EXISTS partido_senado;
CREATE TABLE partido_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_senado_partido
)
SELECT
    CAST(jget1(j, '$.Codigo') AS BIGINT) AS codigo_partido,
    CAST(jget1(j, '$.DataCriacao') AS DATE) AS data_criacao,
    jget1(j, '$.Nome') AS nome,
    jget1(j, '$.Sigla') AS sigla,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.Codigo') IS NOT NULL;
DROP VIEW IF EXISTS bronze_senado_partido;