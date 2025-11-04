

%%sql
DROP TABLE IF EXISTS autores_camara;
CREATE TABLE autores_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) AS j,
    year,
    id AS id_proposicao,
    FROM bronze_camara_autores
),
exploded AS (
    SELECT
        CAST(jget1(elem.value, '$.codTipo') AS BIGINT)        AS cod_tipo,
        jget1(elem.value, '$.uri')                           AS uri,
        CAST(jget1(elem.value, '$.ordemAssinatura') AS INT)  AS ordem_assinatura,
        CAST(jget1(elem.value, '$.proponente') AS BOOLEAN)   AS proponente,
        CAST(b.id_proposicao AS BIGINT)                      AS id_proposicao,
        b.year
    FROM base b
    CROSS JOIN json_each(b.j, '$.dados') AS elem
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_autor,   -- surrogate key
        cod_tipo,
        uri,
        ordem_assinatura,
        proponente,
        id_proposicao,
        year
    FROM exploded
)
SELECT *
FROM numbered;
DROP VIEW IF EXISTS bronze_camara_autores;