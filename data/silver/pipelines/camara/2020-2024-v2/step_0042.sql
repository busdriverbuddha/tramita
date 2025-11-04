-- ### 2.3.8 Legislaturas e mesa


%%sql
CREATE OR REPLACE VIEW bronze_camara_legislaturas_mesa AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/legislaturas/mesa/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'legislaturas/mesa';

SELECT COUNT(*) AS n FROM bronze_camara_legislaturas_mesa;