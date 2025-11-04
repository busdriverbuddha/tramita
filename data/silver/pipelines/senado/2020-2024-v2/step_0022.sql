

%%sql
DROP TABLE IF EXISTS votos_senado;

CREATE TABLE votos_senado AS
WITH base AS (
  SELECT
    TRY_CAST(payload_json AS JSON) AS j,
    year AS year_snapshot
  FROM bronze_senado_votacoes
),
exploded AS (
  SELECT
    CAST(jget1(b.j, '$.codigoVotacaoSve') AS BIGINT)        AS codigo_votacao_sve,
    CAST(jget1(b.j, '$.codigoSessaoVotacao') AS BIGINT)     AS codigo_sessao_votacao,
    CAST(jget1(b.j, '$.codigoMateria') AS BIGINT)           AS codigo_materia,
    jget1(b.j, '$.identificacao')                           AS identificacao_materia,

    -- Campos do voto
    CAST(json_extract_string(e.value, '$.codigoParlamentar') AS BIGINT) AS codigo_parlamentar,
    json_extract_string(e.value, '$.nomeParlamentar')        AS nome_parlamentar,
    json_extract_string(e.value, '$.sexoParlamentar')        AS sexo_parlamentar,
    json_extract_string(e.value, '$.siglaPartidoParlamentar')AS sigla_partido_parlamentar,
    json_extract_string(e.value, '$.siglaUFParlamentar')     AS sigla_uf_parlamentar,
    json_extract_string(e.value, '$.siglaVotoParlamentar')   AS sigla_voto_parlamentar,
    json_extract_string(e.value, '$.descricaoVotoParlamentar') AS descricao_voto_parlamentar,

    -- Snapshot
    b.year_snapshot
  FROM base b
  -- explode apenas quando existir a lista
  CROSS JOIN json_each(b.j, '$.votos') AS e
),
numbered AS (
    SELECT
        ROW_NUMBER() OVER () AS id_voto,
        codigo_votacao_sve,
        codigo_sessao_votacao,
        codigo_materia,
        identificacao_materia,
        codigo_parlamentar,
        nome_parlamentar,
        sexo_parlamentar,
        sigla_partido_parlamentar,
        sigla_uf_parlamentar,
        sigla_voto_parlamentar,
        descricao_voto_parlamentar,
        year_snapshot
    FROM exploded
)
SELECT * FROM numbered;
