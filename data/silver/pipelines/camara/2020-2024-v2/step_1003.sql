-- # Câmara dos Deputados
-- 
-- ## Removemos proposições anteriores a 2019 (unificação dos códigos de projeto de lei)

%%sql
DELETE FROM proposicoes_camara WHERE ano < 2019;