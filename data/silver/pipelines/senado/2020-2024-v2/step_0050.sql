-- ### 3.1.11. Despachos

%%sql
SELECT t.*
FROM despachos_senado t
JOIN (
    SELECT id_despacho
    FROM despachos_senado
    GROUP BY id_despacho
    HAVING COUNT(*) > 1
) dups
ON t.id_despacho = dups.id_despacho
ORDER BY t.id_despacho;