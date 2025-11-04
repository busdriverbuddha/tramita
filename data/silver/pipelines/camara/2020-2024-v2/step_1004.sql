-- ### Removemos linhas de autoria para proposições removidas

%%sql
DELETE FROM autores_camara
WHERE id_proposicao NOT IN (
    SELECT id_proposicao FROM proposicoes_camara
);