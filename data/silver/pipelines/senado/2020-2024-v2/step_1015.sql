-- ### Selecionamos apenas os tipos de projetos que nos interessam

%%sql

DELETE FROM processo_senado
WHERE documento_sigla_tipo NOT IN (
    'PROJETO_LEI_ORDINARIA',
    'PROJETO_LEI_COMPLEMENTAR',
    'PROPOSTA_EMENDA_CONSTITUICAO',
    'MEDIDA_PROVISORIA',
);