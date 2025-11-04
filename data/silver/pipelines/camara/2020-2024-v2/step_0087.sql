-- ### 3.2.4 Deputados e frentes

%%sql
SELECT a.*
FROM deputados_frentes_camara a
JOIN (
    SELECT id_deputado, id_frente
    FROM deputados_frentes_camara
    GROUP BY id_deputado, id_frente
    HAVING COUNT(*) > 1
) dups
ON  a.id_deputado = dups.id_deputado
AND a.id_frente = dups.id_frente
ORDER BY a.id_deputado, a.id_frente;