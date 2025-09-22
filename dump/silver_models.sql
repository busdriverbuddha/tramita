-- peek_json_payloads("data/bronze/snapshots/bronze-2020-smoke", "camara/legislaturas/details")

-- pull from bronze

CREATE OR REPLACE VIEW bronze_camara_frentes AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-smoke/camara/frentes/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'frentes';

SELECT COUNT(*) AS n FROM bronze_camara_frentes;

-- extract to silver

%%sql
DROP TABLE IF EXISTS frentes_camara;
CREATE TABLE frentes_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_frentes
)
SELECT
    CAST(jget1(j, '$.dados.id') AS BIGINT) AS id_frente,
    CAST(jget1(j, '$.dados.coordenador.id') AS BIGINT) AS id_deputado_coordenador,
    CAST(jget1(j, '$.dados.idLegislatura') AS BIGINT) AS id_legislatura,
    jget1(j, '$.dados.titulo') AS titulo,
    jget1(j, '$.dados.uri') AS uri,
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.dados.id') IS NOT NULL;



-- extract to silver, exploding list, repeating elements from the base
%%sql
DROP TABLE IF EXISTS autores_camara;

CREATE TABLE autores_camara AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot,
    id AS id_proposicao
  FROM bronze_camara_autores
),
exploded AS (
  SELECT
    CAST(json_extract_string(e.value, '$.codTipo') AS BIGINT)         AS cod_tipo,
    json_extract_string(e.value, '$.uri')                              AS uri_autor,
    CAST(json_extract_string(e.value, '$.ordemAssinatura') AS INTEGER) AS ordem_assinatura,
    CAST(json_extract_string(e.value, '$.proponente') AS BOOLEAN)      AS proponente,
    b.id_proposicao,
    b.year_snapshot
  FROM base b
  CROSS JOIN json_each(b.j, '$.dados') AS e
)
SELECT cod_tipo, uri_autor, ordem_assinatura, proponente, id_proposicao, year_snapshot
FROM exploded;
