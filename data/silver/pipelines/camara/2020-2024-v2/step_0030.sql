

%%sql
DROP TABLE IF EXISTS blocos_partidos_camara;

CREATE TABLE blocos_partidos_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_bloco
  FROM bronze_camara_blocos_partidos
),
exploded AS (
  SELECT
    CAST(json_extract_string(e.value, '$.id') AS BIGINT) AS id_partido,
    CAST(b.id_bloco AS BIGINT) AS id_bloco,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_bloco_partido,
        id_bloco,
        id_partido,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;
