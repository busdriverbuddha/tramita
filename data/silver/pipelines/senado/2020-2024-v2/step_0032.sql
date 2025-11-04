

%%sql
DROP TABLE IF EXISTS autuacoes_senado;

CREATE TABLE autuacoes_senado AS
WITH base AS (
    SELECT
        TRY_CAST(payload_json AS JSON)                                   AS j,
        year                                                             AS year_snapshot,
        CAST(json_extract_string(payload_json, '$.id') AS BIGINT)        AS id_processo
    FROM bronze_senado_processo
),
exploded AS (
    SELECT
        b.id_processo,
        -- array position within $.autuacoes becomes a stable, deterministic PK within the processo
        CAST(a.key AS INTEGER) + 1                                       AS autuacao_idx,   -- 1-based
        json_extract_string(a.value, '$.descricao')                      AS descricao_autuacao,
        CAST(json_extract_string(a.value, '$.idEnteControleAtual') AS BIGINT)
                                                                          AS id_ente_controle_atual,
        json_extract_string(a.value, '$.nomeEnteControleAtual')          AS nome_ente_controle_atual,
        json_extract_string(a.value, '$.siglaEnteControleAtual')         AS sigla_ente_controle_atual,
        CAST(json_extract_string(a.value, '$.numero') AS INTEGER)        AS numero_autuacao,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.autuacoes') AS a
)
SELECT
    id_processo,
    autuacao_idx,
    descricao_autuacao,
    id_ente_controle_atual,
    nome_ente_controle_atual,
    sigla_ente_controle_atual,
    numero_autuacao,
    year_snapshot
FROM exploded;
