

%%sql
DROP TABLE IF EXISTS providencias_senado;

CREATE TABLE providencias_senado AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    CAST(json_extract_string(payload_json, '$.id') AS BIGINT) AS id_processo
  FROM bronze_senado_processo
),
despachos AS (
  SELECT
    b.id_processo,
    CAST(json_extract_string(d.value, '$.id') AS BIGINT) AS id_despacho,
    d.value AS despacho_json,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.despachos') AS d
),
exploded AS (
  SELECT
    d.id_processo,
    d.id_despacho,
    CAST(json_extract_string(p.value, '$.id') AS BIGINT)            AS id_providencia,
    json_extract_string(p.value, '$.descricao')                      AS descricao,
    json_extract_string(p.value, '$.tipo')                           AS tipo,
    json_extract_string(p.value, '$.analiseConteudo')                AS analise_conteudo,
    json_extract_string(p.value, '$.analiseTempo')                   AS analise_tempo,
    CAST(json_extract_string(p.value, '$.ordem') AS INTEGER)         AS ordem,
    json_extract_string(p.value, '$.reexame')                        AS reexame,       -- "Sim"/"Não"
    d.year_snapshot
  FROM despachos d
  CROSS JOIN json_each(d.despacho_json, '$.providencias') AS p
)
SELECT
  id_processo,
  id_despacho,
  id_providencia,
  descricao,
  tipo,
  analise_conteudo,
  analise_tempo,
  ordem,
  reexame,
  year_snapshot
FROM exploded;
