

%%sql
DROP TABLE IF EXISTS deputados_orgaos_camara;

CREATE TABLE deputados_orgaos_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_deputado
  FROM bronze_camara_deputados_orgaos
),
exploded AS (
  SELECT
    CAST(json_extract_string(e.value, '$.idOrgao') AS INTEGER) AS id_orgao,
    CAST(json_extract_string(e.value, '$.codTitulo') AS INTEGER) AS cod_titulo,
    CAST(json_extract_string(e.value, '$.dataInicio') AS DATETIME) AS data_inicio,
    CAST(json_extract_string(e.value, '$.dataFim') AS DATETIME) AS data_fim,
    CAST(b.id_deputado AS BIGINT) AS id_deputado,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_deputado_orgao,
        id_deputado,
        id_orgao,
        cod_titulo,
        data_inicio,
        data_fim,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;