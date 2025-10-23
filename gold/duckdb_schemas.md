# DuckDB Schemas

_Generated on 2025-10-20T16:15:41_


## main.autores_camara

**Create statement:**

```sql
CREATE TABLE "autores_camara" (
  "id_autor" BIGINT NOT NULL,
  "cod_tipo" BIGINT,
  "uri" VARCHAR,
  "ordem_assinatura" INTEGER,
  "proponente" BOOLEAN,
  "id_proposicao" BIGINT,
  "year" BIGINT,
  "tipo_autor" VARCHAR,
  "id_deputado_ou_orgao" BIGINT,
  PRIMARY KEY ("id_autor")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_autor | BIGINT | NO | 1 |
| cod_tipo | BIGINT | YES | 2 |
| uri | VARCHAR | YES | 3 |
| ordem_assinatura | INTEGER | YES | 4 |
| proponente | BOOLEAN | YES | 5 |
| id_proposicao | BIGINT | YES | 6 |
| year | BIGINT | YES | 7 |
| tipo_autor | VARCHAR | YES | 8 |
| id_deputado_ou_orgao | BIGINT | YES | 9 |

## main.autoria_documento_senado

**Create statement:**

```sql
CREATE TABLE "autoria_documento_senado" (
  "id_autoria_documento" BIGINT,
  "id_processo" BIGINT,
  "id_documento" BIGINT,
  "autor" VARCHAR,
  "sigla_tipo" VARCHAR,
  "descricao_tipo" VARCHAR,
  "ordem" INTEGER,
  "outros_autores_nao_informados" VARCHAR,
  "id_ente" BIGINT,
  "sigla_ente" VARCHAR,
  "casa_ente" VARCHAR,
  "ente" VARCHAR,
  "cargo" VARCHAR,
  "siglaCargo" VARCHAR,
  "partido" VARCHAR,
  "sexo" VARCHAR,
  "uf" VARCHAR,
  "year_snapshot" BIGINT
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_autoria_documento | BIGINT | YES | 1 |
| id_processo | BIGINT | YES | 2 |
| id_documento | BIGINT | YES | 3 |
| autor | VARCHAR | YES | 4 |
| sigla_tipo | VARCHAR | YES | 5 |
| descricao_tipo | VARCHAR | YES | 6 |
| ordem | INTEGER | YES | 7 |
| outros_autores_nao_informados | VARCHAR | YES | 8 |
| id_ente | BIGINT | YES | 9 |
| sigla_ente | VARCHAR | YES | 10 |
| casa_ente | VARCHAR | YES | 11 |
| ente | VARCHAR | YES | 12 |
| cargo | VARCHAR | YES | 13 |
| siglaCargo | VARCHAR | YES | 14 |
| partido | VARCHAR | YES | 15 |
| sexo | VARCHAR | YES | 16 |
| uf | VARCHAR | YES | 17 |
| year_snapshot | BIGINT | YES | 18 |

## main.autoria_iniciativa_senado

**Create statement:**

```sql
CREATE TABLE "autoria_iniciativa_senado" (
  "id_autoria_iniciativa" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "codigo_parlamentar" BIGINT,
  "descricao_tipo" VARCHAR,
  "ente" VARCHAR,
  "ordem" INTEGER,
  "outros_autores_nao_informados" VARCHAR,
  "sigla_ente" VARCHAR,
  "sigla_tipo" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_autoria_iniciativa")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_autoria_iniciativa | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| codigo_parlamentar | BIGINT | YES | 3 |
| descricao_tipo | VARCHAR | YES | 4 |
| ente | VARCHAR | YES | 5 |
| ordem | INTEGER | YES | 6 |
| outros_autores_nao_informados | VARCHAR | YES | 7 |
| sigla_ente | VARCHAR | YES | 8 |
| sigla_tipo | VARCHAR | YES | 9 |
| year_snapshot | BIGINT | YES | 10 |

## main.autuacoes_senado

**Create statement:**

```sql
CREATE TABLE "autuacoes_senado" (
  "id_processo" BIGINT NOT NULL,
  "autuacao_idx" BIGINT NOT NULL,
  "descricao_autuacao" VARCHAR,
  "id_ente_controle_atual" BIGINT,
  "nome_ente_controle_atual" VARCHAR,
  "sigla_ente_controle_atual" VARCHAR,
  "numero_autuacao" INTEGER,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_processo", "autuacao_idx")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_processo | BIGINT | NO | 1 |
| autuacao_idx | BIGINT | NO | 2 |
| descricao_autuacao | VARCHAR | YES | 3 |
| id_ente_controle_atual | BIGINT | YES | 4 |
| nome_ente_controle_atual | VARCHAR | YES | 5 |
| sigla_ente_controle_atual | VARCHAR | YES | 6 |
| numero_autuacao | INTEGER | YES | 7 |
| year_snapshot | BIGINT | YES | 8 |

## main.bloco_senado

**Create statement:**

```sql
CREATE TABLE "bloco_senado" (
  "codigo_bloco" BIGINT NOT NULL,
  "data_criacao" DATE,
  "nome_apelido" VARCHAR,
  "nome_bloco" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("codigo_bloco")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| codigo_bloco | BIGINT | NO | 1 |
| data_criacao | DATE | YES | 2 |
| nome_apelido | VARCHAR | YES | 3 |
| nome_bloco | VARCHAR | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |

## main.blocos_camara

**Create statement:**

```sql
CREATE TABLE "blocos_camara" (
  "id_bloco" BIGINT NOT NULL,
  "nome" VARCHAR,
  "id_legislatura" BIGINT,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  PRIMARY KEY ("id_bloco")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_bloco | BIGINT | NO | 1 |
| nome | VARCHAR | YES | 2 |
| id_legislatura | BIGINT | YES | 3 |
| uri | VARCHAR | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |
| rn | BIGINT | YES | 6 |

## main.blocos_partidos_camara

**Create statement:**

```sql
CREATE TABLE "blocos_partidos_camara" (
  "id_bloco_partido" BIGINT NOT NULL,
  "id_bloco" BIGINT,
  "id_partido" BIGINT,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_bloco_partido")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_bloco_partido | BIGINT | NO | 1 |
| id_bloco | BIGINT | YES | 2 |
| id_partido | BIGINT | YES | 3 |
| year_snapshot | BIGINT | YES | 4 |

## main.colegiado_senado

**Create statement:**

```sql
CREATE TABLE "colegiado_senado" (
  "codigo_colegiado" BIGINT,
  "codigo_tipo_colegiado" BIGINT,
  "data_inicio" DATE,
  "indicador_distr_partidaria" VARCHAR,
  "nome_colegiado" VARCHAR,
  "sigla_colegiado" VARCHAR,
  "ordem" INTEGER,
  "year_snapshot" BIGINT
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| codigo_colegiado | BIGINT | YES | 1 |
| codigo_tipo_colegiado | BIGINT | YES | 2 |
| data_inicio | DATE | YES | 3 |
| indicador_distr_partidaria | VARCHAR | YES | 4 |
| nome_colegiado | VARCHAR | YES | 5 |
| sigla_colegiado | VARCHAR | YES | 6 |
| ordem | INTEGER | YES | 7 |
| year_snapshot | BIGINT | YES | 8 |

## main.correspondencia_proposicoes_processo

**Create statement:**

```sql
CREATE TABLE "correspondencia_proposicoes_processo" (
  "id_proposicao_camara" BIGINT,
  "id_processo_senado" BIGINT,
  "identificacao" VARCHAR
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_proposicao_camara | BIGINT | YES | 1 |
| id_processo_senado | BIGINT | YES | 2 |
| identificacao | VARCHAR | YES | 3 |

## main.deputados_camara

**Create statement:**

```sql
CREATE TABLE "deputados_camara" (
  "id_deputado" BIGINT NOT NULL,
  "nome_civil" VARCHAR,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  "tag" VARCHAR,
  PRIMARY KEY ("id_deputado")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_deputado | BIGINT | NO | 1 |
| nome_civil | VARCHAR | YES | 2 |
| uri | VARCHAR | YES | 3 |
| year_snapshot | BIGINT | YES | 4 |
| rn | BIGINT | YES | 5 |
| tag | VARCHAR | YES | 6 |

## main.deputados_frentes_camara

**Create statement:**

```sql
CREATE TABLE "deputados_frentes_camara" (
  "id_deputado_frente" BIGINT NOT NULL,
  "id_deputado" BIGINT,
  "id_frente" BIGINT,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_deputado_frente")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_deputado_frente | BIGINT | NO | 1 |
| id_deputado | BIGINT | YES | 2 |
| id_frente | BIGINT | YES | 3 |
| year_snapshot | BIGINT | YES | 4 |

## main.deputados_historico_camara

**Create statement:**

```sql
CREATE TABLE "deputados_historico_camara" (
  "id_deputado_historico" BIGINT NOT NULL,
  "id_deputado" BIGINT,
  "id_legislatura" BIGINT,
  "data_hora" TIMESTAMP,
  "condicao_eleitoral" VARCHAR,
  "descricao_status" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_deputado_historico")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_deputado_historico | BIGINT | NO | 1 |
| id_deputado | BIGINT | YES | 2 |
| id_legislatura | BIGINT | YES | 3 |
| data_hora | TIMESTAMP | YES | 4 |
| condicao_eleitoral | VARCHAR | YES | 5 |
| descricao_status | VARCHAR | YES | 6 |
| year_snapshot | BIGINT | YES | 7 |

## main.deputados_orgaos_camara

**Create statement:**

```sql
CREATE TABLE "deputados_orgaos_camara" (
  "id_deputado_orgao" BIGINT NOT NULL,
  "id_deputado" BIGINT,
  "id_orgao" INTEGER,
  "cod_titulo" INTEGER,
  "data_inicio" TIMESTAMP,
  "data_fim" TIMESTAMP,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_deputado_orgao")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_deputado_orgao | BIGINT | NO | 1 |
| id_deputado | BIGINT | YES | 2 |
| id_orgao | INTEGER | YES | 3 |
| cod_titulo | INTEGER | YES | 4 |
| data_inicio | TIMESTAMP | YES | 5 |
| data_fim | TIMESTAMP | YES | 6 |
| year_snapshot | BIGINT | YES | 7 |

## main.despachos_senado

**Create statement:**

```sql
CREATE TABLE "despachos_senado" (
  "id_processo" BIGINT NOT NULL,
  "id_despacho" BIGINT NOT NULL,
  "data_despacho" DATE,
  "cancelado" VARCHAR,
  "tipo_motivacao" VARCHAR,
  "sigla_tipo_motivacao" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_despacho", "id_processo")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_processo | BIGINT | NO | 1 |
| id_despacho | BIGINT | NO | 2 |
| data_despacho | DATE | YES | 3 |
| cancelado | VARCHAR | YES | 4 |
| tipo_motivacao | VARCHAR | YES | 5 |
| sigla_tipo_motivacao | VARCHAR | YES | 6 |
| year_snapshot | BIGINT | YES | 7 |

## main.documento_autoria_senado

**Create statement:**

```sql
CREATE TABLE "documento_autoria_senado" (
  "id_documento_autoria" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "id_ente" BIGINT,
  "autor" VARCHAR,
  "codigo_parlamentar" BIGINT,
  "descricao_tipo" VARCHAR,
  "ente" VARCHAR,
  "ordem" INTEGER,
  "outros_autores_nao_informados" VARCHAR,
  "sigla_ente" VARCHAR,
  "sigla_tipo" VARCHAR,
  "year_snapshot" BIGINT,
  "tipo_autor" VARCHAR,
  "id_senador_ou_ente" BIGINT,
  PRIMARY KEY ("id_documento_autoria")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_documento_autoria | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| id_ente | BIGINT | YES | 3 |
| autor | VARCHAR | YES | 4 |
| codigo_parlamentar | BIGINT | YES | 5 |
| descricao_tipo | VARCHAR | YES | 6 |
| ente | VARCHAR | YES | 7 |
| ordem | INTEGER | YES | 8 |
| outros_autores_nao_informados | VARCHAR | YES | 9 |
| sigla_ente | VARCHAR | YES | 10 |
| sigla_tipo | VARCHAR | YES | 11 |
| year_snapshot | BIGINT | YES | 12 |
| tipo_autor | VARCHAR | YES | 13 |
| id_senador_ou_ente | BIGINT | YES | 14 |

## main.emendas_senado

**Create statement:**

```sql
CREATE TABLE "emendas_senado" (
  "id_emenda" BIGINT NOT NULL,
  "id_ci_emenda" BIGINT,
  "id_ci_emendado" BIGINT,
  "id_documento_emenda" BIGINT,
  "id_processo" BIGINT,
  "identificacao" VARCHAR,
  "numero" INTEGER,
  "autoria" VARCHAR,
  "descricao_documento_emenda" VARCHAR,
  "tipo_emenda" VARCHAR,
  "turno_apresentacao" VARCHAR,
  "casa" VARCHAR,
  "codigo_colegiado" BIGINT,
  "sigla_colegiado" VARCHAR,
  "nome_colegiado" VARCHAR,
  "data_apresentacao" DATE,
  "url_documento_emenda" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_emenda")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_emenda | BIGINT | NO | 1 |
| id_ci_emenda | BIGINT | YES | 2 |
| id_ci_emendado | BIGINT | YES | 3 |
| id_documento_emenda | BIGINT | YES | 4 |
| id_processo | BIGINT | YES | 5 |
| identificacao | VARCHAR | YES | 6 |
| numero | INTEGER | YES | 7 |
| autoria | VARCHAR | YES | 8 |
| descricao_documento_emenda | VARCHAR | YES | 9 |
| tipo_emenda | VARCHAR | YES | 10 |
| turno_apresentacao | VARCHAR | YES | 11 |
| casa | VARCHAR | YES | 12 |
| codigo_colegiado | BIGINT | YES | 13 |
| sigla_colegiado | VARCHAR | YES | 14 |
| nome_colegiado | VARCHAR | YES | 15 |
| data_apresentacao | DATE | YES | 16 |
| url_documento_emenda | VARCHAR | YES | 17 |
| year_snapshot | BIGINT | YES | 18 |

## main.encontro_legislativo_senado

**Create statement:**

```sql
CREATE TABLE "encontro_legislativo_senado" (
  "id_processo" BIGINT,
  "id_despacho" BIGINT,
  "id_encontro_legislativo" BIGINT NOT NULL,
  "data_encontro" DATE,
  "tipo_encontro" VARCHAR,
  "descricao_encontro" VARCHAR,
  "casa_encontro" VARCHAR,
  "numero_encontro" INTEGER,
  "colegiado_casa" VARCHAR,
  "colegiado_codigo" BIGINT,
  "colegiado_nome" VARCHAR,
  "colegiado_sigla" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  PRIMARY KEY ("id_encontro_legislativo")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_processo | BIGINT | YES | 1 |
| id_despacho | BIGINT | YES | 2 |
| id_encontro_legislativo | BIGINT | NO | 3 |
| data_encontro | DATE | YES | 4 |
| tipo_encontro | VARCHAR | YES | 5 |
| descricao_encontro | VARCHAR | YES | 6 |
| casa_encontro | VARCHAR | YES | 7 |
| numero_encontro | INTEGER | YES | 8 |
| colegiado_casa | VARCHAR | YES | 9 |
| colegiado_codigo | BIGINT | YES | 10 |
| colegiado_nome | VARCHAR | YES | 11 |
| colegiado_sigla | VARCHAR | YES | 12 |
| year_snapshot | BIGINT | YES | 13 |
| rn | BIGINT | YES | 14 |

## main.ente_senado

**Create statement:**

```sql
CREATE TABLE "ente_senado" (
  "id_ente" BIGINT NOT NULL,
  "sigla" VARCHAR,
  "nome" VARCHAR,
  "casa" VARCHAR,
  "sigla_tipo" VARCHAR,
  "descricao_tipo" VARCHAR,
  "data_inicio" DATE,
  "data_fim" DATE,
  "tag" VARCHAR,
  PRIMARY KEY ("id_ente")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_ente | BIGINT | NO | 1 |
| sigla | VARCHAR | YES | 2 |
| nome | VARCHAR | YES | 3 |
| casa | VARCHAR | YES | 4 |
| sigla_tipo | VARCHAR | YES | 5 |
| descricao_tipo | VARCHAR | YES | 6 |
| data_inicio | DATE | YES | 7 |
| data_fim | DATE | YES | 8 |
| tag | VARCHAR | YES | 9 |

## main.eventos_camara

**Create statement:**

```sql
CREATE TABLE "eventos_camara" (
  "id_evento" BIGINT NOT NULL,
  "data_hora_inicio" TIMESTAMP,
  "data_hora_fim" TIMESTAMP,
  "descricao" VARCHAR,
  "descricao_tipo" VARCHAR,
  "fases" VARCHAR,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  PRIMARY KEY ("id_evento")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_evento | BIGINT | NO | 1 |
| data_hora_inicio | TIMESTAMP | YES | 2 |
| data_hora_fim | TIMESTAMP | YES | 3 |
| descricao | VARCHAR | YES | 4 |
| descricao_tipo | VARCHAR | YES | 5 |
| fases | VARCHAR | YES | 6 |
| uri | VARCHAR | YES | 7 |
| year_snapshot | BIGINT | YES | 8 |
| rn | BIGINT | YES | 9 |

## main.eventos_orgaos_camara

**Create statement:**

```sql
CREATE TABLE "eventos_orgaos_camara" (
  "id_evento_orgao" BIGINT NOT NULL,
  "id_evento" BIGINT,
  "id_orgao" INTEGER,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_evento_orgao")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_evento_orgao | BIGINT | NO | 1 |
| id_evento | BIGINT | YES | 2 |
| id_orgao | INTEGER | YES | 3 |
| year_snapshot | BIGINT | YES | 4 |

## main.eventos_pauta_camara

**Create statement:**

```sql
CREATE TABLE "eventos_pauta_camara" (
  "id_pauta" BIGINT NOT NULL,
  "id_evento" BIGINT,
  "cod_regime" VARCHAR,
  "ordem" INTEGER,
  "id_proposicao" BIGINT,
  "id_relator" BIGINT,
  "year_snapshot" INTEGER,
  PRIMARY KEY ("id_pauta")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_pauta | BIGINT | NO | 1 |
| id_evento | BIGINT | YES | 2 |
| cod_regime | VARCHAR | YES | 3 |
| ordem | INTEGER | YES | 4 |
| id_proposicao | BIGINT | YES | 5 |
| id_relator | BIGINT | YES | 6 |
| year_snapshot | INTEGER | YES | 7 |

## main.frentes_camara

**Create statement:**

```sql
CREATE TABLE "frentes_camara" (
  "id_frente" BIGINT NOT NULL,
  "id_deputado_coordenador" BIGINT,
  "id_legislatura" BIGINT,
  "titulo" VARCHAR,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  PRIMARY KEY ("id_frente")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_frente | BIGINT | NO | 1 |
| id_deputado_coordenador | BIGINT | YES | 2 |
| id_legislatura | BIGINT | YES | 3 |
| titulo | VARCHAR | YES | 4 |
| uri | VARCHAR | YES | 5 |
| year_snapshot | BIGINT | YES | 6 |
| rn | BIGINT | YES | 7 |

## main.informes_documentos_associados_senado

**Create statement:**

```sql
CREATE TABLE "informes_documentos_associados_senado" (
  "id_documento_associado" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "id_informe" BIGINT,
  "id_documento" BIGINT,
  "autuacao_ordem" INTEGER,
  "informe_ordem" INTEGER,
  "documento_ordem" INTEGER,
  "sigla_tipo_documento" VARCHAR,
  "tipo_documento" VARCHAR,
  "identificacao" VARCHAR,
  "data_documento" TIMESTAMP,
  "autoria_documento" VARCHAR,
  "url_documento" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_documento_associado")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_documento_associado | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| id_informe | BIGINT | YES | 3 |
| id_documento | BIGINT | YES | 4 |
| autuacao_ordem | INTEGER | YES | 5 |
| informe_ordem | INTEGER | YES | 6 |
| documento_ordem | INTEGER | YES | 7 |
| sigla_tipo_documento | VARCHAR | YES | 8 |
| tipo_documento | VARCHAR | YES | 9 |
| identificacao | VARCHAR | YES | 10 |
| data_documento | TIMESTAMP | YES | 11 |
| autoria_documento | VARCHAR | YES | 12 |
| url_documento | VARCHAR | YES | 13 |
| year_snapshot | BIGINT | YES | 14 |

## main.informes_legislativos_senado

**Create statement:**

```sql
CREATE TABLE "informes_legislativos_senado" (
  "id_informe_legislativo" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "id_informe" BIGINT,
  "data_informe" DATE,
  "descricao" VARCHAR,
  "id_situacao_iniciada" BIGINT,
  "sigla_situacao_iniciada" VARCHAR,
  "ente_adm_casa" VARCHAR,
  "ente_adm_id" BIGINT,
  "ente_adm_nome" VARCHAR,
  "ente_adm_sigla" VARCHAR,
  "colegiado_casa" VARCHAR,
  "colegiado_codigo" BIGINT,
  "colegiado_nome" VARCHAR,
  "colegiado_sigla" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_informe_legislativo")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_informe_legislativo | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| id_informe | BIGINT | YES | 3 |
| data_informe | DATE | YES | 4 |
| descricao | VARCHAR | YES | 5 |
| id_situacao_iniciada | BIGINT | YES | 6 |
| sigla_situacao_iniciada | VARCHAR | YES | 7 |
| ente_adm_casa | VARCHAR | YES | 8 |
| ente_adm_id | BIGINT | YES | 9 |
| ente_adm_nome | VARCHAR | YES | 10 |
| ente_adm_sigla | VARCHAR | YES | 11 |
| colegiado_casa | VARCHAR | YES | 12 |
| colegiado_codigo | BIGINT | YES | 13 |
| colegiado_nome | VARCHAR | YES | 14 |
| colegiado_sigla | VARCHAR | YES | 15 |
| year_snapshot | BIGINT | YES | 16 |

## main.legislaturas_camara

**Create statement:**

```sql
CREATE TABLE "legislaturas_camara" (
  "id_legislatura" BIGINT NOT NULL,
  "data_inicio" DATE,
  "data_fim" DATE,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  PRIMARY KEY ("id_legislatura")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_legislatura | BIGINT | NO | 1 |
| data_inicio | DATE | YES | 2 |
| data_fim | DATE | YES | 3 |
| uri | VARCHAR | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |
| rn | BIGINT | YES | 6 |

## main.legislaturas_lideres_camara

**Create statement:**

```sql
CREATE TABLE "legislaturas_lideres_camara" (
  "id_lider" BIGINT NOT NULL,
  "id_legislatura" BIGINT,
  "nome_bancada" VARCHAR,
  "tipo_bancada" VARCHAR,
  "uri_bancada" VARCHAR,
  "data_inicio" TIMESTAMP,
  "data_fim" TIMESTAMP,
  "id_deputado" BIGINT,
  "titulo" VARCHAR,
  "year_snapshot" INTEGER,
  PRIMARY KEY ("id_lider")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_lider | BIGINT | NO | 1 |
| id_legislatura | BIGINT | YES | 2 |
| nome_bancada | VARCHAR | YES | 3 |
| tipo_bancada | VARCHAR | YES | 4 |
| uri_bancada | VARCHAR | YES | 5 |
| data_inicio | TIMESTAMP | YES | 6 |
| data_fim | TIMESTAMP | YES | 7 |
| id_deputado | BIGINT | YES | 8 |
| titulo | VARCHAR | YES | 9 |
| year_snapshot | INTEGER | YES | 10 |

## main.legislaturas_mesa_camara

**Create statement:**

```sql
CREATE TABLE "legislaturas_mesa_camara" (
  "id_legislatura_mesa" BIGINT,
  "id_legislatura" BIGINT,
  "id_deputado" BIGINT,
  "cod_titulo" VARCHAR,
  "data_inicio" DATE,
  "data_fim" DATE,
  "year_snapshot" BIGINT
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_legislatura_mesa | BIGINT | YES | 1 |
| id_legislatura | BIGINT | YES | 2 |
| id_deputado | BIGINT | YES | 3 |
| cod_titulo | VARCHAR | YES | 4 |
| data_inicio | DATE | YES | 5 |
| data_fim | DATE | YES | 6 |
| year_snapshot | BIGINT | YES | 7 |

## main.movimentacoes_senado

**Create statement:**

```sql
CREATE TABLE "movimentacoes_senado" (
  "id_processo" BIGINT NOT NULL,
  "autuacao_idx" INTEGER NOT NULL,
  "movimentacao_idx" INTEGER NOT NULL,
  "id_movimentacao" BIGINT,
  "data_envio" TIMESTAMP,
  "data_recebimento" TIMESTAMP,
  "ente_origem_casa" VARCHAR,
  "ente_origem_id" BIGINT,
  "ente_origem_nome" VARCHAR,
  "ente_origem_sigla" VARCHAR,
  "ente_destino_casa" VARCHAR,
  "ente_destino_id" BIGINT,
  "ente_destino_nome" VARCHAR,
  "ente_destino_sigla" VARCHAR,
  "colegiado_destino_casa" VARCHAR,
  "colegiado_destino_codigo" BIGINT,
  "colegiado_destino_nome" VARCHAR,
  "colegiado_destino_sigla" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_processo", "autuacao_idx", "movimentacao_idx")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_processo | BIGINT | NO | 1 |
| autuacao_idx | INTEGER | NO | 2 |
| movimentacao_idx | INTEGER | NO | 3 |
| id_movimentacao | BIGINT | YES | 4 |
| data_envio | TIMESTAMP | YES | 5 |
| data_recebimento | TIMESTAMP | YES | 6 |
| ente_origem_casa | VARCHAR | YES | 7 |
| ente_origem_id | BIGINT | YES | 8 |
| ente_origem_nome | VARCHAR | YES | 9 |
| ente_origem_sigla | VARCHAR | YES | 10 |
| ente_destino_casa | VARCHAR | YES | 11 |
| ente_destino_id | BIGINT | YES | 12 |
| ente_destino_nome | VARCHAR | YES | 13 |
| ente_destino_sigla | VARCHAR | YES | 14 |
| colegiado_destino_casa | VARCHAR | YES | 15 |
| colegiado_destino_codigo | BIGINT | YES | 16 |
| colegiado_destino_nome | VARCHAR | YES | 17 |
| colegiado_destino_sigla | VARCHAR | YES | 18 |
| year_snapshot | BIGINT | YES | 19 |

## main.orgaos_camara

**Create statement:**

```sql
CREATE TABLE "orgaos_camara" (
  "id_orgao" BIGINT NOT NULL,
  "nome" VARCHAR,
  "cod_tipo_orgao" BIGINT,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  "tag" VARCHAR,
  PRIMARY KEY ("id_orgao")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_orgao | BIGINT | NO | 1 |
| nome | VARCHAR | YES | 2 |
| cod_tipo_orgao | BIGINT | YES | 3 |
| uri | VARCHAR | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |
| rn | BIGINT | YES | 6 |
| tag | VARCHAR | YES | 7 |

## main.orgaos_camara_hotfix

**Create statement:**

```sql
CREATE TABLE "orgaos_camara_hotfix" (
  "id_orgao" BIGINT,
  "nome" VARCHAR,
  "cod_tipo_orgao" BIGINT,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_orgao | BIGINT | YES | 1 |
| nome | VARCHAR | YES | 2 |
| cod_tipo_orgao | BIGINT | YES | 3 |
| uri | VARCHAR | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |
| rn | BIGINT | YES | 6 |

## main.orientacoes_camara

**Create statement:**

```sql
CREATE TABLE "orientacoes_camara" (
  "id_orientacao" BIGINT NOT NULL,
  "id_votacao" VARCHAR,
  "sigla_partido_bloco" VARCHAR,
  "orientacao_voto" VARCHAR,
  "cod_partido_bloco" BIGINT,
  "cod_tipo_lideranca" VARCHAR,
  "uri_partido_bloco" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_orientacao")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_orientacao | BIGINT | NO | 1 |
| id_votacao | VARCHAR | YES | 2 |
| sigla_partido_bloco | VARCHAR | YES | 3 |
| orientacao_voto | VARCHAR | YES | 4 |
| cod_partido_bloco | BIGINT | YES | 5 |
| cod_tipo_lideranca | VARCHAR | YES | 6 |
| uri_partido_bloco | VARCHAR | YES | 7 |
| year_snapshot | BIGINT | YES | 8 |

## main.outros_numeros_senado

**Create statement:**

```sql
CREATE TABLE "outros_numeros_senado" (
  "id_outro_numero" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "id_outro_processo" BIGINT,
  "ano" INTEGER,
  "casa_identificadora" VARCHAR,
  "ente_identificador" VARCHAR,
  "sigla" VARCHAR,
  "numero" VARCHAR,
  "sigla_ente_identificador" VARCHAR,
  "externa_ao_congresso" VARCHAR,
  "tramitando" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_outro_numero")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_outro_numero | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| id_outro_processo | BIGINT | YES | 3 |
| ano | INTEGER | YES | 4 |
| casa_identificadora | VARCHAR | YES | 5 |
| ente_identificador | VARCHAR | YES | 6 |
| sigla | VARCHAR | YES | 7 |
| numero | VARCHAR | YES | 8 |
| sigla_ente_identificador | VARCHAR | YES | 9 |
| externa_ao_congresso | VARCHAR | YES | 10 |
| tramitando | VARCHAR | YES | 11 |
| year_snapshot | BIGINT | YES | 12 |

## main.parlamentar_senado

**Create statement:**

```sql
CREATE TABLE "parlamentar_senado" (
  "codigo_parlamentar" BIGINT NOT NULL,
  "codigo_publico_leg_atual" BIGINT,
  "nome_completo" VARCHAR,
  "nome_parlamentar" VARCHAR,
  "sexo_parlamentar" VARCHAR,
  "sigla_partido" VARCHAR,
  "uf_parlamentar" VARCHAR,
  "email_parlamentar" VARCHAR,
  "data_nascimento" DATE,
  "endereco_parlamentar" VARCHAR,
  "naturalidade" VARCHAR,
  "uf_naturalidade" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  PRIMARY KEY ("codigo_parlamentar")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| codigo_parlamentar | BIGINT | NO | 1 |
| codigo_publico_leg_atual | BIGINT | YES | 2 |
| nome_completo | VARCHAR | YES | 3 |
| nome_parlamentar | VARCHAR | YES | 4 |
| sexo_parlamentar | VARCHAR | YES | 5 |
| sigla_partido | VARCHAR | YES | 6 |
| uf_parlamentar | VARCHAR | YES | 7 |
| email_parlamentar | VARCHAR | YES | 8 |
| data_nascimento | DATE | YES | 9 |
| endereco_parlamentar | VARCHAR | YES | 10 |
| naturalidade | VARCHAR | YES | 11 |
| uf_naturalidade | VARCHAR | YES | 12 |
| year_snapshot | BIGINT | YES | 13 |
| rn | BIGINT | YES | 14 |

## main.partido_senado

**Create statement:**

```sql
CREATE TABLE "partido_senado" (
  "codigo_partido" BIGINT NOT NULL,
  "data_criacao" DATE,
  "nome" VARCHAR,
  "sigla" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("codigo_partido")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| codigo_partido | BIGINT | NO | 1 |
| data_criacao | DATE | YES | 2 |
| nome | VARCHAR | YES | 3 |
| sigla | VARCHAR | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |

## main.partidos_camara

**Create statement:**

```sql
CREATE TABLE "partidos_camara" (
  "id_partido" BIGINT NOT NULL,
  "nome" VARCHAR,
  "sigla" VARCHAR,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  PRIMARY KEY ("id_partido")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_partido | BIGINT | NO | 1 |
| nome | VARCHAR | YES | 2 |
| sigla | VARCHAR | YES | 3 |
| uri | VARCHAR | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |
| rn | BIGINT | YES | 6 |

## main.partidos_lideres_camara

**Create statement:**

```sql
CREATE TABLE "partidos_lideres_camara" (
  "id_partido_lider" BIGINT NOT NULL,
  "id_partido" BIGINT,
  "cod_titulo" VARCHAR,
  "data_inicio" DATE,
  "data_fim" DATE,
  "id_deputado" BIGINT,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_partido_lider")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_partido_lider | BIGINT | NO | 1 |
| id_partido | BIGINT | YES | 2 |
| cod_titulo | VARCHAR | YES | 3 |
| data_inicio | DATE | YES | 4 |
| data_fim | DATE | YES | 5 |
| id_deputado | BIGINT | YES | 6 |
| year_snapshot | BIGINT | YES | 7 |

## main.partidos_membros_camara

**Create statement:**

```sql
CREATE TABLE "partidos_membros_camara" (
  "id_partido_membro" BIGINT NOT NULL,
  "id_partido" BIGINT,
  "id_deputado" BIGINT,
  "id_legislatura" INTEGER,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_partido_membro")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_partido_membro | BIGINT | NO | 1 |
| id_partido | BIGINT | YES | 2 |
| id_deputado | BIGINT | YES | 3 |
| id_legislatura | INTEGER | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |

## main.processo_senado

**Create statement:**

```sql
CREATE TABLE "processo_senado" (
  "id_processo" BIGINT NOT NULL,
  "codigo_materia" BIGINT,
  "id_processo_casa_inicial" BIGINT,
  "identificacao" VARCHAR,
  "identificacao_processo_inicial" VARCHAR,
  "identificacao_externa" VARCHAR,
  "ano" INTEGER,
  "casa_identificadora" VARCHAR,
  "sigla_casa_iniciadora" VARCHAR,
  "sigla_ente_identificador" VARCHAR,
  "descricao_sigla" VARCHAR,
  "sigla" VARCHAR,
  "numero" VARCHAR,
  "objetivo" VARCHAR,
  "tramitando" VARCHAR,
  "id_conteudo" BIGINT,
  "id_tipo_conteudo" BIGINT,
  "sigla_tipo_conteudo" VARCHAR,
  "tipo_conteudo" VARCHAR,
  "tipo_norma_indicada" VARCHAR,
  "ementa" VARCHAR,
  "explicacao_ementa" VARCHAR,
  "deliberacao_id_destino" BIGINT,
  "deliberacao_sigla_destino" VARCHAR,
  "deliberacao_tipo" VARCHAR,
  "deliberacao_sigla_tipo" VARCHAR,
  "deliberacao_data" DATE,
  "deliberacao_destino" VARCHAR,
  "id_documento" BIGINT,
  "documento_sigla_tipo" VARCHAR,
  "documento_tipo" VARCHAR,
  "documento_indexacao" VARCHAR,
  "documento_resumo_autoria" VARCHAR,
  "documento_data_apresentacao" DATE,
  "documento_data_leitura" DATE,
  "norma_codigo" BIGINT,
  "norma_numero" VARCHAR,
  "norma_sigla_tipo" VARCHAR,
  "norma_tipo" VARCHAR,
  "norma_descricao" VARCHAR,
  "norma_sigla_veiculo" VARCHAR,
  "norma_veiculo" VARCHAR,
  "norma_numero_int" INTEGER,
  "norma_ano_assinatura" INTEGER,
  "norma_data_assinatura" DATE,
  "norma_data_publicacao" DATE,
  "year_snapshot" BIGINT,
  "tag" VARCHAR,
  PRIMARY KEY ("id_processo")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_processo | BIGINT | NO | 1 |
| codigo_materia | BIGINT | YES | 2 |
| id_processo_casa_inicial | BIGINT | YES | 3 |
| identificacao | VARCHAR | YES | 4 |
| identificacao_processo_inicial | VARCHAR | YES | 5 |
| identificacao_externa | VARCHAR | YES | 6 |
| ano | INTEGER | YES | 7 |
| casa_identificadora | VARCHAR | YES | 8 |
| sigla_casa_iniciadora | VARCHAR | YES | 9 |
| sigla_ente_identificador | VARCHAR | YES | 10 |
| descricao_sigla | VARCHAR | YES | 11 |
| sigla | VARCHAR | YES | 12 |
| numero | VARCHAR | YES | 13 |
| objetivo | VARCHAR | YES | 14 |
| tramitando | VARCHAR | YES | 15 |
| id_conteudo | BIGINT | YES | 16 |
| id_tipo_conteudo | BIGINT | YES | 17 |
| sigla_tipo_conteudo | VARCHAR | YES | 18 |
| tipo_conteudo | VARCHAR | YES | 19 |
| tipo_norma_indicada | VARCHAR | YES | 20 |
| ementa | VARCHAR | YES | 21 |
| explicacao_ementa | VARCHAR | YES | 22 |
| deliberacao_id_destino | BIGINT | YES | 23 |
| deliberacao_sigla_destino | VARCHAR | YES | 24 |
| deliberacao_tipo | VARCHAR | YES | 25 |
| deliberacao_sigla_tipo | VARCHAR | YES | 26 |
| deliberacao_data | DATE | YES | 27 |
| deliberacao_destino | VARCHAR | YES | 28 |
| id_documento | BIGINT | YES | 29 |
| documento_sigla_tipo | VARCHAR | YES | 30 |
| documento_tipo | VARCHAR | YES | 31 |
| documento_indexacao | VARCHAR | YES | 32 |
| documento_resumo_autoria | VARCHAR | YES | 33 |
| documento_data_apresentacao | DATE | YES | 34 |
| documento_data_leitura | DATE | YES | 35 |
| norma_codigo | BIGINT | YES | 36 |
| norma_numero | VARCHAR | YES | 37 |
| norma_sigla_tipo | VARCHAR | YES | 38 |
| norma_tipo | VARCHAR | YES | 39 |
| norma_descricao | VARCHAR | YES | 40 |
| norma_sigla_veiculo | VARCHAR | YES | 41 |
| norma_veiculo | VARCHAR | YES | 42 |
| norma_numero_int | INTEGER | YES | 43 |
| norma_ano_assinatura | INTEGER | YES | 44 |
| norma_data_assinatura | DATE | YES | 45 |
| norma_data_publicacao | DATE | YES | 46 |
| year_snapshot | BIGINT | YES | 47 |
| tag | VARCHAR | YES | 48 |

## main.processos_relacionados_senado

**Create statement:**

```sql
CREATE TABLE "processos_relacionados_senado" (
  "id_processo_relacionado" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "id_outro_processo" BIGINT,
  "ano" INTEGER,
  "casa_identificadora" VARCHAR,
  "ente_identificador" VARCHAR,
  "sigla" VARCHAR,
  "numero" VARCHAR,
  "sigla_ente_identificador" VARCHAR,
  "tipo_relacao" VARCHAR,
  "tramitando" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_processo_relacionado")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_processo_relacionado | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| id_outro_processo | BIGINT | YES | 3 |
| ano | INTEGER | YES | 4 |
| casa_identificadora | VARCHAR | YES | 5 |
| ente_identificador | VARCHAR | YES | 6 |
| sigla | VARCHAR | YES | 7 |
| numero | VARCHAR | YES | 8 |
| sigla_ente_identificador | VARCHAR | YES | 9 |
| tipo_relacao | VARCHAR | YES | 10 |
| tramitando | VARCHAR | YES | 11 |
| year_snapshot | BIGINT | YES | 12 |

## main.proposicoes_camara

**Create statement:**

```sql
CREATE TABLE "proposicoes_camara" (
  "id_proposicao" BIGINT,
  "sigla_tipo" VARCHAR,
  "numero" INTEGER,
  "ano" INTEGER,
  "ementa" VARCHAR,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "prop_tag" VARCHAR,
  "prop_label" VARCHAR,
  "prop_category" VARCHAR
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_proposicao | BIGINT | YES | 1 |
| sigla_tipo | VARCHAR | YES | 2 |
| numero | INTEGER | YES | 3 |
| ano | INTEGER | YES | 4 |
| ementa | VARCHAR | YES | 5 |
| uri | VARCHAR | YES | 6 |
| year_snapshot | BIGINT | YES | 7 |
| prop_tag | VARCHAR | YES | 8 |
| prop_label | VARCHAR | YES | 9 |
| prop_category | VARCHAR | YES | 10 |

## main.providencias_senado

**Create statement:**

```sql
CREATE TABLE "providencias_senado" (
  "id_processo" BIGINT NOT NULL,
  "id_despacho" BIGINT NOT NULL,
  "id_providencia" BIGINT NOT NULL,
  "descricao" VARCHAR,
  "tipo" VARCHAR,
  "analise_conteudo" VARCHAR,
  "analise_tempo" VARCHAR,
  "ordem" INTEGER,
  "reexame" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_processo", "id_despacho", "id_providencia")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_processo | BIGINT | NO | 1 |
| id_despacho | BIGINT | NO | 2 |
| id_providencia | BIGINT | NO | 3 |
| descricao | VARCHAR | YES | 4 |
| tipo | VARCHAR | YES | 5 |
| analise_conteudo | VARCHAR | YES | 6 |
| analise_tempo | VARCHAR | YES | 7 |
| ordem | INTEGER | YES | 8 |
| reexame | VARCHAR | YES | 9 |
| year_snapshot | BIGINT | YES | 10 |

## main.relatorias_senado

**Create statement:**

```sql
CREATE TABLE "relatorias_senado" (
  "id_relatoria" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "codigo_materia" BIGINT,
  "codigo_parlamentar" BIGINT,
  "codigo_colegiado" BIGINT,
  "codigo_tipo_colegiado" BIGINT,
  "sigla_colegiado" VARCHAR,
  "nome_colegiado" VARCHAR,
  "autoria_processo" VARCHAR,
  "identificacao_processo" VARCHAR,
  "ementa_processo" VARCHAR,
  "numero_autuacao" INTEGER,
  "tramitando" VARCHAR,
  "sigla_casa" VARCHAR,
  "casa_relator" VARCHAR,
  "descricao_tipo_relator" VARCHAR,
  "id_tipo_relator" INTEGER,
  "descricao_tipo_encerramento" VARCHAR,
  "forma_tratamento_parlamentar" VARCHAR,
  "nome_parlamentar" VARCHAR,
  "nome_completo" VARCHAR,
  "sigla_partido_parlamentar" VARCHAR,
  "uf_parlamentar" VARCHAR,
  "sexo_parlamentar" VARCHAR,
  "email_parlamentar" VARCHAR,
  "url_foto_parlamentar" VARCHAR,
  "url_pagina_parlamentar" VARCHAR,
  "data_apresentacao_processo" TIMESTAMP,
  "data_designacao" TIMESTAMP,
  "data_destituicao" TIMESTAMP,
  "data_fim_colegiado" TIMESTAMP,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_relatoria")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_relatoria | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| codigo_materia | BIGINT | YES | 3 |
| codigo_parlamentar | BIGINT | YES | 4 |
| codigo_colegiado | BIGINT | YES | 5 |
| codigo_tipo_colegiado | BIGINT | YES | 6 |
| sigla_colegiado | VARCHAR | YES | 7 |
| nome_colegiado | VARCHAR | YES | 8 |
| autoria_processo | VARCHAR | YES | 9 |
| identificacao_processo | VARCHAR | YES | 10 |
| ementa_processo | VARCHAR | YES | 11 |
| numero_autuacao | INTEGER | YES | 12 |
| tramitando | VARCHAR | YES | 13 |
| sigla_casa | VARCHAR | YES | 14 |
| casa_relator | VARCHAR | YES | 15 |
| descricao_tipo_relator | VARCHAR | YES | 16 |
| id_tipo_relator | INTEGER | YES | 17 |
| descricao_tipo_encerramento | VARCHAR | YES | 18 |
| forma_tratamento_parlamentar | VARCHAR | YES | 19 |
| nome_parlamentar | VARCHAR | YES | 20 |
| nome_completo | VARCHAR | YES | 21 |
| sigla_partido_parlamentar | VARCHAR | YES | 22 |
| uf_parlamentar | VARCHAR | YES | 23 |
| sexo_parlamentar | VARCHAR | YES | 24 |
| email_parlamentar | VARCHAR | YES | 25 |
| url_foto_parlamentar | VARCHAR | YES | 26 |
| url_pagina_parlamentar | VARCHAR | YES | 27 |
| data_apresentacao_processo | TIMESTAMP | YES | 28 |
| data_designacao | TIMESTAMP | YES | 29 |
| data_destituicao | TIMESTAMP | YES | 30 |
| data_fim_colegiado | TIMESTAMP | YES | 31 |
| year_snapshot | BIGINT | YES | 32 |

## main.situacoes_senado

**Create statement:**

```sql
CREATE TABLE "situacoes_senado" (
  "id_situacao" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "numero_autuacao" INTEGER,
  "id_tipo_situacao" INTEGER,
  "sigla_situacao" VARCHAR,
  "descricao_situacao" VARCHAR,
  "data_inicio" DATE,
  "data_fim" DATE,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_situacao")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_situacao | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| numero_autuacao | INTEGER | YES | 3 |
| id_tipo_situacao | INTEGER | YES | 4 |
| sigla_situacao | VARCHAR | YES | 5 |
| descricao_situacao | VARCHAR | YES | 6 |
| data_inicio | DATE | YES | 7 |
| data_fim | DATE | YES | 8 |
| year_snapshot | BIGINT | YES | 9 |

## main.temas_camara

**Create statement:**

```sql
CREATE TABLE "temas_camara" (
  "id_tema" BIGINT NOT NULL,
  "descricao" VARCHAR,
  PRIMARY KEY ("id_tema")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_tema | BIGINT | NO | 1 |
| descricao | VARCHAR | YES | 2 |

## main.tipo_colegiado_senado

**Create statement:**

```sql
CREATE TABLE "tipo_colegiado_senado" (
  "codigo_tipo_colegiado" BIGINT,
  "codigo_natureza_colegiado" BIGINT,
  "descricao_tipo_colegiado" VARCHAR,
  "indicador_ativo" VARCHAR,
  "sigla_casa" VARCHAR,
  "sigla_tipo_colegiado" VARCHAR,
  "year_snapshot" BIGINT
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| codigo_tipo_colegiado | BIGINT | YES | 1 |
| codigo_natureza_colegiado | BIGINT | YES | 2 |
| descricao_tipo_colegiado | VARCHAR | YES | 3 |
| indicador_ativo | VARCHAR | YES | 4 |
| sigla_casa | VARCHAR | YES | 5 |
| sigla_tipo_colegiado | VARCHAR | YES | 6 |
| year_snapshot | BIGINT | YES | 7 |

## main.tipo_conteudo_senado

**Create statement:**

```sql
CREATE TABLE "tipo_conteudo_senado" (
  "id_tipo_conteudo" BIGINT,
  "sigla_tipo_conteudo" VARCHAR,
  "descricao_tipo_conteudo" VARCHAR,
  "tipo_norma_indicada" VARCHAR,
  "year_snapshot" BIGINT
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_tipo_conteudo | BIGINT | YES | 1 |
| sigla_tipo_conteudo | VARCHAR | YES | 2 |
| descricao_tipo_conteudo | VARCHAR | YES | 3 |
| tipo_norma_indicada | VARCHAR | YES | 4 |
| year_snapshot | BIGINT | YES | 5 |

## main.tipo_deliberacao_senado

**Create statement:**

```sql
CREATE TABLE "tipo_deliberacao_senado" (
  "sigla_tipo_deliberacao" VARCHAR,
  "descricao_tipo_deliberacao" VARCHAR,
  "id_destino" BIGINT,
  "sigla_destino" VARCHAR,
  "destino" VARCHAR,
  "year_snapshot" BIGINT
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| sigla_tipo_deliberacao | VARCHAR | YES | 1 |
| descricao_tipo_deliberacao | VARCHAR | YES | 2 |
| id_destino | BIGINT | YES | 3 |
| sigla_destino | VARCHAR | YES | 4 |
| destino | VARCHAR | YES | 5 |
| year_snapshot | BIGINT | YES | 6 |

## main.tipo_emendas_senado

**Create statement:**

```sql
CREATE TABLE "tipo_emendas_senado" (
  "tipo_emenda" VARCHAR,
  "year_snapshot" BIGINT
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| tipo_emenda | VARCHAR | YES | 1 |
| year_snapshot | BIGINT | YES | 2 |

## main.tramitacoes_camara

**Create statement:**

```sql
CREATE TABLE "tramitacoes_camara" (
  "id_tramitacao" BIGINT NOT NULL,
  "id_proposicao" BIGINT,
  "ambito" VARCHAR,
  "apreciacao" VARCHAR,
  "cod_situacao" VARCHAR,
  "cod_tipo_tramitacao" VARCHAR,
  "data_hora" TIMESTAMP,
  "descricao_situacao" VARCHAR,
  "descricao_tramitacao" VARCHAR,
  "despacho" VARCHAR,
  "regime" VARCHAR,
  "sequencia" INTEGER,
  "sigla_orgao" VARCHAR,
  "uri_orgao" VARCHAR,
  "uri_ultimo_relator" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_tramitacao")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_tramitacao | BIGINT | NO | 1 |
| id_proposicao | BIGINT | YES | 2 |
| ambito | VARCHAR | YES | 3 |
| apreciacao | VARCHAR | YES | 4 |
| cod_situacao | VARCHAR | YES | 5 |
| cod_tipo_tramitacao | VARCHAR | YES | 6 |
| data_hora | TIMESTAMP | YES | 7 |
| descricao_situacao | VARCHAR | YES | 8 |
| descricao_tramitacao | VARCHAR | YES | 9 |
| despacho | VARCHAR | YES | 10 |
| regime | VARCHAR | YES | 11 |
| sequencia | INTEGER | YES | 12 |
| sigla_orgao | VARCHAR | YES | 13 |
| uri_orgao | VARCHAR | YES | 14 |
| uri_ultimo_relator | VARCHAR | YES | 15 |
| year_snapshot | BIGINT | YES | 16 |

## main.unidades_destinatarias_senado

**Create statement:**

```sql
CREATE TABLE "unidades_destinatarias_senado" (
  "id_unidade_destinataria" BIGINT NOT NULL,
  "id_processo" BIGINT,
  "id_despacho" BIGINT,
  "id_providencia" BIGINT,
  "colegiado_casa" VARCHAR,
  "colegiado_codigo" BIGINT,
  "colegiado_nome" VARCHAR,
  "colegiado_sigla" VARCHAR,
  "ordem" INTEGER,
  "tipo_analise_deliberacao" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_unidade_destinataria")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_unidade_destinataria | BIGINT | NO | 1 |
| id_processo | BIGINT | YES | 2 |
| id_despacho | BIGINT | YES | 3 |
| id_providencia | BIGINT | YES | 4 |
| colegiado_casa | VARCHAR | YES | 5 |
| colegiado_codigo | BIGINT | YES | 6 |
| colegiado_nome | VARCHAR | YES | 7 |
| colegiado_sigla | VARCHAR | YES | 8 |
| ordem | INTEGER | YES | 9 |
| tipo_analise_deliberacao | VARCHAR | YES | 10 |
| year_snapshot | BIGINT | YES | 11 |

## main.votacoes_camara

**Create statement:**

```sql
CREATE TABLE "votacoes_camara" (
  "id_votacao" VARCHAR NOT NULL,
  "id_proposicao" BIGINT,
  "data" DATE,
  "descricao" VARCHAR,
  "aprovacao" BOOLEAN,
  "uri_evento" VARCHAR,
  "uri_orgao" VARCHAR,
  "uri" VARCHAR,
  "year_snapshot" BIGINT,
  "rn" BIGINT,
  PRIMARY KEY ("id_votacao")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_votacao | VARCHAR | NO | 1 |
| id_proposicao | BIGINT | YES | 2 |
| data | DATE | YES | 3 |
| descricao | VARCHAR | YES | 4 |
| aprovacao | BOOLEAN | YES | 5 |
| uri_evento | VARCHAR | YES | 6 |
| uri_orgao | VARCHAR | YES | 7 |
| uri | VARCHAR | YES | 8 |
| year_snapshot | BIGINT | YES | 9 |
| rn | BIGINT | YES | 10 |

## main.votacoes_senado

**Create statement:**

```sql
CREATE TABLE "votacoes_senado" (
  "id_votacao" BIGINT NOT NULL,
  "id_materia" BIGINT,
  "id_processo" BIGINT,
  "identificacao" VARCHAR,
  "sigla" VARCHAR,
  "numero" VARCHAR,
  "ano" INTEGER,
  "codigo_sessao" BIGINT,
  "numero_sessao" INTEGER,
  "sequencial_sessao" INTEGER,
  "sigla_tipo_sessao" VARCHAR,
  "casa_sessao" VARCHAR,
  "codigo_sessao_legislativa" BIGINT,
  "data_apresentacao" TIMESTAMP,
  "data_sessao" TIMESTAMP,
  "descricao_votacao" VARCHAR,
  "ementa" VARCHAR,
  "resultado_votacao" VARCHAR,
  "total_votos_sim" INTEGER,
  "total_votos_nao" INTEGER,
  "total_votos_abstencao" INTEGER,
  "votacao_secreta" VARCHAR,
  "id_informe" BIGINT,
  "id_evento" BIGINT,
  "codigo_colegiado" BIGINT,
  "nome_colegiado" VARCHAR,
  "sigla_colegiado" VARCHAR,
  "data_informe" TIMESTAMP,
  "texto_informe" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_votacao")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_votacao | BIGINT | NO | 1 |
| id_materia | BIGINT | YES | 2 |
| id_processo | BIGINT | YES | 3 |
| identificacao | VARCHAR | YES | 4 |
| sigla | VARCHAR | YES | 5 |
| numero | VARCHAR | YES | 6 |
| ano | INTEGER | YES | 7 |
| codigo_sessao | BIGINT | YES | 8 |
| numero_sessao | INTEGER | YES | 9 |
| sequencial_sessao | INTEGER | YES | 10 |
| sigla_tipo_sessao | VARCHAR | YES | 11 |
| casa_sessao | VARCHAR | YES | 12 |
| codigo_sessao_legislativa | BIGINT | YES | 13 |
| data_apresentacao | TIMESTAMP | YES | 14 |
| data_sessao | TIMESTAMP | YES | 15 |
| descricao_votacao | VARCHAR | YES | 16 |
| ementa | VARCHAR | YES | 17 |
| resultado_votacao | VARCHAR | YES | 18 |
| total_votos_sim | INTEGER | YES | 19 |
| total_votos_nao | INTEGER | YES | 20 |
| total_votos_abstencao | INTEGER | YES | 21 |
| votacao_secreta | VARCHAR | YES | 22 |
| id_informe | BIGINT | YES | 23 |
| id_evento | BIGINT | YES | 24 |
| codigo_colegiado | BIGINT | YES | 25 |
| nome_colegiado | VARCHAR | YES | 26 |
| sigla_colegiado | VARCHAR | YES | 27 |
| data_informe | TIMESTAMP | YES | 28 |
| texto_informe | VARCHAR | YES | 29 |
| year_snapshot | BIGINT | YES | 30 |

## main.votos_camara

**Create statement:**

```sql
CREATE TABLE "votos_camara" (
  "id_voto" BIGINT NOT NULL,
  "id_votacao" VARCHAR,
  "id_deputado" BIGINT,
  "tipo_voto" VARCHAR,
  "data_hora" TIMESTAMP,
  "year_snapshot" INTEGER,
  PRIMARY KEY ("id_voto")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_voto | BIGINT | NO | 1 |
| id_votacao | VARCHAR | YES | 2 |
| id_deputado | BIGINT | YES | 3 |
| tipo_voto | VARCHAR | YES | 4 |
| data_hora | TIMESTAMP | YES | 5 |
| year_snapshot | INTEGER | YES | 6 |

## main.votos_senado

**Create statement:**

```sql
CREATE TABLE "votos_senado" (
  "id_voto" BIGINT NOT NULL,
  "codigo_votacao_sve" BIGINT,
  "codigo_sessao_votacao" BIGINT,
  "codigo_materia" BIGINT,
  "identificacao_materia" VARCHAR,
  "codigo_parlamentar" BIGINT,
  "nome_parlamentar" VARCHAR,
  "sexo_parlamentar" VARCHAR,
  "sigla_partido_parlamentar" VARCHAR,
  "sigla_uf_parlamentar" VARCHAR,
  "sigla_voto_parlamentar" VARCHAR,
  "descricao_voto_parlamentar" VARCHAR,
  "year_snapshot" BIGINT,
  PRIMARY KEY ("id_voto")
);
```

**Columns:**

| column_name | data_type | nullable | ordinal_position |
| --- | --- | --- | --- |
| id_voto | BIGINT | NO | 1 |
| codigo_votacao_sve | BIGINT | YES | 2 |
| codigo_sessao_votacao | BIGINT | YES | 3 |
| codigo_materia | BIGINT | YES | 4 |
| identificacao_materia | VARCHAR | YES | 5 |
| codigo_parlamentar | BIGINT | YES | 6 |
| nome_parlamentar | VARCHAR | YES | 7 |
| sexo_parlamentar | VARCHAR | YES | 8 |
| sigla_partido_parlamentar | VARCHAR | YES | 9 |
| sigla_uf_parlamentar | VARCHAR | YES | 10 |
| sigla_voto_parlamentar | VARCHAR | YES | 11 |
| descricao_voto_parlamentar | VARCHAR | YES | 12 |
| year_snapshot | BIGINT | YES | 13 |
