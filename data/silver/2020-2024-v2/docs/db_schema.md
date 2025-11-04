# Database Schema Documentation

Total tables: 66

---

## main.autores_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_autor | BIGINT | NO | - |
| cod_tipo | BIGINT | YES | - |
| uri | VARCHAR | YES | - |
| ordem_assinatura | INTEGER | YES | - |
| proponente | BOOLEAN | YES | - |
| id_proposicao | BIGINT | YES | - |
| year | BIGINT | YES | - |
| tipo_autor | VARCHAR | YES | - |
| id_deputado_ou_orgao | BIGINT | YES | - |

---

## main.autoria_documento_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_autoria_documento | BIGINT | YES | - |
| id_processo | BIGINT | YES | - |
| id_documento | BIGINT | YES | - |
| autor | VARCHAR | YES | - |
| sigla_tipo | VARCHAR | YES | - |
| descricao_tipo | VARCHAR | YES | - |
| ordem | INTEGER | YES | - |
| outros_autores_nao_informados | VARCHAR | YES | - |
| id_ente | BIGINT | YES | - |
| sigla_ente | VARCHAR | YES | - |
| casa_ente | VARCHAR | YES | - |
| ente | VARCHAR | YES | - |
| cargo | VARCHAR | YES | - |
| siglaCargo | VARCHAR | YES | - |
| partido | VARCHAR | YES | - |
| sexo | VARCHAR | YES | - |
| uf | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.autoria_iniciativa_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_autoria_iniciativa | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| codigo_parlamentar | BIGINT | YES | - |
| descricao_tipo | VARCHAR | YES | - |
| ente | VARCHAR | YES | - |
| ordem | INTEGER | YES | - |
| outros_autores_nao_informados | VARCHAR | YES | - |
| sigla_ente | VARCHAR | YES | - |
| sigla_tipo | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.autuacoes_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_processo | BIGINT | NO | - |
| autuacao_idx | BIGINT | NO | - |
| descricao_autuacao | VARCHAR | YES | - |
| id_ente_controle_atual | BIGINT | YES | - |
| nome_ente_controle_atual | VARCHAR | YES | - |
| sigla_ente_controle_atual | VARCHAR | YES | - |
| numero_autuacao | INTEGER | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.bloco_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| codigo_bloco | BIGINT | NO | - |
| data_criacao | DATE | YES | - |
| nome_apelido | VARCHAR | YES | - |
| nome_bloco | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.blocos_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_bloco | BIGINT | NO | - |
| nome | VARCHAR | YES | - |
| id_legislatura | BIGINT | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.blocos_partidos_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_bloco_partido | BIGINT | NO | - |
| id_bloco | BIGINT | YES | - |
| id_partido | BIGINT | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.bronze_camara_blocos_partidos

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_camara_deputados_frentes

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_camara_deputados_historico

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_camara_deputados_orgaos

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_camara_eventos_orgaos

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_camara_eventos_pauta

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_camara_legislaturas_mesa

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_camara_votacoes

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_senado_colegiado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.bronze_senado_processo

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| source | VARCHAR | YES | - |
| entity | VARCHAR | YES | - |
| id | VARCHAR | YES | - |
| url | VARCHAR | YES | - |
| payload_json | VARCHAR | YES | - |
| payload_sha256 | VARCHAR | YES | - |
| year | BIGINT | YES | - |

---

## main.camara_authors

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_proposicao | BIGINT | YES | - |
| uri_kind | VARCHAR | YES | - |
| author_id_num | BIGINT | YES | - |

---

## main.colegiado_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| codigo_colegiado | BIGINT | YES | - |
| codigo_tipo_colegiado | BIGINT | YES | - |
| data_inicio | DATE | YES | - |
| indicador_distr_partidaria | VARCHAR | YES | - |
| nome_colegiado | VARCHAR | YES | - |
| sigla_colegiado | VARCHAR | YES | - |
| ordem | INTEGER | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.correspondencia_proposicoes_processo

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_proposicao_camara | BIGINT | YES | - |
| id_processo_senado | BIGINT | YES | - |
| identificacao | VARCHAR | YES | - |

---

## main.deputados_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_deputado | BIGINT | NO | - |
| nome_civil | VARCHAR | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |
| tag | VARCHAR | YES | - |

---

## main.deputados_frentes_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_deputado_frente | BIGINT | NO | - |
| id_deputado | BIGINT | YES | - |
| id_frente | BIGINT | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.deputados_historico_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_deputado_historico | BIGINT | NO | - |
| id_deputado | BIGINT | YES | - |
| id_legislatura | BIGINT | YES | - |
| data_hora | TIMESTAMP | YES | - |
| condicao_eleitoral | VARCHAR | YES | - |
| descricao_status | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.deputados_orgaos_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_deputado_orgao | BIGINT | NO | - |
| id_deputado | BIGINT | YES | - |
| id_orgao | INTEGER | YES | - |
| cod_titulo | INTEGER | YES | - |
| data_inicio | TIMESTAMP | YES | - |
| data_fim | TIMESTAMP | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.despachos_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_processo | BIGINT | NO | - |
| id_despacho | BIGINT | NO | - |
| data_despacho | DATE | YES | - |
| cancelado | VARCHAR | YES | - |
| tipo_motivacao | VARCHAR | YES | - |
| sigla_tipo_motivacao | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.documento_autoria_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_documento_autoria | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| id_ente | BIGINT | YES | - |
| autor | VARCHAR | YES | - |
| codigo_parlamentar | BIGINT | YES | - |
| descricao_tipo | VARCHAR | YES | - |
| ente | VARCHAR | YES | - |
| ordem | INTEGER | YES | - |
| outros_autores_nao_informados | VARCHAR | YES | - |
| sigla_ente | VARCHAR | YES | - |
| sigla_tipo | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| tipo_autor | VARCHAR | YES | - |
| id_senador_ou_ente | BIGINT | YES | - |

---

## main.emendas_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_emenda | BIGINT | NO | - |
| id_ci_emenda | BIGINT | YES | - |
| id_ci_emendado | BIGINT | YES | - |
| id_documento_emenda | BIGINT | YES | - |
| id_processo | BIGINT | YES | - |
| identificacao | VARCHAR | YES | - |
| numero | INTEGER | YES | - |
| autoria | VARCHAR | YES | - |
| descricao_documento_emenda | VARCHAR | YES | - |
| tipo_emenda | VARCHAR | YES | - |
| turno_apresentacao | VARCHAR | YES | - |
| casa | VARCHAR | YES | - |
| codigo_colegiado | BIGINT | YES | - |
| sigla_colegiado | VARCHAR | YES | - |
| nome_colegiado | VARCHAR | YES | - |
| data_apresentacao | DATE | YES | - |
| url_documento_emenda | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.encontro_legislativo_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_processo | BIGINT | YES | - |
| id_despacho | BIGINT | YES | - |
| id_encontro_legislativo | BIGINT | NO | - |
| data_encontro | DATE | YES | - |
| tipo_encontro | VARCHAR | YES | - |
| descricao_encontro | VARCHAR | YES | - |
| casa_encontro | VARCHAR | YES | - |
| numero_encontro | INTEGER | YES | - |
| colegiado_casa | VARCHAR | YES | - |
| colegiado_codigo | BIGINT | YES | - |
| colegiado_nome | VARCHAR | YES | - |
| colegiado_sigla | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.ente_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_ente | BIGINT | NO | - |
| sigla | VARCHAR | YES | - |
| nome | VARCHAR | YES | - |
| casa | VARCHAR | YES | - |
| sigla_tipo | VARCHAR | YES | - |
| descricao_tipo | VARCHAR | YES | - |
| data_inicio | DATE | YES | - |
| data_fim | DATE | YES | - |
| tag | VARCHAR | YES | - |

---

## main.eventos_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_evento | BIGINT | NO | - |
| data_hora_inicio | TIMESTAMP | YES | - |
| data_hora_fim | TIMESTAMP | YES | - |
| descricao | VARCHAR | YES | - |
| descricao_tipo | VARCHAR | YES | - |
| fases | VARCHAR | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.eventos_orgaos_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_evento_orgao | BIGINT | NO | - |
| id_evento | BIGINT | YES | - |
| id_orgao | INTEGER | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.eventos_pauta_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_pauta | BIGINT | NO | - |
| id_evento | BIGINT | YES | - |
| cod_regime | VARCHAR | YES | - |
| ordem | INTEGER | YES | - |
| id_proposicao | BIGINT | YES | - |
| id_relator | BIGINT | YES | - |
| year_snapshot | INTEGER | YES | - |

---

## main.frentes_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_frente | BIGINT | NO | - |
| id_deputado_coordenador | BIGINT | YES | - |
| id_legislatura | BIGINT | YES | - |
| titulo | VARCHAR | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.informes_documentos_associados_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_documento_associado | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| id_informe | BIGINT | YES | - |
| id_documento | BIGINT | YES | - |
| autuacao_ordem | INTEGER | YES | - |
| informe_ordem | INTEGER | YES | - |
| documento_ordem | INTEGER | YES | - |
| sigla_tipo_documento | VARCHAR | YES | - |
| tipo_documento | VARCHAR | YES | - |
| identificacao | VARCHAR | YES | - |
| data_documento | TIMESTAMP | YES | - |
| autoria_documento | VARCHAR | YES | - |
| url_documento | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.informes_legislativos_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_informe_legislativo | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| id_informe | BIGINT | YES | - |
| data_informe | DATE | YES | - |
| descricao | VARCHAR | YES | - |
| id_situacao_iniciada | BIGINT | YES | - |
| sigla_situacao_iniciada | VARCHAR | YES | - |
| ente_adm_casa | VARCHAR | YES | - |
| ente_adm_id | BIGINT | YES | - |
| ente_adm_nome | VARCHAR | YES | - |
| ente_adm_sigla | VARCHAR | YES | - |
| colegiado_casa | VARCHAR | YES | - |
| colegiado_codigo | BIGINT | YES | - |
| colegiado_nome | VARCHAR | YES | - |
| colegiado_sigla | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.legislaturas_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_legislatura | BIGINT | NO | - |
| data_inicio | DATE | YES | - |
| data_fim | DATE | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.legislaturas_lideres_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_lider | BIGINT | NO | - |
| id_legislatura | BIGINT | YES | - |
| nome_bancada | VARCHAR | YES | - |
| tipo_bancada | VARCHAR | YES | - |
| uri_bancada | VARCHAR | YES | - |
| data_inicio | TIMESTAMP | YES | - |
| data_fim | TIMESTAMP | YES | - |
| id_deputado | BIGINT | YES | - |
| titulo | VARCHAR | YES | - |
| year_snapshot | INTEGER | YES | - |

---

## main.legislaturas_mesa_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_legislatura_mesa | BIGINT | YES | - |
| id_legislatura | BIGINT | YES | - |
| id_deputado | BIGINT | YES | - |
| cod_titulo | VARCHAR | YES | - |
| data_inicio | DATE | YES | - |
| data_fim | DATE | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.missing_orgaos

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_orgao | BIGINT | YES | - |

---

## main.movimentacoes_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_processo | BIGINT | NO | - |
| autuacao_idx | INTEGER | NO | - |
| movimentacao_idx | INTEGER | NO | - |
| id_movimentacao | BIGINT | YES | - |
| data_envio | TIMESTAMP | YES | - |
| data_recebimento | TIMESTAMP | YES | - |
| ente_origem_casa | VARCHAR | YES | - |
| ente_origem_id | BIGINT | YES | - |
| ente_origem_nome | VARCHAR | YES | - |
| ente_origem_sigla | VARCHAR | YES | - |
| ente_destino_casa | VARCHAR | YES | - |
| ente_destino_id | BIGINT | YES | - |
| ente_destino_nome | VARCHAR | YES | - |
| ente_destino_sigla | VARCHAR | YES | - |
| colegiado_destino_casa | VARCHAR | YES | - |
| colegiado_destino_codigo | BIGINT | YES | - |
| colegiado_destino_nome | VARCHAR | YES | - |
| colegiado_destino_sigla | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.orgaos_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_orgao | BIGINT | NO | - |
| nome | VARCHAR | YES | - |
| cod_tipo_orgao | BIGINT | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |
| tag | VARCHAR | YES | - |

---

## main.orgaos_camara_hotfix

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_orgao | BIGINT | YES | - |
| nome | VARCHAR | YES | - |
| cod_tipo_orgao | BIGINT | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.orientacoes_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_orientacao | BIGINT | NO | - |
| id_votacao | VARCHAR | YES | - |
| sigla_partido_bloco | VARCHAR | YES | - |
| orientacao_voto | VARCHAR | YES | - |
| cod_partido_bloco | BIGINT | YES | - |
| cod_tipo_lideranca | VARCHAR | YES | - |
| uri_partido_bloco | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.outros_numeros_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_outro_numero | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| id_outro_processo | BIGINT | YES | - |
| ano | INTEGER | YES | - |
| casa_identificadora | VARCHAR | YES | - |
| ente_identificador | VARCHAR | YES | - |
| sigla | VARCHAR | YES | - |
| numero | VARCHAR | YES | - |
| sigla_ente_identificador | VARCHAR | YES | - |
| externa_ao_congresso | VARCHAR | YES | - |
| tramitando | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.parlamentar_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| codigo_parlamentar | BIGINT | NO | - |
| codigo_publico_leg_atual | BIGINT | YES | - |
| nome_completo | VARCHAR | YES | - |
| nome_parlamentar | VARCHAR | YES | - |
| sexo_parlamentar | VARCHAR | YES | - |
| sigla_partido | VARCHAR | YES | - |
| uf_parlamentar | VARCHAR | YES | - |
| email_parlamentar | VARCHAR | YES | - |
| data_nascimento | DATE | YES | - |
| endereco_parlamentar | VARCHAR | YES | - |
| naturalidade | VARCHAR | YES | - |
| uf_naturalidade | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.partido_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| codigo_partido | BIGINT | NO | - |
| data_criacao | DATE | YES | - |
| nome | VARCHAR | YES | - |
| sigla | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.partidos_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_partido | BIGINT | NO | - |
| nome | VARCHAR | YES | - |
| sigla | VARCHAR | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.partidos_lideres_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_partido_lider | BIGINT | NO | - |
| id_partido | BIGINT | YES | - |
| cod_titulo | VARCHAR | YES | - |
| data_inicio | DATE | YES | - |
| data_fim | DATE | YES | - |
| id_deputado | BIGINT | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.partidos_membros_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_partido_membro | BIGINT | NO | - |
| id_partido | BIGINT | YES | - |
| id_deputado | BIGINT | YES | - |
| id_legislatura | INTEGER | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.processo_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_processo | BIGINT | NO | - |
| codigo_materia | BIGINT | YES | - |
| id_processo_casa_inicial | BIGINT | YES | - |
| identificacao | VARCHAR | YES | - |
| identificacao_processo_inicial | VARCHAR | YES | - |
| identificacao_externa | VARCHAR | YES | - |
| ano | INTEGER | YES | - |
| casa_identificadora | VARCHAR | YES | - |
| sigla_casa_iniciadora | VARCHAR | YES | - |
| sigla_ente_identificador | VARCHAR | YES | - |
| descricao_sigla | VARCHAR | YES | - |
| sigla | VARCHAR | YES | - |
| numero | VARCHAR | YES | - |
| objetivo | VARCHAR | YES | - |
| tramitando | VARCHAR | YES | - |
| id_conteudo | BIGINT | YES | - |
| id_tipo_conteudo | BIGINT | YES | - |
| sigla_tipo_conteudo | VARCHAR | YES | - |
| tipo_conteudo | VARCHAR | YES | - |
| tipo_norma_indicada | VARCHAR | YES | - |
| ementa | VARCHAR | YES | - |
| explicacao_ementa | VARCHAR | YES | - |
| deliberacao_id_destino | BIGINT | YES | - |
| deliberacao_sigla_destino | VARCHAR | YES | - |
| deliberacao_tipo | VARCHAR | YES | - |
| deliberacao_sigla_tipo | VARCHAR | YES | - |
| deliberacao_data | DATE | YES | - |
| deliberacao_destino | VARCHAR | YES | - |
| id_documento | BIGINT | YES | - |
| documento_sigla_tipo | VARCHAR | YES | - |
| documento_tipo | VARCHAR | YES | - |
| documento_indexacao | VARCHAR | YES | - |
| documento_resumo_autoria | VARCHAR | YES | - |
| documento_data_apresentacao | DATE | YES | - |
| documento_data_leitura | DATE | YES | - |
| norma_codigo | BIGINT | YES | - |
| norma_numero | VARCHAR | YES | - |
| norma_sigla_tipo | VARCHAR | YES | - |
| norma_tipo | VARCHAR | YES | - |
| norma_descricao | VARCHAR | YES | - |
| norma_sigla_veiculo | VARCHAR | YES | - |
| norma_veiculo | VARCHAR | YES | - |
| norma_numero_int | INTEGER | YES | - |
| norma_ano_assinatura | INTEGER | YES | - |
| norma_data_assinatura | DATE | YES | - |
| norma_data_publicacao | DATE | YES | - |
| year_snapshot | BIGINT | YES | - |
| tag | VARCHAR | YES | - |

---

## main.processos_relacionados_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_processo_relacionado | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| id_outro_processo | BIGINT | YES | - |
| ano | INTEGER | YES | - |
| casa_identificadora | VARCHAR | YES | - |
| ente_identificador | VARCHAR | YES | - |
| sigla | VARCHAR | YES | - |
| numero | VARCHAR | YES | - |
| sigla_ente_identificador | VARCHAR | YES | - |
| tipo_relacao | VARCHAR | YES | - |
| tramitando | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.proposicoes_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_proposicao | BIGINT | YES | - |
| sigla_tipo | VARCHAR | YES | - |
| numero | INTEGER | YES | - |
| ano | INTEGER | YES | - |
| ementa | VARCHAR | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| prop_tag | VARCHAR | YES | - |
| prop_label | VARCHAR | YES | - |
| prop_category | VARCHAR | YES | - |

---

## main.providencias_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_processo | BIGINT | NO | - |
| id_despacho | BIGINT | NO | - |
| id_providencia | BIGINT | NO | - |
| descricao | VARCHAR | YES | - |
| tipo | VARCHAR | YES | - |
| analise_conteudo | VARCHAR | YES | - |
| analise_tempo | VARCHAR | YES | - |
| ordem | INTEGER | YES | - |
| reexame | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.relatorias_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_relatoria | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| codigo_materia | BIGINT | YES | - |
| codigo_parlamentar | BIGINT | YES | - |
| codigo_colegiado | BIGINT | YES | - |
| codigo_tipo_colegiado | BIGINT | YES | - |
| sigla_colegiado | VARCHAR | YES | - |
| nome_colegiado | VARCHAR | YES | - |
| autoria_processo | VARCHAR | YES | - |
| identificacao_processo | VARCHAR | YES | - |
| ementa_processo | VARCHAR | YES | - |
| numero_autuacao | INTEGER | YES | - |
| tramitando | VARCHAR | YES | - |
| sigla_casa | VARCHAR | YES | - |
| casa_relator | VARCHAR | YES | - |
| descricao_tipo_relator | VARCHAR | YES | - |
| id_tipo_relator | INTEGER | YES | - |
| descricao_tipo_encerramento | VARCHAR | YES | - |
| forma_tratamento_parlamentar | VARCHAR | YES | - |
| nome_parlamentar | VARCHAR | YES | - |
| nome_completo | VARCHAR | YES | - |
| sigla_partido_parlamentar | VARCHAR | YES | - |
| uf_parlamentar | VARCHAR | YES | - |
| sexo_parlamentar | VARCHAR | YES | - |
| email_parlamentar | VARCHAR | YES | - |
| url_foto_parlamentar | VARCHAR | YES | - |
| url_pagina_parlamentar | VARCHAR | YES | - |
| data_apresentacao_processo | TIMESTAMP | YES | - |
| data_designacao | TIMESTAMP | YES | - |
| data_destituicao | TIMESTAMP | YES | - |
| data_fim_colegiado | TIMESTAMP | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.situacoes_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_situacao | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| numero_autuacao | INTEGER | YES | - |
| id_tipo_situacao | INTEGER | YES | - |
| sigla_situacao | VARCHAR | YES | - |
| descricao_situacao | VARCHAR | YES | - |
| data_inicio | DATE | YES | - |
| data_fim | DATE | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.temas_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_tema | BIGINT | NO | - |
| descricao | VARCHAR | YES | - |

---

## main.tipo_colegiado_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| codigo_tipo_colegiado | BIGINT | YES | - |
| codigo_natureza_colegiado | BIGINT | YES | - |
| descricao_tipo_colegiado | VARCHAR | YES | - |
| indicador_ativo | VARCHAR | YES | - |
| sigla_casa | VARCHAR | YES | - |
| sigla_tipo_colegiado | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.tipo_conteudo_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_tipo_conteudo | BIGINT | YES | - |
| sigla_tipo_conteudo | VARCHAR | YES | - |
| descricao_tipo_conteudo | VARCHAR | YES | - |
| tipo_norma_indicada | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.tipo_deliberacao_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| sigla_tipo_deliberacao | VARCHAR | YES | - |
| descricao_tipo_deliberacao | VARCHAR | YES | - |
| id_destino | BIGINT | YES | - |
| sigla_destino | VARCHAR | YES | - |
| destino | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.tipo_emendas_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| tipo_emenda | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.tramitacoes_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_tramitacao | BIGINT | NO | - |
| id_proposicao | BIGINT | YES | - |
| ambito | VARCHAR | YES | - |
| apreciacao | VARCHAR | YES | - |
| cod_situacao | VARCHAR | YES | - |
| cod_tipo_tramitacao | VARCHAR | YES | - |
| data_hora | TIMESTAMP | YES | - |
| descricao_situacao | VARCHAR | YES | - |
| descricao_tramitacao | VARCHAR | YES | - |
| despacho | VARCHAR | YES | - |
| regime | VARCHAR | YES | - |
| sequencia | INTEGER | YES | - |
| sigla_orgao | VARCHAR | YES | - |
| uri_orgao | VARCHAR | YES | - |
| uri_ultimo_relator | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.unidades_destinatarias_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_unidade_destinataria | BIGINT | NO | - |
| id_processo | BIGINT | YES | - |
| id_despacho | BIGINT | YES | - |
| id_providencia | BIGINT | YES | - |
| colegiado_casa | VARCHAR | YES | - |
| colegiado_codigo | BIGINT | YES | - |
| colegiado_nome | VARCHAR | YES | - |
| colegiado_sigla | VARCHAR | YES | - |
| ordem | INTEGER | YES | - |
| tipo_analise_deliberacao | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.votacoes_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_votacao | VARCHAR | NO | - |
| id_proposicao | BIGINT | YES | - |
| data | DATE | YES | - |
| descricao | VARCHAR | YES | - |
| aprovacao | BOOLEAN | YES | - |
| uri_evento | VARCHAR | YES | - |
| uri_orgao | VARCHAR | YES | - |
| uri | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |
| rn | BIGINT | YES | - |

---

## main.votacoes_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_votacao | BIGINT | NO | - |
| id_materia | BIGINT | YES | - |
| id_processo | BIGINT | YES | - |
| identificacao | VARCHAR | YES | - |
| sigla | VARCHAR | YES | - |
| numero | VARCHAR | YES | - |
| ano | INTEGER | YES | - |
| codigo_sessao | BIGINT | YES | - |
| numero_sessao | INTEGER | YES | - |
| sequencial_sessao | INTEGER | YES | - |
| sigla_tipo_sessao | VARCHAR | YES | - |
| casa_sessao | VARCHAR | YES | - |
| codigo_sessao_legislativa | BIGINT | YES | - |
| data_apresentacao | TIMESTAMP | YES | - |
| data_sessao | TIMESTAMP | YES | - |
| descricao_votacao | VARCHAR | YES | - |
| ementa | VARCHAR | YES | - |
| resultado_votacao | VARCHAR | YES | - |
| total_votos_sim | INTEGER | YES | - |
| total_votos_nao | INTEGER | YES | - |
| total_votos_abstencao | INTEGER | YES | - |
| votacao_secreta | VARCHAR | YES | - |
| id_informe | BIGINT | YES | - |
| id_evento | BIGINT | YES | - |
| codigo_colegiado | BIGINT | YES | - |
| nome_colegiado | VARCHAR | YES | - |
| sigla_colegiado | VARCHAR | YES | - |
| data_informe | TIMESTAMP | YES | - |
| texto_informe | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

## main.votos_camara

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_voto | BIGINT | NO | - |
| id_votacao | VARCHAR | YES | - |
| id_deputado | BIGINT | YES | - |
| tipo_voto | VARCHAR | YES | - |
| data_hora | TIMESTAMP | YES | - |
| year_snapshot | INTEGER | YES | - |

---

## main.votos_senado

| Column Name | Data Type | Nullable | Default |
|-------------|-----------|----------|----------|
| id_voto | BIGINT | NO | - |
| codigo_votacao_sve | BIGINT | YES | - |
| codigo_sessao_votacao | BIGINT | YES | - |
| codigo_materia | BIGINT | YES | - |
| identificacao_materia | VARCHAR | YES | - |
| codigo_parlamentar | BIGINT | YES | - |
| nome_parlamentar | VARCHAR | YES | - |
| sexo_parlamentar | VARCHAR | YES | - |
| sigla_partido_parlamentar | VARCHAR | YES | - |
| sigla_uf_parlamentar | VARCHAR | YES | - |
| sigla_voto_parlamentar | VARCHAR | YES | - |
| descricao_voto_parlamentar | VARCHAR | YES | - |
| year_snapshot | BIGINT | YES | - |

---

