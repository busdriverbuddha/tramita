-- ### Filtramos as linhas de autoria

%%sql

DELETE FROM documento_autoria_senado as aut
WHERE aut.id_processo NOT IN (
    SELECT p.id_processo FROM processo_senado as p
);
