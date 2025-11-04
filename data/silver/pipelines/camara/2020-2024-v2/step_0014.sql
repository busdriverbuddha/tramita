

%%sql
DROP TABLE IF EXISTS orgaos_camara;
CREATE TABLE orgaos_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_orgaos
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_orgao,
    jget1(j, '$.dados.nome') AS nome,
    CAST(jget1(j, '$.dados.codTipoOrgao') AS BIGINT) AS cod_tipo_orgao,
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_camara_orgaos;
