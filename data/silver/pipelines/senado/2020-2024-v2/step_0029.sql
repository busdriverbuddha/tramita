

%%sql
DROP TABLE IF EXISTS outros_numeros_senado;

CREATE TABLE outros_numeros_senado AS
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
        CAST(json_extract_string(o.value, '$.idOutroProcesso') AS BIGINT) AS id_outro_processo,
        CAST(json_extract_string(o.value, '$.ano') AS INTEGER) AS ano,
        json_extract_string(o.value, '$.casaIdentificadora') AS casa_identificadora,
        json_extract_string(o.value, '$.enteIdentificador') AS ente_identificador,
        json_extract_string(o.value, '$.sigla') AS sigla,
        json_extract_string(o.value, '$.numero') AS numero,
        json_extract_string(o.value, '$.siglaEnteIdentificador') AS sigla_ente_identificador,
        json_extract_string(o.value, '$.externaAoCongresso') AS externa_ao_congresso,
        json_extract_string(o.value, '$.tramitando') AS tramitando,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.outrosNumeros') AS o
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_outro_numero,
        id_processo,
        id_outro_processo,
        ano,
        casa_identificadora,
        ente_identificador,
        sigla,
        numero,
        sigla_ente_identificador,
        externa_ao_congresso,
        tramitando,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;