

%%sql
DELETE FROM votos_camara
WHERE rowid IN (
    SELECT rowid
    FROM (
        SELECT 
            rowid,
            ROW_NUMBER() OVER (
                PARTITION BY id_votacao, id_deputado, data_hora
                ORDER BY rowid
            ) AS rn
        FROM votos_camara
    ) t
    WHERE rn > 1
);