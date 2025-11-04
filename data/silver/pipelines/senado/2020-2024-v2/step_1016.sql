-- ### Regularizamos tags de processos

%%sql
ALTER TABLE processo_senado ADD COLUMN IF NOT EXISTS tag VARCHAR;
update processo_senado SET tag = 'SP:' || CAST(id_processo AS VARCHAR);