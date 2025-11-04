

%%sql
DROP TABLE IF EXISTS partidos_camara;
CREATE TABLE partidos_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_partidos
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_partido,
    jget1(j, '$.dados.nome') AS nome,
    jget1(j, '$.dados.sigla') AS sigla,
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_camara_partidos;
