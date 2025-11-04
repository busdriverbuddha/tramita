

%%sql
DROP TABLE IF EXISTS encontro_legislativo_senado;

CREATE TABLE encontro_legislativo_senado AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    CAST(json_extract_string(payload_json, '$.id') AS BIGINT) AS id_processo
  FROM bronze_senado_processo
),
desp AS (
  SELECT
    b.id_processo,
    CAST(json_extract_string(d.value, '$.id') AS BIGINT) AS id_despacho,
    d.value AS despacho_json,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.despachos') AS d
),
encontro AS (
  SELECT
    id_processo,
    id_despacho,
    CAST(json_extract_string(despacho_json, '$.encontroLegislativo.id') AS BIGINT)          AS id_encontro_legislativo,
    TRY_CAST(json_extract_string(despacho_json, '$.encontroLegislativo.data') AS DATE)      AS data_encontro,
    json_extract_string(despacho_json, '$.encontroLegislativo.tipo')                         AS tipo_encontro,
    json_extract_string(despacho_json, '$.encontroLegislativo.descricao')                    AS descricao_encontro,
    json_extract_string(despacho_json, '$.encontroLegislativo.casa')                         AS casa_encontro,
    CAST(json_extract_string(despacho_json, '$.encontroLegislativo.numero') AS INTEGER)      AS numero_encontro,
    json_extract_string(despacho_json, '$.encontroLegislativo.colegiado.casa')               AS colegiado_casa,
    CAST(json_extract_string(despacho_json, '$.encontroLegislativo.colegiado.codigo') AS BIGINT) AS colegiado_codigo,
    json_extract_string(despacho_json, '$.encontroLegislativo.colegiado.nome')               AS colegiado_nome,
    json_extract_string(despacho_json, '$.encontroLegislativo.colegiado.sigla')              AS colegiado_sigla,
    year_snapshot
  FROM desp
)
SELECT
  id_processo,
  id_despacho,
  id_encontro_legislativo,
  data_encontro,
  tipo_encontro,
  descricao_encontro,
  casa_encontro,
  numero_encontro,
  colegiado_casa,
  colegiado_codigo,
  colegiado_nome,
  colegiado_sigla,
  year_snapshot
FROM encontro
WHERE id_encontro_legislativo IS NOT NULL;
