

%%sql
DROP TABLE IF EXISTS partidos_membros_camara;

CREATE TABLE partidos_membros_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_partido,
  FROM bronze_partidos_membros
),
exploded AS (
  SELECT
    CAST(b.id_partido AS BIGINT) AS id_partido,
    CAST(json_extract_string(e.value, '$.id') AS BIGINT) AS id_deputado,
    CAST(json_extract_string(e.value, '$.id_legislatura') AS INTEGER) AS id_legislatura,
    b.year_snapshot,
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_partido_membro,
        id_partido,
        id_deputado,
        id_legislatura,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;
DROP VIEW IF EXISTS bronze_partidos_membros;