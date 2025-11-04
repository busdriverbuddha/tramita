-- ## 2.3 Outras relações entre tabelas
-- ### 2.3.1 Blocos e partidos

%%sql
CREATE OR REPLACE VIEW bronze_camara_blocos_partidos AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/blocos/partidos/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'blocos/partidos';

SELECT COUNT(*) AS n FROM bronze_camara_blocos_partidos;