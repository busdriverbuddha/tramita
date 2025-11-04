

%%sql

DROP TABLE IF EXISTS emendas_senado;

CREATE TABLE emendas_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) AS j, year
    FROM bronze_senado_emendas
),
flat AS (
    SELECT
        -- chaves e metadados
        CAST(jget1(j, '$.id')                AS BIGINT)  AS id_emenda,
        CAST(jget1(j, '$.idCiEmenda')        AS BIGINT)  AS id_ci_emenda,
        CAST(jget1(j, '$.idCiEmendado')      AS BIGINT)  AS id_ci_emendado,
        CAST(jget1(j, '$.idDocumentoEmenda') AS BIGINT)  AS id_documento_emenda,
        CAST(jget1(j, '$.idProcesso')        AS BIGINT)  AS id_processo,

        -- identificação/descrição
        jget1(j, '$.identificacao')                      AS identificacao,
        CAST(jget1(j, '$.numero') AS INTEGER)            AS numero,
        jget1(j, '$.autoria')                             AS autoria,
        jget1(j, '$.descricaoDocumentoEmenda')            AS descricao_documento_emenda,
        jget1(j, '$.tipo')                                AS tipo_emenda,
        jget1(j, '$.turnoApresentacao')                   AS turno_apresentacao,

        -- casa/colegiado
        jget1(j, '$.casa')                                AS casa,
        CAST(jget1(j, '$.codigoColegiado') AS BIGINT)     AS codigo_colegiado,
        jget1(j, '$.siglaColegiado')                      AS sigla_colegiado,
        jget1(j, '$.nomeColegiado')                       AS nome_colegiado,

        -- documentos e datas
        CAST(jget1(j, '$.dataApresentacao') AS DATE)      AS data_apresentacao,
        jget1(j, '$.urlDocumentoEmenda')                  AS url_documento_emenda,

        -- snapshot
        year AS year_snapshot
    FROM base
)
SELECT *
FROM flat
WHERE id_emenda IS NOT NULL;
