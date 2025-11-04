

%%sql
DROP TABLE IF EXISTS relatorias_senado;

CREATE TABLE relatorias_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) AS j, year
    FROM bronze_senado_relatorias
)
SELECT
    -- chaves e relacionamentos
    CAST(jget1(j, '$.id')                AS BIGINT)   AS id_relatoria,
    CAST(jget1(j, '$.idProcesso')        AS BIGINT)   AS id_processo,
    CAST(jget1(j, '$.codigoMateria')     AS BIGINT)   AS codigo_materia,
    CAST(jget1(j, '$.codigoParlamentar') AS BIGINT)   AS codigo_parlamentar,

    -- colegiado
    CAST(jget1(j, '$.codigoColegiado')      AS BIGINT)  AS codigo_colegiado,
    CAST(jget1(j, '$.codigoTipoColegiado')  AS BIGINT)  AS codigo_tipo_colegiado,
    jget1(j, '$.siglaColegiado')                         AS sigla_colegiado,
    jget1(j, '$.nomeColegiado')                          AS nome_colegiado,

    -- processo
    jget1(j, '$.autoriaProcesso')                        AS autoria_processo,
    jget1(j, '$.identificacaoProcesso')                  AS identificacao_processo,
    jget1(j, '$.ementaProcesso')                         AS ementa_processo,
    CAST(jget1(j, '$.numeroAutuacao') AS INTEGER)        AS numero_autuacao,
    jget1(j, '$.tramitando')                              AS tramitando,

    -- casa/relator
    jget1(j, '$.siglaCasa')                               AS sigla_casa,
    jget1(j, '$.casaRelator')                             AS casa_relator,
    jget1(j, '$.descricaoTipoRelator')                    AS descricao_tipo_relator,
    CAST(jget1(j, '$.idTipoRelator') AS INTEGER)          AS id_tipo_relator,
    jget1(j, '$.descricaoTipoEncerramento')               AS descricao_tipo_encerramento,

    -- parlamentar
    jget1(j, '$.formaTratamentoParlamentar')              AS forma_tratamento_parlamentar,
    jget1(j, '$.nomeParlamentar')                         AS nome_parlamentar,
    jget1(j, '$.nomeCompleto')                            AS nome_completo,
    jget1(j, '$.siglaPartidoParlamentar')                 AS sigla_partido_parlamentar,
    jget1(j, '$.ufParlamentar')                           AS uf_parlamentar,
    jget1(j, '$.sexoParlamentar')                         AS sexo_parlamentar,
    jget1(j, '$.emailParlamentar')                        AS email_parlamentar,
    jget1(j, '$.urlFotoParlamentar')                      AS url_foto_parlamentar,
    jget1(j, '$.urlPaginaParlamentar')                    AS url_pagina_parlamentar,

    -- datas
    CAST(jget1(j, '$.dataApresentacaoProcesso') AS DATETIME) AS data_apresentacao_processo,
    CAST(jget1(j, '$.dataDesignacao')           AS DATETIME) AS data_designacao,
    CAST(jget1(j, '$.dataDestituicao')          AS DATETIME) AS data_destituicao,
    CAST(jget1(j, '$.dataFimColegiado')         AS DATETIME) AS data_fim_colegiado,

    -- snapshot
    year AS year_snapshot
FROM base
WHERE jget1(j, '$.id') IS NOT NULL;
DROP VIEW IF EXISTS bronze_senado_relatorias;