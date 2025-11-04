

%%sql
DELETE FROM orientacoes_camara
WHERE rowid IN (
    SELECT rowid
    FROM (
        SELECT 
            rowid,
            ROW_NUMBER() OVER (
                PARTITION BY id_votacao, sigla_partido_bloco 
                ORDER BY rowid
            ) AS rn
        FROM orientacoes_camara
    ) t
    WHERE rn > 1
);
