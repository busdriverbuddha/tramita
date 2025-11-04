

%%sql
DROP TABLE IF EXISTS votacoes_camara;

CREATE TABLE votacoes_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year as year_snapshot,
    id AS id_proposicao
  FROM bronze_camara_votacoes
),
exploded AS (
  SELECT
    CAST(json_extract_string(e.value, '$.aprovacao') AS BOOLEAN) AS aprovacao,
    CAST(json_extract_string(e.value, '$.data') AS DATE) AS data,
    json_extract_string(e.value, '$.descricao') AS descricao,
    json_extract_string(e.value, '$.id') AS id_votacao, -- como text mesmo, por conta do hífen
    json_extract_string(e.value, '$.uri') AS uri,
    json_extract_string(e.value, '$.uriEvento') AS uri_evento,
    json_extract_string(e.value, '$.uriOrgao') AS uri_orgao,
    CAST(b.id_proposicao AS BIGINT) AS id_proposicao,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
)
SELECT
    id_votacao,
    id_proposicao,
    data,
    descricao,
    aprovacao,
    uri_evento,
    uri_orgao,
    uri,
    year_snapshot,
FROM exploded;
