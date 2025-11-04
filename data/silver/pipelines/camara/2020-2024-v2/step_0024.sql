

%%sql
DROP TABLE IF EXISTS orientacoes_camara;

CREATE TABLE orientacoes_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_votacao
  FROM bronze_camara_orientacoes
),
exploded AS (
  SELECT
    CAST(json_extract_string(e.value, '$.codPartidoBloco') AS BIGINT) AS cod_partido_bloco,
    json_extract_string(e.value, '$.codTipoLideranca') AS cod_tipo_lideranca,
    json_extract_string(e.value, '$.orientacaoVoto') AS orientacao_voto,
    json_extract_string(e.value, '$.siglaPartidoBloco') AS sigla_partido_bloco,
    json_extract_string(e.value, '$.uriPartidoBloco') AS uri_partido_bloco,
    b.id_votacao,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_orientacao,
        id_votacao,
        sigla_partido_bloco,
        orientacao_voto,
        cod_partido_bloco,
        cod_tipo_lideranca,
        uri_partido_bloco,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered;
DROP VIEW IF EXISTS bronze_camara_orientacoes;
