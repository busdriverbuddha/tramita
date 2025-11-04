

%%sql
SELECT SUM(c) AS total_duplicadas
FROM (
    SELECT COUNT(*) - 1 AS c
    FROM tramitacoes_camara
    GROUP BY id_proposicao, despacho, sequencia
    HAVING COUNT(*) > 1
) t;