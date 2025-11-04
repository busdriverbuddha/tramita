

%%sql
DROP TABLE IF EXISTS informes_legislativos_senado;

CREATE TABLE informes_legislativos_senado AS
WITH base AS (
    SELECT
        TRY_CAST(payload_json AS JSON)                            AS j,
        year                                                      AS year_snapshot,
        CAST(json_extract_string(payload_json, '$.id') AS BIGINT) AS id_processo
    FROM bronze_senado_processo
),
autuacoes AS (
    SELECT
        b.id_processo,
        b.year_snapshot,
        a.value AS autuacao_json
    FROM base b
    CROSS JOIN json_each(b.j, '$.autuacoes') AS a
),
informes AS (
    SELECT
        a.id_processo,
        a.year_snapshot,
        i.value AS informe_json
    FROM autuacoes a
    CROSS JOIN json_each(a.autuacao_json, '$.informesLegislativos') AS i
)
SELECT
    ROW_NUMBER() OVER ()                                         AS id_informe_legislativo, -- auto increment PK
    id_processo,

    CAST(json_extract_string(informe_json, '$.id') AS BIGINT)    AS id_informe,
    TRY_CAST(json_extract_string(informe_json, '$.data') AS DATE) AS data_informe,
    json_extract_string(informe_json, '$.descricao')             AS descricao,

    -- situação iniciada (optional)
    CAST(json_extract_string(informe_json, '$.idSituacaoIniciada') AS BIGINT) AS id_situacao_iniciada,
    json_extract_string(informe_json, '$.siglaSituacaoIniciada')  AS sigla_situacao_iniciada,

    -- enteAdministrativo
    json_extract_string(informe_json, '$.enteAdministrativo.casa')               AS ente_adm_casa,
    CAST(json_extract_string(informe_json, '$.enteAdministrativo.id') AS BIGINT) AS ente_adm_id,
    json_extract_string(informe_json, '$.enteAdministrativo.nome')               AS ente_adm_nome,
    json_extract_string(informe_json, '$.enteAdministrativo.sigla')              AS ente_adm_sigla,

    -- colegiado
    json_extract_string(informe_json, '$.colegiado.casa')          AS colegiado_casa,
    CAST(json_extract_string(informe_json, '$.colegiado.codigo') AS BIGINT) AS colegiado_codigo,
    json_extract_string(informe_json, '$.colegiado.nome')          AS colegiado_nome,
    json_extract_string(informe_json, '$.colegiado.sigla')         AS colegiado_sigla,

    year_snapshot
FROM informes;
