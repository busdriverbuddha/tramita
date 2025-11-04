-- ## Processos
-- ### Apagamos os processos anteriores a 2019 e os que originaram de proposições da câmara anteriores a 2019

%%sql
DELETE FROM processo_senado
WHERE ano < 2019;

DELETE
FROM processo_senado
WHERE CAST(SPLIT_PART(identificacao_processo_inicial, '/', 2) AS INTEGER) < 2019;