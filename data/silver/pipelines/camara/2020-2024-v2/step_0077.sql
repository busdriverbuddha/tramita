

%%sql
SELECT SUM(c) AS total_duplicadas
FROM (
    SELECT COUNT(*) - 1 AS c
    FROM orientacoes_camara
    GROUP BY id_votacao, sigla_partido_bloco
    HAVING COUNT(*) > 1
) t;