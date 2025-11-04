

%%sql
DROP TABLE IF EXISTS documento_autoria_senado;

CREATE TABLE documento_autoria_senado AS
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
        CAST(json_extract_string(a.value, '$.idEnte') AS BIGINT) AS id_ente,
        json_extract_string(a.value, '$.autor') AS autor,
        json_extract_string(a.value, '$.casaEnte') AS casa_ente,
        CAST(json_extract_string(a.value, '$.codigoParlamentar') AS BIGINT) as codigo_parlamentar,
        json_extract_string(a.value, '$.descricaoTipo') AS descricao_tipo,
        json_extract_string(a.value, '$.ente') AS ente,
        CAST(json_extract_string(a.value, '$.ordem') AS INTEGER) AS ordem,
        json_extract_string(a.value, '$.outrosAutoresNaoInformados') AS outros_autores_nao_informados,
        json_extract_string(a.value, '$.siglaEnte') AS sigla_ente,
        json_extract_string(a.value, '$.siglaTipo') AS sigla_tipo,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.documento.autoria') AS a
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_documento_autoria,
        id_processo,
        id_ente,
        autor,
        codigo_parlamentar,
        descricao_tipo,
        ente,
        ordem,
        outros_autores_nao_informados,
        sigla_ente,
        sigla_tipo,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;
