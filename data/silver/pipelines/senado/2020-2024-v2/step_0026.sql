

%%sql
DROP TABLE IF EXISTS autoria_documento_senado;

CREATE TABLE autoria_documento_senado AS
WITH base AS (
    SELECT
        TRY_CAST(payload_json AS JSON) as j,
        year AS year_snapshot,
        CAST(json_extract_string(payload_json, '$.id') AS BIGINT) as id_processo,
        CAST(json_extract_string(payload_json, '$.documento.id') AS BIGINT) as id_documento
    FROM bronze_senado_processo
),
exploded as (
    SELECT 
    b.id_processo,
    b.id_documento,
    json_extract_string(e, '$.autor') as autor,
    json_extract_string(e, '$.siglaTipo') as sigla_tipo,
    json_extract_string(e, '$.descricaoTipo') as descricao_tipo,
    CAST(json_extract_string(e, '$.ordem') AS INTEGER) as ordem,
    json_extract_string(e, '$.outrosAutoresNaoInformados') as outros_autores_nao_informados,
    CAST(json_extract_string(e, '$.idEnte') AS BIGINT) as id_ente,
    json_extract_string(e, '$.siglaEnte') as sigla_ente,
    json_extract_string(e, '$.casaEnte') as casa_ente,
    json_extract_string(e, '$.ente') as ente,
    json_extract_string(e, '$.cargo') as cargo,
    json_extract_string(e, '$.siglaCargo') as siglaCargo,
    json_extract_string(e, '$.partido') as partido,
    json_extract_string(e, '$.sexo') as sexo,
    json_extract_string(e, '$.uf') as uf,
    b.year_snapshot,
    FROM base b
    CROSS JOIN json_each(b.j, '$.documento.autoria') as e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_autoria_documento,
        id_processo,
        id_documento,
        autor,
        sigla_tipo,
        descricao_tipo,
        ordem,
        outros_autores_nao_informados,
        id_ente,
        sigla_ente,
        casa_ente,
        ente,
        cargo,
        siglaCargo,
        partido,
        sexo,
        uf,
        year_snapshot
    FROM exploded
)
SELECT * FROM numbered;