-- ### 3.2.2 Tramitações

%%sql
SELECT a.*
FROM tramitacoes_camara a
JOIN (
    SELECT id_proposicao, despacho, sequencia
    FROM tramitacoes_camara
    GROUP BY id_proposicao, despacho, sequencia
    HAVING COUNT(*) > 1
) dups
ON  a.id_proposicao = dups.id_proposicao
AND a.sequencia = dups.sequencia
AND a.despacho = dups.despacho
ORDER BY a.id_proposicao, a.sequencia, a.despacho;
