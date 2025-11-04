-- ### 3.2.5 Pautas de eventos

%%sql
SELECT a.*
FROM eventos_pauta_camara a
JOIN (
    SELECT id_evento, ordem
    FROM eventos_pauta_camara
    GROUP BY id_evento, ordem
    HAVING COUNT(*) > 1
) dups
ON  a.id_evento = dups.id_evento
AND a.ordem = dups.ordem
ORDER BY a.id_evento, a.ordem;