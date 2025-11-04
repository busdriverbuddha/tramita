

%%sql
DROP TABLE IF EXISTS unidades_destinatarias_senado;

CREATE TABLE unidades_destinatarias_senado AS
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
    b.year_snapshot,
    CAST(json_extract_string(d.value, '$.id') AS BIGINT) AS id_despacho,
    d.value AS despacho_json
  FROM base b
  CROSS JOIN json_each(b.j, '$.despachos') AS d
),
prov AS (
  SELECT
    d.id_processo,
    d.year_snapshot,
    d.id_despacho,
    CAST(json_extract_string(p.value, '$.id') AS BIGINT) AS id_providencia,
    p.value AS providencia_json
  FROM desp d
  CROSS JOIN json_each(d.despacho_json, '$.providencias') AS p
),
unid AS (
  SELECT
    p.id_processo,
    p.year_snapshot,
    p.id_despacho,
    p.id_providencia,
    CAST(json_extract_string(u.value, '$.colegiado.codigo') AS BIGINT) AS colegiado_codigo,
    json_extract_string(u.value, '$.colegiado.casa')  AS colegiado_casa,
    json_extract_string(u.value, '$.colegiado.nome')  AS colegiado_nome,
    json_extract_string(u.value, '$.colegiado.sigla') AS colegiado_sigla,
    CAST(json_extract_string(u.value, '$.ordem') AS INTEGER) AS ordem,
    json_extract_string(u.value, '$.tipoAnaliseDeliberacao') AS tipo_analise_deliberacao
  FROM prov p
  CROSS JOIN json_each(p.providencia_json, '$.unidadesDestinatarias') AS u
),
numbered AS (
  SELECT
    ROW_NUMBER() OVER () AS id_unidade_destinataria,
    id_processo,
    id_despacho,
    id_providencia,
    colegiado_casa,
    colegiado_codigo,
    colegiado_nome,
    colegiado_sigla,
    ordem,
    tipo_analise_deliberacao,
    year_snapshot
  FROM unid
)
SELECT *
FROM numbered;
