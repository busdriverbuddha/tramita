

%%sql
DROP TABLE IF EXISTS proposicoes_camara;
CREATE TABLE proposicoes_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_proposicoes
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_proposicao,
    jget1(j, '$.dados.siglaTipo') as sigla_tipo,
    CAST(jget1(j, '$.dados.numero') AS INTEGER) AS numero,
    CAST(jget1(j, '$.dados.ano') AS INTEGER) AS ano,
    jget1(j, '$.dados.ementa') AS ementa,
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_camara_proposicoes;