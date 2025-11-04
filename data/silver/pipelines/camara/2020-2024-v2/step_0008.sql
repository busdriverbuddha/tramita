


%%sql
DROP TABLE IF EXISTS eventos_camara;
CREATE TABLE eventos_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_eventos
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_evento,
    CAST(jget1(j, '$.dados.dataHoraInicio') AS DATETIME) AS data_hora_inicio,
    CAST(jget1(j, '$.dados.dataHoraFim') AS DATETIME) AS data_hora_fim,
    jget1(j, '$.dados.descricao') AS descricao,
    jget1(j, '$.dados.descricaoTipo') AS descricao_tipo,
    jget1(j, '$.dados.fases') AS fases,  -- é sempre null mas deixei por precaução
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_camara_eventos;