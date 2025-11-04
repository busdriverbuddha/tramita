

%%sql
DROP TABLE IF EXISTS deputados_camara;
CREATE TABLE deputados_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_deputados
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_deputado,
    jget1(j, '$.dados.nomeCivil') AS nome_civil,
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_camara_deputados;