-- ## 2.2 Modelos factuais
-- ### 2.2.1 Emendas

%%sql
CREATE OR REPLACE VIEW bronze_senado_emendas AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/senado/emendas/year=*/part-*.parquet")
WHERE source = 'senado' AND entity = 'emendas';

SELECT COUNT(*) AS n FROM bronze_senado_emendas;