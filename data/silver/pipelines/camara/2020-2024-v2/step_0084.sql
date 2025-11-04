-- ### 3.2.3 Votos

%%sql
SELECT a.*
FROM votos_camara a
JOIN (
    SELECT id_votacao, id_deputado, data_hora
    FROM votos_camara
    GROUP BY id_votacao, id_deputado, data_hora
    HAVING COUNT(*) > 1
) dups
ON  a.id_deputado = dups.id_deputado
AND a.id_votacao = dups.id_votacao
AND a.data_hora = dups.data_hora
ORDER BY a.id_deputado, a.id_votacao;