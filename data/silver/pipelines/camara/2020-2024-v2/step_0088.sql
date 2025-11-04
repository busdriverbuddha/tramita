

%%sql
SELECT SUM(c) AS total_duplicadas
FROM (
    SELECT COUNT(*) - 1 AS c
    FROM deputados_frentes_camara
    GROUP BY id_deputado, id_frente
    HAVING COUNT(*) > 1
) t;