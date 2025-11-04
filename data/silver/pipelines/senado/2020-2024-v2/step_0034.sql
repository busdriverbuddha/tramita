

%%sql
DROP TABLE IF EXISTS informes_documentos_associados_senado;

CREATE TABLE informes_documentos_associados_senado AS
WITH base AS (
    SELECT
        TRY_CAST(payload_json AS JSON) AS j,
        year AS year_snapshot,
        CAST(json_extract_string(payload_json, '$.id') AS BIGINT) AS id_processo
    FROM bronze_senado_processo
),
autuacoes AS (
    SELECT
        b.id_processo,
        CAST(a.key AS INTEGER)                    AS autuacao_ordem,
        a.value                                   AS autuacao_json,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.autuacoes') AS a
),
informes AS (
    SELECT
        a.id_processo,
        a.autuacao_ordem,
        CAST(i.key AS INTEGER)                    AS informe_ordem,
        CAST(json_extract_string(i.value, '$.id') AS BIGINT) AS id_informe,
        i.value                                   AS informe_json,
        a.year_snapshot
    FROM autuacoes a
    CROSS JOIN json_each(a.autuacao_json, '$.informesLegislativos') AS i
),
docs AS (
    SELECT
        inf.id_processo,
        inf.id_informe,
        inf.autuacao_ordem,
        inf.informe_ordem,
        CAST(d.key AS INTEGER)                    AS documento_ordem,
        CAST(json_extract_string(d.value, '$.id') AS BIGINT)   AS id_documento,
        json_extract_string(d.value, '$.siglaTipo')            AS sigla_tipo_documento,
        json_extract_string(d.value, '$.tipo')                 AS tipo_documento,
        json_extract_string(d.value, '$.identificacao')        AS identificacao,
        TRY_CAST(json_extract_string(d.value, '$.data') AS TIMESTAMP) AS data_documento,
        json_extract_string(d.value, '$.autoria')              AS autoria_documento,
        json_extract_string(d.value, '$.url')                  AS url_documento,
        inf.year_snapshot
    FROM informes inf
    CROSS JOIN json_each(inf.informe_json, '$.documentosAssociados') AS d
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_documento_associado,
        id_processo,
        id_informe,
        id_documento,
        autuacao_ordem,
        informe_ordem,
        documento_ordem,
        sigla_tipo_documento,
        tipo_documento,
        identificacao,
        data_documento,
        autoria_documento,
        url_documento,
        year_snapshot
    FROM docs
)
SELECT *
FROM numbered;
