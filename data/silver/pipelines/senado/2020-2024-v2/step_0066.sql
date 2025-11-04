

%%sql
DELETE FROM informes_legislativos_senado
WHERE rowid IN (
    SELECT rowid
    FROM (
        SELECT 
            rowid,
            ROW_NUMBER() OVER (
                PARTITION BY id_processo, id_informe, descricao, data_informe, sigla_situacao_iniciada, data_informe
                ORDER BY rowid
            ) AS rn
        FROM informes_legislativos_senado
    ) t
    WHERE rn > 1
);