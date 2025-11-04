

%%sql
SELECT SUM(c) AS total_duplicadas
FROM (
    SELECT COUNT(*) - 1 AS c
    FROM votos_camara
    GROUP BY id_votacao, id_deputado, data_hora
    HAVING COUNT(*) > 1
) t;