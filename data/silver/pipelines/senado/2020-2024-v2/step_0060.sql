-- ### 3.1.20. Unidades destinatárias

%%sql
ALTER TABLE unidades_destinatarias_senado
    ALTER COLUMN id_unidade_destinataria TYPE BIGINT;

ALTER TABLE unidades_destinatarias_senado
    ADD CONSTRAINT pk_unidade_destinataria PRIMARY KEY (id_unidade_destinataria);