

%%sql
DROP TABLE IF EXISTS deputados_frentes_camara;

CREATE TABLE deputados_frentes_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_deputado
  FROM bronze_camara_deputados_frentes
),
exploded AS (
  SELECT
    CAST(json_extract_string(e.value, '$.id') AS BIGINT) AS id_frente,
    CAST(b.id_deputado AS BIGINT) AS id_deputado,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_deputado_frente,
        id_deputado,
        id_frente,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;