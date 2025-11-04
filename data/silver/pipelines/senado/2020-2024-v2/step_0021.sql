

%%sql
DROP TABLE IF EXISTS votacoes_senado;

CREATE TABLE votacoes_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) AS j, year AS year_snapshot
    FROM bronze_senado_votacoes
)
SELECT
    CAST(jget1(j, '$.codigoSessaoVotacao') AS BIGINT) AS id_votacao,
    CAST(jget1(j, '$.codigoMateria') AS BIGINT) AS id_materia,
    CAST(jget1(j, '$.idProcesso') AS BIGINT) AS id_processo,
    jget1(j, '$.identificacao') AS identificacao,

    jget1(j, '$.sigla') AS sigla,
    jget1(j, '$.numero') AS numero,
    CAST(jget1(j, '$.ano') AS INTEGER) AS ano,

    CAST(jget1(j, '$.codigoSessao') AS BIGINT) AS codigo_sessao,
    CAST(jget1(j, '$.numeroSessao') AS INTEGER) AS numero_sessao,
    CAST(jget1(j, '$.sequencialSessao') AS INTEGER) AS sequencial_sessao,
    jget1(j, '$.siglaTipoSessao') AS sigla_tipo_sessao,
    jget1(j, '$.casaSessao') AS casa_sessao,
    CAST(jget1(j, '$.codigoSessaoLegislativa') AS BIGINT) AS codigo_sessao_legislativa,

    CAST(jget1(j, '$.dataApresentacao') AS TIMESTAMP) AS data_apresentacao,
    CAST(jget1(j, '$.dataSessao') AS TIMESTAMP) AS data_sessao,

    jget1(j, '$.descricaoVotacao') AS descricao_votacao,
    jget1(j, '$.ementa') AS ementa,

    jget1(j, '$.resultadoVotacao') AS resultado_votacao,
    CAST(jget1(j, '$.totalVotosSim') AS INTEGER) AS total_votos_sim,
    CAST(jget1(j, '$.totalVotosNao') AS INTEGER) AS total_votos_nao,
    CAST(jget1(j, '$.totalVotosAbstencao') AS INTEGER) AS total_votos_abstencao,
    jget1(j, '$.votacaoSecreta') AS votacao_secreta,

    -- informe legislativo expandido
    CAST(jget1(j, '$.informeLegislativo.id') AS BIGINT) AS id_informe,
    CAST(jget1(j, '$.informeLegislativo.idEvento') AS BIGINT) AS id_evento,
    CAST(jget1(j, '$.informeLegislativo.codigoColegiado') AS BIGINT) AS codigo_colegiado,
    jget1(j, '$.informeLegislativo.nomeColegiado') AS nome_colegiado,
    jget1(j, '$.informeLegislativo.siglaColegiado') AS sigla_colegiado,
    CAST(jget1(j, '$.informeLegislativo.data') AS TIMESTAMP) AS data_informe,
    jget1(j, '$.informeLegislativo.texto') AS texto_informe,

    year_snapshot
FROM base;
