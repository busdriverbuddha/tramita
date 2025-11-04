

%%sql
DROP TABLE IF EXISTS despachos_senado;

CREATE TABLE despachos_senado AS
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
        CAST(json_extract_string(d.value, '$.id') AS BIGINT) AS id_despacho,
        TRY_CAST(json_extract_string(d.value, '$.data') AS DATE) AS data_despacho,
        json_extract_string(d.value, '$.cancelado') AS cancelado,
        json_extract_string(d.value, '$.tipoMotivacao') AS tipo_motivacao,
        json_extract_string(d.value, '$.siglaTipoMotivacao') AS sigla_tipo_motivacao,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.despachos') AS d
)
SELECT
    id_processo,
    id_despacho,
    data_despacho,
    cancelado,
    tipo_motivacao,
    sigla_tipo_motivacao,
    year_snapshot
FROM exploded;
