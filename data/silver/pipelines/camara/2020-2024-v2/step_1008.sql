-- Alterações:
-- 
-- * Descartar de `autores_camara` a linha onde `id_proposicao` = 2239097 e `id_deputado_ou_orgao` = 101489 (João Alberto)
-- * Descartar de `autores_camara` a linha onde `id_proposicao` = 2261160 e `id_deputado_ou_orgao` = 102133 (P50 SERVIÇOS INTEGRADOS)

%%sql
DELETE FROM autores_camara
WHERE (id_proposicao = 2239097 AND id_deputado_ou_orgao = 101489)
   OR (id_proposicao = 2261160 AND id_deputado_ou_orgao = 102133);
