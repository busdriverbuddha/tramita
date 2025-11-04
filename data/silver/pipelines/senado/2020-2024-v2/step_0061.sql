-- ### 3.1.21. Encontros legislativos

%%sql
SELECT t.*
FROM encontro_legislativo_senado t
JOIN (
    SELECT id_encontro_legislativo
    FROM encontro_legislativo_senado
    GROUP BY id_encontro_legislativo
    HAVING COUNT(*) > 1
) dups
ON t.id_encontro_legislativo = dups.id_encontro_legislativo
ORDER BY t.id_encontro_legislativo;