

%%sql
SELECT SUM(c) AS total_duplicadas
FROM (
    SELECT COUNT(*) - 1 AS c
    FROM eventos_pauta_camara
    GROUP BY id_evento, ordem, id_proposicao
    HAVING COUNT(*) > 1
) t;