

%%sql
DROP TABLE IF EXISTS autoria_iniciativa_senado;

CREATE TABLE autoria_iniciativa_senado AS
WITH base AS (
    SELECT
        TRY_CAST(payload_json AS JSON) AS j,
        year AS year_snapshot,
        CAST(jget1(payload_json, '$.id') AS BIGINT) AS id_processo
    FROM bronze_senado_processo
),
exploded AS (
    SELECT
        b.id_processo,
        CAST(json_extract_string(e.value, '$.idEnte') AS BIGINT) AS id_ente,
        json_extract_string(e.value, '$.autor') AS autor,
        json_extract_string(e.value, '$.casaEnte') AS casa_ente,
        CAST(json_extract_string(e.value, '$.codigoParlamentar') AS BIGINT) AS codigo_parlamentar,
        json_extract_string(e.value, '$.descricaoTipo') AS descricao_tipo,
        json_extract_string(e.value, '$.ente') AS ente,
        CAST(json_extract_string(e.value, '$.ordem') AS INTEGER) AS ordem,
        json_extract_string(e.value, '$.outrosAutoresNaoInformados') AS outros_autores_nao_informados,
        json_extract_string(e.value, '$.siglaEnte') AS sigla_ente,
        json_extract_string(e.value, '$.siglaTipo') AS sigla_tipo,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.autoriaIniciativa') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_autoria_iniciativa,
        id_processo,
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
