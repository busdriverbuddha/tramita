-- ### 3.1.19. Movimentações

%%sql
ALTER TABLE movimentacoes_senado
    ADD CONSTRAINT pk_movimentacao PRIMARY KEY (
        id_processo,
        autuacao_idx,
        movimentacao_idx
    );