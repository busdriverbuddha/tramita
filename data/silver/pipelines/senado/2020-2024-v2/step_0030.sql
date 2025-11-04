

%%sql
DROP TABLE IF EXISTS processos_relacionados_senado;

CREATE TABLE processos_relacionados_senado AS
WITH base AS (
    SELECT
        TRY_CAST(payload_json AS JSON) AS j,
        year AS year_snapshot,
        CAST(json_extract_string(payload_json, '$.id') AS BIGINT) AS id_processo
    FROM bronze_senado_processo
),
exploded AS (
    SELECT
        b.id_processo,
        CAST(json_extract_string(p.value, '$.idOutroProcesso') AS BIGINT) AS id_outro_processo,
        CAST(json_extract_string(p.value, '$.ano') AS INTEGER) AS ano,
        json_extract_string(p.value, '$.casaIdentificadora') AS casa_identificadora,
        json_extract_string(p.value, '$.enteIdentificador') AS ente_identificador,
        json_extract_string(p.value, '$.sigla') AS sigla,
        json_extract_string(p.value, '$.numero') AS numero,
        json_extract_string(p.value, '$.siglaEnteIdentificador') AS sigla_ente_identificador,
        json_extract_string(p.value, '$.tipoRelacao') AS tipo_relacao,
        json_extract_string(p.value, '$.tramitando') AS tramitando,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.processosRelacionados') AS p
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_processo_relacionado,
        id_processo,
        id_outro_processo,
        ano,
        casa_identificadora,
        ente_identificador,
        sigla,
        numero,
        sigla_ente_identificador,
        tipo_relacao,
        tramitando,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;