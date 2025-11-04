-- ### 2.2.3 Tramitações

%%sql
-- View over the Parquet snapshot
CREATE OR REPLACE VIEW bronze_camara_tramitacoes AS
SELECT *
FROM parquet_scan('data/bronze/snapshots/bronze-2020-2024-v2/camara/tramitacoes/year=*/part-*.parquet')
WHERE source = 'camara' AND entity = 'tramitacoes';

-- Materialize exploded tramitacoes
DROP TABLE IF EXISTS tramitacoes_camara;

CREATE TABLE tramitacoes_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id   AS id_proposicao
  FROM bronze_camara_tramitacoes
),
exploded AS (
  SELECT
    CAST(b.id_proposicao AS BIGINT)                                        AS id_proposicao,
    json_extract_string(e.value, '$.ambito')                               AS ambito,
    json_extract_string(e.value, '$.apreciacao')                           AS apreciacao,
    json_extract_string(e.value, '$.codSituacao')                          AS cod_situacao,
    json_extract_string(e.value, '$.codTipoTramitacao')                    AS cod_tipo_tramitacao,
    CAST(json_extract_string(e.value, '$.dataHora') AS TIMESTAMP)          AS data_hora,
    json_extract_string(e.value, '$.descricaoSituacao')                    AS descricao_situacao,
    json_extract_string(e.value, '$.descricaoTramitacao')                  AS descricao_tramitacao,
    json_extract_string(e.value, '$.despacho')                             AS despacho,
    json_extract_string(e.value, '$.regime')                               AS regime,
    CAST(json_extract_string(e.value, '$.sequencia') AS INTEGER)           AS sequencia,
    json_extract_string(e.value, '$.siglaOrgao')                           AS sigla_orgao,
    json_extract_string(e.value, '$.uriOrgao')                             AS uri_orgao,
    json_extract_string(e.value, '$.uriUltimoRelator')                     AS uri_ultimo_relator,
    b.year_snapshot                                                         AS year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_tramitacao,
        id_proposicao,
        ambito,
        apreciacao,
        cod_situacao,
        cod_tipo_tramitacao,
        data_hora,
        descricao_situacao,
        descricao_tramitacao,
        despacho,
        regime,
        sequencia,
        sigla_orgao,
        uri_orgao,
        uri_ultimo_relator,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;


DROP VIEW IF EXISTS bronze_camara_tramitacoes;
