

%%sql
SELECT SUM(c) AS total_duplicadas
FROM (
    SELECT COUNT(*) - 1 AS c
    FROM informes_legislativos_senado
    GROUP BY id_processo, id_informe, descricao, data_informe, sigla_situacao_iniciada, data_informe
    HAVING COUNT(*) > 1
) t;