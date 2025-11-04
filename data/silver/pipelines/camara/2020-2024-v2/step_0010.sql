

%%sql
DROP TABLE IF EXISTS frentes_camara;
CREATE TABLE frentes_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_frentes
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_frente,
    CAST(jget1(j, '$.dados.coordenador.id') AS BIGINT) AS id_deputado_coordenador,
    CAST(jget1(j, '$.dados.idLegislatura') AS BIGINT) AS id_legislatura,
    jget1(j, '$.dados.titulo') AS titulo,
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_camara_frentes;