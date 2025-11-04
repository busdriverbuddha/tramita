

%%sql
DROP TABLE IF EXISTS blocos_camara;
CREATE TABLE blocos_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_blocos
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_bloco,
    jget1(j, '$.dados.nome') AS nome,
    CAST(jget1(j, '$.dados.idLegislatura') AS BIGINT) AS id_legislatura,
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_camara_blocos;