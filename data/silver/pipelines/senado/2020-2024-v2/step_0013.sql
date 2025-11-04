

%%sql
DROP TABLE IF EXISTS processo_senado;

CREATE TABLE processo_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) AS j, year
    FROM bronze_senado_processo
),
flat AS (
    SELECT
        -- identificadores principais
        CAST(jget1(j, '$.id') AS BIGINT)                       AS id_processo,
        CAST(jget1(j, '$.codigoMateria') AS BIGINT)            AS codigo_materia,
        CAST(jget1(j, '$.idProcessoCasaInicial') AS BIGINT)    AS id_processo_casa_inicial,

        jget1(j, '$.identificacao')                            AS identificacao,
        jget1(j, '$.identificacaoProcessoInicial')             AS identificacao_processo_inicial,
        jget1(j, '$.identificacaoExterna')                     AS identificacao_externa,

        -- campos simples de nível superior
        CAST(jget1(j, '$.ano') AS INTEGER)                     AS ano,
        jget1(j, '$.casaIdentificadora')                       AS casa_identificadora,
        jget1(j, '$.siglaCasaIniciadora')                      AS sigla_casa_iniciadora,
        jget1(j, '$.siglaEnteIdentificador')                   AS sigla_ente_identificador,
        jget1(j, '$.descricaoSigla')                           AS descricao_sigla,
        jget1(j, '$.sigla')                                    AS sigla,
        jget1(j, '$.numero')                                   AS numero,
        jget1(j, '$.objetivo')                                 AS objetivo,
        jget1(j, '$.tramitando')                               AS tramitando,

        -- conteúdo principal
        CAST(jget1(j, '$.conteudo.id') AS BIGINT)              AS id_conteudo,
        CAST(jget1(j, '$.conteudo.idTipo') AS BIGINT)          AS id_tipo_conteudo,
        jget1(j, '$.conteudo.siglaTipo')                       AS sigla_tipo_conteudo,
        jget1(j, '$.conteudo.tipo')                            AS tipo_conteudo,
        jget1(j, '$.conteudo.tipoNormaIndicada')               AS tipo_norma_indicada,
        jget1(j, '$.conteudo.ementa')                          AS ementa,
        jget1(j, '$.conteudo.explicacaoEmenta')                AS explicacao_ementa,

        -- deliberação final
        CAST(jget1(j, '$.deliberacao.idDestino') AS BIGINT)    AS deliberacao_id_destino,
        jget1(j, '$.deliberacao.siglaDestino')                 AS deliberacao_sigla_destino,
        jget1(j, '$.deliberacao.tipoDeliberacao')              AS deliberacao_tipo,
        jget1(j, '$.deliberacao.siglaTipo')                    AS deliberacao_sigla_tipo,
        CAST(jget1(j, '$.deliberacao.data') AS DATE)           AS deliberacao_data,
        jget1(j, '$.deliberacao.destino')                      AS deliberacao_destino,

        -- documento associado
        CAST(jget1(j, '$.documento.id') AS BIGINT)             AS id_documento,
        jget1(j, '$.documento.siglaTipo')                      AS documento_sigla_tipo,
        jget1(j, '$.documento.tipo')                           AS documento_tipo,
        jget1(j, '$.documento.indexacao')                      AS documento_indexacao,
        jget1(j, '$.documento.resumoAutoria')                  AS documento_resumo_autoria,
        CAST(jget1(j, '$.documento.dataApresentacao') AS DATE) AS documento_data_apresentacao,
        CAST(jget1(j, '$.documento.dataLeitura') AS DATE)      AS documento_data_leitura,

        -- norma gerada
        CAST(jget1(j, '$.normaGerada.codigo') AS BIGINT)       AS norma_codigo,
        jget1(j, '$.normaGerada.numero')                       AS norma_numero,
        jget1(j, '$.normaGerada.siglaTipo')                    AS norma_sigla_tipo,
        jget1(j, '$.normaGerada.tipo')                         AS norma_tipo,
        jget1(j, '$.normaGerada.descricao')                    AS norma_descricao,
        jget1(j, '$.normaGerada.siglaVeiculoPublicacao')       AS norma_sigla_veiculo,
        jget1(j, '$.normaGerada.veiculoPublicacao')            AS norma_veiculo,
        CAST(jget1(j, '$.normaGerada.numero') AS INTEGER)      AS norma_numero_int,
        CAST(jget1(j, '$.normaGerada.anoAssinatura') AS INTEGER) AS norma_ano_assinatura,
        CAST(jget1(j, '$.normaGerada.dataAssinatura') AS DATE) AS norma_data_assinatura,
        CAST(jget1(j, '$.normaGerada.dataPublicacao') AS DATE) AS norma_data_publicacao,

        year AS year_snapshot
    FROM base
)
SELECT *
FROM flat
WHERE id_processo IS NOT NULL;


DROP TABLE IF EXISTS tipo_deliberacao_senado;

CREATE TABLE tipo_deliberacao_senado AS
WITH base AS (
  SELECT
    deliberacao_sigla_tipo   AS sigla_tipo_deliberacao,
    deliberacao_tipo         AS descricao_tipo_deliberacao,
    -- campos auxiliares úteis (opc.)
    deliberacao_id_destino   AS id_destino,
    deliberacao_sigla_destino AS sigla_destino,
    deliberacao_destino      AS destino,
    year_snapshot
  FROM processo_senado
  WHERE deliberacao_sigla_tipo IS NOT NULL
)
SELECT
  sigla_tipo_deliberacao,
  arg_max(descricao_tipo_deliberacao, year_snapshot) AS descricao_tipo_deliberacao,
  arg_max(id_destino,               year_snapshot)   AS id_destino,
  arg_max(sigla_destino,            year_snapshot)   AS sigla_destino,
  arg_max(destino,                  year_snapshot)   AS destino,
  max(year_snapshot)                                AS year_snapshot
FROM base
GROUP BY sigla_tipo_deliberacao;

DROP TABLE IF EXISTS tipo_conteudo_senado;

CREATE TABLE tipo_conteudo_senado AS
WITH base AS (
  SELECT
    id_tipo_conteudo       AS id_tipo_conteudo,      -- chave numérica
    sigla_tipo_conteudo    AS sigla_tipo_conteudo,
    tipo_conteudo          AS descricao_tipo_conteudo,
    tipo_norma_indicada    AS tipo_norma_indicada,   -- pode ser NULL dependendo do caso
    year_snapshot
  FROM processo_senado
  WHERE id_tipo_conteudo IS NOT NULL
)
SELECT
  id_tipo_conteudo,
  arg_max(sigla_tipo_conteudo,    year_snapshot) AS sigla_tipo_conteudo,
  arg_max(descricao_tipo_conteudo,year_snapshot) AS descricao_tipo_conteudo,
  arg_max(tipo_norma_indicada,    year_snapshot) AS tipo_norma_indicada,
  max(year_snapshot)                             AS year_snapshot
FROM base
GROUP BY id_tipo_conteudo;

DROP VIEW IF EXISTS bronze_senado_processo;
