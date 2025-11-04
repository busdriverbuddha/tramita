


%%sql
DROP TABLE IF EXISTS legislaturas_mesa_camara;
CREATE TABLE legislaturas_mesa_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, 
    year AS year_snapshot,
    id AS id_legislatura,
    FROM bronze_camara_legislaturas_mesa
),
exploded as (
    SELECT
        CAST(base.id_legislatura AS BIGINT) AS id_legislatura,
        -- id
        CAST(jget1(elem.value, '$.id') AS BIGINT) AS id_deputado,
        -- codTitulo
        jget1(elem.value, '$.codTitulo') AS cod_titulo,
        -- dataInicio
        CAST(jget1(elem.value, '$.dataInicio') AS DATE) AS data_inicio,
        -- dataFim
        CAST(jget1(elem.value, '$.dataFim') AS DATE) AS data_fim,
        year_snapshot,
    FROM base
    CROSS JOIN json_each(json_extract(j, '$.dados')) AS elem
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_legislatura_mesa,
        id_legislatura,
        id_deputado,
        cod_titulo,
        data_inicio,
        data_fim,
        year_snapshot
    FROM exploded
)
SELECT *
FROM numbered
WHERE id_legislatura IS NOT NULL AND id_deputado IS NOT NULL
ORDER BY id_legislatura, cod_titulo;


