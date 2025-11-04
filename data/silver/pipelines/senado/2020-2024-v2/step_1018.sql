-- ### Criamos uma tabela fazendo a correspondência entre as proposições da Câmara e os processos do Senado

%%sql
CREATE OR REPLACE TABLE correspondencia_proposicoes_processo AS
SELECT 
    pc.id_proposicao AS id_proposicao_camara,
    ps.id_processo   AS id_processo_senado,
    ps.identificacao
FROM proposicoes_camara AS pc
JOIN processo_senado AS ps
    ON pc.prop_label = ps.identificacao;
