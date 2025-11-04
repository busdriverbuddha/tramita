

%%sql
DELETE FROM eventos_pauta_camara
WHERE rowid IN (
    SELECT rowid
    FROM (
        SELECT 
            rowid,
            ROW_NUMBER() OVER (
                PARTITION BY id_evento, ordem, id_proposicao
                ORDER BY rowid
            ) AS rn
        FROM eventos_pauta_camara
    ) t
    WHERE rn > 1
);