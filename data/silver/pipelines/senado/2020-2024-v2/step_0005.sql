


%%sql
DROP TABLE IF EXISTS bloco_senado;
CREATE TABLE bloco_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_senado_bloco
)
SELECT
    -- CodigoBloco
    CAST(jget1(j, '$.CodigoBloco') AS BIGINT) AS codigo_bloco,
    -- DataCriacao
    CAST(jget1(j, '$.DataCriacao') AS DATE) AS data_criacao,
    -- NomeApelido
    jget1(j, '$.NomeApelido') AS nome_apelido,
    -- NomeBloco
    jget1(j, '$.NomeBloco') AS nome_bloco,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.CodigoBloco') IS NOT NULL;
DROP VIEW IF EXISTS bronze_senado_bloco;
