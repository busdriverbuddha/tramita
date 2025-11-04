

%%sql
DROP TABLE IF EXISTS colegiado_senado;
CREATE TABLE colegiado_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_senado_colegiado
)
SELECT
    -- CodigoColegiado
    CAST(jget1(j, '$.CodigoColegiado') AS BIGINT) AS codigo_colegiado,
    -- CodigoTipoColegiado
    CAST(jget1(j, '$.CodigoTipoColegiado') AS BIGINT) AS codigo_tipo_colegiado,
    -- DataInicio
    CAST(jget1(j, '$.DataInicio') AS DATE) AS data_inicio,
    -- IndicadorDistrPartidaria
    jget1(j, '$.IndicadorDistrPartidaria') AS indicador_distr_partidaria,
    -- NomeColegiado
    jget1(j, '$.NomeColegiado') AS nome_colegiado,
    -- SiglaColegiado
    jget1(j, '$.SiglaColegiado') AS sigla_colegiado,
    -- ordem
    CAST(jget1(j, '$.ordem') AS INTEGER) AS ordem,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.CodigoColegiado') IS NOT NULL;

DROP TABLE IF EXISTS tipo_colegiado_senado;
CREATE TABLE tipo_colegiado_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) AS j, year
    FROM bronze_senado_colegiado
),
typed AS (
    SELECT
        CAST(jget1(j, '$.tipocolegiado.CodigoNaturezaColegiado') AS BIGINT) AS codigo_natureza_colegiado,
        CAST(jget1(j, '$.tipocolegiado.CodigoTipoColegiado') AS BIGINT) AS codigo_tipo_colegiado,
        jget1(j, '$.tipocolegiado.DescricaoTipoColegiado') AS descricao_tipo_colegiado,
        jget1(j, '$.tipocolegiado.IndicadorAtivo') AS indicador_ativo,
        jget1(j, '$.tipocolegiado.SiglaCasa') AS sigla_casa,
        jget1(j, '$.tipocolegiado.SiglaTipoColegiado') AS sigla_tipo_colegiado,
        year AS year_snapshot
    FROM base
    WHERE jget1(j, '$.tipocolegiado.CodigoTipoColegiado') IS NOT NULL
)
SELECT
    codigo_tipo_colegiado,
    arg_max(codigo_natureza_colegiado, year_snapshot) AS codigo_natureza_colegiado,
    arg_max(descricao_tipo_colegiado,  year_snapshot) AS descricao_tipo_colegiado,
    arg_max(indicador_ativo,           year_snapshot) AS indicador_ativo,
    arg_max(sigla_casa,                year_snapshot) AS sigla_casa,
    arg_max(sigla_tipo_colegiado,      year_snapshot) AS sigla_tipo_colegiado,
    max(year_snapshot)                              AS year_snapshot
FROM typed
GROUP BY codigo_tipo_colegiado;



DROP VIEW IF EXISTS bronze_senado_bloco;