-- ## 3.2 Deduplicação de tabelas relacionais
-- ### 3.2.1 Orientações

%%sql
SELECT a.*
FROM orientacoes_camara a
JOIN (
    SELECT sigla_partido_bloco, id_votacao
    FROM orientacoes_camara
    GROUP BY sigla_partido_bloco, id_votacao
    HAVING COUNT(*) > 1
) dups
ON  a.sigla_partido_bloco = dups.sigla_partido_bloco
AND a.id_votacao = dups.id_votacao
ORDER BY a.id_votacao, a.sigla_partido_bloco;
