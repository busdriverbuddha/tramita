


%%sql
DROP TABLE IF EXISTS legislaturas_camara;
CREATE TABLE legislaturas_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_legislaturas
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_legislatura,
    CAST(jget1(j, '$.dados.dataInicio') AS DATE) AS data_inicio,
    CAST(jget1(j, '$.dados.dataFim') AS DATE) AS data_fim,
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_camara_legislaturas;
