-- ### Populamos as linhas de autoria com os descritivos dos autores

%%sql
-- Add new columns
ALTER TABLE autores_camara ADD COLUMN IF NOT EXISTS tipo_autor VARCHAR;
ALTER TABLE autores_camara ADD COLUMN IF NOT EXISTS id_deputado_ou_orgao BIGINT;

-- Populate from URI
UPDATE autores_camara
SET
  tipo_autor = REGEXP_EXTRACT(uri, '.*/(deputados|orgaos)/([0-9]+)$', 1),
  id_deputado_ou_orgao = TRY_CAST(REGEXP_EXTRACT(uri, '.*/(deputados|orgaos)/([0-9]+)$', 2) AS BIGINT)
WHERE uri IS NOT NULL;