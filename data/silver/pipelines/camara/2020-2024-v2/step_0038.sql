

%%sql
DROP TABLE IF EXISTS eventos_orgaos_camara;

CREATE TABLE eventos_orgaos_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_evento
  FROM bronze_camara_eventos_orgaos
),
exploded AS (
  SELECT
    CAST(b.id_evento AS BIGINT) AS id_evento,
    CAST(json_extract_string(e.value, '$.id') AS INTEGER) AS id_orgao,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT 
        ROW_NUMBER() OVER () AS id_evento_orgao,
        id_evento, id_orgao, year_snapshot
    FROM exploded
)
SELECT * FROM numbered;