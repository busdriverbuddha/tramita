

%%sql
DROP TABLE IF EXISTS partidos_lideres_camara;

CREATE TABLE partidos_lideres_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_partido,
  FROM bronze_partidos_lideres
),
exploded AS (
  SELECT
    CAST(b.id_partido AS BIGINT) AS id_partido,
      -- codTitulo
    json_extract_string(e.value, '$.codTitulo') AS cod_titulo,
    -- dataInicio
    CAST(json_extract_string(e.value, '$.dataInicio') AS DATE) AS data_inicio,
    -- dataFim
    CAST(json_extract_string(e.value, '$.dataFim') AS DATE) AS data_fim,
    -- id (deputado)
    CAST(json_extract_string(e.value, '$.id') AS BIGINT) AS id_deputado,
    -- year
    b.year_snapshot,
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_partido_lider,
        id_partido,
        cod_titulo,
        data_inicio,
        data_fim,
        id_deputado,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;
DROP VIEW IF EXISTS bronze_partidos_lideres;