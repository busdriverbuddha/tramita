# DuckDB Samples

_Generated on 2025-10-20T16:15:43_


## main.autores_camara

_Query_: `SELECT * FROM "main"."autores_camara" LIMIT 10;`

| id_autor | cod_tipo | uri | ordem_assinatura | proponente | id_proposicao | year | tipo_autor | id_deputado_ou_orgao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 462 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/160655 | 1 | True | 538196 | 2020 | deputados | 160655 |
| 545 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/141488 | 1 | True | 559138 | 2020 | deputados | 141488 |
| 647 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/73584 | 1 | True | 593065 | 2020 | deputados | 73584 |
| 687 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/160518 | 2 | True | 601739 | 2020 | deputados | 160518 |
| 744 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/151208 | 1 | True | 614512 | 2020 | deputados | 151208 |
| 834 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/73466 | 1 | True | 946475 | 2020 | deputados | 73466 |
| 962 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/178862 | 1 | True | 1301128 | 2020 | deputados | 178862 |
| 1017 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/74570 | 1 | True | 1555295 | 2020 | deputados | 74570 |
| 1019 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/160512 | 1 | True | 1555470 | 2020 | deputados | 160512 |
| 1216 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/160565 | 1 | True | 2074843 | 2020 | deputados | 160565 |

## main.autoria_documento_senado

_Query_: `SELECT * FROM "main"."autoria_documento_senado" LIMIT 10;`

| id_autoria_documento | id_processo | id_documento | autor | sigla_tipo | descricao_tipo | ordem | outros_autores_nao_informados | id_ente | sigla_ente | casa_ente | ente | cargo | siglaCargo | partido | sexo | uf | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 | 2526464 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2001 |
| 2 | 663587 | 663593 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2005 |
| 3 | 1066060 | 1066066 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2007 |
| 4 | 2978567 | 2978573 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2007 |
| 5 | 2968939 | 2968945 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2008 |
| 6 | 2970890 | 2970896 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2008 |
| 7 | 1035192 | 1035198 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2009 |
| 8 | 2965245 | 2965251 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2009 |
| 9 | 3021092 | 3021098 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2009 |
| 10 | 3333348 | 3333354 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2009 |

## main.autoria_iniciativa_senado

_Query_: `SELECT * FROM "main"."autoria_iniciativa_senado" LIMIT 10;`

| id_autoria_iniciativa | id_processo | codigo_parlamentar | descricao_tipo | ente | ordem | outros_autores_nao_informados | sigla_ente | sigla_tipo | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 |  | PRESIDENTE_REPUBLICA | Presidência da República | 1 | Não | PR | PRESIDENTE_REPUBLICA | 2001 |
| 2 | 663587 | 825 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2005 |
| 3 | 1066060 |  | COMISSAO_CAMARA | Comissão de Ciência e Tecnologia, Comunicação e Informática | 1 | Não | CCTCI | COMISSAO_CAMARA | 2007 |
| 4 | 2978567 | 825 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2007 |
| 5 | 2968939 | 825 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2008 |
| 6 | 2970890 | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2008 |
| 7 | 1035192 |  | COMISSAO_CAMARA | Comissão de Ciência e Tecnologia, Comunicação e Informática | 1 | Não | CCTCI | COMISSAO_CAMARA | 2009 |
| 8 | 2965245 | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2009 |
| 9 | 3021092 |  | COMISSAO_CAMARA | Comissão de Ciência e Tecnologia, Comunicação e Informática | 1 | Não | CCTCI | COMISSAO_CAMARA | 2009 |
| 10 | 3333348 |  | CAMARA | Câmara dos Deputados | 1 | Não | CD | CAMARA | 2009 |

## main.autuacoes_senado

_Query_: `SELECT * FROM "main"."autuacoes_senado" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."bloco_senado" LIMIT 10;`

| codigo_bloco | data_criacao | nome_apelido | nome_bloco | year_snapshot |
| --- | --- | --- | --- | --- |
| 335 | 2023-02-01 | BLPRD | Bloco Parlamentar da Resistência Democrática | 2023 |
| 337 | 2023-02-03 | Minoria | Minoria | 2023 |
| 346 | 2023-03-20 | BLALIANÇA | Bloco Parlamentar Aliança | 2023 |
| 357 | 2025-02-03 | BLVANG | Bloco Parlamentar Vanguarda | 2025 |
| 358 | 2025-02-18 | BLDEM | Bloco Parlamentar Democracia | 2025 |
| 359 | 2025-02-18 | BLPBR | Bloco Parlamentar Pelo Brasil | 2025 |

## main.blocos_camara

_Query_: `SELECT * FROM "main"."blocos_camara" LIMIT 10;`

| id_bloco | nome | id_legislatura | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- |
| 586 | Federação PSOL REDE | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/586 | 0 | 1 |
| 585 | Federação PSDB CIDADANIA | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/585 | 0 | 1 |
| 590 | AVANTE, SOLIDARIEDADE, PRD | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/590 | 0 | 1 |
| 584 | Federação Brasil da Esperança - Fe Brasil | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/584 | 0 | 1 |
| 589 | PL, UNIÃO, PP, PSD, REPUBLICANOS, MDB, Federação PSDB CIDADANIA, PODE | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/589 | 0 | 1 |

## main.blocos_partidos_camara

_Query_: `SELECT * FROM "main"."blocos_partidos_camara" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."colegiado_senado" LIMIT 10;`

| codigo_colegiado | codigo_tipo_colegiado | data_inicio | indicador_distr_partidaria | nome_colegiado | sigla_colegiado | ordem | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 34 | 21 | 1900-01-01 | S | Comissão de Constituição, Justiça e Cidadania | CCJ | 3 | 1900 |
| 38 | 21 | 1900-01-01 | S | Comissão de Assuntos Econômicos | CAE | 1 | 1900 |
| 40 | 21 | 1900-01-01 | S | Comissão de Assuntos Sociais | CAS | 2 | 1900 |
| 47 | 21 | 1900-01-01 | S | Comissão de Educação e Cultura | CE | 4 | 1900 |
| 50 | 21 | 1900-01-01 | S | Comissão de Meio Ambiente | CMA | 13 | 1900 |
| 54 | 21 | 1900-01-01 | S | Comissão de Relações Exteriores e Defesa Nacional | CRE | 7 | 1900 |
| 59 | 21 | 1900-01-01 | S | Comissão de Serviços de Infraestrutura | CI | 8 | 1900 |
| 834 | 21 | 2002-12-13 | S | Comissão de Direitos Humanos e Legislação Participativa | CDH | 6 | 2002 |
| 1306 | 21 | 2005-02-18 | S | Comissão de Desenvolvimento Regional e Turismo | CDR | 9 | 2005 |
| 1307 | 21 | 2005-02-22 | S | Comissão de Agricultura e Reforma Agrária | CRA | 10 | 2005 |

## main.correspondencia_proposicoes_processo

_Query_: `SELECT * FROM "main"."correspondencia_proposicoes_processo" LIMIT 10;`

| id_proposicao_camara | id_processo_senado | identificacao |
| --- | --- | --- |
| 2190585 | 8006262 | PL 123/2019 |
| 2190598 | 8311169 | PL 130/2019 |
| 2191635 | 8074610 | PL 610/2019 |
| 2192978 | 7858383 | PL 1095/2019 |
| 2193223 | 8070435 | PL 1177/2019 |
| 2193438 | 8135478 | PL 1269/2019 |
| 2193767 | 8011990 | PL 1422/2019 |
| 2194013 | 8070419 | PL 1501/2019 |
| 2195031 | 7827537 | PL 1679/2019 |
| 2195665 | 8072151 | PL 1802/2019 |

## main.deputados_camara

_Query_: `SELECT * FROM "main"."deputados_camara" LIMIT 10;`

| id_deputado | nome_civil | uri | year_snapshot | rn | tag |
| --- | --- | --- | --- | --- | --- |
| 62926 | REINALDO SANTOS E SILVA | https://dadosabertos.camara.leg.br/api/v2/deputados/62926 | 2020 | 1 | CD:62926 |
| 66828 | FAUSTO RUY PINATO | https://dadosabertos.camara.leg.br/api/v2/deputados/66828 | 2020 | 1 | CD:66828 |
| 73439 | Carlos Nelson Bueno | https://dadosabertos.camara.leg.br/api/v2/deputados/73439 | 2023 | 1 | CD:73439 |
| 73463 | OSMAR JOSÉ SERRAGLIO | https://dadosabertos.camara.leg.br/api/v2/deputados/73463 | 2020 | 1 | CD:73463 |
| 73464 | BERNARDINO BARRETO DE OLIVEIRA | https://dadosabertos.camara.leg.br/api/v2/deputados/73464 | 2021 | 1 | CD:73464 |
| 73472 | GERVÁSIO JOSÉ DA SILVA | https://dadosabertos.camara.leg.br/api/v2/deputados/73472 | 2020 | 1 | CD:73472 |
| 73483 | LUIS CARLOS HEINZE | https://dadosabertos.camara.leg.br/api/v2/deputados/73483 | 2020 | 1 | CD:73483 |
| 73486 | DARCI POMPEO DE MATTOS | https://dadosabertos.camara.leg.br/api/v2/deputados/73486 | 2020 | 1 | CD:73486 |
| 73507 | ROSILDA DE FREITAS | https://dadosabertos.camara.leg.br/api/v2/deputados/73507 | 2022 | 1 | CD:73507 |
| 73545 | EUSTÁQUIO LUCIANO ZICA | https://dadosabertos.camara.leg.br/api/v2/deputados/73545 | 2021 | 1 | CD:73545 |

## main.deputados_frentes_camara

_Query_: `SELECT * FROM "main"."deputados_frentes_camara" LIMIT 10;`

| id_deputado_frente | id_deputado | id_frente | year_snapshot |
| --- | --- | --- | --- |
| 1 | 62881 | 348 | 2020 |
| 2 | 66385 | 54304 | 2020 |
| 3 | 66828 | 53450 | 2020 |
| 4 | 69871 | 53466 | 2020 |
| 5 | 72442 | 53460 | 2020 |
| 6 | 73433 | 347 | 2020 |
| 7 | 73441 | 53457 | 2020 |
| 8 | 73486 | 53455 | 2020 |
| 9 | 73531 | 347 | 2020 |
| 10 | 73579 | 53456 | 2020 |

## main.deputados_historico_camara

_Query_: `SELECT * FROM "main"."deputados_historico_camara" LIMIT 10;`

| id_deputado_historico | id_deputado | id_legislatura | data_hora | condicao_eleitoral | descricao_status | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 62881 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2020 |
| 2 | 73692 | 57 | 2025-08-08 19:00:00 | Titular | Alteração de partido | 2020 |
| 3 | 74044 | 57 | 2024-05-09 16:50:00 | Titular | Entrada - Reassunção | 2020 |
| 4 | 74273 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2020 |
| 5 | 141408 | 57 | 2023-05-31 16:20:00 | Titular | Alteração de partido | 2020 |
| 6 | 143632 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2020 |
| 7 | 160591 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2020 |
| 8 | 160601 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2020 |
| 9 | 178866 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2020 |
| 10 | 178887 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2020 |

## main.deputados_orgaos_camara

_Query_: `SELECT * FROM "main"."deputados_orgaos_camara" LIMIT 10;`

| id_deputado_orgao | id_deputado | id_orgao | cod_titulo | data_inicio | data_fim | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 62881 | 539776 | 102 | 2025-04-29 00:00:00 |  | 2023 |
| 2 | 66385 | 5971 | 101 | 2025-06-30 00:00:00 |  | 2023 |
| 3 | 69871 | 2011 | 101 | 2025-03-19 00:00:00 |  | 2023 |
| 4 | 72442 | 539772 | 101 | 2025-05-08 00:00:00 |  | 2023 |
| 5 | 73433 | 2018 | 101 | 2025-03-19 00:00:00 |  | 2023 |
| 6 | 73441 | 539808 | 102 | 2025-09-09 00:00:00 |  | 2023 |
| 7 | 73486 | 539813 | 101 | 2025-09-02 00:00:00 |  | 2023 |
| 8 | 73692 | 539813 | 101 | 2025-09-02 00:00:00 |  | 2023 |
| 9 | 73701 | 539815 | 1 | 2025-09-16 00:00:00 |  | 2023 |
| 10 | 73801 | 539808 | 101 | 2025-09-03 00:00:00 |  | 2023 |

## main.despachos_senado

_Query_: `SELECT * FROM "main"."despachos_senado" LIMIT 10;`

| id_processo | id_despacho | data_despacho | cancelado | tipo_motivacao | sigla_tipo_motivacao | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 663587 | 7806929 | 2009-03-24 | Não | Aprovação de requerimento | APROV_REQ | 2005 |
| 1066060 | 7889688 | 2018-11-26 | Não | Decisão da Presidência | DECISAO_PRESID | 2007 |
| 2978567 | 7938573 | 2019-03-26 | Não | Aprovação de requerimento | APROV_REQ | 2007 |
| 2968939 | 7936023 | 2019-03-26 | Não | Aprovação de requerimento | APROV_REQ | 2008 |
| 2970890 | 7812982 | 2013-06-27 | Não | Aprovação de requerimento | APROV_REQ | 2008 |
| 1035192 | 7804728 | 2009-08-12 | Não | Motivação não categorizada | NAO_CATEGORIZADO | 2009 |
| 2965245 | 7819608 | 2015-11-05 | Não | Aprovação de requerimento | APROV_REQ | 2009 |
| 3021092 | 7804773 | 2009-08-18 | Não | Motivação não categorizada | NAO_CATEGORIZADO | 2009 |
| 2958548 | 9175542 | 2022-06-21 | Não | Decisão da Presidência | DECISAO_PRESID | 2010 |
| 2958841 | 7812984 | 2013-06-27 | Não | Aprovação de requerimento | APROV_REQ | 2010 |

## main.documento_autoria_senado

_Query_: `SELECT * FROM "main"."documento_autoria_senado" LIMIT 10;`

| id_documento_autoria | id_processo | id_ente | autor | codigo_parlamentar | descricao_tipo | ente | ordem | outros_autores_nao_informados | sigla_ente | sigla_tipo | year_snapshot | tipo_autor | id_senador_ou_ente |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1963 | 7711601 | 1 | Jean-Paul Prates | 5627 | SENADOR | Senado Federal | 2 | Não | SF | SENADOR | 2019 | senador | 5627 |
| 1964 | 7711690 | 1 | Weverton | 5411 | SENADOR | Senado Federal | 29 | Não | SF | SENADOR | 2019 | senador | 5411 |
| 1965 | 7712043 | 1 | Eduardo Girão | 5976 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2019 | senador | 5976 |
| 1966 | 7714029 | 1 | Alvaro Dias | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2019 | senador | 945 |
| 1967 | 7714041 | 1 | Alvaro Dias | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2019 | senador | 945 |
| 1968 | 7714045 | 1 | Alvaro Dias | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2019 | senador | 945 |
| 1969 | 7714051 | 1 | Alvaro Dias | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2019 | senador | 945 |
| 1970 | 7714055 | 1 | Alvaro Dias | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2019 | senador | 945 |
| 1971 | 7714145 | 1 | Alvaro Dias | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2019 | senador | 945 |
| 1972 | 7714257 | 1 | Alvaro Dias | 945 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2019 | senador | 945 |

## main.emendas_senado

_Query_: `SELECT * FROM "main"."emendas_senado" LIMIT 10;`

| id_emenda | id_ci_emenda | id_ci_emendado | id_documento_emenda | id_processo | identificacao | numero | autoria | descricao_documento_emenda | tipo_emenda | turno_apresentacao | casa | codigo_colegiado | sigla_colegiado | nome_colegiado | data_apresentacao | url_documento_emenda | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4694683 | 4694680 | 1330444 | 4694674 | 1330439 | EMENDA 1 PLEN - PRS 57/2015 | 1 | Senador Romero Jucá (MDB/RR) |  | EMENDA_PARCIAL | NORMAL | SF | 1998 | PLEN | Plenário do Senado Federal | 2015-12-01 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4694674 | 2015 |
| 4429988 | 4429985 | 1331407 | 4429979 | 1331402 | EMENDA 1 / CE - PRS 2/2015 | 1 | Autoria não registrada. |  | EMENDA_PARCIAL | NORMAL | SF | 47 | CE | Comissão de Educação e Cultura | 2015-10-13 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4429979 | 2015 |
| 4338177 | 4338174 | 1331428 | 4338168 | 1331423 | EMENDA 1 / CE - PRS 1/2015 | 1 | Autoria não registrada. |  | EMENDA_PARCIAL | NORMAL | SF | 47 | CE | Comissão de Educação e Cultura | 2015-05-05 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4338168 | 2015 |
| 4012973 | 4012970 | 1399053 | 4012964 | 1399048 | EMENDA 1 - PEC 83/2015 | 1 | Senador Antonio Anastasia (PSDB/MG) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-12 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4012964 | 2015 |
| 4012989 | 4012986 | 1399053 | 4012980 | 1399048 | EMENDA 2 - PEC 83/2015 | 2 | Senador Ricardo Ferraço (MDB/ES) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-12 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4012980 | 2015 |
| 4013005 | 4013002 | 1399053 | 4012996 | 1399048 | EMENDA 4 - PEC 83/2015 | 4 | Senador Ricardo Ferraço (MDB/ES) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-12 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4012996 | 2015 |
| 4013021 | 4013018 | 1399053 | 4013012 | 1399048 | EMENDA 3 - PEC 83/2015 | 3 | Senador Ricardo Ferraço (MDB/ES) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-12 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4013012 | 2015 |
| 4013046 | 4013043 | 1399053 | 4013037 | 1399048 | EMENDA 5 - PEC 83/2015 | 5 | Senador Walter Pinheiro (PT/BA) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-18 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4013037 | 2015 |
| 4013062 | 4013059 | 1399053 | 4013053 | 1399048 | EMENDA 7 - PEC 83/2015 | 7 | Senador Walter Pinheiro (PT/BA) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-18 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4013053 | 2015 |
| 4013078 | 4013075 | 1399053 | 4013069 | 1399048 | EMENDA 8 - PEC 83/2015 | 8 | Senador Walter Pinheiro (PT/BA) |  | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2015-08-18 | http://legis.senado.leg.br/sdleg-getter/documento?dm=4013069 | 2015 |

## main.encontro_legislativo_senado

_Query_: `SELECT * FROM "main"."encontro_legislativo_senado" LIMIT 10;`

| id_processo | id_despacho | id_encontro_legislativo | data_encontro | tipo_encontro | descricao_encontro | casa_encontro | numero_encontro | colegiado_casa | colegiado_codigo | colegiado_nome | colegiado_sigla | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5227247 | 7903678 | 7369084 | 2018-03-15 | SES | Sessão Deliberativa Extraordinária | SF | 27 | SF | 1998 | Plenário do Senado Federal | PLEN | 2017 | 1 |
| 7696069 | 7886528 | 7697524 | 2018-11-16 | SES | Sessão Não Deliberativa | SF | 8 | SF | 1998 | Plenário do Senado Federal | PLEN | 2018 | 1 |
| 7703737 | 7894097 | 7703646 | 2018-12-11 | SES | Sessão Deliberativa Ordinária | SF | 154 | SF | 1998 | Plenário do Senado Federal | PLEN | 2018 | 1 |
| 7741404 | 7940462 | 7741033 | 2019-04-10 | SES | Sessão Deliberativa Ordinária | SF | 47 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 7758398 | 7958926 | 7757881 | 2019-05-28 | SES | Sessão Deliberativa Ordinária | SF | 84 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 7762202 | 7963054 | 7761771 | 2019-06-06 | SES | Sessão Deliberativa Extraordinária | SF | 90 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 2914544 | 7971974 | 7774190 | 2019-06-27 | SES | Sessão Não Deliberativa | SF | 104 | SF | 1998 | Plenário do Senado Federal | PLEN | 2016 | 1 |
| 7778890 | 7978217 | 7778834 | 2019-07-10 | SES | Sessão Deliberativa Ordinária | SF | 117 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 7783495 | 7985093 | 7782566 | 2019-08-06 | SES | Sessão Deliberativa Ordinária | SF | 127 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |
| 7791472 | 8007570 | 7800450 | 2019-09-11 | SES | Sessão Deliberativa Ordinária | SF | 163 | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 | 1 |

## main.ente_senado

_Query_: `SELECT * FROM "main"."ente_senado" LIMIT 10;`

| id_ente | sigla | nome | casa | sigla_tipo | descricao_tipo | data_inicio | data_fim | tag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7378493 |  | 1ª Câmara de Coordenação e Revisão -Direitos Sociais e Fiscalização de Atos Administrativos em Geral |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:7378493 |
| 7378350 |  | 1ª Câmara de Coordenação e Revisão do Ministério Público Federal |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:7378350 |
| 301 |  | 1º Vice-Presidente da Mesa do Congresso Nacional, no exercício da Presidência |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:301 |
| 7376109 |  | 2ª Vara Cível, Família e Sucessões Inf. e Juvent. de Guaraí |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:7376109 |
| 7376147 |  | 2ª Vara de Família, Sucessões, Órfãos, Interditos e Ausentes do Tribunal de Justiça de Roraima |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:7376147 |
| 7217780 | TORIA | ??? | SF | COLEGIADO_LEGISLATIVO | Colegiado Legislativo | 1900-01-01 | 1999-01-31 | SE:7217780 |
| 7380112 |  | ABA |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:7380112 |
| 7359096 |  | ABAC - Associação Brasileira de Administradoras de Consórcios |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:7359096 |
| 7374323 |  | ABCA - ABRAJI - ABRA - AJOR - CLUBE DA VOZ - COMISSÃO ESPECIAL DE DIREITOS AUTORAIS DO CONSELHO FEDE |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:7374323 |
| 7361383 |  | ABDIB |  | ENTE_JURIDICO | Ente Jurídico - não categorizado |  |  | SE:7361383 |

## main.eventos_camara

_Query_: `SELECT * FROM "main"."eventos_camara" LIMIT 10;`

| id_evento | data_hora_inicio | data_hora_fim | descricao | descricao_tipo | fases | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59130 | 2020-02-13 09:00:00 | 2020-02-13 19:00:00 | Visita Técnica - Colômbia
 Reunião no Ministério da Justiça da Colômbia

9:00  - 9:15   Boas vindas com a Dra. Margarita Cabello Blanco (por confirmar) Ministra de Justicia y del derecho

9:15 - 9:30  Cannabis para uso médico e científico na Colombia, Contexto e importância.
Dr. Dúmar Javier Cárdenas Poveda - Ministerio de Justicia y del Derecho.

9:30 - 10:30  Marco regulatório:
Manejo de sementes e cultivo de cannabis. Ministerio de Justicia y del Derecho. Instituto Colombiano Agropecuario (ICA) 

Produtos que contém derivados de cannabis com finalidade médica e sua distribiução a nivel nacional. Ministerio de Salud y Protección Social, Instituto Nacional De Vigilancia De Medicamentos Y Alimentos INVIMA.

Control de productos terminados. Fondo Nacional de Estupefacientes.

10:30 - 11:30  Modelo de controle de cannabis no Brasil  - Delegação visitante

11:30 - 12:00  Perguntas e encerramento

Almoço

13:00 - 18:00 Visita a Colombian Organics S A S - Escritório e Cultivo

Delegação confirmada: Deputado Paulo Teixeira, Deputado Luciano Ducci e Deputado Eduardo Costa

Requerimento nº 33 - Dep. Luciano Ducci | Outro Evento |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59130 | 2020 | 1 |
| 59154 | 2021-03-23 09:30:00 | 2021-03-23 10:35:00 | Reunião deliberativa
 | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59154 | 2021 | 1 |
| 59253 | 2020-02-04 14:30:00 | 2020-02-04 18:07:00 | Audiência Pública e Deliberação de Requerimentos
 I - Audiência Pública com a presença confirmada dos seguintes convidados:

-Coronel MARCOS ANTÔNIO NUNES DE OLIVEIRA, Representante da Associação dos Militares Estaduais - AMEBRASIL (Req. 4/19);

- Tenente-Coronel LÁZARO TAVARES DE MELO DA SILVA, PMMG (Req. 4/19);

- RODRIGO BUENO GUSSO, Delegado da Polícia Civil de Santa Catarina (Req. 10/19); 

-  RODOLFO LATERZA, Representante da Federação Nacional dos Delegados de Polícia Civil - FENDEPOL (Req. 8/19);

- THIAGO TURBAY FREIRIA, IBCCRIM (Req. 3/19); e

- NEY DE BARROS BELLO FILHO, Desembargador Federal do TRF-1 (Req. 22/19).


II - Deliberação de Requerimentos entregues à Secretaria-Executiva da Comissão até as 18h da véspera da reunião. | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59253 | 2020 | 1 |
| 59271 | 2020-02-05 10:00:00 | 2020-02-05 12:25:00 | CORANAVÍRUS: Ministério da Saúde; CSSF; FP da Saúde
 | Palestra |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59271 | 2020 | 1 |
| 59336 | 2020-02-18 16:30:00 | 2020-02-18 18:58:00 | Discussão e Votação de Propostas
 Deliberação de Requerimentos. | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59336 | 2020 | 1 |
| 59341 | 2020-02-19 09:00:00 | 2020-02-19 11:00:00 | Visita técnica ao Ministério da Saúde
 Visita Técnica ao Ministério da Saúde
Com o Secretário-Executivo João Gabbardo dos Reis
Horário:09h
Endereço: Ministério da Saúde - Esplanada dos Ministérios, Bloco G, 3º Andar. Brasília, Distrito Federal. CEP: 70.058-900

(Req. 1/20, Dep. Dr. Luiz Antonio Teixeira Jr) | Outro Evento |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59341 | 2020 | 1 |
| 59403 | 2020-03-11 10:00:00 |  | Discussão e Votação do Parecer do Relator
 - Discussão e Votação do Parecer do Relator, Deputado Juscelino Filho | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59403 | 2020 | 1 |
| 59407 | 2020-03-04 14:30:00 | 2020-03-04 18:16:00 | Avaliação e Acompanhamento-GAA e Plano Nacional de Contingenciamento.
 I - Audiência Pública com a participação das seguintes autoridades:


-Antonio Roque Pedreira Júnior, Chefe de Gabinete do Ministro do Meio Ambiente - MMA  (Req. 09/2020, do Dep. Rodrigo Agostinho);

-Samuel Vieira de Souza, Assessor do Ministério do Meio Ambiente - MMA  (Req. 09/2020, do Dep. Rodrigo Agostinho);

-Olivaldi Alves Borges Azevedo, Instituto Brasileiro de Meio Ambiente e Recursos Naturais Renováveis - IBAMA (Req. 09/2020, do Dep. Rodrigo Agostinho);

-Rodolfo Henrique de Saboia, Contra-Almirante da Marinha do Brasil e Coordenação Operacional do Grupo de Acompanhamento e Avaliação - GAA/Marinha do Brasil (Req. 23/2019, do Dep. Adolfo Viana e Req. 09/2020, do Dep. Rodrigo Agostinho); 

-Moisés Vieira Pinto,  Agência Nacional de Petróleo, Gás Natural e Biocombustíveis - ANP,  Especialista em Geologia e Geofísica do Petróleo e Gás Natural, em substituição a  Luciene Ferreira Pedrosa, Agência Nacional de Petróleo, Gás Natural e Biocombustíveis - ANP (Req. 09/2020, do Dep. Rodrigo Agostinho);

-Robson José Calixto, Analista Ambiental da Secretaria de Qualidade Ambiental do Ministério do Meio Ambiente  (Req. 09/2020, do Dep. Rodrigo Agostinho); e

-André Felisberto França, Secretário de Qualidade Ambiental do Ministério do Meio Ambiente - MMA  (Req. 33/2019, do Dep. João H. Campos). | Reunião Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59407 | 2020 | 1 |
| 59413 | 2020-03-04 13:55:00 | 2020-03-04 21:07:00 | Sessão Deliberativa Extraordinária
 | Sessão Deliberativa |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59413 | 2020 | 1 |
| 59440 | 2020-03-06 15:00:00 | 2020-03-06 17:31:00 | Homenagem ao Centenário da Mãe Ruth de Oxalá e às Mulheres de Terreiro do DF e Entorno
 Homenagem ao Centenário da Mãe Ruth de Oxalá e às Mulheres de Terreiro do DF e Entorno | Sessão Não Deliberativa Solene |  | https://dadosabertos.camara.leg.br/api/v2/eventos/59440 | 2020 | 1 |

## main.eventos_orgaos_camara

_Query_: `SELECT * FROM "main"."eventos_orgaos_camara" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."eventos_pauta_camara" LIMIT 10;`

| id_pauta | id_evento | cod_regime | ordem | id_proposicao | id_relator | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 58552 | 106.0 | 1 | 1198512 | 160639 | 2020 |
| 2 | 59113 | 21.0 | 1 | 2238574 | 204510 | 2020 |
| 3 | 59129 | 14.0 | 1 | 2233088 | 178931 | 2020 |
| 4 | 59129 | 99.0 | 2 | 2234669 |  | 2020 |
| 5 | 59129 | 99.0 | 3 | 2236762 | 178931 | 2020 |
| 6 | 59154 | 99.0 | 1 | 2273905 |  | 2021 |
| 7 | 59154 | 20.0 | 2 | 2220726 | 75431 | 2021 |
| 8 | 59154 | 20.0 | 3 | 2223631 | 160575 | 2021 |
| 9 | 59154 | 14.0 | 4 | 2219323 | 204416 | 2021 |
| 10 | 59154 | 20.0 | 5 | 2210603 | 160575 | 2021 |

## main.frentes_camara

_Query_: `SELECT * FROM "main"."frentes_camara" LIMIT 10;`

| id_frente | id_deputado_coordenador | id_legislatura | titulo | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- |
| 356 | 73483 | 54 | Frente Parlamentar da Agropecuária - FPA | https://dadosabertos.camara.leg.br/api/v2/frentes/356 | 0 | 1 |
| 362 | 74749 | 54 | Frente Parlamentar do Transporte Público - FPTP | https://dadosabertos.camara.leg.br/api/v2/frentes/362 | 0 | 1 |
| 370 | 160655 | 54 | Frente Parlamentar da Habitação e Desenvolvimento Urbano do Congresso Nacional | https://dadosabertos.camara.leg.br/api/v2/frentes/370 | 0 | 1 |
| 420 | 74784 | 54 | Frente Parlamentar pela Liberdade de Expressão e o Direito à Comunicação com Participação Popular | https://dadosabertos.camara.leg.br/api/v2/frentes/420 | 0 | 1 |
| 436 | 160555 | 54 | Frente Parlamentar da Mineração Brasileira | https://dadosabertos.camara.leg.br/api/v2/frentes/436 | 0 | 1 |
| 447 | 109152 | 54 | Frente Parlamentar em Defesa da Cadeia do Aço, Ferro Gusa, Ferro Ligas, Silício Metálico, seus insumos e derivados. | https://dadosabertos.camara.leg.br/api/v2/frentes/447 | 0 | 1 |
| 451 | 160659 | 54 | Frente Parlamentar em Defesa das Vítimas da Violência | https://dadosabertos.camara.leg.br/api/v2/frentes/451 | 0 | 1 |
| 461 | 160636 | 54 | Frente Parlamentar pelo Desenvolvimento do Semiárido | https://dadosabertos.camara.leg.br/api/v2/frentes/461 | 0 | 1 |
| 477 | 160529 | 54 | Frente Parlamentar de Combate ao Trauma | https://dadosabertos.camara.leg.br/api/v2/frentes/477 | 0 | 1 |
| 488 |  | 54 | Frente Parlamentar do Cooperativismo (Frencoop) | https://dadosabertos.camara.leg.br/api/v2/frentes/488 | 0 | 1 |

## main.informes_documentos_associados_senado

_Query_: `SELECT * FROM "main"."informes_documentos_associados_senado" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."informes_legislativos_senado" LIMIT 10;`

| id_informe_legislativo | id_processo | id_informe | data_informe | descricao | id_situacao_iniciada | sigla_situacao_iniciada | ente_adm_casa | ente_adm_id | ente_adm_nome | ente_adm_sigla | colegiado_casa | colegiado_codigo | colegiado_nome | colegiado_sigla | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 | 2230315 | 2025-03-07 | Remetido Ofício CN nº 33, de 06/03/25, ao Senhor Primeiro-Secretário da Câmara dos Deputados, comunicando o término do prazo estabelecido no § 2º do art. 11 da Resolução nº 1, de 2002-CN, e no § 11 do art. 62 da Constituição Federal, em 1º de março de 2025, para edição do decreto legislativo destinado a regular as relações jurídicas decorrentes da Medida Provisória nº 2.224, de 4 de setembro 2001, cuja vigência encerrou-se com sua revogação, na íntegra, pela Lei nº 14.286, de 29 de dezembro de 2021.
À COARQ. |  |  | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2001 |
| 2 | 663587 | 2151518 | 2023-08-05 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2005 |
| 3 | 1066060 | 2063899 | 2021-09-20 | A Presidência declara o Projeto prejudicado, em atenção à decisão da CCT, em reunião ocorrida no dia 16 de setembro, que deliberou pela prejudicialidade da matéria, nos termos do art. 334 do Regimento Interno.
Ao Arquivo. | 43 | PRJDA | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 1998 | Plenário do Senado Federal | PLEN | 2007 |
| 4 | 2978567 | 2151970 | 2023-08-05 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2007 |
| 5 | 2968939 | 2152226 | 2023-08-05 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2008 |
| 6 | 2970890 | 2151099 | 2023-08-05 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2008 |
| 7 | 1035192 | 2153518 | 2022-04-26 | Publicado no Diário do Congresso Nacional n° 13, de 14/04/22, pág, 0034.

À COARQ. |  |  | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2009 |
| 8 | 2965245 | 2151638 | 2023-08-05 | A matéria vai ao arquivo. |  |  | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF |  |  |  |  | 2009 |
| 9 | 3021092 | 2153552 | 2022-08-11 | Publicado no Diário do Congresso Nacional n° 30, de 11/08/22, pág, 0073.

À COARQ. |  |  | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2009 |
| 10 | 3333348 | 2052475 | 2021-04-30 | (PR) PRESIDÊNCIA DA REPÚBLICA..
PROMULGADAS partes vetadas e rejeitadas pelo Congresso Nacional, da Lei nº 11.907, de 2 de fevereiro de 2009.
DOUE (Diário Oficial da União) - 30/04/2021 - Seção I - pág. 1.
promulgada em 29/04/2021.

À COARQ. |  |  | SF | 55304 | Secretaria de Expediente | SEXPE |  |  |  |  | 2009 |

## main.legislaturas_camara

_Query_: `SELECT * FROM "main"."legislaturas_camara" LIMIT 10;`

| id_legislatura | data_inicio | data_fim | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- |
| 3 | 1834-04-25 | 1838-04-24 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/3 | 0 | 1 |
| 6 | 1844-12-24 | 1848-04-24 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/6 | 0 | 1 |
| 38 | 1946-09-23 | 1951-03-09 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/38 | 0 | 1 |
| 41 | 1959-02-01 | 1963-01-31 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/41 | 0 | 1 |
| 12 | 1863-12-14 | 1867-04-14 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/12 | 0 | 1 |
| 20 | 1886-04-15 | 1889-06-15 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/20 | 0 | 1 |
| 36 | 1934-07-21 | 1935-04-27 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/36 | 0 | 1 |
| 53 | 2007-02-01 | 2011-01-31 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/53 | 0 | 1 |
| 4 | 1838-04-25 | 1842-04-24 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/4 | 0 | 1 |
| 23 | 1894-04-18 | 1897-04-17 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/23 | 0 | 1 |

## main.legislaturas_lideres_camara

_Query_: `SELECT * FROM "main"."legislaturas_lideres_camara" LIMIT 10;`

| id_lider | id_legislatura | nome_bancada | tipo_bancada | uri_bancada | data_inicio | data_fim | id_deputado | titulo | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2004-05-05 00:00:00 | 2007-01-31 00:00:00 | 73442 | Vice-Líder | 2003 |
| 2 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2005-05-31 00:00:00 | 2006-04-19 00:00:00 | 73472 | Vice-Líder | 2003 |
| 3 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-12 00:00:00 | 2007-01-31 00:00:00 | 73546 | Vice-Líder | 2003 |
| 4 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2005-07-12 00:00:00 | 2007-01-31 00:00:00 | 73579 | Vice-Líder | 2003 |
| 5 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-12 00:00:00 | 2006-05-31 00:00:00 | 73592 | Vice-Líder | 2003 |
| 6 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2006-05-31 00:00:00 | 2007-01-31 00:00:00 | 73592 | 1º Vice-Líder | 2003 |
| 7 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-24 00:00:00 | 2006-03-23 00:00:00 | 73764 | Vice-Líder | 2003 |
| 8 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-24 00:00:00 | 2005-05-31 00:00:00 | 73882 | Vice-Líder | 2003 |
| 9 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-05-20 00:00:00 | 2007-01-31 00:00:00 | 74055 | Vice-Líder | 2003 |
| 10 | 52 | DEM | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36769 | 2003-03-12 00:00:00 | 2007-01-31 00:00:00 | 74058 | Vice-Líder | 2003 |

## main.legislaturas_mesa_camara

_Query_: `SELECT * FROM "main"."legislaturas_mesa_camara" LIMIT 10;`

| id_legislatura_mesa | id_legislatura | id_deputado | cod_titulo | data_inicio | data_fim | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 103 | 52 | 73428 | 1 | 2005-09-28 | 2007-01-31 | 2003 |
| 109 | 52 | 73534 | 1 | 2003-02-02 | 2005-02-14 | 2003 |
| 85 | 52 | 74436 | 1 | 2005-02-14 | 2005-09-21 | 2003 |
| 121 | 52 | 74801 | 10 | 2003-02-02 | 2004-12-01 | 2003 |
| 115 | 52 | 74563 | 10 | 2005-02-14 | 2007-01-31 | 2003 |
| 91 | 52 | 74097 | 11 | 2003-02-02 | 2004-12-31 | 2003 |
| 97 | 52 | 74374 | 11 | 2005-02-14 | 2007-01-31 | 2003 |
| 1 | 52 | 74158 | 12 | 2005-02-14 | 2007-01-31 | 2003 |
| 19 | 52 | 74559 | 12 | 2003-02-02 | 2005-02-14 | 2003 |
| 49 | 52 | 74421 | 2 | 2003-02-02 | 2005-02-14 | 2003 |

## main.movimentacoes_senado

_Query_: `SELECT * FROM "main"."movimentacoes_senado" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."orgaos_camara" LIMIT 10;`

| id_orgao | nome | cod_tipo_orgao | uri | year_snapshot | rn | tag |
| --- | --- | --- | --- | --- | --- | --- |
| 201 | COMISSÃO DO TRABALHO | 2 | https://dadosabertos.camara.leg.br/api/v2/orgaos/201 | 2023 | 1 | CO:201 |
| 218 | COMISSÃO DE CONSTITUIÇÃO E JUSTIÇA | 2 | https://dadosabertos.camara.leg.br/api/v2/orgaos/218 | 2023 | 1 | CO:218 |
| 5306 | Dispõe sobre o Conselho de Altos Estudos e Avaliação Tecnológica, de que trata o artigo 275 do Regimento Interno. | 11 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5306 | 0 | 1 | CO:5306 |
| 5437 | Comissão Especial destinada a apreciar e  proferir parecer  à Proposta de Emenda à Constituição nº 57-A, de 1999, que " altera o art. 159 para instituir o Fundo Nacional de Desenvolvimento do Semi-Árido e prevê suas fontes de recursos". | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5437 | 2023 | 1 | CO:5437 |
| 5604 | Altera a Legislação Tributária Federal, e dá outras providências. | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5604 | 0 | 1 | CO:5604 |
| 5942 | Altera dispositivos da Lei nº 8.745, de 9 de dezembro de 1993, e da Lei nº 10.470, de 25 de junho de 2002, cria cargos efetivos, cargos comissionados e gratificações no âmbito da Administração Pública Federal, e dá outras providências. | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5942 | 0 | 1 | CO:5942 |
| 5956 | Altera as Leis nºs. 8.248, de 23 de outubro de 1991, 8.387, de 30 de dezembro de 1991, e 10.176, de 11 de janeiro de 2001, dispondo sobre a capacitação e competitividade do setor de tecnologia da informação, e dá outras providências. | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5956 | 0 | 1 | CO:5956 |
| 5957 | Dispõe sobre a contribuição para o Programa de Integração Social e de Formação do Patrimônio do Servidor Público - PIS/PASEP e da Contribuição para Seguridade Social - COFINS devidas pelas sociedades cooperativas em geral. | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5957 | 0 | 1 | CO:5957 |
| 5986 | Cria a Carreira de Agente Penitenciário Federal no Quadro de Pessoal do Departamento de Polícia Federal e dá outras providências. | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5986 | 0 | 1 | CO:5986 |
| 8669 | Comissão Especial destinada a proferir parecer à Proposta de Emenda à Constituição nº 53-A, de 2007, do Sr. Jofran Frejat, que "dá nova redação ao § 3º do Art. 39 da Constituição Federal" (garante ao servidor de cargo em comissão de livre nomeação e exoneração, direito a aviso prévio, seguro desemprego, FGTS, entre outros) | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/8669 | 2021 | 1 | CO:8669 |

## main.orgaos_camara_hotfix

_Query_: `SELECT * FROM "main"."orgaos_camara_hotfix" LIMIT 10;`

| id_orgao | nome | cod_tipo_orgao | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- |
| 262 | COMISSÃO MISTA | 20 | https://dadosabertos.camara.leg.br/api/v2/orgaos/262 | 2020 | 1 |
| 5996 | Comissão Parlamentar de Inquérito com a finalidade de investigar denúncias de irregularidade na prestação de serviços por empresas e instituições privadas de Planos de Saúde. | 4 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5996 | 2020 | 1 |
| 6502 | Comissão Parlamentar de Inquérito com a finalidade de investigar escutas telefônicas clandestinas/ilegais, conforme denúncia publicada na Revista "Veja", edição 2022, nº 33, de 22 de agosto de 2007. | 4 | https://dadosabertos.camara.leg.br/api/v2/orgaos/6502 | 2020 | 1 |
| 6726 | Comissão Especial destinada ao exame e a avaliação da Crise Econômico-Financeira e, ao final, formular propostas ao Poder Executivo e ao País, especificamente no que diz respeito à repercussão na Agricultura. | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/6726 | 2020 | 1 |
| 81 | Superior Tribunal de Justiça | 50000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/81 | 2020 | 1 |
| 537485 | Comissão Parlamentar de Inquérito destinada a investigar a realidade do Sistema Carcerário Brasileiro | 4 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537485 | 2020 | 1 |
| 537337 | Comissão Parlamentar de Inquérito destinada a investigar a prática de atos ilícitos e irregulares no âmbito da empresa Petróleo Brasileiro S/A (PETROBRAS), entre os anos de 2005 e 2015, relacionados a superfaturamento e gestão temerária na construção de refinarias no Brasil; à constituição de empresas subsidiárias e sociedades de propósito específico pela Petrobras com o fim de praticar atos ilícitos; ao superfaturamento e gestão temerária na construção e afretamento de navios de transporte, navios-plataforma e navios-sonda; a irregularidades na operação da companhia Sete Brasil e na venda de ativos da Petrobras na África | 4 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537337 | 2020 | 1 |
| 537914 | Comissão Parlamentar de Inquérito destinada a apurar as irregularidades nas concessões de benefícios fiscais concedidos por aplicação da Lei nº 8.313, de 23 de dezembro de 1991, que instituiu o Programa Nacional de Apoio à Cultura (Pronac) e deu outras providências. | 4 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537914 | 2020 | 1 |
| 537742 | Comissão Especial destinada a estudar o processo de inovação e incorporação tecnológica no complexo produtivo da saúde, no Brasil e no mundo | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537742 | 2020 | 1 |
| 538202 | Comissão Especial Mista, destinada à oferecer propostas sobre alteração da Lei Kandir no que se refere a compensação da União aos Estados, Distrito Federal e Municípios, por conta da perda de receita decorrente de desoneração do Imposto sobre Circulação de Mercadorias e Serviços (ICMS) | 21 | https://dadosabertos.camara.leg.br/api/v2/orgaos/538202 | 2020 | 1 |

## main.orientacoes_camara

_Query_: `SELECT * FROM "main"."orientacoes_camara" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."outros_numeros_senado" LIMIT 10;`

| id_outro_numero | id_processo | id_outro_processo | ano | casa_identificadora | ente_identificador | sigla | numero | sigla_ente_identificador | externa_ao_congresso | tramitando | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 |  | 2001 |  | Presidência da República | MSG | 954 | PR |  | Não | 2001 |
| 2 | 1066060 |  | 2006 | CN | Congresso Nacional | MSG | 696 | CN | Não | Não | 2007 |
| 3 | 1035192 |  | 2008 | CN | Congresso Nacional | MSG | 185 | CN | Não | Não | 2009 |
| 4 | 3021092 |  | 2008 | CN | Congresso Nacional | MSG | 185 | CN | Não | Não | 2009 |
| 5 | 3333348 |  | 2009 |  | Presidência da República | MSG | 48 | PR |  | Não | 2009 |
| 6 | 2958548 | 2958545 | 2008 | CD | Câmara dos Deputados | PL | 03512 | CD | Não | Não | 2010 |
| 7 | 3020085 |  | 2009 | CN | Congresso Nacional | MSG | 730 | CN | Não | Não | 2010 |
| 8 | 3346770 |  | 2010 |  | Presidência da República | MSG | 305 | PR |  | Não | 2010 |
| 9 | 516008 | 516005 | 1999 | CD | Câmara dos Deputados | PL | 01664 | CD | Não | Não | 2011 |
| 10 | 516203 | 516200 | 2004 | CD | Câmara dos Deputados | PL | 04479 | CD | Não | Não | 2011 |

## main.parlamentar_senado

_Query_: `SELECT * FROM "main"."parlamentar_senado" LIMIT 10;`

| codigo_parlamentar | codigo_publico_leg_atual | nome_completo | nome_parlamentar | sexo_parlamentar | sigla_partido | uf_parlamentar | email_parlamentar | data_nascimento | endereco_parlamentar | naturalidade | uf_naturalidade | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4606 |  | José Eleonildo Soares | Pinto Itamaraty | Masculino | PSDB |  | pinto.itamaraty@senador.leg.br | 1960-05-10 | Senado Federal Anexo I  25º Andar   | São Luís | MA | 2023 | 1 |
| 4811 | 900 | Laércio José de Oliveira | Laércio Oliveira | Masculino | PP | SE | sen.laerciooliveira@senado.leg.br | 1959-04-15 | Senado Federal Anexo 2   Ala Teotônio Vilela Gabinete 09 | Recife | PE | 2024 | 1 |
| 5257 |  | Renzo do Amaral Braz | Renzo Braz | Masculino | PP |  |  | 1980-04-11 |  | Muriaé | MG | 2024 | 1 |
| 5537 | 928 | Dário Elias Berger | Dário Berger | Masculino | PSB |  | sen.darioberger@senado.leg.br | 1956-12-07 | Senado Federal Anexo 1  16º Pavimento   | Bom Retiro | SC | 2023 | 1 |
| 5615 |  | Gilberto Piselo do Nascimento | Gilberto Piselo | Masculino | PDT |  |  | 1959-07-04 |  |  |  | 2023 | 1 |
| 5633 |  | Atilio Francisco da Silva | Atilio Francisco | Masculino | REPUBLICANOS |  |  | 1951-08-02 |  | São Caetano do Sul | SP | 2023 | 1 |
| 5639 | 892 | Guaracy Batista da Silveira | Guaracy Silveira | Masculino | PP |  | sen.guaracysilveira@senado.leg.br | 1951-01-02 | Senado Federal Anexo 1  6º Pavimento   | São Paulo | SP | 2023 | 1 |
| 5942 | 862 | Marcos Ribeiro do Val | Marcos do Val | Masculino | PODEMOS | ES | sen.marcosdoval@senado.leg.br | 1971-06-15 | Senado Federal Anexo 1  18º Pavimento   | Vitória | ES | 2024 | 1 |
| 5986 | 440 | Rodolfo Oliveira Nogueira | Rodolfo Nogueira | Masculino | PL | MS | dep.rodolfonogueira@camara.leg.br | 1973-11-24 |  |  |  | 2024 | 1 |
| 5996 | 947 | Marcio Diego Fernandes Tavares de Albuquerque | Diego Tavares | Masculino | PP |  | sen.diegotavares@senado.leg.br | 1983-01-15 | Senado Federal Anexo 2   Ala Teotônio Vilela Gabinete 13 | João Pessoa | PB | 2024 | 1 |

## main.partido_senado

_Query_: `SELECT * FROM "main"."partido_senado" LIMIT 10;`

| codigo_partido | data_criacao | nome | sigla | year_snapshot |
| --- | --- | --- | --- | --- |
| 146 | 1900-01-01 | Partido Federalista | PF | 1900 |
| 148 | 1900-01-01 | Partido Humanista Democrático Brasil Solidariedade | PHDBS | 1900 |
| 150 | 1900-01-01 | Partido Nacional do Consumidor | PNC | 1900 |
| 155 | 1900-01-01 | Partido de Representação da Vontade Popular | PRVP | 1900 |
| 163 | 1900-01-01 | Sem Partido | S/Partido | 1900 |
| 94 | 1922-03-25 | Partido Comunista Brasileiro | PCB | 1922 |
| 544 | 1927-01-01 | Partido Liberal | PL | 1927 |
| 500 | 1928-03-03 | Partido Libertador | PL_RS | 1928 |
| 248 | 1930-01-01 | Partido Republicano | PR | 1930 |
| 531 | 1930-01-01 | Partido Nacional | PNAC | 1930 |

## main.partidos_camara

_Query_: `SELECT * FROM "main"."partidos_camara" LIMIT 10;`

| id_partido | nome | sigla | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- |
| 36851 | Partido Verde | PV | https://dadosabertos.camara.leg.br/api/v2/partidos/36851 | 0 | 1 |
| 37906 | Partido Liberal | PL | https://dadosabertos.camara.leg.br/api/v2/partidos/37906 | 0 | 1 |
| 36834 | Partido Social Democrático | PSD | https://dadosabertos.camara.leg.br/api/v2/partidos/36834 | 0 | 1 |
| 38009 | União Brasil | UNIÃO | https://dadosabertos.camara.leg.br/api/v2/partidos/38009 | 0 | 1 |
| 36835 | Partido da Social Democracia Brasileira | PSDB | https://dadosabertos.camara.leg.br/api/v2/partidos/36835 | 0 | 1 |
| 37901 | Partido Novo | NOVO | https://dadosabertos.camara.leg.br/api/v2/partidos/37901 | 0 | 1 |
| 38010 | Partido Renovação Democrática | PRD | https://dadosabertos.camara.leg.br/api/v2/partidos/38010 | 0 | 1 |
| 36779 | Partido Comunista do Brasil | PCdoB | https://dadosabertos.camara.leg.br/api/v2/partidos/36779 | 0 | 1 |
| 36899 | Movimento Democrático Brasileiro | MDB | https://dadosabertos.camara.leg.br/api/v2/partidos/36899 | 0 | 1 |
| 37908 | Republicanos | REPUBLICANOS | https://dadosabertos.camara.leg.br/api/v2/partidos/37908 | 0 | 1 |

## main.partidos_lideres_camara

_Query_: `SELECT * FROM "main"."partidos_lideres_camara" LIMIT 10;`

| id_partido_lider | id_partido | cod_titulo | data_inicio | data_fim | id_deputado | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 36834 | 1001 | 2023-02-01 |  | 160553 | 2023 |
| 2 | 36896 | 1001 | 2025-02-03 |  | 220641 | 2023 |
| 3 | 36898 | 1001 | 2025-05-08 |  | 220703 | 2023 |
| 4 | 36899 | 1001 | 2023-02-01 |  | 204436 | 2023 |
| 5 | 37903 | 1001 | 2023-09-12 |  | 204450 | 2023 |
| 6 | 37904 | 1 | 2024-06-21 |  | 141518 | 2023 |
| 7 | 37908 | 1001 | 2025-02-04 |  | 204491 | 2023 |
| 8 | 37905 | 1007 | 2024-08-01 |  | 178972 | 2024 |
| 9 | 38010 | 1001 | 2024-04-16 |  | 204494 | 2024 |
| 10 | 36779 | 1007 | 2025-02-19 |  | 73801 | 2025 |

## main.partidos_membros_camara

_Query_: `SELECT * FROM "main"."partidos_membros_camara" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."processo_senado" LIMIT 10;`

| id_processo | codigo_materia | id_processo_casa_inicial | identificacao | identificacao_processo_inicial | identificacao_externa | ano | casa_identificadora | sigla_casa_iniciadora | sigla_ente_identificador | descricao_sigla | sigla | numero | objetivo | tramitando | id_conteudo | id_tipo_conteudo | sigla_tipo_conteudo | tipo_conteudo | tipo_norma_indicada | ementa | explicacao_ementa | deliberacao_id_destino | deliberacao_sigla_destino | deliberacao_tipo | deliberacao_sigla_tipo | deliberacao_data | deliberacao_destino | id_documento | documento_sigla_tipo | documento_tipo | documento_indexacao | documento_resumo_autoria | documento_data_apresentacao | documento_data_leitura | norma_codigo | norma_numero | norma_sigla_tipo | norma_tipo | norma_descricao | norma_sigla_veiculo | norma_veiculo | norma_numero_int | norma_ano_assinatura | norma_data_assinatura | norma_data_publicacao | year_snapshot | tag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7711601 | 135112 | 7711601 | PL 547/2019 | PL 547/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 547 | Iniciadora | Não | 7370394 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 13.152, de 29 de julho de 2015, para dispor sobre o valor do salário mínimo em 2019. | Fixa em R$1.006,00 o valor do salário mínimo a partir de 1º de janeiro de 2019. | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 | Ao arquivo | 7904798 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  LEI FEDERAL ,  AUMENTO ,  VALOR ,  SALARIO MINIMO . | Senador Paulo Rocha (PT/PA), Senador Jean Paul Prates (PT/RN) | 2019-01-04 | 2019-02-07 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7711601 |
| 7711690 | 135118 | 7711690 | PEC 2/2019 | PEC 2/2019 | {} | 2019 | SF | SF | SF | Proposta de Emenda à Constituição | PEC | 2 | Iniciadora | Não | 7370886 | 11 | NORMA_GERAL | Norma Geral | EMC | Modifica o art. 37 da Constituição Federal, para suspender o transcurso do prazo de validade de concurso público na hipótese de o Poder Público suspender as nomeações por falta de recursos financeiros. | Estabelece que, na hipótese de o Poder Público suspender as nomeações de aprovados em concurso público por falta de recursos financeiros, o transcurso do prazo de validade do concurso será automaticamente suspenso, até o retomo das nomeações, quando o prazo voltará a transcorrer. | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 | Ao arquivo | 7910196 | PROPOSTA_EMENDA_CONSTITUICAO | Proposta de Emenda à Constituição |  ALTERAÇÃO ,  CONSTITUIÇÃO FEDERAL ,  SUSPENSÃO ,  PRAZO ,  VALIDADE ,  CONCURSO PUBLICO ,  HIPOTESE ,  PROIBIÇÃO ,  NOMEAÇÃO ,  AUSENCIA ,  RECURSOS FINANCEIROS . | Senadora Rose de Freitas (PODEMOS/ES), Senador Acir Gurgacz (PDT/RO), Senador Alvaro Dias (PODEMOS/PR), Senador Antonio Anastasia (PSDB/MG), Senador Carlos Viana (PSD/MG), Senador Ciro Nogueira (PP/PI), Senador Eduardo Gomes (MDB/TO), Senador Elmano Férrer (PODEMOS/PI), Senador Fabiano Contarato (REDE/ES), Senador Fernando Bezerra Coelho (MDB/PE), Senador Humberto Costa (PT/PE), Senador Izalci Lucas (PSDB/DF), Senador Jorge Kajuru (PSB/GO), Senador José Maranhão (MDB/PB), Senador Lasier Martins (PODEMOS/RS), Senadora Leila Barros (PSB/DF), Senadora Mailza Gomes (PP/AC), Senador Marcos do Val (CIDADANIA/ES), Senadora Maria do Carmo Alves (DEM/SE), Senador Nelsinho Trad (PSD/MS), Senador Otto Alencar (PSD/BA), Senador Rodrigo Pacheco (DEM/MG), Senador Romário (PODEMOS/RJ), Senadora Juíza Selma (PSL/MT), Senador Sérgio Petecão (PSD/AC), Senadora Soraya Thronicke (PSL/MS), Senador Styvenson Valentim (PODEMOS/RN), Senador Veneziano Vital do Rêgo (PSB/PB), Senador Weverton (PDT/MA) | 2019-02-06 | 2019-02-07 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7711690 |
| 7712043 | 135122 | 7712043 | PL 557/2019 | PL 557/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 557 | Iniciadora | Não | 7371070 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 4.375, de 17 de agosto de 1964, que dispõe sobre o Serviço Militar, para conceder prioridade a jovens egressos de instituições de acolhimento na seleção para o serviço militar. | Determina que na elaboração dos critérios para a seleção do serviço militar, será concedida prioridade aos jovens egressos de instituições de acolhimento familiar ou institucional. | 1 | CAMARA | Aprovada por Comissão em decisão terminativa | APROVADA_EM_COMISSAO_TERMINATIVA | 2022-12-13 | À Câmara dos Deputados | 7910821 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  LEI FEDERAL ,  CONCESSÃO ,  PRIORIDADE ,  RECRUTAMENTO ,  CONVOCAÇÃO ,  SELEÇÃO ,  SERVIÇO MILITAR ,  JUVENTUDE ,  EGRESSO ,  RESIDENCIA ,  ACOLHIMENTO . | Senador Eduardo Girão (PODEMOS/CE) | 2019-02-06 | 2019-02-07 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7712043 |
| 7714029 | 135126 | 7714029 | PL 577/2019 | PL 577/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 577 | Iniciadora | Não | 7371759 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 9.250, de 26 de dezembro de 1995, que dispõe sobre o imposto de renda das pessoas físicas, para permitir a dedução de despesas com pagamento de prestações do único imóvel residencial. | Permite no Imposto de Renda o abatimento de despesas aos pagamentos efetuados, no ano-calendário, a título de prestação para aquisição do único imóvel residencial, cujo custo original não ultrapasse o valor total de R$ 150.000,00. | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 | Ao arquivo | 7913026 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  LEI FEDERAL ,  LEGISLAÇÃO ,  IMPOSTO DE RENDA ,  PESSOA FISICA ,  AUTORIZAÇÃO ,  DEDUÇÃO ,  DESPESA ,  PAGAMENTO ,  PARCELA ,  AQUISIÇÃO ,  IMOVEL RESIDENCIAL . | Senador Alvaro Dias (PODEMOS/PR) | 2019-02-05 | 2019-02-11 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7714029 |
| 7714041 | 135128 | 7714041 | PL 581/2019 | PL 581/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 581 | Iniciadora | Não | 7371770 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 10.101, de 19 de dezembro de 2000, para dar à participação dos trabalhadores nos lucros ou resultados das empresas o mesmo tratamento fiscal dado à distribuição de lucros ou dividendos aos sócios ou acionistas. | Dá tratamento equitativo entre as parcelas do lucro apropriado pelo capitalista e pelo trabalhador, aplicando à participação dos lucros dos trabalhadores a mesma distribuição de lucros e dividendos dada aos sócios e acionistas. | 1 | CAMARA | Aprovada pelo Plenário | APROVADA_NO_PLENARIO | 2022-12-15 | À Câmara dos Deputados | 7913059 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  LEI FEDERAL ,  PARTICIPAÇÃO ,  TRABALHADOR ,  LUCRO ,  RESULTADO ,  EMPRESA ,  EQUIPARAÇÃO ,  TRATAMENTO FISCAL ,  LUCRO DISTRIBUIDO ,  DIVIDENDOS ,  SOCIO ,  ACIONISTA . | Senador Alvaro Dias (PODEMOS/PR) | 2019-02-05 | 2019-02-11 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7714041 |
| 7714045 | 135129 | 7714045 | PLP 16/2019 | PLP 16/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei Complementar | PLP | 16 | Iniciadora | Não | 7371814 | 11 | NORMA_GERAL | Norma Geral | LCP | Regulamenta os §§ 1º e 3º do art. 173 da Constituição Federal, para instituir o estatuto jurídico da empresa pública e da sociedade de economia mista que explorem atividade econômica de produção ou comercialização de bens ou de prestação de serviços, bem como de suas subsidiárias. | Estabelece o regulamento da empresa pública e da sociedade de economia mista exploradoras de atividade econômica. | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 | Ao arquivo | 7913191 | PROJETO_LEI_COMPLEMENTAR | Projeto de Lei Complementar |  REGULAMENTAÇÃO ,  DISPOSITIVOS ,  CONSTITUIÇÃO FEDERAL ,  CRIAÇÃO ,  ESTATUTO ,  EMPRESA PUBLICA ,  SOCIEDADE DE ECONOMIA MISTA ,  EXPLORAÇÃO ,  ATIVIDADE ECONOMICA ,  PRODUÇÃO ,  COMERCIALIZAÇÃO ,  BENS ,  PRESTAÇÃO DE SERVIÇO ,  EMPRESA SUBSIDIARIA . | Senador Alvaro Dias (PODEMOS/PR) | 2019-02-05 | 2019-02-11 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7714045 |
| 7714051 | 135132 | 7714051 | PL 579/2019 | PL 579/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 579 | Iniciadora | Não | 7371768 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera dispositivos da Lei 9.491, de 9 de setembro de 1997, que dispõe sobre procedimentos relativos ao Programa Nacional de Desestatização. | Objetiva garantir que a União mantenha o controle acionário da Petrobrás e que preserve as ações excedentes ao seu controle acionário. | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 | Ao arquivo | 7913053 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  LEI FEDERAL ,  PROGRAMA NACIONAL DE DESESTATIZAÇÃO ,  PETROLEO BRASILEIRO S/A (PETROBRAS) ,  PRESERVAÇÃO ,  AÇÕES ,  EXCEDENTE ,  MANUTENÇÃO ,  CONTROLE ACIONARIO ,  PARTICIPAÇÃO ACIONARIA . | Senador Alvaro Dias (PODEMOS/PR) | 2019-02-05 | 2019-02-11 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7714051 |
| 7714055 | 135133 | 7714055 | PL 580/2019 | PL 580/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 580 | Iniciadora | Não | 7371769 | 11 | NORMA_GERAL | Norma Geral | LEI | Destina percentual da arrecadação de loterias para o Fundo Especial para Calamidades Públicas (Funcap). | Autoriza a Caixa Econômica Federal a destinar um ponto percentual da arrecadação total de todas as loterias por ela administradas para o Fundo Especial para Calamidades Públicas (Funcap), | 1 | CAMARA | Aprovada por Comissão em decisão terminativa | APROVADA_EM_COMISSAO_TERMINATIVA | 2023-09-28 | À Câmara dos Deputados | 7913056 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  CRIAÇÃO ,  LEI FEDERAL ,  PRODUTO ,  ARRECADAÇÃO ,  LOTERIA ,  PERCENTAGEM ,  DESTINAÇÃO ,  FUNDO ESPECIAL PARA CALAMIDADE PUBLICA (FUNCAP) . | Senador Alvaro Dias (PODEMOS/PR) | 2019-02-05 | 2019-02-11 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7714055 |
| 7714145 | 135135 | 7714145 | PL 586/2019 | PL 586/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 586 | Iniciadora | Não | 7371804 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 7.713, de 22 dezembro de 1988, para isentar do imposto de renda das pessoas físicas os rendimentos correspondentes a honorários por serviços prestados ao Sistema Único de Saúde por profissionais de saúde. | Isenta do imposto de renda os valores recebidos pelos profissionais de saúde pela prestação de serviços ao SUS. | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 | Ao arquivo | 7913161 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  LEI FEDERAL ,  ISENÇÃO ,  TRIBUTOS ,  IMPOSTO DE RENDA ,  PESSOA FISICA ,  PROFISSÃO ,  SAUDE ,  HONORARIOS ,  PRESTAÇÃO DE SERVIÇO ,  SISTEMA UNICO DE SAUDE (SUS) . | Senador Alvaro Dias (PODEMOS/PR) | 2019-02-05 | 2019-02-11 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7714145 |
| 7714257 | 135137 | 7714257 | PL 576/2019 | PL 576/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 576 | Iniciadora | Não | 7371751 | 11 | NORMA_GERAL | Norma Geral | LEI | Concede isenção do Imposto sobre Produtos Industrializados (IPI), da contribuição para o PIS/PASEP e da COFINS incidentes sobre veículos para transporte coletivo de estudantes, quando adquiridos por Prefeituras Municipais e pelo Distrito Federal, bem como por profissionais autônomos e suas cooperativas habilitados e dedicados exclusivamente ao transporte escolar. | Isenta do Imposto sobre Produtos Industrializados (IPI), do PIS/PASEP e da COFINS, os veículos destinados a transporte coletivo de estudantes, quando adquiridos por Prefeituras Municipais, pelo Distrito Federal, por profissionais autônomos e suas cooperativas, habilitados e dedicados exclusivamente ao transporte escolar, na forma do regulamento. | 4 | ARQUIVO | Arquivada ao final da Legislatura (art. 332 do RISF) | ARQUIVADO_FIM_LEGISLATURA | 2022-12-21 | Ao arquivo | 7913002 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  CRIAÇÃO ,  LEI FEDERAL ,  ISENÇÃO ,  IMPOSTO SOBRE PRODUTOS INDUSTRIALIZADOS (IPI) ,  PROGRAMA DE INTEGRAÇÃO SOCIAL (PIS) ,  PROGRAMA DE FORMAÇÃO DO PATRIMONIO DO SERVIDOR PUBLICO (PASEP) ,  CONTRIBUIÇÃO PARA FINANCIAMENTO DA SEGURIDADE SOCIAL (COFINS) ,  VENDA ,  VEICULO AUTOMOTOR ,  TRANSPORTE COLETIVO ,  ESTUDANTE . | Senador Alvaro Dias (PODEMOS/PR) | 2019-02-05 | 2019-02-11 |  |  |  |  |  |  |  |  |  |  |  | 2019 | SP:7714257 |

## main.processos_relacionados_senado

_Query_: `SELECT * FROM "main"."processos_relacionados_senado" LIMIT 10;`

| id_processo_relacionado | id_processo | id_outro_processo | ano | casa_identificadora | ente_identificador | sigla | numero | sigla_ente_identificador | tipo_relacao | tramitando | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2978567 | 3230984 | 2012 | SF | Plenário do Senado Federal | RQS | 482 | PLEN | REFERENCIA | Não | 2007 |
| 2 | 2968939 | 3219261 | 2013 | SF | Plenário do Senado Federal | RQS | 597 | PLEN | REFERENCIA | Não | 2008 |
| 3 | 2970890 | 3219261 | 2013 | SF | Plenário do Senado Federal | RQS | 597 | PLEN | REFERENCIA | Não | 2008 |
| 4 | 1035192 | 2910736 | 2009 | SF | Plenário do Senado Federal | RQS | 1490 | PLEN | REFERENCIA | Não | 2009 |
| 5 | 2965245 | 3232356 | 2012 | SF | Plenário do Senado Federal | RQS | 354 | PLEN | REFERENCIA | Não | 2009 |
| 6 | 3021092 | 3252893 | 2009 | SF | Plenário do Senado Federal | RQS | 1596 | PLEN | REFERENCIA | Não | 2009 |
| 7 | 3333348 | 8063644 | 2021 | CN | Plenário do Congresso Nacional | RQN | 26 | PLEN | REFERENCIA | Não | 2009 |
| 8 | 2958548 | 3134536 | 2014 | SF | Senado Federal | R.S | 1 | SF | PROCESSADO | Não | 2010 |
| 9 | 2958841 | 3136821 | 2013 | SF | Senado Federal | R.S | 4 | SF | PROCESSADO | Não | 2010 |
| 10 | 3020085 | 8315340 | 2022 | SF | Comissão de Ciência, Tecnologia, Inovação, Comunicação e Informática | REQ | 34 | CCT | REFERENCIA | Não | 2010 |

## main.proposicoes_camara

_Query_: `SELECT * FROM "main"."proposicoes_camara" LIMIT 10;`

| id_proposicao | sigla_tipo | numero | ano | ementa | uri | year_snapshot | prop_tag | prop_label | prop_category |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2187087 | PL | 5029 | 2019 | Dispõe sobre a remuneração recebida por funcionário de partido político com recursos do fundo partidário e dá outras providências.

NOVA EMENTA: Altera as Leis n°s 9.096, de 19 de setembro de 1995, 9.504, de 30 setembro de 1997, 4.737, de 15 de julho de 1965 (Código Eleitoral), 13.831, de 17 de maio de 2019, e a Consolidação das Leis do Trabalho, aprovada pelo Decreto-Lei nº 5.452, de 1º de maio de 1943, para dispor sobre regras aplicadas às eleições; revoga dispositivo da Lei nº 13.488, de 6 de outubro de 2017; e dá outras providências. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2187087 | 2020 | CP:2187087 | PL 5029/2019 | PL |
| 2190408 | PL | 2 | 2019 | Proíbe o uso o nome e/ou título BÍBLIA ou BÍBLIA SAGRADA em qualquer publicação impressa e/ou eletrônica com conteúdo (livros, capítulos e versículos) diferente do já consagrado há milênios pelas diversas religiões Cristãs (Católicas, Evangélicas e outras que se orientam por este Livro - Bíblia) | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190408 | 2020 | CP:2190408 | PL 2/2019 | PL |
| 2190417 | PL | 10 | 2019 | Altera a Lei nº 7.210, de 11 de julho de 1984, para disciplinar o regime das visitas íntimas. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190417 | 2020 | CP:2190417 | PL 10/2019 | PL |
| 2190423 | PL | 15 | 2019 | Altera a Lei no 9.096, de 19 de setembro de 1995 (Lei dos Partidos Políticos), e a Lei no 9.504, de 30 de setembro de 1997 (Lei das Eleições), para dispor sobre a destinação dos recursos dos Fundos Partidário e Eleitoral, quando não utilizados total ou parcialmente pelos partidos políticos, permitindo que sejam destinados às áreas de educação, saúde e segurança. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190423 | 2020 | CP:2190423 | PL 15/2019 | PL |
| 2190450 | PL | 21 | 2019 | Dispõe sobre a garantia ao consumidor da disponibilização de mecanismos de segurança alternativos aos sistemas biométricos para controle de transações | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190450 | 2020 | CP:2190450 | PL 21/2019 | PL |
| 2190462 | PL | 32 | 2019 | Proíbe o uso da substância Caramelo IV nos refrigerantes, sucos, demais bebidas e produtos comestíveis no Brasil. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190462 | 2020 | CP:2190462 | PL 32/2019 | PL |
| 2190472 | PL | 39 | 2019 | Estabelece mecanismos de seguro para garantir o interesse público nos processos de licitação e a correta aplicação dos recursos públicos. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190472 | 2020 | CP:2190472 | PL 39/2019 | PL |
| 2190495 | PL | 62 | 2019 | Dispõe sobre a guarda dos animais de estimação nos casos de dissolução litigiosa da sociedade e do vínculo conjugal entre seus possuidores, e dá outras providências. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190495 | 2020 | CP:2190495 | PL 62/2019 | PL |
| 2190519 | PL | 76 | 2019 | Altera a Lei de Ação Popular, para instituir novas hipóteses de cabimento, regulamentar aspectos de tramitação e dá outras providências. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190519 | 2020 | CP:2190519 | PL 76/2019 | PL |
| 2190532 | PL | 89 | 2019 | Altera a Lei n. 12.529, de 30 de novembro de 2011, dispondo sobre a responsabilização civil e administrativa de pessoas jurídicas por corrupção privada. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2190532 | 2020 | CP:2190532 | PL 89/2019 | PL |

## main.providencias_senado

_Query_: `SELECT * FROM "main"."providencias_senado" LIMIT 10;`

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

## main.relatorias_senado

_Query_: `SELECT * FROM "main"."relatorias_senado" LIMIT 10;`

| id_relatoria | id_processo | codigo_materia | codigo_parlamentar | codigo_colegiado | codigo_tipo_colegiado | sigla_colegiado | nome_colegiado | autoria_processo | identificacao_processo | ementa_processo | numero_autuacao | tramitando | sigla_casa | casa_relator | descricao_tipo_relator | id_tipo_relator | descricao_tipo_encerramento | forma_tratamento_parlamentar | nome_parlamentar | nome_completo | sigla_partido_parlamentar | uf_parlamentar | sexo_parlamentar | email_parlamentar | url_foto_parlamentar | url_pagina_parlamentar | data_apresentacao_processo | data_designacao | data_destituicao | data_fim_colegiado | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7701594 | 663587 | 73682 | 53 | 834 | 21 | CDH | Comissão de Direitos Humanos e Legislação Participativa | Senador Paulo Paim (PT/RS) | PLS 169/2005 | Altera dispositivo da Lei nº 10.741, de 1º de outubro de 2003, que dispõe sobre o Estatuto do Idoso e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Redistribuição | Senador | Leomar Quintanilha | Leomar de Melo Quintanilha | MDB | TO | M | leomar@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador53.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/53 | 2005-05-12 00:00:00 | 2005-05-17 00:00:00 | 2006-05-24 00:00:00 |  | 2005 |
| 7692977 | 663587 | 73682 | 3 | 834 | 21 | CDH | Comissão de Direitos Humanos e Legislação Participativa | Senador Paulo Paim (PT/RS) | PLS 169/2005 | Altera dispositivo da Lei nº 10.741, de 1º de outubro de 2003, que dispõe sobre o Estatuto do Idoso e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Redistribuição | Senador | Antonio Carlos Valadares | Antonio Carlos Valadares | PSB | SE | M | antoniocarlosvaladares@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3 | 2005-05-12 00:00:00 | 2006-05-31 00:00:00 | 2007-02-07 00:00:00 |  | 2006 |
| 7698040 | 663587 | 73682 | 345 | 834 | 21 | CDH | Comissão de Direitos Humanos e Legislação Participativa | Senador Paulo Paim (PT/RS) | PLS 169/2005 | Altera dispositivo da Lei nº 10.741, de 1º de outubro de 2003, que dispõe sobre o Estatuto do Idoso e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Parecer Oferecido | Senador | Flávio Arns | Flávio José Arns | PT | PR | M | sen.flavioarns@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador345.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/345 | 2005-05-12 00:00:00 | 2007-04-26 00:00:00 | 2007-05-10 00:00:00 |  | 2007 |
| 7698764 | 663587 | 73682 | 3393 | 834 | 21 | CDH | Comissão de Direitos Humanos e Legislação Participativa | Senador Paulo Paim (PT/RS) | PLS 169/2005 | Altera dispositivo da Lei nº 10.741, de 1º de outubro de 2003, que dispõe sobre o Estatuto do Idoso e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Substituído por "ad hoc" | Senador | Papaléo Paes | João Bosco Papaléo Paes | PSDB | AP | M | gab.papaleopaes@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3393.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3393 | 2005-05-12 00:00:00 | 2007-02-08 00:00:00 | 2007-04-26 00:00:00 |  | 2007 |
| 7692575 | 2970890 | 86332 | 3372 | 40 | 21 | CAS | Comissão de Assuntos Sociais | Senador Alvaro Dias (PSDB/PR) | PLS 260/2008 | Altera o § 1º do art. 12 da Lei nº 8.212, de 24 de julho de 1991, e o § 1º do art. 11 da Lei nº 8.213, de 24 de julho de 1991, acrescentando-lhe § 6º, para permitir a contratação eventual de empregados, pelos segurados especiais, e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Fim de Legislatura | Senador | Valdir Raupp | Valdir Raupp de Matos | MDB | RO | M | valdir.raupp@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3372.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3372 | 2008-07-01 00:00:00 | 2008-12-03 00:00:00 | 2010-12-22 00:00:00 |  | 2008 |
| 7693176 | 2970890 | 86332 | 4774 | 1307 | 21 | CRA | Comissão de Agricultura e Reforma Agrária | Senador Alvaro Dias (PSDB/PR) | PLS 260/2008 | Altera o § 1º do art. 12 da Lei nº 8.212, de 24 de julho de 1991, e o § 1º do art. 11 da Lei nº 8.213, de 24 de julho de 1991, acrescentando-lhe § 6º, para permitir a contratação eventual de empregados, pelos segurados especiais, e dá outras providências. | 1 | N | SF | SF | Relator Ad hoc | 3 | Parecer Oferecido | Senador | João Pedro | João Pedro Gonçalves da Costa | PT | AM | M | joaopedro@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador4774.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/4774 | 2008-07-01 00:00:00 | 2008-11-12 00:00:00 | 2008-11-26 00:00:00 |  | 2008 |
| 7694148 | 2970890 | 86332 | 3432 | 1307 | 21 | CRA | Comissão de Agricultura e Reforma Agrária | Senador Alvaro Dias (PSDB/PR) | PLS 260/2008 | Altera o § 1º do art. 12 da Lei nº 8.212, de 24 de julho de 1991, e o § 1º do art. 11 da Lei nº 8.213, de 24 de julho de 1991, acrescentando-lhe § 6º, para permitir a contratação eventual de empregados, pelos segurados especiais, e dá outras providências. | 1 | N | SF | SF | Relator | 1 | Substituído por "ad hoc" | Senador | Augusto Botelho | Augusto Affonso Botelho Neto | PT | RR | M | augusto.botelho@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3432.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3432 | 2008-07-01 00:00:00 | 2008-07-08 00:00:00 | 2008-11-12 00:00:00 |  | 2008 |
| 7690304 | 1035192 | 90433 | 3579 | 1363 | 21 | CCT | Comissão de Ciência, Tecnologia, Inovação e Informática | Câmara dos Deputados | PDS 181/2009 | Aprova o ato que outorga permissão à RÁDIO E TV FAROL DA COMUNICAÇÃO LTDA. para explorar serviço de radiodifusão sonora em frequência modulada na cidade de Turilândia, Estado do Maranhão. | 1 | N | SF | SF | Relator | 1 | Deliberação da matéria | Senador | Lobão Filho | Edison Lobão Filho | MDB | MA | M | lobaofilho@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3579.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3579 | 2009-04-14 00:00:00 | 2009-04-28 00:00:00 | 2009-11-04 00:00:00 |  | 2009 |
| 7689207 | 2965245 | 91380 | 3396 | 34 | 21 | CCJ | Comissão de Constituição, Justiça e Cidadania | Senador Alvaro Dias (PSDB/PR) | PLS 230/2009 | Altera a Lei Complementar nº 101, de 4 de maio de 2000, que estabelece normas de finanças públicas voltadas para a responsabilidade na gestão fiscal e dá outras providências, para exigir compensações no caso de atos de concessão ou ampliação de incentivos ou benefícios de natureza tributária que impliquem redução dos montantes financeiros repartidos com os Estados, o Distrito Federal e os Municípios. | 1 | N | SF | SF | Relator | 1 | Fim de Legislatura | Senador | Tasso Jereissati | Tasso Ribeiro Jereissati | PSDB | CE | M | sen.tassojereissati@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3396.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3396 | 2009-06-01 00:00:00 | 2009-06-09 00:00:00 | 2010-12-22 00:00:00 |  | 2009 |
| 7690666 | 2968939 | 88039 | 73 | 34 | 21 | CCJ | Comissão de Constituição, Justiça e Cidadania | Senador Paulo Paim (PT/RS) | PLS 413/2008 | Altera a Lei Nº 8.213 de 24 de junho de 1991, que dispõe sobre os Planos de Benefícios da Previdência Social e dá outras providências, para concessão de aposentadoria especial ao segurado que tiver trabalhado em atividade penosa, insalubre ou perigosa, que coloque em risco a saúde e a integridade física. | 1 | N | SF | SF | Relator | 1 | Fim de Legislatura | Senador | Romero Jucá | Romero Jucá Filho | MDB | RR | M | romero.juca@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador73.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/73 | 2008-11-03 00:00:00 | 2009-04-07 00:00:00 | 2010-12-22 00:00:00 |  | 2009 |

## main.situacoes_senado

_Query_: `SELECT * FROM "main"."situacoes_senado" LIMIT 10;`

| id_situacao | id_processo | numero_autuacao | id_tipo_situacao | sigla_situacao | descricao_situacao | data_inicio | data_fim | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2526458 | 1 | 48 | RVGA | REVOGADA | 2024-11-21 |  | 2001 |
| 2 | 663587 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 |  | 2005 |
| 3 | 1066060 | 1 | 43 | PRJDA | PREJUDICADA | 2021-09-20 |  | 2007 |
| 4 | 2978567 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 | 2025-08-14 | 2007 |
| 5 | 2968939 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 | 2025-07-10 | 2008 |
| 6 | 2970890 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 | 2025-07-22 | 2008 |
| 7 | 1035192 | 1 | 64 | TNJR | TRANSFORMADA EM NORMA JURÍDICA | 2022-04-14 |  | 2009 |
| 8 | 2965245 | 1 | 28 | ARQVD | ARQUIVADA AO FINAL DA LEGISLATURA | 2022-12-22 |  | 2009 |
| 9 | 3021092 | 1 | 64 | TNJR | TRANSFORMADA EM NORMA JURÍDICA | 2022-08-05 |  | 2009 |
| 10 | 3333348 | 1 | 184 | VETDELIB | VETO DELIBERADO PELO PLENÁRIO | 2021-04-19 |  | 2009 |

## main.temas_camara

_Query_: `SELECT * FROM "main"."temas_camara" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."tipo_colegiado_senado" LIMIT 10;`

| codigo_tipo_colegiado | codigo_natureza_colegiado | descricao_tipo_colegiado | indicador_ativo | sigla_casa | sigla_tipo_colegiado | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | 1 | Comissão Permanente | S | SF | PERMANENTE | 2023 |
| 121 | 2 | Comissão Temporária Externa | S | SF | CT | 2025 |

## main.tipo_conteudo_senado

_Query_: `SELECT * FROM "main"."tipo_conteudo_senado" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."tipo_deliberacao_senado" LIMIT 10;`

| sigla_tipo_deliberacao | descricao_tipo_deliberacao | id_destino | sigla_destino | destino | year_snapshot |
| --- | --- | --- | --- | --- | --- |
| ARQUIVADO_FIM_LEGISLATURA | Arquivada ao final da Legislatura (art. 332 do RISF) | 4 | ARQUIVO | Ao arquivo | 2022 |
| REJEITADO_COMISSAO_TERM | Rejeitada por Comissão em decisão terminativa (art. 91, § 5º, do RISF) | 4 | ARQUIVO | Ao arquivo | 2023 |
| APROVADA_NO_PLENARIO | Aprovada pelo Plenário | 1 | CAMARA | À Câmara dos Deputados | 2024 |
| APROVADA_EM_COMISSAO_TERMINATIVA | Aprovada por Comissão em decisão terminativa | 1 | CAMARA | À Câmara dos Deputados | 2024 |
| PREJUDICADO | Prejudicada | 4 | ARQUIVO | Ao arquivo | 2024 |
| RETIRADO_PELO_AUTOR | Retirada pelo autor | 4 | ARQUIVO | Ao arquivo | 2024 |
| DEFERIDO_CDIR | Deferida pela Comissão Diretora | 4 | ARQUIVO | Ao arquivo | 2024 |
| CONHECIDA | Conhecida | 4 | ARQUIVO | Ao arquivo | 2024 |
| TRANSF_PROJ_DECRETO_LEG | Transformada em Projeto de Decreto Legislativo |  |  |  | 2023 |
| INADIMITIDA_MATE | Inadmitida |  |  |  | 2023 |

## main.tipo_emendas_senado

_Query_: `SELECT * FROM "main"."tipo_emendas_senado" LIMIT 10;`

| tipo_emenda | year_snapshot |
| --- | --- |
| EMENDA_PARCIAL | 2024 |
| EMENDA_TOTAL | 2024 |

## main.tramitacoes_camara

_Query_: `SELECT * FROM "main"."tramitacoes_camara" LIMIT 10;`

| id_tramitacao | id_proposicao | ambito | apreciacao | cod_situacao | cod_tipo_tramitacao | data_hora | descricao_situacao | descricao_tramitacao | despacho | regime | sequencia | sigla_orgao | uri_orgao | uri_ultimo_relator | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 15009 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 70/1995 nos termos do art. 105 do RICD, desapense-se do PL 70/1995 o PL 2976/2008, o PL 1281/2011, o PL 4241/2012, o PL 4870/2016 e o PL 2232/2020, e, em seguida, apense-os ao PL 5872/2005. | Prioridade (Art. 151, II, RICD) | 52 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/73654 | 2020 |
| 2 | 15532 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 505/1991 nos termos do art. 105 do RICD, desapense-se do PL 505/1991 o PL 5448/2005, o PL 1982/2007, o PL 3484/2008, o PL 6185/2009, o PL 7087/2010, o PL 7362/2010, o PL 7488/2010, o PL 4043/2012, o PL 6823/2013, o PL 681/2015, o PL 3284/2015, o PL 6170/2016, o PL 6436/2016, o PL 10506/2018, o PL 1059/2019, o PL 2975/2019 e o PL 2152/2020, e, em seguida, apense-os ao PL 687/2003. | Ordinário (Art. 151, III, RICD) | 215 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/73463 | 2020 |
| 3 | 15749 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 693/1999 nos termos do art. 105 do RICD, desapense-se do PL 693/1999 o PL 7174/2014, o PL 7412/2014, o PL 7842/2017, o PL 9134/2017, o PL 5975/2019, o PL 5327/2020 e o PL 1340/2021, e, em seguida, apense-os ao PL 4353/2012. | Ordinário (Art. 151, III, RICD) | 178 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/116379 | 2020 |
| 4 | 15990 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 502 | 2023-01-31 00:00:00 | Arquivada | Arquivamento | Arquivado nos termos do Artigo 105 do Regimento Interno da Câmara dos Deputados. | Especial (Arts. 142 e 143, RCCN) | 40 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/98057 | 2020 |
| 5 | 16481 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 1258/1995 nos termos do art. 105 do RICD, desapense-se do PL 1258/1995 o PL 195/2003, o PL 2114/2003, o PL 4323/2004, o PL 43/2007, o PL 432/2007, o PL 1303/2007, o PL 1443/2007, o PL 2841/2008, o PL 3272/2008, o PL 3577/2008, o PL 3579/2008, o PL 4047/2008, o PL 4155/2008, o PL 4192/2008, o PL 5285/2009, o PL 891/2011, o PL 4214/2012, o PL 6577/2013, o PL 4677/2016, o PL 63/2020 e o PL 3372/2021, e, em seguida, apense-os ao PL 173/2003. | Prioridade (Art. 151, II, RICD) | 147 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/73460 | 2020 |
| 6 | 16969 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 1610/1996 nos termos do art. 105 do RICD, desapense-se do PL 1610/1996 o PL 5265/2009, o PL 3509/2015, o PL 5335/2016, o PL 4447/2019 e o PL 1737/2020, e, em seguida, apense-os ao PL 7099/2006. | Prioridade (Art. 151, II, RICD) | 176 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/141417 | 2020 |
| 7 | 17563 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 2051/1996 nos termos do art. 105 do RICD, desapense-se o PL 4785/2009 do PL 2051/1996. Em decorrência disso, distribua-se o PL 4785/2009 às comissões de Relações Exteriores e de Defesa Nacional; Educação; Seguridade Social e Família; Finanças e Tributação (Art. 54, RICD); e Constituição e Justiça e de Cidadania (Art. 54, RICD). Proposição Sujeita à Apreciação do Plenário. Prioridade (Art. 151, II, RICD). | Prioridade (Art. 151, II, RICD) | 174 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/159237 | 2020 |
| 8 | 17823 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II |  | 1010 | 2020-01-10 00:00:00 |  | Devolução à CCP | Devolução à CCP | Ordinário (Art. 151, III, RICD) | 113 | CSAUDE | https://dadosabertos.camara.leg.br/api/v2/orgaos/2014 | https://dadosabertos.camara.leg.br/api/v2/deputados/164360 | 2020 |
| 9 | 17915 | Regimental | Proposição Sujeita à Apreciação do Plenário | 923 | 505 | 2023-01-31 00:00:00 | Arquivada | Notificação de Desapensação | Devido ao arquivamento do PL 2295/2000 nos termos do art. 105 do RICD, desapense-se do PL 2295/2000 o PL 1313/2019, o PL 1384/2019 e o PL 1607/2019, e, em seguida, apense-os ao PL 6091/2016. | Urgência (Art. 155, RICD) | 493 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/141451 | 2020 |
| 10 | 18420 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II |  | 1010 | 2020-01-30 00:00:00 |  | Devolução à CCP | Devolução à CCP | Ordinário (Art. 151, III, RICD) | 124 | CSAUDE | https://dadosabertos.camara.leg.br/api/v2/orgaos/2014 | https://dadosabertos.camara.leg.br/api/v2/deputados/178923 | 2020 |

## main.unidades_destinatarias_senado

_Query_: `SELECT * FROM "main"."unidades_destinatarias_senado" LIMIT 10;`

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

_Query_: `SELECT * FROM "main"."votacoes_camara" LIMIT 10;`

| id_votacao | id_proposicao | data | descricao | aprovacao | uri_evento | uri_orgao | uri | year_snapshot | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1006386-48 | 1006386 | 2018-08-14 | Aprovado o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/53552 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2002 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1006386-48 | 2021 | 1 |
| 1048959-27 | 1048959 | 2015-09-16 | Aprovado por Unanimidade o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/40973 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2001 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1048959-27 | 2020 | 1 |
| 1050804-2 | 14562 | 2015-03-26 | Aprovado, transformado em convite. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/38333 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537363 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1050804-2 | 2023 | 1 |
| 1050852-8 | 581206 | 2015-03-30 | Rejeitado o Requerimento de Urgência (Art. 155 do RICD). Sim: 216; Não: 181; abstenção: 1; total: 398 . | False | https://dadosabertos.camara.leg.br/api/v2/eventos/38389 | https://dadosabertos.camara.leg.br/api/v2/orgaos/180 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1050852-8 | 2021 | 1 |
| 106586-30 | 106586 | 2003-12-10 | Aprovado por Unanimidade o Parecer | True | https://dadosabertos.camara.leg.br/api/v2/eventos/5880 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2004 | https://dadosabertos.camara.leg.br/api/v2/votacoes/106586-30 | 2022 | 1 |
| 106586-71 | 106586 | 2006-05-17 | Aprovado por Unanimidade o Parecer com Complementação de Voto | True | https://dadosabertos.camara.leg.br/api/v2/eventos/12911 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/106586-71 | 2022 | 1 |
| 1116134-23 | 1116134 | 2015-07-15 | Aprovado por Unanimidade o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/40010 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2001 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1116134-23 | 2021 | 1 |
| 113531-50 | 113531 | 2004-08-25 | Aprovado o Parecer, apresentou voto em separado o Deputado Edmar Moreira | True | https://dadosabertos.camara.leg.br/api/v2/eventos/7596 | https://dadosabertos.camara.leg.br/api/v2/orgaos/5503 | https://dadosabertos.camara.leg.br/api/v2/votacoes/113531-50 | 2020 | 1 |
| 114808-39 | 114808 | 2008-10-29 | Aprovado por Unanimidade o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/18966 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2015 | https://dadosabertos.camara.leg.br/api/v2/votacoes/114808-39 | 2021 | 1 |
| 1191094-122 | 1191094 | 2019-09-19 | Aprovada a Redação Final. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/57377 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1191094-122 | 2023 | 1 |

## main.votacoes_senado

_Query_: `SELECT * FROM "main"."votacoes_senado" LIMIT 10;`

| id_votacao | id_materia | id_processo | identificacao | sigla | numero | ano | codigo_sessao | numero_sessao | sequencial_sessao | sigla_tipo_sessao | casa_sessao | codigo_sessao_legislativa | data_apresentacao | data_sessao | descricao_votacao | ementa | resultado_votacao | total_votos_sim | total_votos_nao | total_votos_abstencao | votacao_secreta | id_informe | id_evento | codigo_colegiado | nome_colegiado | sigla_colegiado | data_informe | texto_informe | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5481 | 121994 | 1399048 | PEC 83/2015 | PEC | 83 | 2015 | 22254 | 176 | 3 | DOR | SF | 850 | 2015-06-25 00:00:00 | 2015-10-06 00:00:00 | Votação nominal da Emenda nº 15-CCJ (Substituvivo) | Acrescenta o art. 166-A à Constituição Federal, para dispor sobre a Autoridade Fiscal Independente. |  |  |  |  | N | 1881857 | 9815176 |  |  |  | 2015-10-06 00:00:01 | Anunciada a votação da matéria, em primeiro turno, usam da palavra o Senador José Serra, Relator, e o Senador Delcídio do Amaral; tendo o Relator proposto Adendo ao Substitutivo da CCJ.
A seguir, usam da palavra os Senadores Lindbergh Farias, Roberto Requião, Randolfe Rodrigues, Vanessa Grazziotin, Waldemir Moka, Blairo Maggi, Telmário Mota, Lúcia Vânia, Rose de Freitas e Magno Malta.  
Rejeitado, em primeiro turno, o Substitutivo (Emenda nº 15-CCJ), com o Adendo proposto pelo Senador José Serra, Relator, nesta oportunidade, com o seguinte resultado: Sim 40, Não 19, Abst. 02, Presidente 01, Total 62. 
      
 | 2015 |
| 5554 | 123909 | 3036223 | PEC 143/2015 | PEC | 143 | 2015 | 22507 | 50 | 1 | DOR | SF | 853 | 2015-11-04 00:00:00 | 2016-04-13 00:00:00 | Votação nominal da Emenda nº 1 - CCJ (Substitutivo) com alteração proposta pelo relator à PEC 143/2015, em primeiro turno. Acrescenta os artigos 101 e 102 ao Ato das Disposições Constitucionais Transitórias para instituir a desvinculação de receitas dos Estados, do Distrito Federal e dos Municípios. | Acrescenta os arts. 101 e 102 ao Ato das Disposições Constitucionais Transitórias para instituir a desvinculação de receitas dos Estados, do Distrito Federal e dos Municípios. | A |  |  |  | N | 1904012 | 9848989 | 1998 | Plenário do Senado Federal | PLEN | 2016-04-13 00:00:01 | (Matéria constante do item 4 da Ordem do Dia, apreciado em 1º lugar, com aquiescência do Plenário)
Anunciada a matéria, usam da palavra os Senadores Randolfe Rodrigues, Reguffe, Lindbergh Farias, José Pimentel, Dalírio Beber, Antônio Carlos Valadares, Romero Jucá (relator), Marta Suplicy, Roberto Requião, Fátima Bezerra, Blairo Maggi e Waldemir Moka.
O Senador Romero Jucá (Relator) propõe adequação no texto para dispor sobre o prazo de vigência da proposta. 
Continuam no uso da palavra os Senadores Aloysio Nunes Ferreira, Garibaldi Alves Filho, Randolfe Rodrigues, Cristovam Buarque e Reguffe.
Aprovada a Emenda nº 1- CCJ (Substitutiva), em primeiro turno, com adequação do relator proposta em Plenário, com o seguinte resultado: Sim - 53; Não - 17; Presidente - 1; Total - 71, tendo usado da palavra a Senadora Lúcia Vânia, os Senadores José Pimentel, Ronaldo Caiado, João Capiberibe, Otto Alencar, Randolfe Rodrigues, José Agripino e Cristovam Buarque.
Leitura do Parecer nº 438, de 2016 – CDIR, oferecendo a redação para o segundo turno.
(Tendo sido aprovado calendário especial para a proposta, passa-se a imediata apreciação em 2º turno)
Encerrada a discussão, em segundo turno.
A proposta constará da Ordem do Dia da próxima sessão deliberativa para votação. | 2016 |
| 5708 | 128035 | 4985566 | PEC 2/2017 | PEC | 2 | 2017 | 41887 | 75 | 1 | DOR | SF | 854 | 2017-02-08 00:00:00 | 2017-05-30 00:00:00 | Votação que altera o §1º do artigo 31 e o artigo 75 da Constituição Federal para estabelecer os Tribunais de Contas como órgãos permanentes e essenciais ao controle externo da administração pública. | Altera o § 1º do art. 31 e o art. 75 da Constituição Federal para estabelecer os Tribunais de Contas como órgãos permanentes e essenciais ao controle externo da administração pública. |  |  |  |  | N | 1944735 | 9927212 | 1998 | Plenário do Senado Federal | PLEN | 2017-05-30 00:00:01 | Aprovada em primeiro turno, com o seguinte resultado: Sim 50, Não 20, Abst. 03, Presidente 1, Total 74.
A matéria constará da Ordem do Dia oportunamente, para o segundo turno constitucional. | 2017 |
| 5960 | 127414 | 3035168 | PEC 57/2016 | PEC | 57 | 2016 | 95294 | 65 | 1 | DOR | SF | 858 | 2016-11-08 00:00:00 | 2019-05-07 00:00:00 | PEC nº 57, de 2016, com as Emendas nºs 1 a 6 - CCJ, nos termos do Parecer (1º Turno) | Altera os arts. 30, 37, 146, 150, 179 e 195 da Constituição Federal para prever que lei complementar conceituará pequeno Município, poderá disciplinar os princípios da Administração Pública e as normas gerais aplicáveis ao processo administrativo fiscal, à substituição tributária, à moralidade tributária, à eficiência tributária e à vedação de confisco, e ao estabelecimento do estatuto de defesa dos direitos contribuintes; dá nova disciplina ao princípio da anterioridade; elimina a exigência de certidão negativa dos débitos previdenciários para participação em procedimentos licitatórios e contratação com o setor público; e fixa a obrigatoriedade de especificação de tratamento diferenciado e simplificado das microempresas e empresas de pequeno porte no âmbito das normas de caráter geral aplicáveis às empresas. | A | 68 | 0 | 0 | N | 1940240 | 9917858 | 1998 | Plenário do Senado Federal | PLEN | 2019-05-07 00:00:01 | Aprovada a Proposta e as Emendas nºs 1 a 6-CCJ, em primeiro turno, com o seguinte resultado: Sim 68, Presidente 1, Total 69. | 2019 |
| 5965 | 129887 | 5377266 | PEC 26/2017 | PEC | 26 | 2017 | 102966 | 89 | 1 | DOR | SF | 858 | 2017-06-29 00:00:00 | 2019-06-04 00:00:00 | PEC nº 26, de 2017, com a Emenda nº 1 - CCJ, nos termos do Parecer (1º Turno) | Acrescenta o art. 75-A à Constituição Federal, para dispor sobre a criação de um sistema de avaliação de políticas públicas. | A | 55 | 0 | 0 | N | 1960909 | 9956542 | 1998 | Plenário do Senado Federal | PLEN | 2019-06-04 00:00:01 | Aprovada a proposta, em primeiro turno, com o seguinte resultado: Sim 55, Presidente 1, Total 56.
A matéria constará da Ordem do Dia oportunamente, para apreciação em segundo turno.
(A PEC é aprovada nesta data, em primeiro turno, com a Emenda nº 1-CCJ) | 2019 |
| 6075 | 124513 | 573632 | PLS 796/2015 | PLS | 796 | 2015 | 155306 | 5 | 1 | DOR | SF | 863 | 2015-12-17 00:00:00 | 2020-02-11 00:00:00 | Estende a estabilidade provisória no emprego para as empregadas adotantes ou que venham a obter a guarda judicial para fins de adoção. | Altera a redação do art. 1º da Lei Complementar nº 146, de 25 de junho de 2014, para estender a estabilidade provisória no emprego para as empregadas adotantes ou que venham a obter a guarda judicial para fins de adoção. | A |  |  |  | N | 1911617 | 9861624 | 1998 | Plenário do Senado Federal | PLEN | 2020-02-11 00:00:01 | Discussão encerrada.
Aprovado o Substitutivo - Emenda nº 1-CCJ, com o seguinte resultado: Sim 69, Não 1, Presidente 1, Total 71; ficando prejudicado o projeto.
Encaminhado à publicação o Parecer nº 4, de 2020-PLEN, da CDIR, apresentando a redação para o turno suplementar.
Discussão encerrada no turno suplementar sem apresentação de emendas, sendo o Substitutivo adotado definitivamente, sem votação, nos termos do art. 284, do RISF.
À Câmara dos Deputados. | 2020 |
| 6248 | 135147 | 7716769 | PLP 19/2019 | PLP | 19 | 2019 | 199976 | 96 | 2 | SDR | SF | 863 | 2019-02-06 00:00:00 | 2020-11-03 00:00:00 | Votação da Emenda nº 18 - PLEN (Substitutivo) do Relator ao PLP nº 19, de 2019, ressalvado o destaque. | Dispõe sobre nomeação e demissão do Presidente e diretores do Banco Central do Brasil. | A |  |  |  | N | 2041705 | 10130692 | 1998 | Plenário do Senado Federal | PLEN | 2020-11-03 22:42:29 | (Sessão Deliberativa Remota realizada em 03/11/2020) 
Encaminhadas à publicação as Emendas nºs 6 a 17 – PLEN. 
Proferido pelo Senador Telmário Mota o Parecer nº 157/2020-PLEN/SF, concluindo pela aprovação do PLP nº 19/2019; acatando as Emendas nºs 7 e 8 - PLEN, parcialmente, as Emendas nºs 10, 12, 15 e 17 - PLEN; e pela rejeição das Emendas nºs 6, 9, 11, 13, 14 e 16- PLEN, na forma da Emenda nº 18 – PLEN (Substitutivo). 
Encaminhados à publicação e deferidos os seguintes requerimentos:  
- nº 2606/2020, da liderança do PT, solicitando destaque para votação em separado da Emenda nº 12 – PLEN; 
- nº 2612/2020, da Liderança do Podemos, solicitando destaque para votação em separado, dos termos "administrativa e financeira" do caput do art. 6º, bem como do § 1º do art. 6º do substitutivo (retirado posteriormente); e  
- n 2618/2020, da Liderança do PSD, solicitando destaque para votação em separado Emenda nº 7 – PLEN (retirado posteriormente). 
Aprovado o Substitutivo, ressalvado o destaque, nos termos do Parecer nº 157/2020, com os ajustes apresentados pelo Relator, com o seguinte resultado: Sim - 56; Não - 12, Abst. - 1, Total - 69.  
Ficam prejudicados o projeto e as demais emendas a ele apresentadas. 
Rejeitada a Emenda nº 12 – PLEN, destacada, com o seguinte resultado: Sim - 12; Não - 50; Pres. - 1; Total - 63.  
Encerrada a discussão, sem emendas, o Substitutivo é dado como definitivamente adotado, sem votação. 
A consolidação do texto e as adequações de técnica legislativa serão apostas aos autógrafos da matéria, dispensada a redação final. 
A matéria vai à Câmara dos Deputados. 
(Encaminhados à publicação os Requerimentos nºs 2611, 2614, 2616, 2619 e 2620, de 2020) | 2020 |
| 6249 | 135147 | 7716769 | PLP 19/2019 | PLP | 19 | 2019 | 199976 | 96 | 3 | SDR | SF | 863 | 2019-02-06 00:00:00 | 2020-11-03 00:00:00 | Votação da Emenda nº 12 - PLEN ao Projeto de Lei Complementar nº 19, de 2019, destacada. | Dispõe sobre nomeação e demissão do Presidente e diretores do Banco Central do Brasil. | A |  |  |  | N | 2041705 | 10130692 | 1998 | Plenário do Senado Federal | PLEN | 2020-11-03 22:42:29 | (Sessão Deliberativa Remota realizada em 03/11/2020) 
Encaminhadas à publicação as Emendas nºs 6 a 17 – PLEN. 
Proferido pelo Senador Telmário Mota o Parecer nº 157/2020-PLEN/SF, concluindo pela aprovação do PLP nº 19/2019; acatando as Emendas nºs 7 e 8 - PLEN, parcialmente, as Emendas nºs 10, 12, 15 e 17 - PLEN; e pela rejeição das Emendas nºs 6, 9, 11, 13, 14 e 16- PLEN, na forma da Emenda nº 18 – PLEN (Substitutivo). 
Encaminhados à publicação e deferidos os seguintes requerimentos:  
- nº 2606/2020, da liderança do PT, solicitando destaque para votação em separado da Emenda nº 12 – PLEN; 
- nº 2612/2020, da Liderança do Podemos, solicitando destaque para votação em separado, dos termos "administrativa e financeira" do caput do art. 6º, bem como do § 1º do art. 6º do substitutivo (retirado posteriormente); e  
- n 2618/2020, da Liderança do PSD, solicitando destaque para votação em separado Emenda nº 7 – PLEN (retirado posteriormente). 
Aprovado o Substitutivo, ressalvado o destaque, nos termos do Parecer nº 157/2020, com os ajustes apresentados pelo Relator, com o seguinte resultado: Sim - 56; Não - 12, Abst. - 1, Total - 69.  
Ficam prejudicados o projeto e as demais emendas a ele apresentadas. 
Rejeitada a Emenda nº 12 – PLEN, destacada, com o seguinte resultado: Sim - 12; Não - 50; Pres. - 1; Total - 63.  
Encerrada a discussão, sem emendas, o Substitutivo é dado como definitivamente adotado, sem votação. 
A consolidação do texto e as adequações de técnica legislativa serão apostas aos autógrafos da matéria, dispensada a redação final. 
A matéria vai à Câmara dos Deputados. 
(Encaminhados à publicação os Requerimentos nºs 2611, 2614, 2616, 2619 e 2620, de 2020) | 2020 |
| 6076 | 139427 | 7826311 | MPV 899/2019 | MPV | 899 | 2019 | 162448 | 23 | 1 | SDR | SF | 863 | 2019-10-17 00:00:00 | 2020-03-24 00:00:00 | Votação do PLV n. 2, de 2020 | Dispõe sobre a transação nas hipóteses que especifica. | A |  |  |  | N | 2026084 | 10080776 |  |  |  | 2020-03-24 00:00:01 | (Sessão Deliberativa Remota)
Aprovado o PLV nº 2, de 2020, sendo impugnado o art. 28. 
À sanção.
(DETALHAMENTO DA AÇÃO LEGISLATIVA)
(Sessão Deliberativa Remota realizada em 24/03/2020)
Encaminhados à publicação os seguintes Requerimentos:
- nº 138, de 2020, de autoria do Senador Fabiano Contarato, que solicita a impugnação do artigo 28 do PLV nº 2, de 2020, por tratar de matéria estranha à Medida Provisória nº 899, de 2019;
- nº 139, de 2020, de autoria do Senador Carlos Viana, que solicita a impugnação das alterações promovidas nos artigos 6º e 14 da Lei 13.464, de 2017, com redação dada pelo art. 28 do PLV nº 2, de 2020, por tratarem de matérias estranhas à Medida Provisória nº 899, de 2019;
- nº 140, de 2020, deautoria do Senador Chico Rodrigues, que solicita a impugnação da redação dada pelo art. 28 do PLV nº 2, de 2020, por tratarem de matérias estranhas à Medida Provisória nº 899, de 2019;
- nº 141/2020, de autoria do Senador Alessandro Vieira, que solicita a impugnação do art. 24 do PLVnº 2/2020. (Retirado pelo autor)
- nº 142, de 2020, de autoria do Senador Alessandro Vieira, que solicita a impugnação do art. 29 do PLV 2, de 2020; e 28 do PLV nº 2, de 2020, por tratar de matéria estranha à Medida Provisória nº 899, de 2019.
- nº 145/2020, da Liderança do PT, que solicita destaque para votação em separado do art. 29 do PLVnº 2/2020.
A Presidência anuncia a apreciação da impugnação do art. 28 do PLV – Requerimentos nºs 138, 139, 140 e 144/2020
A Presidência concorda com a impugnação do art. 28 do PLV abrindo espaço para recursos a sua decisão.
Declarado como não escrito o artigo 28 do PLV nº 2, de 2020, por tratar de matéria estranha à Medida Provisória nº 899, de 2019.
A Presidência anuncia a apreciação do Requerimento que solicita impugnação do art. 29 do PLV – Requerimento nº 142/2020
A Presidência concorda com a impugnação do art. 29, abrindo espaço para recurso a sua decisão.
Fica mantido o art. 29 no texto do PLV, com o seguinte resultado:Sim: 50, Não:28, Total: 79.
A Presidência anuncia a retirada, pela Liderança do PT, do Requerimento nº 145, de 2020.
Discussão encerrada.
Aprovados os pressupostos constitucionais de relevância e urgência, adequação financeira e orçamentária, pertinência temática da matéria remanescente e, quanto ao mérito, pela apreciação do PLV 2/2020.
Aprovado o PLV 2/2020, com impugnação do art. 28, com o seguinte resultado: Sim: 77; Presidente: 1; Total:78.
Ficam prejudicadas a medida provisória e as emendas a ela apresentadas.
À sanção. | 2020 |
| 6086 | 139736 | 7834698 | MPV 903/2019 | MPV | 903 | 2019 | 167009 | 32 | 1 | SDR | SF | 863 | 2019-11-07 00:00:00 | 2020-04-14 00:00:00 | Votação da Medida Provisória nº 903, de 2019. | Autoriza a prorrogação de contratos por tempo determinado do Ministério da Agricultura, Pecuária e Abastecimento. | A |  |  |  | N | 2035393 | 10100072 |  |  |  | 2020-04-08 00:00:01 | Incluída em ordem do dia da sessão deliberativa remota de 14/04/2020. | 2020 |

## main.votos_camara

_Query_: `SELECT * FROM "main"."votos_camara" LIMIT 10;`

| id_voto | id_votacao | id_deputado | tipo_voto | data_hora | year_snapshot |
| --- | --- | --- | --- | --- | --- |
| 1 | 1050795-6 | 4930 | Não | 2015-03-24 18:11:10 | 2021 |
| 2 | 1050795-6 | 4931 | Não | 2015-03-24 18:18:25 | 2021 |
| 3 | 1050795-6 | 62881 | Sim | 2015-03-24 18:07:57 | 2021 |
| 4 | 1050795-6 | 64960 | Sim | 2015-03-24 18:30:38 | 2021 |
| 5 | 1050795-6 | 66828 | Não | 2015-03-24 18:15:15 | 2021 |
| 6 | 1050795-6 | 67312 | Não | 2015-03-24 18:11:46 | 2021 |
| 7 | 1050795-6 | 69871 | Não | 2015-03-24 18:08:44 | 2021 |
| 8 | 1050795-6 | 72912 | Sim | 2015-03-24 18:09:44 | 2021 |
| 9 | 1050795-6 | 73433 | Não | 2015-03-24 18:11:56 | 2021 |
| 10 | 1050795-6 | 73434 | Não | 2015-03-24 18:10:09 | 2021 |

## main.votos_senado

_Query_: `SELECT * FROM "main"."votos_senado" LIMIT 10;`

| id_voto | codigo_votacao_sve | codigo_sessao_votacao | codigo_materia | identificacao_materia | codigo_parlamentar | nome_parlamentar | sexo_parlamentar | sigla_partido_parlamentar | sigla_uf_parlamentar | sigla_voto_parlamentar | descricao_voto_parlamentar | year_snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  | 5481 | 121994 | PEC 83/2015 | 4697 | Ângela Portela | F | PT | RR | Sim |  | 2015 |
| 2 |  | 5554 | 123909 | PEC 143/2015 | 4697 | Ângela Portela | F | PT | RR | Sim |  | 2016 |
| 3 |  | 5708 | 128035 | PEC 2/2017 | 4697 | Ângela Portela | F | PDT | RR | Sim |  | 2017 |
| 4 | 2725 | 5960 | 127414 | PEC 57/2016 | 3806 | Zequinha Marinho | M | PSC | PA | Sim |  | 2019 |
| 5 | 2778 | 5965 | 129887 | PEC 26/2017 | 3806 | Zequinha Marinho | M | PSC | PA | MIS | Missão da Casa no País/exterior | 2019 |
| 6 | 3533 | 6075 | 124513 | PLS 796/2015 | 3806 | Zequinha Marinho | M | PSC | PA | Sim |  | 2020 |
| 7 |  | 6248 | 135147 | PLP 19/2019 | 3806 | Zequinha Marinho | M | PSC | PA | AP | Atividade parlamentar | 2020 |
| 8 |  | 6249 | 135147 | PLP 19/2019 | 3806 | Zequinha Marinho | M | PSC | PA | AP | Atividade parlamentar | 2020 |
| 9 |  | 6076 | 139427 | MPV 899/2019 | 3806 | Zequinha Marinho | M | PSC | PA | Sim |  | 2020 |
| 10 |  | 6086 | 139736 | MPV 903/2019 | 3806 | Zequinha Marinho | M | PSC | PA | Sim |  | 2020 |
