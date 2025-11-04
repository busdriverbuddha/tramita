

%%sql
DROP TABLE IF EXISTS deputados_historico_camara;

CREATE TABLE deputados_historico_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_deputado
  FROM bronze_camara_deputados_historico
),
exploded AS (
  SELECT
    json_extract_string(e.value, '$.condicaoEleitoral') AS condicao_eleitoral,
    CAST(json_extract_string(e.value, '$.dataHora') AS DATETIME) AS data_hora,
    json_extract_string(e.value, '$.descricaoStatus') AS descricao_status,
    CAST(json_extract_string(e.value, '$.idLegislatura') AS BIGINT) AS id_legislatura,
    json_extract_string(e.value, '$.situacao') AS situacao,
    CAST(b.id_deputado AS BIGINT) AS id_deputado,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_deputado_historico,
        id_deputado,
        id_legislatura,
        data_hora,
        condicao_eleitoral,
        descricao_status,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;
