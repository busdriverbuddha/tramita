-- ### Extraímos as tags referentes aos deputados, órgãos e proposições para construção dos grafos

%%sql

ALTER TABLE deputados_camara ADD COLUMN IF NOT EXISTS tag VARCHAR;
UPDATE deputados_camara SET tag = 'CD:' || CAST(id_deputado AS VARCHAR);

ALTER TABLE orgaos_camara ADD COLUMN IF NOT EXISTS tag VARCHAR;
UPDATE orgaos_camara SET tag = 'CO:' || CAST(id_orgao AS VARCHAR);

ALTER TABLE proposicoes_camara
  ADD COLUMN IF NOT EXISTS prop_tag VARCHAR;
ALTER TABLE proposicoes_camara
  ADD COLUMN IF NOT EXISTS prop_label VARCHAR;
ALTER TABLE proposicoes_camara
  ADD COLUMN IF NOT EXISTS prop_category VARCHAR;

CREATE OR REPLACE TABLE proposicoes_camara AS
WITH typed AS (
  SELECT
    p.* EXCLUDE (prop_tag, prop_label, prop_category),
    'CP:' || CAST(id_proposicao AS VARCHAR) AS prop_tag,
    sigla_tipo || ' ' || CAST(numero AS VARCHAR) || '/' || CAST(ano AS VARCHAR) AS prop_label,
    CASE
      WHEN sigla_tipo IN ('PL','PLP','PLN','PLV','PLS') THEN 'PL'
      WHEN sigla_tipo = 'PEC' THEN 'PEC'
      WHEN sigla_tipo = 'MPV' THEN 'MPV'
      ELSE NULL
    END AS prop_category
  FROM proposicoes_camara p
)
SELECT *
FROM typed
WHERE prop_category IS NOT NULL;