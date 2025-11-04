

%%sql
DROP TABLE IF EXISTS situacoes_senado;

CREATE TABLE situacoes_senado AS
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
        CAST(json_extract_string(a.value, '$.numero') AS INTEGER) AS numero_autuacao,
        a.value AS autuacao_json,
        b.year_snapshot
    FROM base b
    CROSS JOIN json_each(b.j, '$.autuacoes') AS a
),
situacoes AS (
    SELECT
        a.id_processo,
        a.numero_autuacao,
        CAST(json_extract_string(s.value, '$.idTipo') AS INTEGER) AS id_tipo_situacao,
        json_extract_string(s.value, '$.sigla') AS sigla_situacao,
        json_extract_string(s.value, '$.descricao') AS descricao_situacao,
        TRY_CAST(json_extract_string(s.value, '$.inicio') AS DATE) AS data_inicio,
        TRY_CAST(json_extract_string(s.value, '$.fim') AS DATE) AS data_fim,
        a.year_snapshot
    FROM autuacoes a
    CROSS JOIN json_each(a.autuacao_json, '$.situacoes') AS s
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_situacao,
        id_processo,
        numero_autuacao,
        id_tipo_situacao,
        sigla_situacao,
        descricao_situacao,
        data_inicio,
        data_fim,
        year_snapshot
    FROM situacoes
)
SELECT *
FROM numbered;
