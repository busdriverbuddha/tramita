

%%sql
DELETE FROM tramitacoes_camara
WHERE rowid IN (
    SELECT rowid
    FROM (
        SELECT 
            rowid,
            ROW_NUMBER() OVER (
                PARTITION BY id_proposicao, despacho, sequencia 
                ORDER BY rowid
            ) AS rn
        FROM tramitacoes_camara
    ) t
    WHERE rn > 1
);
