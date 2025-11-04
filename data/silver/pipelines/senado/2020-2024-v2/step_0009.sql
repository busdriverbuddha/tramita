

%%sql
DROP TABLE IF EXISTS parlamentar_senado;

CREATE TABLE parlamentar_senado AS
WITH base AS (
    SELECT TRY_CAST(payload_json AS JSON) AS j, year
    FROM bronze_senado_parlamentar
),
par_root AS (
    SELECT
        json_extract(j, '$.DetalheParlamentar.Parlamentar') AS par,
        year
    FROM base
),
flattened AS (
    SELECT
        -- Identificação
        CAST(jget1(par, '$.IdentificacaoParlamentar.CodigoParlamentar') AS BIGINT) AS codigo_parlamentar,
        CAST(jget1(par, '$.IdentificacaoParlamentar.CodigoPublicoNaLegAtual') AS BIGINT) AS codigo_publico_leg_atual,
        jget1(par, '$.IdentificacaoParlamentar.NomeCompletoParlamentar') AS nome_completo,
        jget1(par, '$.IdentificacaoParlamentar.NomeParlamentar') AS nome_parlamentar,
        jget1(par, '$.IdentificacaoParlamentar.SexoParlamentar') AS sexo_parlamentar,
        jget1(par, '$.IdentificacaoParlamentar.SiglaPartidoParlamentar') AS sigla_partido,
        jget1(par, '$.IdentificacaoParlamentar.UfParlamentar') AS uf_parlamentar,
        jget1(par, '$.IdentificacaoParlamentar.EmailParlamentar') AS email_parlamentar,
        -- Dados básicos
        CAST(jget1(par, '$.DadosBasicosParlamentar.DataNascimento') AS DATE) AS data_nascimento,
        jget1(par, '$.DadosBasicosParlamentar.EnderecoParlamentar') AS endereco_parlamentar,
        jget1(par, '$.DadosBasicosParlamentar.Naturalidade') AS naturalidade,
        jget1(par, '$.DadosBasicosParlamentar.UfNaturalidade') AS uf_naturalidade,
        year AS year_snapshot
    FROM par_root
)
SELECT *
FROM flattened
WHERE codigo_parlamentar IS NOT NULL;

DROP VIEW IF EXISTS bronze_senado_parlamentar;
