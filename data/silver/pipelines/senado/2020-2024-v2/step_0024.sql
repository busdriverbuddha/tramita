-- ### 2.2.4 Votações / Colegiado
-- ## 2.3 Outras relações entre tabelas
-- ### 2.3.1 Processos: autoria iniciativa, autoria documento

%%sql
CREATE OR REPLACE VIEW bronze_senado_processo AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/senado/processo/details/year=*/part-*.parquet")
WHERE source = 'senado' AND entity = 'processo';

SELECT COUNT(*) AS n FROM bronze_senado_processo;