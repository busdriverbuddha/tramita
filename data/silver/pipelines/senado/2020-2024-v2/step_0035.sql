

%%sql
-- Movimentações dentro de cada autuação do processo
DROP TABLE IF EXISTS movimentacoes_senado;

CREATE TABLE movimentacoes_senado AS
WITH base AS (
    SELECT
        TRY_CAST(payload_json AS JSON)                                           AS j,
        year                                                                     AS year_snapshot,
        CAST(json_extract_string(payload_json, '$.id') AS BIGINT)                AS id_processo
    FROM bronze_senado_processo
),
autuacoes AS (  -- explode top-level autuações and keep their array index as autuacao_idx
    SELECT
        b.id_processo,
        CAST(a.key AS INTEGER)                                                   AS autuacao_idx,
        a.value                                                                  AS autuacao_json,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.autuacoes') AS a
),
exploded AS (  -- explode movimentações under each autuação
    SELECT
        a.id_processo,
        a.autuacao_idx,
        CAST(m.key AS INTEGER)                                                   AS movimentacao_idx,
        CAST(json_extract_string(m.value, '$.id') AS BIGINT)                     AS id_movimentacao,
        TRY_CAST(json_extract_string(m.value, '$.dataEnvio') AS TIMESTAMP)       AS data_envio,
        TRY_CAST(json_extract_string(m.value, '$.dataRecebimento') AS TIMESTAMP) AS data_recebimento,

        -- Ente de origem
        json_extract_string(m.value, '$.enteOrigem.casa')                        AS ente_origem_casa,
        CAST(json_extract_string(m.value, '$.enteOrigem.id') AS BIGINT)          AS ente_origem_id,
        json_extract_string(m.value, '$.enteOrigem.nome')                        AS ente_origem_nome,
        json_extract_string(m.value, '$.enteOrigem.sigla')                       AS ente_origem_sigla,

        -- Ente de destino
        json_extract_string(m.value, '$.enteDestino.casa')                       AS ente_destino_casa,
        CAST(json_extract_string(m.value, '$.enteDestino.id') AS BIGINT)         AS ente_destino_id,
        json_extract_string(m.value, '$.enteDestino.nome')                       AS ente_destino_nome,
        json_extract_string(m.value, '$.enteDestino.sigla')                      AS ente_destino_sigla,

        -- Colegiado de destino (pode vir vazio {})
        json_extract_string(m.value, '$.colegiadoDestino.casa')                  AS colegiado_destino_casa,
        CAST(json_extract_string(m.value, '$.colegiadoDestino.codigo') AS BIGINT) AS colegiado_destino_codigo,
        json_extract_string(m.value, '$.colegiadoDestino.nome')                  AS colegiado_destino_nome,
        json_extract_string(m.value, '$.colegiadoDestino.sigla')                 AS colegiado_destino_sigla,

        a.year_snapshot
    FROM autuacoes a
    CROSS JOIN json_each(a.autuacao_json, '$.movimentacoes') AS m
)
SELECT
    id_processo,
    autuacao_idx,            -- FK para autuacoes_senado (id_processo, autuacao_idx)
    movimentacao_idx,        -- posição dentro da autuação (opcional como parte da PK composta)
    id_movimentacao,
    data_envio,
    data_recebimento,
    ente_origem_casa,
    ente_origem_id,
    ente_origem_nome,
    ente_origem_sigla,
    ente_destino_casa,
    ente_destino_id,
    ente_destino_nome,
    ente_destino_sigla,
    colegiado_destino_casa,
    colegiado_destino_codigo,
    colegiado_destino_nome,
    colegiado_destino_sigla,
    year_snapshot
FROM exploded;
