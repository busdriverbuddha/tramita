# DuckDB Schema & Data Preview


## main.autores_camara

**Create statement:**

```sql
CREATE TABLE "autores_camara" (
  id_autor BIGINT,
  cod_tipo BIGINT,
  uri VARCHAR,
  ordem_assinatura INTEGER,
  proponente BOOLEAN,
  id_proposicao BIGINT,
  year BIGINT
);
```

| id_autor | cod_tipo | uri | ordem_assinatura | proponente | id_proposicao | year |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/73538 | 1 | True | 15009 | 2020 |
| 2 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/73910 | 1 | True | 15532 | 2020 |
| 3 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/74316 | 1 | True | 15749 | 2020 |
| 4 | 20 | https://dadosabertos.camara.leg.br/api/v2/orgaos/262 | 1 | True | 15990 | 2020 |
| 5 | 40000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/78 | 1 | True | 16481 | 2020 |
| 6 | 40000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/78 | 1 | True | 16969 | 2020 |
| 7 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/73788 | 1 | True | 17563 | 2020 |
| 8 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/74671 | 1 | True | 17823 | 2020 |
| 9 | 40000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/78 | 1 | True | 17915 | 2020 |
| 10 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/73458 | 1 | True | 18420 | 2020 |


## main.autoria_iniciativa_senado

**Create statement:**

```sql
CREATE TABLE "autoria_iniciativa_senado" (
  id_autoria_iniciativa BIGINT,
  id_processo BIGINT,
  codigo_parlamentar BIGINT,
  descricao_tipo VARCHAR,
  ente VARCHAR,
  ordem INTEGER,
  outros_autores_nao_informados VARCHAR,
  sigla_ente VARCHAR,
  sigla_tipo VARCHAR,
  year_snapshot BIGINT
);
```

| id_autoria_iniciativa | id_processo | codigo_parlamentar | descricao_tipo | ente | ordem | outros_autores_nao_informados | sigla_ente | sigla_tipo | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 |  | PRESIDENTE_REPUBLICA | Presidência da República | 1 | Não | PR | PRESIDENTE_REPUBLICA | 2001 |
| 2 | 663587 | 825.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2005 |
| 3 | 1066060 |  | COMISSAO_CAMARA | Comissão de Ciência e Tecnologia, Comunicação e Informática | 1 | Não | CCTCI | COMISSAO_CAMARA | 2007 |
| 4 | 2978567 | 825.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2007 |
| 5 | 2968939 | 825.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2008 |
| 6 | 2970890 | 945.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2008 |
| 7 | 1035192 |  | COMISSAO_CAMARA | Comissão de Ciência e Tecnologia, Comunicação e Informática | 1 | Não | CCTCI | COMISSAO_CAMARA | 2009 |
| 8 | 2965245 | 945.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2009 |
| 9 | 3021092 |  | COMISSAO_CAMARA | Comissão de Ciência e Tecnologia, Comunicação e Informática | 1 | Não | CCTCI | COMISSAO_CAMARA | 2009 |
| 10 | 3333348 |  | CAMARA | Câmara dos Deputados | 1 | Não | CD | CAMARA | 2009 |


## main.autuacoes_senado

**Create statement:**

```sql
CREATE TABLE "autuacoes_senado" (
  id_processo BIGINT,
  autuacao_idx BIGINT,
  descricao_autuacao VARCHAR,
  id_ente_controle_atual BIGINT,
  nome_ente_controle_atual VARCHAR,
  sigla_ente_controle_atual VARCHAR,
  numero_autuacao INTEGER,
  year_snapshot BIGINT
);
```

| id_processo | autuacao_idx | descricao_autuacao | id_ente_controle_atual | nome_ente_controle_atual | sigla_ente_controle_atual | numero_autuacao | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2526458 | 1 | Autuação Principal | 55304 | Secretaria de Expediente | SEXPE | 1 | 2001 |
| 663587 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2005 |
| 1066060 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2007 |
| 2978567 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2007 |
| 2968939 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2008 |
| 2970890 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2008 |
| 1035192 | 1 | Autuação Principal | 55304 | Secretaria de Expediente | SEXPE | 1 | 2009 |
| 2965245 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2009 |
| 3021092 | 1 | Autuação Principal | 55304 | Secretaria de Expediente | SEXPE | 1 | 2009 |
| 3333348 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2009 |


## main.bloco_senado

**Create statement:**

```sql
CREATE TABLE "bloco_senado" (
  codigo_bloco BIGINT,
  data_criacao DATE,
  nome_apelido VARCHAR,
  nome_bloco VARCHAR,
  year_snapshot BIGINT
);
```

| codigo_bloco | data_criacao | nome_apelido | nome_bloco | year_snapshot |
| --- | --- | --- | --- | --- |
| 335 | 2023-02-01 00:00:00 | BLPRD | Bloco Parlamentar da Resistência Democrática | 2023 |
| 337 | 2023-02-03 00:00:00 | Minoria | Minoria | 2023 |
| 346 | 2023-03-20 00:00:00 | BLALIANÇA | Bloco Parlamentar Aliança | 2023 |
| 357 | 2025-02-03 00:00:00 | BLVANG | Bloco Parlamentar Vanguarda | 2025 |
| 358 | 2025-02-18 00:00:00 | BLDEM | Bloco Parlamentar Democracia | 2025 |
| 359 | 2025-02-18 00:00:00 | BLPBR | Bloco Parlamentar Pelo Brasil | 2025 |


## main.blocos_camara

**Create statement:**

```sql
CREATE TABLE "blocos_camara" (
  id_bloco BIGINT,
  nome VARCHAR,
  id_legislatura BIGINT,
  uri VARCHAR,
  year_snapshot BIGINT
);
```

| id_bloco | nome | id_legislatura | uri | year_snapshot |
| --- | --- | --- | --- | --- |
| 584 | Federação Brasil da Esperança - Fe Brasil | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/584 | 0 |
| 585 | Federação PSDB CIDADANIA | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/585 | 0 |
| 586 | Federação PSOL REDE | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/586 | 0 |
| 589 | PL, UNIÃO, PP, PSD, REPUBLICANOS, MDB, Federação PSDB CIDADANIA, PODE | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/589 | 0 |
| 590 | AVANTE, SOLIDARIEDADE, PRD | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/590 | 0 |


## main.blocos_partidos_camara

**Create statement:**

```sql
CREATE TABLE "blocos_partidos_camara" (
  id_bloco_partido BIGINT,
  id_bloco BIGINT,
  id_partido BIGINT,
  year_snapshot BIGINT
);
```

| id_bloco_partido | id_bloco | id_partido | year_snapshot |
| --- | --- | --- | --- |
| 1 | 584 | 36851 | 2020 |
| 2 | 585 | 36835 | 2020 |
| 3 | 586 | 36886 | 2020 |
| 4 | 589 | 38009 | 2020 |
| 5 | 590 | 37904 | 2020 |
| 6 | 584 | 36844 | 2020 |
| 7 | 585 | 37905 | 2020 |
| 8 | 586 | 36839 | 2020 |
| 9 | 589 | 37904 | 2020 |
| 10 | 590 | 38010 | 2020 |


## main.colegiado_senado

**Create statement:**

```sql
CREATE TABLE "colegiado_senado" (
  codigo_colegiado BIGINT,
  codigo_tipo_colegiado BIGINT,
  data_inicio DATE,
  indicador_distr_partidaria VARCHAR,
  nome_colegiado VARCHAR,
  sigla_colegiado VARCHAR,
  ordem INTEGER,
  year_snapshot BIGINT
);
```

| codigo_colegiado | codigo_tipo_colegiado | data_inicio | indicador_distr_partidaria | nome_colegiado | sigla_colegiado | ordem | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 34 | 21 | 1900-01-01 00:00:00 | S | Comissão de Constituição, Justiça e Cidadania | CCJ | 3 | 1900 |
| 38 | 21 | 1900-01-01 00:00:00 | S | Comissão de Assuntos Econômicos | CAE | 1 | 1900 |
| 40 | 21 | 1900-01-01 00:00:00 | S | Comissão de Assuntos Sociais | CAS | 2 | 1900 |
| 47 | 21 | 1900-01-01 00:00:00 | S | Comissão de Educação e Cultura | CE | 4 | 1900 |
| 50 | 21 | 1900-01-01 00:00:00 | S | Comissão de Meio Ambiente | CMA | 13 | 1900 |
| 54 | 21 | 1900-01-01 00:00:00 | S | Comissão de Relações Exteriores e Defesa Nacional | CRE | 7 | 1900 |
| 59 | 21 | 1900-01-01 00:00:00 | S | Comissão de Serviços de Infraestrutura | CI | 8 | 1900 |
| 834 | 21 | 2002-12-13 00:00:00 | S | Comissão de Direitos Humanos e Legislação Participativa | CDH | 6 | 2002 |
| 1306 | 21 | 2005-02-18 00:00:00 | S | Comissão de Desenvolvimento Regional e Turismo | CDR | 9 | 2005 |
| 1307 | 21 | 2005-02-22 00:00:00 | S | Comissão de Agricultura e Reforma Agrária | CRA | 10 | 2005 |


## main.deputados_camara

**Create statement:**

```sql
CREATE TABLE "deputados_camara" (
  id_deputado BIGINT,
  nome_civil VARCHAR,
  uri VARCHAR,
  year_snapshot BIGINT,
  rn BIGINT
);
```

| id_deputado | nome_civil | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- |
| 488 | José Jorge da Silva | https://dadosabertos.camara.leg.br/api/v2/deputados/488 | 2024 | 1 |
| 62926 | REINALDO SANTOS E SILVA | https://dadosabertos.camara.leg.br/api/v2/deputados/62926 | 2020 | 1 |
| 66828 | FAUSTO RUY PINATO | https://dadosabertos.camara.leg.br/api/v2/deputados/66828 | 2020 | 1 |
| 73439 | Carlos Nelson Bueno | https://dadosabertos.camara.leg.br/api/v2/deputados/73439 | 2023 | 1 |
| 73463 | OSMAR JOSÉ SERRAGLIO | https://dadosabertos.camara.leg.br/api/v2/deputados/73463 | 2020 | 1 |
| 73464 | BERNARDINO BARRETO DE OLIVEIRA | https://dadosabertos.camara.leg.br/api/v2/deputados/73464 | 2020 | 1 |
| 73472 | GERVÁSIO JOSÉ DA SILVA | https://dadosabertos.camara.leg.br/api/v2/deputados/73472 | 2020 | 1 |
| 73483 | LUIS CARLOS HEINZE | https://dadosabertos.camara.leg.br/api/v2/deputados/73483 | 2020 | 1 |
| 73486 | DARCI POMPEO DE MATTOS | https://dadosabertos.camara.leg.br/api/v2/deputados/73486 | 2020 | 1 |
| 73507 | ROSILDA DE FREITAS | https://dadosabertos.camara.leg.br/api/v2/deputados/73507 | 2022 | 1 |


## main.deputados_frentes_camara

**Create statement:**

```sql
CREATE TABLE "deputados_frentes_camara" (
  id_deputado_frente BIGINT,
  id_deputado BIGINT,
  id_frente BIGINT,
  year_snapshot BIGINT
);
```

| id_deputado_frente | id_deputado | id_frente | year_snapshot |
| --- | --- | --- | --- |
| 1 | 220594 | 54284 | 2020 |
| 2 | 220597 | 54284 | 2020 |
| 3 | 220602 | 54283 | 2020 |
| 4 | 220605 | 54293 | 2020 |
| 5 | 220606 | 54283 | 2020 |
| 6 | 220608 | 54293 | 2020 |
| 7 | 220609 | 54284 | 2020 |
| 8 | 220610 | 54283 | 2020 |
| 9 | 220617 | 54293 | 2020 |
| 10 | 220618 | 54293 | 2020 |


## main.deputados_historico_camara

**Create statement:**

```sql
CREATE TABLE "deputados_historico_camara" (
  id_deputado_historico BIGINT,
  id_deputado BIGINT,
  id_legislatura BIGINT,
  data_hora TIMESTAMP,
  condicao_eleitoral VARCHAR,
  descricao_status VARCHAR,
  year_snapshot BIGINT
);
```

| id_deputado_historico | id_deputado | id_legislatura | data_hora | condicao_eleitoral | descricao_status | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 220594 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 2 | 220597 | 57 | 2024-04-16 20:57:00 | Titular | Alteração de partido | 2023 |
| 3 | 220602 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 4 | 220605 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 5 | 220606 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 6 | 220608 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 7 | 220609 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 8 | 220610 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 9 | 220617 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 10 | 220618 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |


## main.deputados_orgaos_camara

**Create statement:**

```sql
CREATE TABLE "deputados_orgaos_camara" (
  id_deputado_orgao BIGINT,
  id_deputado BIGINT,
  id_orgao INTEGER,
  cod_titulo INTEGER,
  data_inicio TIMESTAMP,
  data_fim TIMESTAMP,
  year_snapshot BIGINT
);
```

| id_deputado_orgao | id_deputado | id_orgao | cod_titulo | data_inicio | data_fim | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 220594 | 539808 | 101 | 2025-09-09 00:00:00 |  | 2023 |
| 2 | 220597 | 539798 | 101 | 2025-06-11 00:00:00 |  | 2023 |
| 3 | 220602 | 539385 | 101 | 2025-08-05 00:00:00 |  | 2023 |
| 4 | 220606 | 5971 | 102 | 2025-09-01 00:00:00 |  | 2023 |
| 5 | 220608 | 2006 | 102 | 2025-03-18 00:00:00 |  | 2023 |
| 6 | 220610 | 539809 | 102 | 2025-08-13 00:00:00 |  | 2023 |
| 7 | 220618 | 539808 | 101 | 2025-09-03 00:00:00 |  | 2023 |
| 8 | 220621 | 539808 | 101 | 2025-09-03 00:00:00 |  | 2023 |
| 9 | 220622 | 539813 | 101 | 2025-09-02 00:00:00 |  | 2023 |
| 10 | 220625 | 539808 | 102 | 2025-09-03 00:00:00 |  | 2023 |


## main.despachos_senado

**Create statement:**

```sql
CREATE TABLE "despachos_senado" (
  id_processo BIGINT,
  id_despacho BIGINT,
  data_despacho DATE,
  cancelado VARCHAR,
  tipo_motivacao VARCHAR,
  sigla_tipo_motivacao VARCHAR,
  year_snapshot BIGINT
);
```

| id_processo | id_despacho | data_despacho | cancelado | tipo_motivacao | sigla_tipo_motivacao | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 663587 | 7806929 | 2009-03-24 00:00:00 | Não | Aprovação de requerimento | APROV_REQ | 2005 |
| 1066060 | 7889688 | 2018-11-26 00:00:00 | Não | Decisão da Presidência | DECISAO_PRESID | 2007 |
| 2978567 | 7938573 | 2019-03-26 00:00:00 | Não | Aprovação de requerimento | APROV_REQ | 2007 |
| 2968939 | 7936023 | 2019-03-26 00:00:00 | Não | Aprovação de requerimento | APROV_REQ | 2008 |
| 2970890 | 7812982 | 2013-06-27 00:00:00 | Não | Aprovação de requerimento | APROV_REQ | 2008 |
| 1035192 | 7804728 | 2009-08-12 00:00:00 | Não | Motivação não categorizada | NAO_CATEGORIZADO | 2009 |
| 2965245 | 7819608 | 2015-11-05 00:00:00 | Não | Aprovação de requerimento | APROV_REQ | 2009 |
| 3021092 | 7804773 | 2009-08-18 00:00:00 | Não | Motivação não categorizada | NAO_CATEGORIZADO | 2009 |
| 2958548 | 9175542 | 2022-06-21 00:00:00 | Não | Decisão da Presidência | DECISAO_PRESID | 2010 |
| 2958841 | 7812984 | 2013-06-27 00:00:00 | Não | Aprovação de requerimento | APROV_REQ | 2010 |


## main.documento_autoria_senado

**Create statement:**

```sql
CREATE TABLE "documento_autoria_senado" (
  id_documento_autoria BIGINT,
  id_processo BIGINT,
  id_ente BIGINT,
  autor VARCHAR,
  codigo_parlamentar BIGINT,
  descricao_tipo VARCHAR,
  ente VARCHAR,
  ordem INTEGER,
  outros_autores_nao_informados VARCHAR,
  sigla_ente VARCHAR,
  sigla_tipo VARCHAR,
  year_snapshot BIGINT
);
```

| id_documento_autoria | id_processo | id_ente | autor | codigo_parlamentar | descricao_tipo | ente | ordem | outros_autores_nao_informados | sigla_ente | sigla_tipo | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 | 55126 | Presidência da República |  | PRESIDENTE_REPUBLICA | Presidência da República | 1 | Não | PR | PRESIDENTE_REPUBLICA | 2001 |
| 2 | 663587 | 1 | Paulo Paim | 825.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2005 |
| 3 | 1066060 | 2 | Câmara dos Deputados |  | CAMARA | Câmara dos Deputados | 1 | Não | CD | CAMARA | 2007 |
| 4 | 2978567 | 1 | Paulo Paim | 825.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2007 |
| 5 | 2968939 | 1 | Paulo Paim | 825.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2008 |
| 6 | 2970890 | 1 | Alvaro Dias | 945.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2008 |
| 7 | 1035192 | 2 | Câmara dos Deputados |  | CAMARA | Câmara dos Deputados | 1 | Não | CD | CAMARA | 2009 |
| 8 | 2965245 | 1 | Alvaro Dias | 945.0 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2009 |
| 9 | 3021092 | 2 | Câmara dos Deputados |  | CAMARA | Câmara dos Deputados | 1 | Não | CD | CAMARA | 2009 |
| 10 | 3333348 | 55126 | Presidência da República |  | PRESIDENTE_REPUBLICA | Presidência da República | 1 | Não | PR | PRESIDENTE_REPUBLICA | 2009 |


## main.emendas_senado

**Create statement:**

```sql
CREATE TABLE "emendas_senado" (
  id_emenda BIGINT,
  id_ci_emenda BIGINT,
  id_ci_emendado BIGINT,
  id_documento_emenda BIGINT,
  id_processo BIGINT,
  identificacao VARCHAR,
  numero INTEGER,
  autoria VARCHAR,
  descricao_documento_emenda VARCHAR,
  tipo_emenda VARCHAR,
  turno_apresentacao VARCHAR,
  casa VARCHAR,
  codigo_colegiado BIGINT,
  sigla_colegiado VARCHAR,
  nome_colegiado VARCHAR,
  data_apresentacao DATE,
  url_documento_emenda VARCHAR,
  year_snapshot BIGINT
);
```

| id_emenda | id_ci_emenda | id_ci_emendado | id_documento_emenda | id_processo | identificacao | numero | autoria | descricao_documento_emenda | tipo_emenda | turno_apresentacao | casa | codigo_colegiado | sigla_colegiado | nome_colegiado | data_apresentacao | url_documento_emenda | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4694683 | 4694680 | 1330444 | 4694674 | 1330439 | EMENDA 1 PLEN - PRS 57/2015 | 1 | Senador Romero Jucá (MDB/RR) |  | EMENDA_PARCIAL | NORMAL | SF | 1998 | PLEN | Plenário do Senado Federal | 2015-12-01 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4694674 | 2015 |
| 4429988 | 4429985 | 1331407 | 4429979 | 1331402 | EMENDA 1 / CE - PRS 2/2015 | 1 | Autoria não registrada. |  | EMENDA_PARCIAL | NORMAL | SF | 47 | CE | Comissão de Educação e Cultura | 2015-10-13 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4429979 | 2015 |
| 4338177 | 4338174 | 1331428 | 4338168 | 1331423 | EMENDA 1 / CE - PRS 1/2015 | 1 | Autoria não registrada. |  | EMENDA_PARCIAL | NORMAL | SF | 47 | CE | Comissão de Educação e Cultura | 2015-05-05 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4338168 | 2015 |
| 4012973 | 4012970 | 1399053 | 4012964 | 1399048 | EMENDA 1 - PEC 83/2015 | 1 | Senador Antonio Anastasia (PSDB/MG) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-12 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4012964 | 2015 |
| 4012989 | 4012986 | 1399053 | 4012980 | 1399048 | EMENDA 2 - PEC 83/2015 | 2 | Senador Ricardo Ferraço (MDB/ES) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-12 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4012980 | 2015 |
| 4013005 | 4013002 | 1399053 | 4012996 | 1399048 | EMENDA 4 - PEC 83/2015 | 4 | Senador Ricardo Ferraço (MDB/ES) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-12 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4012996 | 2015 |
| 4013021 | 4013018 | 1399053 | 4013012 | 1399048 | EMENDA 3 - PEC 83/2015 | 3 | Senador Ricardo Ferraço (MDB/ES) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-12 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4013012 | 2015 |
| 4013046 | 4013043 | 1399053 | 4013037 | 1399048 | EMENDA 5 - PEC 83/2015 | 5 | Senador Walter Pinheiro (PT/BA) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-18 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4013037 | 2015 |
| 4013062 | 4013059 | 1399053 | 4013053 | 1399048 | EMENDA 7 - PEC 83/2015 | 7 | Senador Walter Pinheiro (PT/BA) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-18 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4013053 | 2015 |
| 4013078 | 4013075 | 1399053 | 4013069 | 1399048 | EMENDA 8 - PEC 83/2015 | 8 | Senador Walter Pinheiro (PT/BA) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-18 00:00:00 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4013069 | 2015 |


## main.encontro_legislativo_senado

**Create statement:**

```sql
CREATE TABLE "encontro_legislativo_senado" (
  id_processo BIGINT,
  id_despacho BIGINT,
  id_encontro_legislativo BIGINT,
  data_encontro DATE,
  tipo_encontro VARCHAR,
  descricao_encontro VARCHAR,
  casa_encontro VARCHAR,
  numero_encontro INTEGER,
  colegiado_casa VARCHAR,
  colegiado_codigo BIGINT,
  colegiado_nome VARCHAR,
  colegiado_sigla VARCHAR,
  year_snapshot BIGINT,
  rn BIGINT
);
```

| id_processo | id_despacho | id_encontro_legislativo | data_encontro | tipo_encontro | descricao_encontro | casa_encontro | numero_encontro | colegiado_casa | colegiado_codigo | colegiado_nome | colegiado_sigla | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5227247 | 7903678 | 7369084 | 2018-03-15 00:00:00 | SES | Sessão Deliberativa Extraordinária | SF | 27 | SF | 1998 | Plenário do Senado Federal | PLEN | 2017 | 1 |
| 7696069 | 7886528 | 7697524 | 2018-11-16 00:00:00 | SES | Sessão Não Deliberativa | SF | 8 | SF | 1998 | Plenário do Senado Federal | PLEN | 2018 | 1 |
| 7703737 | 7894097 | 7703646 | 2018-12-11 00:00:00 | SES | Sessão Deliberativa Ordinária | SF | 154 | SF | 1998 | Plenário do Senado Federal | PLEN | 2018 | 1 |
| 7741404 | 7940462 | 7741033 | 2019-04-10 00:00:00 | SES | Sessão Deliberativa Ordinária | SF | 47 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 7758398 | 7958926 | 7757881 | 2019-05-28 00:00:00 | SES | Sessão Deliberativa Ordinária | SF | 84 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 7762202 | 7963054 | 7761771 | 2019-06-06 00:00:00 | SES | Sessão Deliberativa Extraordinária | SF | 90 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 2914544 | 7971974 | 7774190 | 2019-06-27 00:00:00 | SES | Sessão Não Deliberativa | SF | 104 | SF | 1998 | Plenário do Senado Federal | PLEN | 2016 | 1 |
| 7778890 | 7978217 | 7778834 | 2019-07-10 00:00:00 | SES | Sessão Deliberativa Ordinária | SF | 117 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 7783495 | 7985093 | 7782566 | 2019-08-06 00:00:00 | SES | Sessão Deliberativa Ordinária | SF | 127 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 7791472 | 8007570 | 7800450 | 2019-09-11 00:00:00 | SES | Sessão Deliberativa Ordinária | SF | 163 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |


## main.eventos_camara

**Create statement:**

```sql
CREATE TABLE "eventos_camara" (
  id_evento BIGINT,
  data_hora_inicio TIMESTAMP,
  data_hora_fim TIMESTAMP,
  descricao VARCHAR,
  descricao_tipo VARCHAR,
  fases VARCHAR,
  uri VARCHAR,
  year_snapshot BIGINT,
  rn BIGINT
);
```

| id_evento | data_hora_inicio | data_hora_fim | descricao | descricao_tipo | fases | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59130 | 2020-02-13 09:00:00 | 2020-02-13 19:00:00 | Visita Técnica - Colômbia
 Reunião no Ministério da Justiça da Colômbia

9:00  - 9:15   Boas vindas com a Dra. Margarita Cabello Blanco (por confirmar) Ministra de Justicia y del derecho

9:15 - … | Outro Evento |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59130 | 2020 | 1 |
| 59154 | 2021-03-23 09:30:00 | 2021-03-23 10:35:00 | Reunião deliberativa
 | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59154 | 2021 | 1 |
| 59253 | 2020-02-04 14:30:00 | 2020-02-04 18:07:00 | Audiência Pública e Deliberação de Requerimentos
 I - Audiência Pública com a presença confirmada dos seguintes convidados:

-Coronel MARCOS ANTÔNIO NUNES DE OLIVEIRA, Representante da Associação d… | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59253 | 2020 | 1 |
| 59271 | 2020-02-05 10:00:00 | 2020-02-05 12:25:00 | CORANAVÍRUS: Ministério da Saúde; CSSF; FP da Saúde
 | Palestra |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59271 | 2020 | 1 |
| 59336 | 2020-02-18 16:30:00 | 2020-02-18 18:58:00 | Discussão e Votação de Propostas
 Deliberação de Requerimentos. | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59336 | 2020 | 1 |
| 59341 | 2020-02-19 09:00:00 | 2020-02-19 11:00:00 | Visita técnica ao Ministério da Saúde
 Visita Técnica ao Ministério da Saúde
Com o Secretário-Executivo João Gabbardo dos Reis
Horário:09h
Endereço: Ministério da Saúde - Esplanada dos Ministérios… | Outro Evento |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59341 | 2020 | 1 |
| 59403 | 2020-03-11 10:00:00 |  | Discussão e Votação do Parecer do Relator
 - Discussão e Votação do Parecer do Relator, Deputado Juscelino Filho | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59403 | 2020 | 1 |
| 59407 | 2020-03-04 14:30:00 | 2020-03-04 18:16:00 | Avaliação e Acompanhamento-GAA e Plano Nacional de Contingenciamento.
 I - Audiência Pública com a participação das seguintes autoridades:


-Antonio Roque Pedreira Júnior, Chefe de Gabinete do Mi… | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59407 | 2020 | 1 |
| 59413 | 2020-03-04 13:55:00 | 2020-03-04 21:07:00 | Sessão Deliberativa Extraordinária
 | Sessão Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59413 | 2020 | 1 |
| 59440 | 2020-03-06 15:00:00 | 2020-03-06 17:31:00 | Homenagem ao Centenário da Mãe Ruth de Oxalá e às Mulheres de Terreiro do DF e Entorno
 Homenagem ao Centenário da Mãe Ruth de Oxalá e às Mulheres de Terreiro do DF e Entorno | Sessão Não Deliberativa Solene |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59440 | 2020 | 1 |


## main.eventos_orgaos_camara

**Create statement:**

```sql
CREATE TABLE "eventos_orgaos_camara" (
  id_evento_orgao BIGINT,
  id_evento BIGINT,
  id_orgao INTEGER,
  year_snapshot BIGINT
);
```

| id_evento_orgao | id_evento | id_orgao | year_snapshot |
| --- | --- | --- | --- |
| 1 | 58552 | 538357 | 2020 |
| 2 | 59113 | 538315 | 2020 |
| 3 | 59129 | 538408 | 2020 |
| 4 | 59130 | 538408 | 2020 |
| 5 | 59186 | 538364 | 2020 |
| 6 | 59216 | 538621 | 2020 |
| 7 | 59227 | 538272 | 2020 |
| 8 | 59234 | 538408 | 2020 |
| 9 | 59236 | 538734 | 2020 |
| 10 | 59244 | 180 | 2020 |


## main.eventos_pauta_camara

**Create statement:**

```sql
CREATE TABLE "eventos_pauta_camara" (
  id_pauta BIGINT,
  id_evento BIGINT,
  cod_regime VARCHAR,
  ordem INTEGER,
  id_proposicao BIGINT,
  id_relator BIGINT,
  year_snapshot INTEGER
);
```

| id_pauta | id_evento | cod_regime | ordem | id_proposicao | id_relator | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 58552 | 106.0 | 1 | 1198512 | 160639.0 | 2020 |
| 2 | 59113 | 21.0 | 1 | 2238574 | 204510.0 | 2020 |
| 3 | 59129 | 14.0 | 1 | 2233088 | 178931.0 | 2020 |
| 4 | 59129 | 99.0 | 2 | 2234669 |  | 2020 |
| 5 | 59129 | 99.0 | 3 | 2236762 | 178931.0 | 2020 |
| 6 | 59154 | 99.0 | 1 | 2273905 |  | 2021 |
| 7 | 59154 | 20.0 | 2 | 2220726 | 75431.0 | 2021 |
| 8 | 59154 | 20.0 | 3 | 2223631 | 160575.0 | 2021 |
| 9 | 59154 | 14.0 | 4 | 2219323 | 204416.0 | 2021 |
| 10 | 59154 | 20.0 | 5 | 2210603 | 160575.0 | 2021 |


## main.frentes_camara

**Create statement:**

```sql
CREATE TABLE "frentes_camara" (
  id_frente BIGINT,
  id_deputado_coordenador BIGINT,
  id_legislatura BIGINT,
  titulo VARCHAR,
  uri VARCHAR,
  year_snapshot BIGINT,
  rn BIGINT
);
```

| id_frente | id_deputado_coordenador | id_legislatura | titulo | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- |
| 356 | 73483.0 | 54 | Frente Parlamentar da Agropecuária - FPA | https://dadosabertos.camara.leg.br/api/v2/frentes/356 | 0 | 1 |
| 362 | 74749.0 | 54 | Frente Parlamentar do Transporte Público - FPTP | https://dadosabertos.camara.leg.br/api/v2/frentes/362 | 0 | 1 |
| 370 | 160655.0 | 54 | Frente Parlamentar da Habitação e Desenvolvimento Urbano do Congresso Nacional | https://dadosabertos.camara.leg.br/api/v2/frentes/370 | 0 | 1 |
| 420 | 74784.0 | 54 | Frente Parlamentar pela Liberdade de Expressão e o Direito à Comunicação com Participação Popular | https://dadosabertos.camara.leg.br/api/v2/frentes/420 | 0 | 1 |
| 436 | 160555.0 | 54 | Frente Parlamentar da Mineração Brasileira | https://dadosabertos.camara.leg.br/api/v2/frentes/436 | 0 | 1 |
| 447 | 109152.0 | 54 | Frente Parlamentar em Defesa da Cadeia do Aço, Ferro Gusa, Ferro Ligas, Silício Metálico, seus insumos e derivados. | https://dadosabertos.camara.leg.br/api/v2/frentes/447 | 0 | 1 |
| 451 | 160659.0 | 54 | Frente Parlamentar em Defesa das Vítimas da Violência | https://dadosabertos.camara.leg.br/api/v2/frentes/451 | 0 | 1 |
| 461 | 160636.0 | 54 | Frente Parlamentar pelo Desenvolvimento do Semiárido | https://dadosabertos.camara.leg.br/api/v2/frentes/461 | 0 | 1 |
| 477 | 160529.0 | 54 | Frente Parlamentar de Combate ao Trauma | https://dadosabertos.camara.leg.br/api/v2/frentes/477 | 0 | 1 |
| 488 |  | 54 | Frente Parlamentar do Cooperativismo (Frencoop) | https://dadosabertos.camara.leg.br/api/v2/frentes/488 | 0 | 1 |


## main.informes_documentos_associados_senado

**Create statement:**

```sql
CREATE TABLE "informes_documentos_associados_senado" (
  id_documento_associado BIGINT,
  id_processo BIGINT,
  id_informe BIGINT,
  id_documento BIGINT,
  autuacao_ordem INTEGER,
  informe_ordem INTEGER,
  documento_ordem INTEGER,
  sigla_tipo_documento VARCHAR,
  tipo_documento VARCHAR,
  identificacao VARCHAR,
  data_documento TIMESTAMP,
  autoria_documento VARCHAR,
  url_documento VARCHAR,
  year_snapshot BIGINT
);
```

| id_documento_associado | id_processo | id_informe | id_documento | autuacao_ordem | informe_ordem | documento_ordem | sigla_tipo_documento | tipo_documento | identificacao | data_documento | autoria_documento | url_documento | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 | 2230315 | 9909757 | 0 | 30 | 0 | OFICIO | Ofício | OFCN 33/2025 | 2025-03-06 00:00:00 | Primeiro-Secretário do Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9909757 | 2001 |
| 2 | 663587 | 2151518 | 9422566 | 0 | 170 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF236016344002 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9422566 | 2005 |
| 3 | 2978567 | 2151970 | 9424373 | 0 | 72 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF238672940695 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9424373 | 2007 |
| 4 | 2968939 | 2152226 | 9425397 | 0 | 47 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF236991863667 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9425397 | 2008 |
| 5 | 2970890 | 2151099 | 9420891 | 0 | 56 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF237916023879 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9420891 | 2008 |
| 6 | 2965245 | 2151638 | 9423047 | 0 | 134 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF230920751366 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9423047 | 2009 |
| 7 | 2958548 | 2152183 | 9425225 | 0 | 121 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF238814653014 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9425225 | 2010 |
| 8 | 2958841 | 2152192 | 9425261 | 0 | 81 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF231854240730 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9425261 | 2010 |
| 9 | 3020085 | 2199700 | 9637788 | 0 | 383 | 1 | OFICIO | Ofício | OFSF 585/2024 | 2024-06-21 00:00:00 | Primeiro-Secretário do Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9637788 | 2010 |
| 10 | 516008 | 2152214 | 9425349 | 0 | 26 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF230584564270 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9425349 | 2011 |


## main.informes_legislativos_senado

**Create statement:**

```sql
CREATE TABLE "informes_legislativos_senado" (
  id_informe_legislativo BIGINT,
  id_processo BIGINT,
  id_informe BIGINT,
  data_informe DATE,
  descricao VARCHAR,
  id_situacao_iniciada BIGINT,
  sigla_situacao_iniciada VARCHAR,
  ente_adm_casa VARCHAR,
  ente_adm_id BIGINT,
  ente_adm_nome VARCHAR,
  ente_adm_sigla VARCHAR,
  colegiado_casa VARCHAR,
  colegiado_codigo BIGINT,
  colegiado_nome VARCHAR,
  colegiado_sigla VARCHAR,
  year_snapshot BIGINT
);
```

| id_informe_legislativo | id_processo | id_informe | data_informe | descricao | id_situacao_iniciada | sigla_situacao_iniciada | ente_adm_casa | ente_adm_id | ente_adm_nome | ente_adm_sigla | colegiado_casa | colegiado_codigo | colegiado_nome | colegiado_sigla | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 | 2230315 | 2025-03-07 00:00:00 | Remetido Ofício CN nº 33, de 06/03/25, ao Senhor Primeiro-Secretário da Câmara dos Deputados, comunicando o término do prazo estabelecido no § 2º do art. 11 da Resolução nº 1, de 2002-CN, e no § 11 do… |  |  | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2001 |
| 2 | 663587 | 2151518 | 2023-08-05 00:00:00 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2005 |
| 3 | 1066060 | 2063899 | 2021-09-20 00:00:00 | A Presidência declara o Projeto prejudicado, em atenção à decisão da CCT, em reunião ocorrida no dia 16 de setembro, que deliberou pela prejudicialidade da matéria, nos termos do art. 334 do Regimento… | 43.0 | PRJDA | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 1998.0 | Plenário do Senado Federal | PLEN | 2007 |
| 4 | 2978567 | 2151970 | 2023-08-05 00:00:00 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2007 |
| 5 | 2968939 | 2152226 | 2023-08-05 00:00:00 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2008 |
| 6 | 2970890 | 2151099 | 2023-08-05 00:00:00 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2008 |
| 7 | 1035192 | 2153518 | 2022-04-26 00:00:00 | Publicado no Diário do Congresso Nacional n° 13, de 14/04/22, pág, 0034.

À COARQ. |  |  | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2009 |
| 8 | 2965245 | 2151638 | 2023-08-05 00:00:00 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2009 |
| 9 | 3021092 | 2153552 | 2022-08-11 00:00:00 | Publicado no Diário do Congresso Nacional n° 30, de 11/08/22, pág, 0073.

À COARQ. |  |  | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2009 |
| 10 | 3333348 | 2052475 | 2021-04-30 00:00:00 | (PR) PRESIDÊNCIA DA REPÚBLICA..
PROMULGADAS partes vetadas e rejeitadas pelo Congresso Nacional, da Lei nº 11.907, de 2 de fevereiro de 2009.
DOUE (Diário Oficial da União) - 30/04/2021 - Seção I - … |  |  | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2009 |


## main.legislaturas_camara

**Create statement:**

```sql
CREATE TABLE "legislaturas_camara" (
  id_legislatura BIGINT,
  data_inicio DATE,
  data_fim DATE,
  uri VARCHAR,
  year_snapshot BIGINT
);
```

| id_legislatura | data_inicio | data_fim | uri | year_snapshot |
| --- | --- | --- | --- | --- |
| 1 | 1826-04-29 00:00:00 | 1830-04-24 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/1 | 0 |
| 2 | 1830-04-25 00:00:00 | 1834-04-24 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/2 | 0 |
| 3 | 1834-04-25 00:00:00 | 1838-04-24 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/3 | 0 |
| 4 | 1838-04-25 00:00:00 | 1842-04-24 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/4 | 0 |
| 5 | 1842-04-25 00:00:00 | 1844-05-24 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/5 | 0 |
| 6 | 1844-12-24 00:00:00 | 1848-04-24 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/6 | 0 |
| 7 | 1848-04-25 00:00:00 | 1849-02-19 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/7 | 0 |
| 8 | 1849-12-15 00:00:00 | 1853-04-14 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/8 | 0 |
| 9 | 1853-04-15 00:00:00 | 1857-04-14 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/9 | 0 |
| 10 | 1857-04-15 00:00:00 | 1861-04-14 00:00:00 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/10 | 0 |


## main.legislaturas_lideres_camara

**Create statement:**

```sql
CREATE TABLE "legislaturas_lideres_camara" (
  id_lider BIGINT,
  id_legislatura BIGINT,
  nome_bancada VARCHAR,
  tipo_bancada VARCHAR,
  uri_bancada VARCHAR,
  data_inicio TIMESTAMP,
  data_fim TIMESTAMP,
  id_deputado BIGINT,
  titulo VARCHAR,
  year_snapshot INTEGER
);
```

| id_lider | id_legislatura | nome_bancada | tipo_bancada | uri_bancada | data_inicio | data_fim | id_deputado | titulo | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2004-05-05 00:00:00 | 2007-01-31 00:00:00 | 73442 | Vice-Líder | 2003 |
| 2 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2005-05-31 00:00:00 | 2006-04-19 00:00:00 | 73472 | Vice-Líder | 2003 |
| 3 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-12 00:00:00 | 2007-01-31 00:00:00 | 73546 | Vice-Líder | 2003 |
| 4 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2005-07-12 00:00:00 | 2007-01-31 00:00:00 | 73579 | Vice-Líder | 2003 |
| 5 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2006-05-31 00:00:00 | 2007-01-31 00:00:00 | 73592 | 1º Vice-Líder | 2003 |
| 6 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-12 00:00:00 | 2006-05-31 00:00:00 | 73592 | Vice-Líder | 2003 |
| 7 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-24 00:00:00 | 2006-03-23 00:00:00 | 73764 | Vice-Líder | 2003 |
| 8 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-24 00:00:00 | 2005-05-31 00:00:00 | 73882 | Vice-Líder | 2003 |
| 9 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-05-20 00:00:00 | 2007-01-31 00:00:00 | 74055 | Vice-Líder | 2003 |
| 10 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-12 00:00:00 | 2007-01-31 00:00:00 | 74058 | Vice-Líder | 2003 |


## main.legislaturas_mesa_camara

**Create statement:**

```sql
CREATE TABLE "legislaturas_mesa_camara" (
  id_legislatura_mesa BIGINT,
  id_legislatura BIGINT,
  id_deputado BIGINT,
  cod_titulo VARCHAR,
  data_inicio DATE,
  data_fim DATE,
  year_snapshot BIGINT
);
```

| id_legislatura_mesa | id_legislatura | id_deputado | cod_titulo | data_inicio | data_fim | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 85 | 52 | 74436 | 1 | 2005-02-14 00:00:00 | 2005-09-21 00:00:00 | 2003 |
| 103 | 52 | 73428 | 1 | 2005-09-28 00:00:00 | 2007-01-31 00:00:00 | 2003 |
| 109 | 52 | 73534 | 1 | 2003-02-02 00:00:00 | 2005-02-14 00:00:00 | 2003 |
| 115 | 52 | 74563 | 10 | 2005-02-14 00:00:00 | 2007-01-31 00:00:00 | 2003 |
| 121 | 52 | 74801 | 10 | 2003-02-02 00:00:00 | 2004-12-01 00:00:00 | 2003 |
| 91 | 52 | 74374 | 11 | 2005-02-14 00:00:00 | 2007-01-31 00:00:00 | 2003 |
| 97 | 52 | 74097 | 11 | 2003-02-02 00:00:00 | 2004-12-31 00:00:00 | 2003 |
| 55 | 52 | 74158 | 12 | 2005-02-14 00:00:00 | 2007-01-31 00:00:00 | 2003 |
| 13 | 52 | 74559 | 12 | 2003-02-02 00:00:00 | 2005-02-14 00:00:00 | 2003 |
| 43 | 52 | 74421 | 2 | 2003-02-02 00:00:00 | 2005-02-14 00:00:00 | 2003 |


## main.movimentacoes_senado

**Create statement:**

```sql
CREATE TABLE "movimentacoes_senado" (
  id_processo BIGINT,
  autuacao_idx INTEGER,
  movimentacao_idx INTEGER,
  id_movimentacao BIGINT,
  data_envio TIMESTAMP,
  data_recebimento TIMESTAMP,
  ente_origem_casa VARCHAR,
  ente_origem_id BIGINT,
  ente_origem_nome VARCHAR,
  ente_origem_sigla VARCHAR,
  ente_destino_casa VARCHAR,
  ente_destino_id BIGINT,
  ente_destino_nome VARCHAR,
  ente_destino_sigla VARCHAR,
  colegiado_destino_casa VARCHAR,
  colegiado_destino_codigo BIGINT,
  colegiado_destino_nome VARCHAR,
  colegiado_destino_sigla VARCHAR,
  year_snapshot BIGINT
);
```

| id_processo | autuacao_idx | movimentacao_idx | id_movimentacao | data_envio | data_recebimento | ente_origem_casa | ente_origem_id | ente_origem_nome | ente_origem_sigla | ente_destino_casa | ente_destino_id | ente_destino_nome | ente_destino_sigla | colegiado_destino_casa | colegiado_destino_codigo | colegiado_destino_nome | colegiado_destino_sigla | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2526458 | 0 | 1 | 9909703 | 2025-03-06 14:28:34 | 2025-03-06 16:01:29 | SF | 55296 | Secretaria Legislativa do Congresso Nacional | SLCN | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2001 |
| 663587 | 0 | 20 | 10037487 | 2025-09-01 13:53:00 | 2025-09-01 13:53:00 | SF | 55299 | Coordenação de Arquivo | COARQ | SF | 55299 | Coordenação de Arquivo | COARQ |  |  |  |  | 2005 |
| 1066060 | 0 | 4 | 9018086 | 2021-09-20 13:19:49 | 2022-03-14 09:48:50 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55299 | Coordenação de Arquivo | COARQ |  |  |  |  | 2007 |
| 2978567 | 0 | 20 | 10016286 | 2025-08-14 15:15:37 | 2025-08-14 15:17:36 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55299 | Coordenação de Arquivo | COARQ |  |  |  |  | 2007 |
| 2968939 | 0 | 20 | 9994083 | 2025-07-10 15:04:43 | 2025-07-10 15:05:40 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55299 | Coordenação de Arquivo | COARQ |  |  |  |  | 2008 |
| 2970890 | 0 | 20 | 10005088 | 2025-07-22 14:19:37 | 2025-07-22 14:27:42 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55299 | Coordenação de Arquivo | COARQ |  |  |  |  | 2008 |
| 1035192 | 0 | 9 | 9128300 | 2022-04-05 16:52:19 | 2022-04-06 09:58:02 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2009 |
| 2965245 | 0 | 77 | 9423054 | 2023-08-05 02:56:32 | 2023-11-13 16:41:23 | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF | SF | 55299 | Coordenação de Arquivo | COARQ |  |  |  |  | 2009 |
| 3021092 | 0 | 9 | 9173439 | 2022-06-14 17:11:27 | 2022-06-14 17:19:30 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2009 |
| 3333348 | 0 | 6 | 9139462 | 2022-05-05 15:27:02 | 2022-05-24 09:09:17 | SF | 55304 | Secretaria de Expediente | SEXPE | SF | 55299 | Coordenação de Arquivo | COARQ |  |  |  |  | 2009 |


## main.orgaos_camara

**Create statement:**

```sql
CREATE TABLE "orgaos_camara" (
  id_orgao BIGINT,
  nome VARCHAR,
  cod_tipo_orgao BIGINT,
  uri VARCHAR,
  year_snapshot BIGINT,
  rn BIGINT
);
```

| id_orgao | nome | cod_tipo_orgao | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- |
| 201 | COMISSÃO DO TRABALHO | 2 | https://dadosabertos.camara.leg.br/api/v2/orgaos/201 | 2023 | 1 |
| 218 | COMISSÃO DE CONSTITUIÇÃO E JUSTIÇA | 2 | https://dadosabertos.camara.leg.br/api/v2/orgaos/218 | 2020 | 1 |
| 5306 | Dispõe sobre o Conselho de Altos Estudos e Avaliação Tecnológica, de que trata o artigo 275 do Regimento Interno. | 11 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5306 | 0 | 1 |
| 5437 | Comissão Especial destinada a apreciar e  proferir parecer  à Proposta de Emenda à Constituição nº 57-A, de 1999, que " altera o art. 159 para instituir o Fundo Nacional de Desenvolvimento do Semi-Ári… | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5437 | 2023 | 1 |
| 5604 | Altera a Legislação Tributária Federal, e dá outras providências. | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5604 | 0 | 1 |
| 5942 | Altera dispositivos da Lei nº 8.745, de 9 de dezembro de 1993, e da Lei nº 10.470, de 25 de junho de 2002, cria cargos efetivos, cargos comissionados e gratificações no âmbito da Administração Pública… | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5942 | 0 | 1 |
| 5956 | Altera as Leis nºs. 8.248, de 23 de outubro de 1991, 8.387, de 30 de dezembro de 1991, e 10.176, de 11 de janeiro de 2001, dispondo sobre a capacitação e competitividade do setor de tecnologia da info… | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5956 | 0 | 1 |
| 5957 | Dispõe sobre a contribuição para o Programa de Integração Social e de Formação do Patrimônio do Servidor Público - PIS/PASEP e da Contribuição para Seguridade Social - COFINS devidas pelas sociedades … | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5957 | 0 | 1 |
| 5986 | Cria a Carreira de Agente Penitenciário Federal no Quadro de Pessoal do Departamento de Polícia Federal e dá outras providências. | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5986 | 0 | 1 |
| 8669 | Comissão Especial destinada a proferir parecer à Proposta de Emenda à Constituição nº 53-A, de 2007, do Sr. Jofran Frejat, que "dá nova redação ao § 3º do Art. 39 da Constituição Federal" (garante ao … | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/8669 | 2021 | 1 |


## main.orientacoes_camara

**Create statement:**

```sql
CREATE TABLE "orientacoes_camara" (
  id_orientacao BIGINT,
  id_votacao VARCHAR,
  sigla_partido_bloco VARCHAR,
  orientacao_voto VARCHAR,
  cod_partido_bloco BIGINT,
  cod_tipo_lideranca VARCHAR,
  uri_partido_bloco VARCHAR,
  year_snapshot BIGINT
);
```

| id_orientacao | id_votacao | sigla_partido_bloco | orientacao_voto | cod_partido_bloco | cod_tipo_lideranca | uri_partido_bloco | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 105464-262 | NOVO | Não | 37901 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/37901 | 2020 |
| 2 | 105464-319 | PT | Sim | 36844 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36844 | 2020 |
| 3 | 105464-326 | NOVO | Não | 37901 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/37901 | 2020 |
| 4 | 1198512-250 | PTB | Sim | 36845 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36845 | 2020 |
| 5 | 1198512-254 | DEM | Não | 36769 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2020 |
| 6 | 1198512-257 | REPUBLICANOS | Sim | 37908 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/37908 | 2020 |
| 7 | 1198512-272 | PCdoB | Sim | 36779 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36779 | 2020 |
| 8 | 1198512-279 | PCdoB | Sim | 36779 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36779 | 2020 |
| 9 | 1212657-35 | DEM | Não | 36769 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2020 |
| 10 | 1301128-43 | PSOL | Sim | 36839 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36839 | 2020 |


## main.outros_numeros_senado

**Create statement:**

```sql
CREATE TABLE "outros_numeros_senado" (
  id_outro_numero BIGINT,
  id_processo BIGINT,
  id_outro_processo BIGINT,
  ano INTEGER,
  casa_identificadora VARCHAR,
  ente_identificador VARCHAR,
  sigla VARCHAR,
  numero VARCHAR,
  sigla_ente_identificador VARCHAR,
  externa_ao_congresso VARCHAR,
  tramitando VARCHAR,
  year_snapshot BIGINT
);
```

| id_outro_numero | id_processo | id_outro_processo | ano | casa_identificadora | ente_identificador | sigla | numero | sigla_ente_identificador | externa_ao_congresso | tramitando | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 |  | 2001 |  | Presidência da República | MSG | 954 | PR |  | Não | 2001 |
| 2 | 1066060 |  | 2006 | CN | Congresso Nacional | MSG | 696 | CN | Não | Não | 2007 |
| 3 | 1035192 |  | 2008 | CN | Congresso Nacional | MSG | 185 | CN | Não | Não | 2009 |
| 4 | 3021092 |  | 2008 | CN | Congresso Nacional | MSG | 185 | CN | Não | Não | 2009 |
| 5 | 3333348 |  | 2009 |  | Presidência da República | MSG | 48 | PR |  | Não | 2009 |
| 6 | 2958548 | 2958545.0 | 2008 | CD | Câmara dos Deputados | PL | 03512 | CD | Não | Não | 2010 |
| 7 | 3020085 |  | 2009 | CN | Congresso Nacional | MSG | 730 | CN | Não | Não | 2010 |
| 8 | 3346770 |  | 2010 |  | Presidência da República | MSG | 305 | PR |  | Não | 2010 |
| 9 | 516008 | 516005.0 | 1999 | CD | Câmara dos Deputados | PL | 01664 | CD | Não | Não | 2011 |
| 10 | 516203 | 516200.0 | 2004 | CD | Câmara dos Deputados | PL | 04479 | CD | Não | Não | 2011 |


## main.parlamentar_senado

**Create statement:**

```sql
CREATE TABLE "parlamentar_senado" (
  codigo_parlamentar BIGINT,
  codigo_publico_leg_atual BIGINT,
  nome_completo VARCHAR,
  nome_parlamentar VARCHAR,
  sexo_parlamentar VARCHAR,
  sigla_partido VARCHAR,
  uf_parlamentar VARCHAR,
  email_parlamentar VARCHAR,
  data_nascimento DATE,
  endereco_parlamentar VARCHAR,
  naturalidade VARCHAR,
  uf_naturalidade VARCHAR,
  year_snapshot BIGINT,
  rn BIGINT
);
```

| codigo_parlamentar | codigo_publico_leg_atual | nome_completo | nome_parlamentar | sexo_parlamentar | sigla_partido | uf_parlamentar | email_parlamentar | data_nascimento | endereco_parlamentar | naturalidade | uf_naturalidade | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4606 |  | José Eleonildo Soares | Pinto Itamaraty | Masculino | PSDB |  | pinto.itamaraty@senador.leg.br | 1960-05-10 00:00:00 | Senado Federal Anexo I  25º Andar   | São Luís | MA | 2023 | 1 |
| 4811 | 900.0 | Laércio José de Oliveira | Laércio Oliveira | Masculino | PP | SE | sen.laerciooliveira@senado.leg.br | 1959-04-15 00:00:00 | Senado Federal Anexo 2   Ala Teotônio Vilela Gabinete 09 | Recife | PE | 2024 | 1 |
| 5257 |  | Renzo do Amaral Braz | Renzo Braz | Masculino | PP |  |  | 1980-04-11 00:00:00 |  | Muriaé | MG | 2024 | 1 |
| 5537 | 928.0 | Dário Elias Berger | Dário Berger | Masculino | PSB |  | sen.darioberger@senado.leg.br | 1956-12-07 00:00:00 | Senado Federal Anexo 1  16º Pavimento   | Bom Retiro | SC | 2023 | 1 |
| 5615 |  | Gilberto Piselo do Nascimento | Gilberto Piselo | Masculino | PDT |  |  | 1959-07-04 00:00:00 |  |  |  | 2023 | 1 |
| 5633 |  | Atilio Francisco da Silva | Atilio Francisco | Masculino | REPUBLICANOS |  |  | 1951-08-02 00:00:00 |  | São Caetano do Sul | SP | 2023 | 1 |
| 5639 | 892.0 | Guaracy Batista da Silveira | Guaracy Silveira | Masculino | PP |  | sen.guaracysilveira@senado.leg.br | 1951-01-02 00:00:00 | Senado Federal Anexo 1  6º Pavimento   | São Paulo | SP | 2023 | 1 |
| 5942 | 862.0 | Marcos Ribeiro do Val | Marcos do Val | Masculino | PODEMOS | ES | sen.marcosdoval@senado.leg.br | 1971-06-15 00:00:00 | Senado Federal Anexo 1  18º Pavimento   | Vitória | ES | 2024 | 1 |
| 5986 | 440.0 | Rodolfo Oliveira Nogueira | Rodolfo Nogueira | Masculino | PL | MS | dep.rodolfonogueira@camara.leg.br | 1973-11-24 00:00:00 |  |  |  | 2024 | 1 |
| 5996 | 947.0 | Marcio Diego Fernandes Tavares de Albuquerque | Diego Tavares | Masculino | PP |  | sen.diegotavares@senado.leg.br | 1983-01-15 00:00:00 | Senado Federal Anexo 2   Ala Teotônio Vilela Gabinete 13 | João Pessoa | PB | 2024 | 1 |


## main.partido_senado

**Create statement:**

```sql
CREATE TABLE "partido_senado" (
  codigo_partido BIGINT,
  data_criacao DATE,
  nome VARCHAR,
  sigla VARCHAR,
  year_snapshot BIGINT
);
```

| codigo_partido | data_criacao | nome | sigla | year_snapshot |
| --- | --- | --- | --- | --- |
| 146 | 1900-01-01 00:00:00 | Partido Federalista | PF | 1900 |
| 148 | 1900-01-01 00:00:00 | Partido Humanista Democrático Brasil Solidariedade | PHDBS | 1900 |
| 150 | 1900-01-01 00:00:00 | Partido Nacional do Consumidor | PNC | 1900 |
| 155 | 1900-01-01 00:00:00 | Partido de Representação da Vontade Popular | PRVP | 1900 |
| 163 | 1900-01-01 00:00:00 | Sem Partido | S/Partido | 1900 |
| 94 | 1922-03-25 00:00:00 | Partido Comunista Brasileiro | PCB | 1922 |
| 544 | 1927-01-01 00:00:00 | Partido Liberal | PL | 1927 |
| 500 | 1928-03-03 00:00:00 | Partido Libertador | PL_RS | 1928 |
| 248 | 1930-01-01 00:00:00 | Partido Republicano | PR | 1930 |
| 531 | 1930-01-01 00:00:00 | Partido Nacional | PNAC | 1930 |


## main.partidos_camara

**Create statement:**

```sql
CREATE TABLE "partidos_camara" (
  id_partido BIGINT,
  nome VARCHAR,
  sigla VARCHAR,
  uri VARCHAR,
  year_snapshot BIGINT
);
```

| id_partido | nome | sigla | uri | year_snapshot |
| --- | --- | --- | --- | --- |
| 36779 | Partido Comunista do Brasil | PCdoB | https://dadosabertos.camara.leg.br/api/v2/partidos/36779 | 0 |
| 36786 | Partido Democrático Trabalhista | PDT | https://dadosabertos.camara.leg.br/api/v2/partidos/36786 | 0 |
| 36832 | Partido Socialista Brasileiro | PSB | https://dadosabertos.camara.leg.br/api/v2/partidos/36832 | 0 |
| 36834 | Partido Social Democrático | PSD | https://dadosabertos.camara.leg.br/api/v2/partidos/36834 | 0 |
| 36835 | Partido da Social Democracia Brasileira | PSDB | https://dadosabertos.camara.leg.br/api/v2/partidos/36835 | 0 |
| 36839 | Partido Socialismo e Liberdade | PSOL | https://dadosabertos.camara.leg.br/api/v2/partidos/36839 | 0 |
| 36844 | Partido dos Trabalhadores | PT | https://dadosabertos.camara.leg.br/api/v2/partidos/36844 | 0 |
| 36851 | Partido Verde | PV | https://dadosabertos.camara.leg.br/api/v2/partidos/36851 | 0 |
| 36886 | Rede Sustentabilidade | REDE | https://dadosabertos.camara.leg.br/api/v2/partidos/36886 | 0 |
| 36896 | Podemos | PODE | https://dadosabertos.camara.leg.br/api/v2/partidos/36896 | 0 |


## main.partidos_lideres_camara

**Create statement:**

```sql
CREATE TABLE "partidos_lideres_camara" (
  id_partido_lider BIGINT,
  id_partido BIGINT,
  cod_titulo VARCHAR,
  data_inicio DATE,
  data_fim DATE,
  id_deputado BIGINT,
  year_snapshot BIGINT
);
```

| id_partido_lider | id_partido | cod_titulo | data_inicio | data_fim | id_deputado | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 36834 | 1001 | 2023-02-01 00:00:00 |  | 160553 | 2023 |
| 2 | 36896 | 1001 | 2025-02-03 00:00:00 |  | 220641 | 2023 |
| 3 | 36898 | 1001 | 2025-05-08 00:00:00 |  | 220703 | 2023 |
| 4 | 36899 | 1001 | 2023-02-01 00:00:00 |  | 204436 | 2023 |
| 5 | 37903 | 1001 | 2023-09-12 00:00:00 |  | 204450 | 2023 |
| 6 | 37904 | 1 | 2024-06-21 00:00:00 |  | 141518 | 2023 |
| 7 | 37908 | 1001 | 2025-02-04 00:00:00 |  | 204491 | 2023 |
| 8 | 37905 | 1007 | 2024-08-01 00:00:00 |  | 178972 | 2024 |
| 9 | 38010 | 1001 | 2024-04-16 00:00:00 |  | 204494 | 2024 |
| 10 | 36779 | 1007 | 2025-02-19 00:00:00 |  | 73801 | 2025 |


## main.partidos_membros_camara

**Create statement:**

```sql
CREATE TABLE "partidos_membros_camara" (
  id_partido_membro BIGINT,
  id_partido BIGINT,
  id_deputado BIGINT,
  id_legislatura INTEGER,
  year_snapshot BIGINT
);
```

| id_partido_membro | id_partido | id_deputado | id_legislatura | year_snapshot |
| --- | --- | --- | --- | --- |
| 1 | 36779 | 230765 |  | 2020 |
| 2 | 36786 | 229082 |  | 2020 |
| 3 | 36832 | 220686 |  | 2020 |
| 4 | 36834 | 228042 |  | 2020 |
| 5 | 36835 | 220683 |  | 2020 |
| 6 | 36839 | 233592 |  | 2020 |
| 7 | 36844 | 231911 |  | 2020 |
| 8 | 36851 | 220697 |  | 2020 |
| 9 | 36886 | 220637 |  | 2020 |
| 10 | 36896 | 233598 |  | 2020 |


## main.processo_senado

**Create statement:**

```sql
CREATE TABLE "processo_senado" (
  id_processo BIGINT,
  codigo_materia BIGINT,
  id_processo_casa_inicial BIGINT,
  identificacao VARCHAR,
  identificacao_processo_inicial VARCHAR,
  identificacao_externa VARCHAR,
  ano INTEGER,
  casa_identificadora VARCHAR,
  sigla_casa_iniciadora VARCHAR,
  sigla_ente_identificador VARCHAR,
  descricao_sigla VARCHAR,
  sigla VARCHAR,
  numero VARCHAR,
  objetivo VARCHAR,
  tramitando VARCHAR,
  id_conteudo BIGINT,
  id_tipo_conteudo BIGINT,
  sigla_tipo_conteudo VARCHAR,
  tipo_conteudo VARCHAR,
  tipo_norma_indicada VARCHAR,
  ementa VARCHAR,
  explicacao_ementa VARCHAR,
  deliberacao_id_destino BIGINT,
  deliberacao_sigla_destino VARCHAR,
  deliberacao_tipo VARCHAR,
  deliberacao_sigla_tipo VARCHAR,
  deliberacao_data DATE,
  deliberacao_destino VARCHAR,
  id_documento BIGINT,
  documento_sigla_tipo VARCHAR,
  documento_tipo VARCHAR,
  documento_indexacao VARCHAR,
  documento_resumo_autoria VARCHAR,
  documento_data_apresentacao DATE,
  documento_data_leitura DATE,
  norma_codigo BIGINT,
  norma_numero VARCHAR,
  norma_sigla_tipo VARCHAR,
  norma_tipo VARCHAR,
  norma_descricao VARCHAR,
  norma_sigla_veiculo VARCHAR,
  norma_veiculo VARCHAR,
  norma_numero_int INTEGER,
  norma_ano_assinatura INTEGER,
  norma_data_assinatura DATE,
  norma_data_publicacao DATE,
  year_snapshot BIGINT
);
```

| id_processo | codigo_materia | id_processo_casa_inicial | identificacao | identificacao_processo_inicial | identificacao_externa | ano | casa_identificadora | sigla_casa_iniciadora | sigla_ente_identificador | descricao_sigla | sigla | numero | objetivo | tramitando | id_conteudo | id_tipo_conteudo | sigla_tipo_conteudo | tipo_conteudo | tipo_norma_indicada | ementa | explicacao_ementa | deliberacao_id_destino | deliberacao_sigla_destino | deliberacao_tipo | deliberacao_sigla_tipo | deliberacao_data | deliberacao_destino | id_documento | documento_sigla_tipo | documento_tipo | documento_indexacao | documento_resumo_autoria | documento_data_apresentacao | documento_data_leitura | norma_codigo | norma_numero | norma_sigla_tipo | norma_tipo | norma_descricao | norma_sigla_veiculo | norma_veiculo | norma_numero_int | norma_ano_assinatura | norma_data_assinatura | norma_data_publicacao | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 502664 | 124528 | 502661 | PLC 215/2015 | PL 546/2003 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 215 | Revisora | Não | 502669 | 11 | NORMA_GERAL | Norma Geral | LEI | Estabelece a inclusão do leite na pauta de produtos amparados pela Política de Garantia de Preços Mínimos - PGPM. | Autoriza o Poder Executivo a incluir o leite na pauta dos produtos amparados pela Política de Garantia de Preços Mínimos – PGPM. Beneficia produtores e suas cooperativas. | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 502670 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | CRIAÇÃO, LEI FEDERAL, INCLUSÃO, LEITE, POLITICA, GARANTIA, PREÇO MINIMO. AGROPECUARIA, ATIVIDADE PECUARIA, PRODUTOR RURAL. | Câmara dos Deputados | 2015-12-17 00:00:00 | 2015-12-18 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 502818 | 124522 | 502815 | PLC 217/2015 | PL 3019/2008 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 217 | Revisora | Não | 502823 | 11 | NORMA_GERAL | Norma Geral | LEI | Acrescenta §§ 1º a 4º ao art. 43 da Lei nº 4.591, de 16 de dezembro de 1964, que dispõe sobre o condomínio em edificações e as incorporações imobiliárias. | Altera a Lei nº 4.591/1964, que dispõe sobre o condomínio em edificações e as incorporações imobiliárias, para fixar multa por mês de atraso na entrega do imóvel, considerando-se retardo excessivo no … | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 502824 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | ALTERAÇÃO, LEI FEDERAL, LEI DOS CONDOMINIOS, INCORPORAÇÃO IMOBILIARIA, ATRASO, ENTREGA, OBRAS, IMOVEL, PAGAMENTO, INDENIZAÇÃO, ALUGUEL. DESTITUIÇÃO, INCORPORADOR. | Câmara dos Deputados | 2015-12-17 00:00:00 | 2015-12-18 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 502857 | 124521 | 502854 | PLC 218/2015 | PL 1611/2011 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 218 | Revisora | Não | 502862 | 11 | NORMA_GERAL | Norma Geral | LEI | Acrescenta o art. 9º-A à Lei nº 7.347, de 24 de julho de 1985, que “disciplina a ação civil pública de responsabilidade por danos causados ao meio-ambiente, ao consumidor, a bens e direitos de valor a… | Altera a Lei 7.347/1985 que disciplina a ação civil pública de responsabilidade por danos causados ao meio-ambiente, ao consumidor, a bens e direitos de valor artístico, estético, histórico, turístico… | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 502863 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | ALTERAÇÃO, LEI FEDERAL, LEI DOS INTERESSES DIFUSOS, AÇÃO CIVIL PUBLICA, RECURSO, RECLAMAÇÃO, ATO, DECISÃO, MINISTERIO PUBLICO, INQUERITO. | Câmara dos Deputados | 2015-12-17 00:00:00 | 2015-12-18 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 502935 | 124515 | 502932 | PLC 216/2015 | PL 4642/2004 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 216 | Revisora | Não | 502940 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera o art. 1º da Lei 8.989, de 24 de fevereiro de 1995. | Altera a Lei 8.989/95, que dispõe sobre a isenção do IPI na aquisição de automóveis para utilização no transporte autônomo de passageiros, bem como por pessoas portadoras de deficiência física, para e… | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 502941 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | ALTERAÇÃO, LEI FEDERAL, LEGISLAÇÃO TRIBUTARIA, TRIBUTAÇÃO, TRIBUTOS, IMPOSTOS, ISENÇÃO FISCAL, BENEFICIO FISCAL, INCENTIVO FISCAL, DESONERAÇÃO TRIBUTARIA, (IPI), INCLUSÃO, VEICULO AUTOMOTOR, AUTOMOVEL… | Câmara dos Deputados | 2015-12-17 00:00:00 | 2015-12-18 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 503091 | 124412 | 503088 | PLC 207/2015 | PL 1511/2011 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 207 | Revisora | Não | 503096 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 10.962, de 11 de outubro de 2004, para aditar formas de afixação de preço de bens e serviços para o consumidor. | Altera a Lei nº 10.962/2004 para determinar que além do preço à vista referente à embalagem oferecida, deve ser afixado o preço à vista proporcional a uma unidade, um metro, um metro quadrado, um quil… | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 503097 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | ALTERAÇÃO, LEI FEDERAL, DEFESA DO CONSUMIDOR, APRESENTAÇÃO, PREÇO, PRODUTO, SERVIÇO. | Câmara dos Deputados | 2015-12-10 00:00:00 | 2015-12-10 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 503130 | 124410 | 503127 | PLC 206/2015 | PL 540/2011 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 206 | Revisora | Não | 503135 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a redação dos arts. 5º e 14 da Lei nº 1.060, de 5 de fevereiro de 1950, que “estabelece normas para a concessão de assistência judiciária aos necessitados”. | Altera a Lei nº 1.060/50, que estabelece normas para a concessão de assistência judiciária aos necessitados. Aumenta o valor da multa aos profissionais que se omitirem às designações da autoridade jud… | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 503136 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | ALTERAÇÃO, LEI FEDERAL, DIREITO CIVIL, ASSISTENCIA JURIDICA, ASSISTENCIA JURIDICA GRATUITA, DEFENSOR PUBLICO, DEFENSORIA PUBLICA, ADVOGADO, (OAB). | Câmara dos Deputados | 2015-12-10 00:00:00 | 2015-12-10 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 503208 | 124344 | 503205 | PLC 201/2015 | PL 2517/1996 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 201 | Revisora | Não | 503213 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera o art. 10 da Lei nº 11.540, de 12 de novembro de 2007, que dispõe sobre o Fundo Nacional de Desenvolvimento Científico e Tecnológico – FNDCT. | Altera a Lei nº 11.540/2007, que dispõe sobre o Fundo Nacional de Desenvolvimento Científico e Tecnológico – FNDCT, para destinar-lhe 1% (um por cento) da arrecadação bruta dos concursos de prognóstic… | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 503214 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | ALTERAÇÃO, LEI FEDERAL, FUNDO FINANCEIRO, (FNDCT), CIENCIA E TECNOLOGIA, ARRECADAÇÃO, RECEITA, LOTERIA FEDERAL, CONCURSO DE PROGNOSTICO. | Câmara dos Deputados | 2015-12-04 00:00:00 | 2015-12-07 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 503286 | 124341 | 503283 | PLC 202/2015 | PL 2805/2008 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 202 | Revisora | Não | 503291 | 11 | NORMA_GERAL | Norma Geral | LEI | Dispõe sobre a publicidade das informações relativas aos fundos que especifica. | Dispõe que o Poder Executivo manterá atualizadas e disponíveis para consulta pública, pela rede mundial de computadores, todas as informações relativas à gestão dos recursos do Fundo Partidário, do Fu… | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 503292 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | CRIAÇÃO, LEI FEDERAL, INFORMAÇÕES, PUBLICIDADE, (INTERNET), TRANSPARENCIA ADMINISTRATIVA, FUNDO FINANCEIRO, FUNDO PARTIDARIO, (FAT), (FUNDEB), (FNS), (FNE), (FNO), (FCO). | Câmara dos Deputados | 2015-12-03 00:00:00 | 2015-12-07 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 503403 | 124294 | 503400 | PLC 197/2015 | PL 1446/2011 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 197 | Revisora | Não | 503408 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 6.888, de 10 de dezembro de 1980. | Altera a Lei nº  6.888/80, que dispõe sobre o exercício da profissão de Sociólogo, para estabelecer a competência exclusiva para o ensino da Sociologia aos licenciados em Sociologia, Sociologia Políti… | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 503409 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | ALTERAÇÃO, LEI FEDERAL, REGULAMENTAÇÃO, PROFISSÃO, SOCIOLOGO, LIMITAÇÃO, FORMAÇÃO, PROFESSOR, SOCIOLOGIA, CIENCIAS SOCIAIS. | Câmara dos Deputados | 2015-12-02 00:00:00 | 2015-12-07 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |
| 503442 | 124293 | 503439 | PLC 196/2015 | PL 331/2007 | {} | 2015 | SF | CD | SF | Projeto de Lei da Câmara | PLC | 196 | Revisora | Não | 503447 | 11 | NORMA_GERAL | Norma Geral | LEI | Institui no âmbito da administração pública federal a Semana da Consciência Negra, a ser realizada, anualmente, no mês de novembro, na semana em que recair o dia 20 de novembro, Dia Nacional de Zumbi … | Institui no âmbito da administração pública federal a Semana da Consciência Negra, que será dedicada ao desenvolvimento de ações educativas acerca da situação socioeconômica da população negra em noss… | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 00:00:00 | Ao arquivo | 503448 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | CRIAÇÃO, LEI FEDERAL, SEMANA, NOVEMBRO, DIA NACIONAL, NEGRO, QUILOMBOS, ZUMBI DOS PALMARES, ATIVIDADE, EDUCAÇÃO. | Câmara dos Deputados | 2015-12-02 00:00:00 | 2015-12-07 00:00:00 |  |  |  |  |  |  |  |  |  |  |  | 2015 |


## main.processos_relacionados_senado

**Create statement:**

```sql
CREATE TABLE "processos_relacionados_senado" (
  id_processo_relacionado BIGINT,
  id_processo BIGINT,
  id_outro_processo BIGINT,
  ano INTEGER,
  casa_identificadora VARCHAR,
  ente_identificador VARCHAR,
  sigla VARCHAR,
  numero VARCHAR,
  sigla_ente_identificador VARCHAR,
  tipo_relacao VARCHAR,
  tramitando VARCHAR,
  year_snapshot BIGINT
);
```

| id_processo_relacionado | id_processo | id_outro_processo | ano | casa_identificadora | ente_identificador | sigla | numero | sigla_ente_identificador | tipo_relacao | tramitando | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2978567 | 3230984 | 2012 | SF | Plenário do Senado Federal | RQS | 482 | PLEN | REFERENCIA | Não | 2007 |
| 2 | 2968939 | 3219261 | 2013 | SF | Plenário do Senado Federal | RQS | 597 | PLEN | REFERENCIA | Não | 2008 |
| 3 | 2970890 | 3219261 | 2013 | SF | Plenário do Senado Federal | RQS | 597 | PLEN | REFERENCIA | Não | 2008 |
| 4 | 1035192 | 2910736 | 2009 | SF | Plenário do Senado Federal | RQS | 1490 | PLEN | REFERENCIA | Não | 2009 |
| 5 | 2965245 | 3232356 | 2012 | SF | Plenário do Senado Federal | RQS | 354 | PLEN | REFERENCIA | Não | 2009 |
| 6 | 3021092 | 3252893 | 2009 | SF | Plenário do Senado Federal | RQS | 1596 | PLEN | REFERENCIA | Não | 2009 |
| 7 | 3333348 | 8063644 | 2021 | CN | Plenário do Congresso Nacional | RQN | 26 | PLEN | REFERENCIA | Não | 2009 |
| 8 | 2958548 | 7737207 | 2019 | SF | Plenário do Senado Federal | RQS | 233 | PLEN | REFERENCIA | Não | 2010 |
| 9 | 2958841 | 3220169 | 2013 | SF | Plenário do Senado Federal | RQS | 478 | PLEN | REFERENCIA | Não | 2010 |
| 10 | 3020085 | 8315340 | 2022 | SF | Comissão de Ciência, Tecnologia, Inovação, Comunicação e Informática | REQ | 34 | CCT | REFERENCIA | Não | 2010 |


## main.proposicoes_camara

**Create statement:**

```sql
CREATE TABLE "proposicoes_camara" (
  id_proposicao BIGINT,
  sigla_tipo VARCHAR,
  numero INTEGER,
  ano INTEGER,
  ementa VARCHAR,
  uri VARCHAR,
  year_snapshot BIGINT
);
```

| id_proposicao | sigla_tipo | numero | ano | ementa | uri | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 15009 | PL | 70 | 1995 | Dispõe sobre intervenções cirúrgicas que visem à alteração de sexo e dá outras providências. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/15009 | 2020 |
| 15532 | PL | 505 | 1991 | Revoga a alínea "l" do art. 20 do Decreto-lei nº 73, de 21 de novembro de 1966, extinguindo o Seguro Obrigatório de Veículos Automotores | https://dadosabertos.camara.leg.br/api/v2/proposicoes/15532 | 2020 |
| 15749 | PL | 693 | 1999 | Altera a Lei nº 8.245, de 18 de outubro de 1991, Lei do Inquilinato, nos dispositivos que menciona. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/15749 | 2020 |
| 15990 | PL | 887 | 1991 | Cria salvaguardas para a tecnologia no campo nuclear.  (AUTOR: Comissão Parlamentar Mista de Inquérito Destinada a Apurar o Programa Nuclear Paralelo) | https://dadosabertos.camara.leg.br/api/v2/proposicoes/15990 | 2020 |
| 16481 | PL | 1258 | 1995 | Disciplina o inciso XII do art. 5º da Constituição Federal e dá outras providências. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/16481 | 2020 |
| 16969 | PL | 1610 | 1996 | Dispõe sobre a exploração e o aproveitamento de recursos minerais em terras indígenas, de que tratam os arts. 176, parágrafo 1º, e 231, parágrafo 3º, da Constituição Federal. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/16969 | 2020 |
| 17563 | PL | 2051 | 1996 | Dispõe sobre a assistência médica, hospitalar e educacional gratuita aos ex-combatentes e a seus dependentes, prevista no inciso IV do artigo 53 do Ato das Disposições Constitucionais Transitórias. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/17563 | 2020 |
| 17823 | PL | 2231 | 1999 | Obriga os responsáveis por "sites" provedores de informações na Internet a fornecer classificação indicativa do conteúdo veiculado. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/17823 | 2020 |
| 17915 | PL | 2295 | 2000 | Dispõe sobre a jornada de trabalho dos Enfermeiros, Técnicos e Auxiliares de Enfermagem. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/17915 | 2020 |
| 18420 | PL | 2639 | 2000 | Dispõe sobre a atividade de curta duração em propriedades rurais. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/18420 | 2020 |


## main.providencias_senado

**Create statement:**

```sql
CREATE TABLE "providencias_senado" (
  id_processo BIGINT,
  id_despacho BIGINT,
  id_providencia BIGINT,
  descricao VARCHAR,
  tipo VARCHAR,
  analise_conteudo VARCHAR,
  analise_tempo VARCHAR,
  ordem INTEGER,
  reexame VARCHAR,
  year_snapshot BIGINT
);
```

| id_processo | id_despacho | id_providencia | descricao | tipo | analise_conteudo | analise_tempo | ordem | reexame | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 663587 | 7806929 | 7568428 | Análise | ANALISE |  | SUCESSIVA | 1 | Não | 2005 |
| 1066060 | 7889688 | 7699479 | Análise | ANALISE | MATERIA | SUCESSIVA | 1 | Não | 2007 |
| 2978567 | 7938573 | 7739359 | Análise | ANALISE | MATERIA | SUCESSIVA | 1 | Não | 2007 |
| 2968939 | 7936023 | 7736261 | Análise | ANALISE | MATERIA | SUCESSIVA | 1 | Não | 2008 |
| 2970890 | 7812982 | 7592137 | Análise | ANALISE |  | SUCESSIVA | 2 | Não | 2008 |
| 1035192 | 7804728 | 7560836 | Análise | ANALISE |  | SUCESSIVA | 1 | Não | 2009 |
| 2965245 | 7819608 | 7616321 | Análise | ANALISE |  | SUCESSIVA | 2 | Não | 2009 |
| 3021092 | 7804773 | 7560980 | Análise | ANALISE |  | SUCESSIVA | 1 | Não | 2009 |
| 2958548 | 9175542 | 8277534 | Ao Plenário, nos termos do Ato da Comissão Diretora nº 8, de 2021 | AO_PLENARIO_ATO_8_2021 |  | SUCESSIVA | 1 | Não | 2010 |
| 2958841 | 7812984 | 7592151 | Análise | ANALISE |  | SUCESSIVA | 2 | Não | 2010 |


## main.relacionadas_camara

**Create statement:**

```sql
CREATE TABLE "relacionadas_camara" (
  id_relacionada BIGINT,
  id_proposicao_origem BIGINT,
  id_proposicao_destino BIGINT,
  year_snapshot BIGINT
);
```

| id_relacionada | id_proposicao_origem | id_proposicao_destino | year_snapshot |
| --- | --- | --- | --- |
| 1 | 15009 | 20118 | 2020 |
| 2 | 15532 | 491539 | 2020 |
| 3 | 15749 | 509059 | 2020 |
| 4 | 15990 | 71351 | 2020 |
| 5 | 16481 | 436930 | 2020 |
| 6 | 16969 | 436722 | 2020 |
| 7 | 17563 | 438211 | 2020 |
| 8 | 17823 | 946106 | 2020 |
| 9 | 17915 | 46672 | 2020 |
| 10 | 18420 | 285427 | 2020 |


## main.relatorias_senado

**Create statement:**

```sql
CREATE TABLE "relatorias_senado" (
  id_relatoria BIGINT,
  id_processo BIGINT,
  codigo_materia BIGINT,
  codigo_parlamentar BIGINT,
  codigo_colegiado BIGINT,
  codigo_tipo_colegiado BIGINT,
  sigla_colegiado VARCHAR,
  nome_colegiado VARCHAR,
  autoria_processo VARCHAR,
  identificacao_processo VARCHAR,
  ementa_processo VARCHAR,
  numero_autuacao INTEGER,
  tramitando VARCHAR,
  sigla_casa VARCHAR,
  casa_relator VARCHAR,
  descricao_tipo_relator VARCHAR,
  id_tipo_relator INTEGER,
  descricao_tipo_encerramento VARCHAR,
  forma_tratamento_parlamentar VARCHAR,
  nome_parlamentar VARCHAR,
  nome_completo VARCHAR,
  sigla_partido_parlamentar VARCHAR,
  uf_parlamentar VARCHAR,
  sexo_parlamentar VARCHAR,
  email_parlamentar VARCHAR,
  url_foto_parlamentar VARCHAR,
  url_pagina_parlamentar VARCHAR,
  data_apresentacao_processo TIMESTAMP,
  data_designacao TIMESTAMP,
  data_destituicao TIMESTAMP,
  data_fim_colegiado TIMESTAMP,
  year_snapshot BIGINT
);
```

| id_relatoria | id_processo | codigo_materia | codigo_parlamentar | codigo_colegiado | codigo_tipo_colegiado | sigla_colegiado | nome_colegiado | autoria_processo | identificacao_processo | ementa_processo | numero_autuacao | tramitando | sigla_casa | casa_relator | descricao_tipo_relator | id_tipo_relator | descricao_tipo_encerramento | forma_tratamento_parlamentar | nome_parlamentar | nome_completo | sigla_partido_parlamentar | uf_parlamentar | sexo_parlamentar | email_parlamentar | url_foto_parlamentar | url_pagina_parlamentar | data_apresentacao_processo | data_designacao | data_destituicao | data_fim_colegiado | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7701594 | 663587 | 73682 | 53 | 834 | 21 | CDH | Comissão de Direitos Humanos e Legislação Participativa | Senador Paulo Paim (PT/RS) | PLS 169/2005 | Altera dispositivo da Lei nº 10.741, de 1º de outubro de 2003, que dispõe sobre o Estatuto do Idoso e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Redistribuição | Senador | Leomar Quintanilha | Leomar de Melo Quintanilha | MDB | TO | M | leomar@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador53.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/53 | 2005-05-12 00:00:00 | 2005-05-17 00:00:00 | 2006-05-24 00:00:00 |  | 2005 |
| 7692977 | 663587 | 73682 | 3 | 834 | 21 | CDH | Comissão de Direitos Humanos e Legislação Participativa | Senador Paulo Paim (PT/RS) | PLS 169/2005 | Altera dispositivo da Lei nº 10.741, de 1º de outubro de 2003, que dispõe sobre o Estatuto do Idoso e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Redistribuição | Senador | Antonio Carlos Valadares | Antonio Carlos Valadares | PSB | SE | M | antoniocarlosvaladares@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3 | 2005-05-12 00:00:00 | 2006-05-31 00:00:00 | 2007-02-07 00:00:00 |  | 2006 |
| 7698040 | 663587 | 73682 | 345 | 834 | 21 | CDH | Comissão de Direitos Humanos e Legislação Participativa | Senador Paulo Paim (PT/RS) | PLS 169/2005 | Altera dispositivo da Lei nº 10.741, de 1º de outubro de 2003, que dispõe sobre o Estatuto do Idoso e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Parecer Oferecido | Senador | Flávio Arns | Flávio José Arns | PT | PR | M | sen.flavioarns@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador345.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/345 | 2005-05-12 00:00:00 | 2007-04-26 00:00:00 | 2007-05-10 00:00:00 |  | 2007 |
| 7698764 | 663587 | 73682 | 3393 | 834 | 21 | CDH | Comissão de Direitos Humanos e Legislação Participativa | Senador Paulo Paim (PT/RS) | PLS 169/2005 | Altera dispositivo da Lei nº 10.741, de 1º de outubro de 2003, que dispõe sobre o Estatuto do Idoso e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Substituído por "ad hoc" | Senador | Papaléo Paes | João Bosco Papaléo Paes | PSDB | AP | M | gab.papaleopaes@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3393.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3393 | 2005-05-12 00:00:00 | 2007-02-08 00:00:00 | 2007-04-26 00:00:00 |  | 2007 |
| 7692575 | 2970890 | 86332 | 3372 | 40 | 21 | CAS | Comissão de Assuntos Sociais | Senador Alvaro Dias (PSDB/PR) | PLS 260/2008 | Altera o § 1º do art. 12 da Lei nº 8.212, de 24 de julho de 1991, e o § 1º do art. 11 da Lei nº 8.213, de 24 de julho de 1991, acrescentando-lhe § 6º, para permitir a contratação eventual de empregado… | 1 | N | SF | SF | Relator | 1 | Fim de Legislatura | Senador | Valdir Raupp | Valdir Raupp de Matos | MDB | RO | M | valdir.raupp@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3372.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3372 | 2008-07-01 00:00:00 | 2008-12-03 00:00:00 | 2010-12-22 00:00:00 |  | 2008 |
| 7693176 | 2970890 | 86332 | 4774 | 1307 | 21 | CRA | Comissão de Agricultura e Reforma Agrária | Senador Alvaro Dias (PSDB/PR) | PLS 260/2008 | Altera o § 1º do art. 12 da Lei nº 8.212, de 24 de julho de 1991, e o § 1º do art. 11 da Lei nº 8.213, de 24 de julho de 1991, acrescentando-lhe § 6º, para permitir a contratação eventual de empregado… | 1 | N | SF | SF | Relator Ad hoc | 3 | Parecer Oferecido | Senador | João Pedro | João Pedro Gonçalves da Costa | PT | AM | M | joaopedro@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador4774.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/4774 | 2008-07-01 00:00:00 | 2008-11-12 00:00:00 | 2008-11-26 00:00:00 |  | 2008 |
| 7694148 | 2970890 | 86332 | 3432 | 1307 | 21 | CRA | Comissão de Agricultura e Reforma Agrária | Senador Alvaro Dias (PSDB/PR) | PLS 260/2008 | Altera o § 1º do art. 12 da Lei nº 8.212, de 24 de julho de 1991, e o § 1º do art. 11 da Lei nº 8.213, de 24 de julho de 1991, acrescentando-lhe § 6º, para permitir a contratação eventual de empregado… | 1 | N | SF | SF | Relator | 1 | Substituído por "ad hoc" | Senador | Augusto Botelho | Augusto Affonso Botelho Neto | PT | RR | M | augusto.botelho@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3432.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3432 | 2008-07-01 00:00:00 | 2008-07-08 00:00:00 | 2008-11-12 00:00:00 |  | 2008 |
| 7690304 | 1035192 | 90433 | 3579 | 1363 | 21 | CCT | Comissão de Ciência, Tecnologia, Inovação e Informática | Câmara dos Deputados | PDS 181/2009 | Aprova o ato que outorga permissão à RÁDIO E TV FAROL DA COMUNICAÇÃO LTDA. para explorar serviço de radiodifusão sonora em frequência modulada na cidade de Turilândia, Estado do Maranhão. | 1 | N | SF | SF | Relator | 1 | Deliberação da matéria | Senador | Lobão Filho | Edison Lobão Filho | MDB | MA | M | lobaofilho@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3579.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3579 | 2009-04-14 00:00:00 | 2009-04-28 00:00:00 | 2009-11-04 00:00:00 |  | 2009 |
| 7689207 | 2965245 | 91380 | 3396 | 34 | 21 | CCJ | Comissão de Constituição, Justiça e Cidadania | Senador Alvaro Dias (PSDB/PR) | PLS 230/2009 | Altera a Lei Complementar nº 101, de 4 de maio de 2000, que estabelece normas de finanças públicas voltadas para a responsabilidade na gestão fiscal e dá outras providências, para exigir compensações … | 1 | N | SF | SF | Relator | 1 | Fim de Legislatura | Senador | Tasso Jereissati | Tasso Ribeiro Jereissati | PSDB | CE | M | sen.tassojereissati@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3396.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3396 | 2009-06-01 00:00:00 | 2009-06-09 00:00:00 | 2010-12-22 00:00:00 |  | 2009 |
| 7690666 | 2968939 | 88039 | 73 | 34 | 21 | CCJ | Comissão de Constituição, Justiça e Cidadania | Senador Paulo Paim (PT/RS) | PLS 413/2008 | Altera a Lei Nº 8.213 de 24 de junho de 1991, que dispõe sobre os Planos de Benefícios da Previdência Social e dá outras providências, para concessão de aposentadoria especial ao segurado que tiver tr… | 1 | N | SF | SF | Relator | 1 | Fim de Legislatura | Senador | Romero Jucá | Romero Jucá Filho | MDB | RR | M | romero.juca@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador73.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/73 | 2008-11-03 00:00:00 | 2009-04-07 00:00:00 | 2010-12-22 00:00:00 |  | 2009 |


## main.situacoes_senado

**Create statement:**

```sql
CREATE TABLE "situacoes_senado" (
  id_situacao BIGINT,
  id_processo BIGINT,
  numero_autuacao INTEGER,
  id_tipo_situacao INTEGER,
  sigla_situacao VARCHAR,
  descricao_situacao VARCHAR,
  data_inicio DATE,
  data_fim DATE,
  year_snapshot BIGINT
);
```

| id_situacao | id_processo | numero_autuacao | id_tipo_situacao | sigla_situacao | descricao_situacao | data_inicio | data_fim | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 | 1 | 48 | RVGA | REVOGADA | 2024-11-21 00:00:00 |  | 2001 |
| 2 | 663587 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 00:00:00 |  | 2005 |
| 3 | 1066060 | 1 | 43 | PRJDA | PREJUDICADA | 2021-09-20 00:00:00 |  | 2007 |
| 4 | 2978567 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 00:00:00 | 2025-08-14 00:00:00 | 2007 |
| 5 | 2968939 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 00:00:00 | 2025-07-10 00:00:00 | 2008 |
| 6 | 2970890 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 00:00:00 | 2025-07-22 00:00:00 | 2008 |
| 7 | 1035192 | 1 | 64 | TNJR | TRANSFORMADA EM NORMA JURÍDICA | 2022-04-14 00:00:00 |  | 2009 |
| 8 | 2965245 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 00:00:00 |  | 2009 |
| 9 | 3021092 | 1 | 64 | TNJR | TRANSFORMADA EM NORMA JURÍDICA | 2022-08-05 00:00:00 |  | 2009 |
| 10 | 3333348 | 1 | 184 | VETDELIB | VETO DELIBERADO PELO PLENÁRIO | 2021-04-19 00:00:00 |  | 2009 |


## main.temas_camara

**Create statement:**

```sql
CREATE TABLE "temas_camara" (
  id_tema BIGINT,
  descricao VARCHAR
);
```

| id_tema | descricao |
| --- | --- |
| 34 | Administração Pública |
| 35 | Arte, Cultura e Religião |
| 37 | Comunicações |
| 39 | Esporte e Lazer |
| 40 | Economia |
| 41 | Cidades e Desenvolvimento Urbano |
| 42 | Direito Civil e Processual Civil |
| 43 | Direito Penal e Processual Penal |
| 44 | Direitos Humanos e Minorias |
| 46 | Educação |


## main.tipo_colegiado_senado

**Create statement:**

```sql
CREATE TABLE "tipo_colegiado_senado" (
  codigo_tipo_colegiado BIGINT,
  codigo_natureza_colegiado BIGINT,
  descricao_tipo_colegiado VARCHAR,
  indicador_ativo VARCHAR,
  sigla_casa VARCHAR,
  sigla_tipo_colegiado VARCHAR,
  year_snapshot BIGINT
);
```

| codigo_tipo_colegiado | codigo_natureza_colegiado | descricao_tipo_colegiado | indicador_ativo | sigla_casa | sigla_tipo_colegiado | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | 1 | Comissão Permanente | S | SF | PERMANENTE | 2023 |
| 121 | 2 | Comissão Temporária Externa | S | SF | CT | 2025 |


## main.tipo_conteudo_senado

**Create statement:**

```sql
CREATE TABLE "tipo_conteudo_senado" (
  id_tipo_conteudo BIGINT,
  sigla_tipo_conteudo VARCHAR,
  descricao_tipo_conteudo VARCHAR,
  tipo_norma_indicada VARCHAR,
  year_snapshot BIGINT
);
```

| id_tipo_conteudo | sigla_tipo_conteudo | descricao_tipo_conteudo | tipo_norma_indicada | year_snapshot |
| --- | --- | --- | --- | --- |
| 11 | NORMA_GERAL | Norma Geral | LEI | 2024 |
| 167 | SUSTACAO_ATO_PODER_EXECUTIVO | Sustação de ato do Poder Executivo | DLG | 2024 |
| 164 | CONCESSAO_SERVICO_TELECOM | Concessão/renovação de serviços de telecomunicação | DLG | 2023 |
| 3010 | NAOCAT_NORMA_JURIDICA | Norma Jurídica - não categorizada | DLG | 2020 |
| 168 | FIXACAO_SUBSIDIO | Fixação de subsídios | DLG | 2022 |
| 989 | ZELAR_COMPETENCIA_LEG_CN | Zelar pela preservação da competência legislativa do Congresso Nacional | DLG | 2018 |
| 1041 | RCCN | Regimento Comum do Congresso Nacional e Normas Conexas | RSF | 2022 |
| 162 | RISF | Regimento Interno do Senado Federal e Normas Conexas | RSF | 2023 |
| 363 | GRUPO_FRENTE_PARLAMENTAR | Grupos e frentes parlamentares |  | 2024 |
| 362 | HONORIFICO | Homenagens, diplomas, condecorações, premiações e comemorações | RSF | 2023 |


## main.tipo_deliberacao_senado

**Create statement:**

```sql
CREATE TABLE "tipo_deliberacao_senado" (
  sigla_tipo_deliberacao VARCHAR,
  descricao_tipo_deliberacao VARCHAR,
  id_destino BIGINT,
  sigla_destino VARCHAR,
  destino VARCHAR,
  year_snapshot BIGINT
);
```

| sigla_tipo_deliberacao | descricao_tipo_deliberacao | id_destino | sigla_destino | destino | year_snapshot |
| --- | --- | --- | --- | --- | --- |
| ARQUIVADO_FIM_LEGISLATURA | Arquivada ao final da Legislatura (art. 332 do RISF) | 4.0 | ARQUIVO | Ao arquivo | 2022 |
| REJEITADO_COMISSAO_TERM | Rejeitada por Comissão em decisão terminativa (art. 91, § 5º, do RISF) | 4.0 | ARQUIVO | Ao arquivo | 2023 |
| APROVADA_NO_PLENARIO | Aprovada pelo Plenário | 1.0 | CAMARA | À Câmara dos Deputados | 2024 |
| APROVADA_EM_COMISSAO_TERMINATIVA | Aprovada por Comissão em decisão terminativa | 1.0 | CAMARA | À Câmara dos Deputados | 2024 |
| PREJUDICADO | Prejudicada | 4.0 | ARQUIVO | Ao arquivo | 2024 |
| RETIRADO_PELO_AUTOR | Retirada pelo autor | 4.0 | ARQUIVO | Ao arquivo | 2024 |
| DEFERIDO_CDIR | Deferida pela Comissão Diretora | 4.0 | ARQUIVO | Ao arquivo | 2024 |
| CONHECIDA | Conhecida | 4.0 | ARQUIVO | Ao arquivo | 2024 |
| TRANSF_PROJ_DECRETO_LEG | Transformada em Projeto de Decreto Legislativo |  |  |  | 2023 |
| INADIMITIDA_MATE | Inadmitida |  |  |  | 2023 |


## main.tipo_emendas_senado

**Create statement:**

```sql
CREATE TABLE "tipo_emendas_senado" (
  tipo_emenda VARCHAR,
  year_snapshot BIGINT
);
```

| tipo_emenda | year_snapshot |
| --- | --- |
| EMENDA_PARCIAL | 2024 |
| EMENDA_TOTAL | 2024 |


## main.tramitacoes_camara

**Create statement:**

```sql
CREATE TABLE "tramitacoes_camara" (
  id_tramitacao BIGINT,
  id_proposicao BIGINT,
  ambito VARCHAR,
  apreciacao VARCHAR,
  cod_situacao VARCHAR,
  cod_tipo_tramitacao VARCHAR,
  data_hora TIMESTAMP,
  descricao_situacao VARCHAR,
  descricao_tramitacao VARCHAR,
  despacho VARCHAR,
  regime VARCHAR,
  sequencia INTEGER,
  sigla_orgao VARCHAR,
  uri_orgao VARCHAR,
  uri_ultimo_relator VARCHAR,
  year_snapshot BIGINT
);
```

| id_tramitacao | id_proposicao | ambito | apreciacao | cod_situacao | cod_tipo_tramitacao | data_hora | descricao_situacao | descricao_tramitacao | despacho | regime | sequencia | sigla_orgao | uri_orgao | uri_ultimo_relator | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 15009 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 70/1995 nos termos do art. 105 do RICD, desapense-se do PL 70/1995 o PL 2976/2008, o PL 1281/2011, o PL 4241/2012, o PL 4870/2016 e o PL 2232/2020, e, em seguida, apense-o… | Prioridade (Art. 151, II, RICD) | 52 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/73654 | 2020 |
| 2 | 15532 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 505/1991 nos termos do art. 105 do RICD, desapense-se do PL 505/1991 o PL 5448/2005, o PL 1982/2007, o PL 3484/2008, o PL 6185/2009, o PL 7087/2010, o PL 7362/2010, o PL 7… | Ordinário (Art. 151, III, RICD) | 215 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/73463 | 2020 |
| 3 | 15749 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 693/1999 nos termos do art. 105 do RICD, desapense-se do PL 693/1999 o PL 7174/2014, o PL 7412/2014, o PL 7842/2017, o PL 9134/2017, o PL 5975/2019, o PL 5327/2020 e o PL … | Ordinário (Art. 151, III, RICD) | 178 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/116379 | 2020 |
| 4 | 15990 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 502 | 2023-01-31 00:00:00 | Arquivada | Arquivamento | Arquivado nos termos do Artigo 105 do Regimento Interno da Câmara dos Deputados. | Especial (Arts. 142 e 143, RCCN) | 40 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/98057 | 2020 |
| 5 | 16481 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 1258/1995 nos termos do art. 105 do RICD, desapense-se do PL 1258/1995 o PL 195/2003, o PL 2114/2003, o PL 4323/2004, o PL 43/2007, o PL 432/2007, o PL 1303/2007, o PL 144… | Prioridade (Art. 151, II, RICD) | 147 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/73460 | 2020 |
| 6 | 16969 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 1610/1996 nos termos do art. 105 do RICD, desapense-se do PL 1610/1996 o PL 5265/2009, o PL 3509/2015, o PL 5335/2016, o PL 4447/2019 e o PL 1737/2020, e, em seguida, apen… | Prioridade (Art. 151, II, RICD) | 176 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/141417 | 2020 |
| 7 | 17563 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 2051/1996 nos termos do art. 105 do RICD, desapense-se o PL 4785/2009 do PL 2051/1996. Em decorrência disso, distribua-se o PL 4785/2009 às comissões de Relações Exteriore… | Prioridade (Art. 151, II, RICD) | 174 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/159237 | 2020 |
| 8 | 17823 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II |  | 1010 | 2020-01-10 00:00:00 |  | Devolução à CCP | Devolução à CCP | Ordinário (Art. 151, III, RICD) | 113 | CSAUDE | https://dadosabertos.camara.leg.br/api/v2/orgaos/2014 | https://dadosabertos.camara.leg.br/api/v2/deputados/164360 | 2020 |
| 9 | 17915 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 2295/2000 nos termos do art. 105 do RICD, desapense-se do PL 2295/2000 o PL 1313/2019, o PL 1384/2019 e o PL 1607/2019, e, em seguida, apense-os ao PL 6091/2016. | Urgência (Art. 155, RICD) | 493 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/141451 | 2020 |
| 10 | 18420 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II |  | 1010 | 2020-01-30 00:00:00 |  | Devolução à CCP | Devolução à CCP | Ordinário (Art. 151, III, RICD) | 124 | CSAUDE | https://dadosabertos.camara.leg.br/api/v2/orgaos/2014 | https://dadosabertos.camara.leg.br/api/v2/deputados/178923 | 2020 |


## main.unidades_destinatarias_senado

**Create statement:**

```sql
CREATE TABLE "unidades_destinatarias_senado" (
  id_unidade_destinataria BIGINT,
  id_processo BIGINT,
  id_despacho BIGINT,
  id_providencia BIGINT,
  colegiado_casa VARCHAR,
  colegiado_codigo BIGINT,
  colegiado_nome VARCHAR,
  colegiado_sigla VARCHAR,
  ordem INTEGER,
  tipo_analise_deliberacao VARCHAR,
  year_snapshot BIGINT
);
```

| id_unidade_destinataria | id_processo | id_despacho | id_providencia | colegiado_casa | colegiado_codigo | colegiado_nome | colegiado_sigla | ordem | tipo_analise_deliberacao | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 663587 | 7806929 | 7568428 | SF | 38 | Comissão de Assuntos Econômicos | CAE | 3 | NAO_TERMINATIVA | 2005 |
| 2 | 1066060 | 7889688 | 7699479 | SF | 1363 | Comissão de Ciência, Tecnologia, Inovação e Informática | CCT | 2 | NAO_TERMINATIVA | 2007 |
| 3 | 2978567 | 7938573 | 7739359 | SF | 38 | Comissão de Assuntos Econômicos | CAE | 1 | TERMINATIVA | 2007 |
| 4 | 2968939 | 7936023 | 7736261 | SF | 40 | Comissão de Assuntos Sociais | CAS | 2 | TERMINATIVA | 2008 |
| 5 | 2970890 | 7812982 | 7592137 | SF | 40 | Comissão de Assuntos Sociais | CAS | 4 | NAO_TERMINATIVA | 2008 |
| 6 | 1035192 | 7804728 | 7560836 | SF | 1363 | Comissão de Ciência, Tecnologia, Inovação e Informática | CCT | 1 | TERMINATIVA | 2009 |
| 7 | 2965245 | 7819608 | 7616321 | SF | 38 | Comissão de Assuntos Econômicos | CAE | 8 | NAO_TERMINATIVA | 2009 |
| 8 | 3021092 | 7804773 | 7560980 | SF | 1363 | Comissão de Ciência, Tecnologia, Inovação e Informática | CCT | 1 | TERMINATIVA | 2009 |
| 9 | 2958548 | 9175542 | 8277534 | SF | 1998 | Plenário do Senado Federal | PLEN | 1 | NAO_TERMINATIVA | 2010 |
| 10 | 2958841 | 7812984 | 7592151 | SF | 40 | Comissão de Assuntos Sociais | CAS | 4 | NAO_TERMINATIVA | 2010 |


## main.votacoes_camara

**Create statement:**

```sql
CREATE TABLE "votacoes_camara" (
  id_votacao VARCHAR,
  id_proposicao BIGINT,
  data DATE,
  descricao VARCHAR,
  aprovacao BOOLEAN,
  uri_evento VARCHAR,
  uri_orgao VARCHAR,
  uri VARCHAR,
  year_snapshot BIGINT,
  rn BIGINT
);
```

| id_votacao | id_proposicao | data | descricao | aprovacao | uri_evento | uri_orgao | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1006386-48 | 1006386 | 2018-08-14 00:00:00 | Aprovado o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/53552 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2002 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1006386-48 | 2021 | 1 |
| 1048959-27 | 1048959 | 2015-09-16 00:00:00 | Aprovado por Unanimidade o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/40973 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2001 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1048959-27 | 2020 | 1 |
| 1050804-2 | 14562 | 2015-03-26 00:00:00 | Aprovado, transformado em convite. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/38333 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537363 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1050804-2 | 2023 | 1 |
| 1050852-8 | 581206 | 2015-03-30 00:00:00 | Rejeitado o Requerimento de Urgência (Art. 155 do RICD). Sim: 216; Não: 181; abstenção: 1; total: 398 . | False | https://dadosabertos.camara.leg.br/api/v2/eventos/38389 | https://dadosabertos.camara.leg.br/api/v2/orgaos/180 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1050852-8 | 2021 | 1 |
| 106586-30 | 106586 | 2003-12-10 00:00:00 | Aprovado por Unanimidade o Parecer | True | https://dadosabertos.camara.leg.br/api/v2/eventos/5880 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2004 | https://dadosabertos.camara.leg.br/api/v2/votacoes/106586-30 | 2022 | 1 |
| 106586-71 | 106586 | 2006-05-17 00:00:00 | Aprovado por Unanimidade o Parecer com Complementação de Voto | True | https://dadosabertos.camara.leg.br/api/v2/eventos/12911 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/106586-71 | 2022 | 1 |
| 1116134-23 | 1116134 | 2015-07-15 00:00:00 | Aprovado por Unanimidade o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/40010 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2001 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1116134-23 | 2021 | 1 |
| 113531-50 | 113531 | 2004-08-25 00:00:00 | Aprovado o Parecer, apresentou voto em separado o Deputado Edmar Moreira | True | https://dadosabertos.camara.leg.br/api/v2/eventos/7596 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5503 | https://dadosabertos.camara.leg.br/api/v2/votacoes/113531-50 | 2020 | 1 |
| 114808-39 | 114808 | 2008-10-29 00:00:00 | Aprovado por Unanimidade o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/18966 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2015 | https://dadosabertos.camara.leg.br/api/v2/votacoes/114808-39 | 2021 | 1 |
| 1191094-122 | 1191094 | 2019-09-19 00:00:00 | Aprovada a Redação Final. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/57377 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1191094-122 | 2023 | 1 |


## main.votacoes_senado

**Create statement:**

```sql
CREATE TABLE "votacoes_senado" (
  id_votacao BIGINT,
  id_materia BIGINT,
  id_processo BIGINT,
  identificacao VARCHAR,
  sigla VARCHAR,
  numero VARCHAR,
  ano INTEGER,
  codigo_sessao BIGINT,
  numero_sessao INTEGER,
  sequencial_sessao INTEGER,
  sigla_tipo_sessao VARCHAR,
  casa_sessao VARCHAR,
  codigo_sessao_legislativa BIGINT,
  data_apresentacao TIMESTAMP,
  data_sessao TIMESTAMP,
  descricao_votacao VARCHAR,
  ementa VARCHAR,
  resultado_votacao VARCHAR,
  total_votos_sim INTEGER,
  total_votos_nao INTEGER,
  total_votos_abstencao INTEGER,
  votacao_secreta VARCHAR,
  id_informe BIGINT,
  id_evento BIGINT,
  codigo_colegiado BIGINT,
  nome_colegiado VARCHAR,
  sigla_colegiado VARCHAR,
  data_informe TIMESTAMP,
  texto_informe VARCHAR,
  year_snapshot BIGINT
);
```

| id_votacao | id_materia | id_processo | identificacao | sigla | numero | ano | codigo_sessao | numero_sessao | sequencial_sessao | sigla_tipo_sessao | casa_sessao | codigo_sessao_legislativa | data_apresentacao | data_sessao | descricao_votacao | ementa | resultado_votacao | total_votos_sim | total_votos_nao | total_votos_abstencao | votacao_secreta | id_informe | id_evento | codigo_colegiado | nome_colegiado | sigla_colegiado | data_informe | texto_informe | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5481 | 121994 | 1399048 | PEC 83/2015 | PEC | 83 | 2015 | 22254 | 176 | 3 | DOR | SF | 850 | 2015-06-25 00:00:00 | 2015-10-06 00:00:00 | Votação nominal da Emenda nº 15-CCJ (Substituvivo) | Acrescenta o art. 166-A à Constituição Federal, para dispor sobre a Autoridade Fiscal Independente. |  |  |  |  | N | 1881857 | 9815176 |  |  |  | 2015-10-06 00:00:01 | Anunciada a votação da matéria, em primeiro turno, usam da palavra o Senador José Serra, Relator, e o Senador Delcídio do Amaral; tendo o Relator proposto Adendo ao Substitutivo da CCJ.
A seguir, usam… | 2015 |
| 5554 | 123909 | 3036223 | PEC 143/2015 | PEC | 143 | 2015 | 22507 | 50 | 1 | DOR | SF | 853 | 2015-11-04 00:00:00 | 2016-04-13 00:00:00 | Votação nominal da Emenda nº 1 - CCJ (Substitutivo) com alteração proposta pelo relator à PEC 143/2015, em primeiro turno. Acrescenta os artigos 101 e 102 ao Ato das Disposições Constitucionais Transi… | Acrescenta os arts. 101 e 102 ao Ato das Disposições Constitucionais Transitórias para instituir a desvinculação de receitas dos Estados, do Distrito Federal e dos Municípios. | A |  |  |  | N | 1904012 | 9848989 | 1998.0 | Plenário do Senado Federal | PLEN | 2016-04-13 00:00:01 | (Matéria constante do item 4 da Ordem do Dia, apreciado em 1º lugar, com aquiescência do Plenário)
Anunciada a matéria, usam da palavra os Senadores Randolfe Rodrigues, Reguffe, Lindbergh Farias, Jos… | 2016 |
| 5708 | 128035 | 4985566 | PEC 2/2017 | PEC | 2 | 2017 | 41887 | 75 | 1 | DOR | SF | 854 | 2017-02-08 00:00:00 | 2017-05-30 00:00:00 | Votação que altera o §1º do artigo 31 e o artigo 75 da Constituição Federal para estabelecer os Tribunais de Contas como órgãos permanentes e essenciais ao controle externo da administração pública. | Altera o § 1º do art. 31 e o art. 75 da Constituição Federal para estabelecer os Tribunais de Contas como órgãos permanentes e essenciais ao controle externo da administração pública. |  |  |  |  | N | 1944735 | 9927212 | 1998.0 | Plenário do Senado Federal | PLEN | 2017-05-30 00:00:01 | Aprovada em primeiro turno, com o seguinte resultado: Sim 50, Não 20, Abst. 03, Presidente 1, Total 74.
A matéria constará da Ordem do Dia oportunamente, para o segundo turno constitucional. | 2017 |
| 5960 | 127414 | 3035168 | PEC 57/2016 | PEC | 57 | 2016 | 95294 | 65 | 1 | DOR | SF | 858 | 2016-11-08 00:00:00 | 2019-05-07 00:00:00 | PEC nº 57, de 2016, com as Emendas nºs 1 a 6 - CCJ, nos termos do Parecer (1º Turno) | Altera os arts. 30, 37, 146, 150, 179 e 195 da Constituição Federal para prever que lei complementar conceituará pequeno Município, poderá disciplinar os princípios da Administração Pública e as norma… | A | 68.0 | 0.0 | 0.0 | N | 1940240 | 9917858 | 1998.0 | Plenário do Senado Federal | PLEN | 2019-05-07 00:00:01 | Aprovada a Proposta e as Emendas nºs 1 a 6-CCJ, em primeiro turno, com o seguinte resultado: Sim 68, Presidente 1, Total 69. | 2019 |
| 5965 | 129887 | 5377266 | PEC 26/2017 | PEC | 26 | 2017 | 102966 | 89 | 1 | DOR | SF | 858 | 2017-06-29 00:00:00 | 2019-06-04 00:00:00 | PEC nº 26, de 2017, com a Emenda nº 1 - CCJ, nos termos do Parecer (1º Turno) | Acrescenta o art. 75-A à Constituição Federal, para dispor sobre a criação de um sistema de avaliação de políticas públicas. | A | 55.0 | 0.0 | 0.0 | N | 1960909 | 9956542 | 1998.0 | Plenário do Senado Federal | PLEN | 2019-06-04 00:00:01 | Aprovada a proposta, em primeiro turno, com o seguinte resultado: Sim 55, Presidente 1, Total 56.
A matéria constará da Ordem do Dia oportunamente, para apreciação em segundo turno.
(A PEC é aprovada… | 2019 |
| 6075 | 124513 | 573632 | PLS 796/2015 | PLS | 796 | 2015 | 155306 | 5 | 1 | DOR | SF | 863 | 2015-12-17 00:00:00 | 2020-02-11 00:00:00 | Estende a estabilidade provisória no emprego para as empregadas adotantes ou que venham a obter a guarda judicial para fins de adoção. | Altera a redação do art. 1º da Lei Complementar nº 146, de 25 de junho de 2014, para estender a estabilidade provisória no emprego para as empregadas adotantes ou que venham a obter a guarda judicial … | A |  |  |  | N | 1911617 | 9861624 | 1998.0 | Plenário do Senado Federal | PLEN | 2020-02-11 00:00:01 | Discussão encerrada.
Aprovado o Substitutivo - Emenda nº 1-CCJ, com o seguinte resultado: Sim 69, Não 1, Presidente 1, Total 71; ficando prejudicado o projeto.
Encaminhado à publicação o Parecer nº … | 2020 |
| 6248 | 135147 | 7716769 | PLP 19/2019 | PLP | 19 | 2019 | 199976 | 96 | 2 | SDR | SF | 863 | 2019-02-06 00:00:00 | 2020-11-03 00:00:00 | Votação da Emenda nº 18 - PLEN (Substitutivo) do Relator ao PLP nº 19, de 2019, ressalvado o destaque. | Dispõe sobre nomeação e demissão do Presidente e diretores do Banco Central do Brasil. | A |  |  |  | N | 2041705 | 10130692 | 1998.0 | Plenário do Senado Federal | PLEN | 2020-11-03 22:42:29 | (Sessão Deliberativa Remota realizada em 03/11/2020) 
Encaminhadas à publicação as Emendas nºs 6 a 17 – PLEN. 
Proferido pelo Senador Telmário Mota o Parecer nº 157/2020-PLEN/SF, concluindo pela apr… | 2020 |
| 6249 | 135147 | 7716769 | PLP 19/2019 | PLP | 19 | 2019 | 199976 | 96 | 3 | SDR | SF | 863 | 2019-02-06 00:00:00 | 2020-11-03 00:00:00 | Votação da Emenda nº 12 - PLEN ao Projeto de Lei Complementar nº 19, de 2019, destacada. | Dispõe sobre nomeação e demissão do Presidente e diretores do Banco Central do Brasil. | A |  |  |  | N | 2041705 | 10130692 | 1998.0 | Plenário do Senado Federal | PLEN | 2020-11-03 22:42:29 | (Sessão Deliberativa Remota realizada em 03/11/2020) 
Encaminhadas à publicação as Emendas nºs 6 a 17 – PLEN. 
Proferido pelo Senador Telmário Mota o Parecer nº 157/2020-PLEN/SF, concluindo pela apr… | 2020 |
| 6076 | 139427 | 7826311 | MPV 899/2019 | MPV | 899 | 2019 | 162448 | 23 | 1 | SDR | SF | 863 | 2019-10-17 00:00:00 | 2020-03-24 00:00:00 | Votação do PLV n. 2, de 2020 | Dispõe sobre a transação nas hipóteses que especifica. | A |  |  |  | N | 2026084 | 10080776 |  |  |  | 2020-03-24 00:00:01 | (Sessão Deliberativa Remota)
Aprovado o PLV nº 2, de 2020, sendo impugnado o art. 28. 
À sanção.
(DETALHAMENTO DA AÇÃO LEGISLATIVA)
(Sessão Deliberativa Remota realizada em 24/03/2020)
Encaminhado… | 2020 |
| 6086 | 139736 | 7834698 | MPV 903/2019 | MPV | 903 | 2019 | 167009 | 32 | 1 | SDR | SF | 863 | 2019-11-07 00:00:00 | 2020-04-14 00:00:00 | Votação da Medida Provisória nº 903, de 2019. | Autoriza a prorrogação de contratos por tempo determinado do Ministério da Agricultura, Pecuária e Abastecimento. | A |  |  |  | N | 2035393 | 10100072 |  |  |  | 2020-04-08 00:00:01 | Incluída em ordem do dia da sessão deliberativa remota de 14/04/2020. | 2020 |


## main.votos_camara

**Create statement:**

```sql
CREATE TABLE "votos_camara" (
  id_voto BIGINT,
  id_votacao VARCHAR,
  id_deputado BIGINT,
  tipo_voto VARCHAR,
  data_hora TIMESTAMP,
  year_snapshot INTEGER
);
```

| id_voto | id_votacao | id_deputado | tipo_voto | data_hora | year_snapshot |
| --- | --- | --- | --- | --- | --- |
| 1 | 1049075-6 | 4930 | Sim | 2015-03-24 17:59:46 | 2023 |
| 2 | 1049075-6 | 67312 | Sim | 2015-03-24 17:59:24 | 2023 |
| 3 | 1049075-6 | 69871 | Não | 2015-03-24 17:48:53 | 2023 |
| 4 | 1049075-6 | 72912 | Sim | 2015-03-24 17:59:20 | 2023 |
| 5 | 1049075-6 | 73424 | Sim | 2015-03-24 17:58:38 | 2023 |
| 6 | 1049075-6 | 73434 | Não | 2015-03-24 17:50:58 | 2023 |
| 7 | 1049075-6 | 73441 | Sim | 2015-03-24 18:01:02 | 2023 |
| 8 | 1049075-6 | 73458 | Sim | 2015-03-24 17:57:43 | 2023 |
| 9 | 1049075-6 | 73463 | Sim | 2015-03-24 17:47:30 | 2023 |
| 10 | 1049075-6 | 73466 | Sim | 2015-03-24 17:50:20 | 2023 |


## main.votos_senado

**Create statement:**

```sql
CREATE TABLE "votos_senado" (
  id_voto BIGINT,
  codigo_votacao_sve BIGINT,
  codigo_sessao_votacao BIGINT,
  codigo_materia BIGINT,
  identificacao_materia VARCHAR,
  codigo_parlamentar BIGINT,
  nome_parlamentar VARCHAR,
  sexo_parlamentar VARCHAR,
  sigla_partido_parlamentar VARCHAR,
  sigla_uf_parlamentar VARCHAR,
  sigla_voto_parlamentar VARCHAR,
  descricao_voto_parlamentar VARCHAR,
  year_snapshot BIGINT
);
```

| id_voto | codigo_votacao_sve | codigo_sessao_votacao | codigo_materia | identificacao_materia | codigo_parlamentar | nome_parlamentar | sexo_parlamentar | sigla_partido_parlamentar | sigla_uf_parlamentar | sigla_voto_parlamentar | descricao_voto_parlamentar | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  | 5481 | 121994 | PEC 83/2015 | 4697 | Ângela Portela | F | PT | RR | Sim |  | 2015 |
| 2 |  | 5554 | 123909 | PEC 143/2015 | 4697 | Ângela Portela | F | PT | RR | Sim |  | 2016 |
| 3 |  | 5708 | 128035 | PEC 2/2017 | 4697 | Ângela Portela | F | PDT | RR | Sim |  | 2017 |
| 4 | 2725.0 | 5960 | 127414 | PEC 57/2016 | 3806 | Zequinha Marinho | M | PSC | PA | Sim |  | 2019 |
| 5 | 2778.0 | 5965 | 129887 | PEC 26/2017 | 3806 | Zequinha Marinho | M | PSC | PA | MIS | Missão da Casa no País/exterior | 2019 |
| 6 | 3533.0 | 6075 | 124513 | PLS 796/2015 | 3806 | Zequinha Marinho | M | PSC | PA | Sim |  | 2020 |
| 7 |  | 6248 | 135147 | PLP 19/2019 | 3806 | Zequinha Marinho | M | PSC | PA | AP | Atividade parlamentar | 2020 |
| 8 |  | 6249 | 135147 | PLP 19/2019 | 3806 | Zequinha Marinho | M | PSC | PA | AP | Atividade parlamentar | 2020 |
| 9 |  | 6076 | 139427 | MPV 899/2019 | 3806 | Zequinha Marinho | M | PSC | PA | Sim |  | 2020 |
| 10 |  | 6086 | 139736 | MPV 903/2019 | 3806 | Zequinha Marinho | M | PSC | PA | Sim |  | 2020 |
