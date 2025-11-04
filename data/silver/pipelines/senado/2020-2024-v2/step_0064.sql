-- ## 3.2. Deduplicação de tabelas relacionais
-- ### 3.2.1. Informes legislativos

%%sql
SELECT a.*
FROM informes_legislativos_senado a
JOIN (
    SELECT id_processo, id_informe
    FROM informes_legislativos_senado
    GROUP BY id_processo, id_informe
    HAVING COUNT(*) > 1
) dups
ON  a.id_processo = dups.id_processo
-- AND a.id_ente = dups.id_ente
-- AND a.autor = dups.autor
-- AND a.sigla_ente = dups.sigla_ente
AND a.id_informe = dups.id_informe
ORDER BY a.id_processo, a.id_informe
