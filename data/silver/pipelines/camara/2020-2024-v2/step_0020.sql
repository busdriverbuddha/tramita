

%%sql
DROP TABLE IF EXISTS temas_camara;
CREATE TABLE temas_camara AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) as j, year
    FROM bronze_camara_temas
),
exploded as (
    SELECT
        CAST(jget1(elem.value, '$.codTema') AS BIGINT) AS id_tema,
        jget1(elem.value, '$.tema') AS descricao,
    FROM base
    CROSS JOIN json_each(json_extract(j, '$.dados')) AS elem
)
SELECT
    id_tema,
    max(descricao) as descricao,
FROM exploded
WHERE id_tema IS NOT NULL
GROUP BY id_tema
ORDER BY id_tema;
DROP VIEW IF EXISTS bronze_camara_temas;