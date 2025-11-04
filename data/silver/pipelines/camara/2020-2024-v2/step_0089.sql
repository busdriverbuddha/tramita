

%%sql
DELETE FROM deputados_frentes_camara
WHERE rowid IN (
    SELECT rowid
    FROM (
        SELECT 
            rowid,
            ROW_NUMBER() OVER (
                PARTITION BY id_deputado, id_frente
                ORDER BY rowid
            ) AS rn
        FROM deputados_frentes_camara
    ) t
    WHERE rn > 1
);