# Database Sample Data

Showing up to 10 random rows from each table.

---

## main.autores_camara

| id_autor | cod_tipo | uri | ordem_assinatura | proponente | id_proposicao | year | tipo_autor | id_deputado_ou_orgao |
|----------|----------|-----|------------------|------------|---------------|------|------------|----------------------|
| 4254 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/178987 | 1 | True | 2239648 | 2020 | deputados | 178987 |
| 6396 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/73586 | 1 | True | 2243098 | 2020 | deputados | 73586 |
| 10097 | 20000 |  | 1 | True | 2246931 | 2020 |  | NULL |
| 10545 | 20000 |  | 1 | True | 2247738 | 2020 |  | NULL |
| 14823 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/73701 | 1 | True | 2253026 | 2020 | deputados | 73701 |
| 19066 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/160610 | 1 | True | 2256780 | 2020 | deputados | 160610 |
| 27623 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/204546 | 1 | True | 2262879 | 2020 | deputados | 204546 |
| 40942 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/213762 | 2 | True | 2203687 | 2021 | deputados | 213762 |
| 125741 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/204415 | 1 | True | 2209755 | 2024 | deputados | 204415 |
| 127520 | 10000 | https://dadosabertos.camara.leg.br/api/v2/deputados/163321 | 1 | True | 2418649 | 2024 | deputados | 163321 |

---

## main.autoria_documento_senado

| id_autoria_documento | id_processo | id_documento | autor | sigla_tipo | descricao_tipo | ordem | outros_autores_nao_informados | id_ente | sigla_ente | casa_ente | ente | cargo | siglaCargo | partido | sexo | uf | year_snapshot |
|----------------------|-------------|--------------|-------|------------|----------------|-------|-------------------------------|---------|------------|-----------|------|-------|------------|---------|------|----|---------------|
| 1625 | 7405239 | 7749676 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2018 |
| 7379 | 7812042 | 8013542 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2019 |
| 14579 | 8005189 | 8911418 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2020 |
| 19645 | 8148277 | 9024407 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2021 |
| 22065 | 8524432 | 9440684 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2021 |
| 24314 | 8290942 | 9187360 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2022 |
| 28008 | 8303331 | 9197788 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2022 |
| 28721 | 8380902 | 9282203 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2023 |
| 31704 | 8599321 | 9520895 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2023 |
| 34653 | 8685174 | 9642658 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2024 |

---

## main.autoria_iniciativa_senado

| id_autoria_iniciativa | id_processo | codigo_parlamentar | descricao_tipo | ente | ordem | outros_autores_nao_informados | sigla_ente | sigla_tipo | year_snapshot |
|-----------------------|-------------|--------------------|----------------|------|-------|-------------------------------|------------|------------|---------------|
| 1420 | 7373300 | 615 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2018 |
| 10413 | 7905419 | 825 | SENADOR | Senado Federal | 3 | Não | SF | SENADOR | 2020 |
| 13074 | 7972097 | 5352 | LIDER | Partido dos Trabalhadores | 1 | Não | PT | LIDER | 2020 |
| 14423 | 8004071 | 5666 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2020 |
| 22506 | 8244615 | 5008 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2022 |
| 23266 | 8289835 | 4610 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2022 |
| 25899 | 8399610 | 1173 | SENADOR | Senado Federal | 27 | Não | SF | SENADOR | 2023 |
| 26818 | 8372816 | 5926 | SENADOR | Senado Federal | 8 | Não | SF | SENADOR | 2023 |
| 30976 | 8583350 | 581 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2023 |
| 34313 | 8715676 | NULL | PRESIDENTE_REPUBLICA | Presidência da República | 1 | Não | PR | PRESIDENTE_REPUBLICA | 2024 |

---

## main.autuacoes_senado

| id_processo | autuacao_idx | descricao_autuacao | id_ente_controle_atual | nome_ente_controle_atual | sigla_ente_controle_atual | numero_autuacao | year_snapshot |
|-------------|--------------|--------------------|------------------------|--------------------------|---------------------------|-----------------|---------------|
| 7878532 | 1 | Autuação Principal | 13594 | Secretaria de Atas e Diários | SEADI | 1 | 2020 |
| 7919419 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2020 |
| 7928520 | 1 | Autuação Principal | 13594 | Secretaria de Atas e Diários | SEADI | 1 | 2020 |
| 7994716 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2020 |
| 8049850 | 1 | Autuação Principal | 55312 | Secretaria Legislativa do Senado Federal | SLSF | 1 | 2021 |
| 8086478 | 1 | Autuação Principal | 55304 | Secretaria de Expediente | SEXPE | 1 | 2021 |
| 8247263 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2022 |
| 8325997 | 1 | Autuação Principal | 55312 | Secretaria Legislativa do Senado Federal | SLSF | 1 | 2022 |
| 8581144 | 1 | Autuação Principal | 55312 | Secretaria Legislativa do Senado Federal | SLSF | 1 | 2023 |
| 8698040 | 1 | Autuação Principal | 55299 | Coordenação de Arquivo | COARQ | 1 | 2024 |

---

## main.bloco_senado

| codigo_bloco | data_criacao | nome_apelido | nome_bloco | year_snapshot |
|--------------|--------------|--------------|------------|---------------|
| 335 | 2023-02-01 | BLPRD | Bloco Parlamentar da Resistência Democrática | 2023 |
| 337 | 2023-02-03 | Minoria | Minoria | 2023 |
| 346 | 2023-03-20 | BLALIANÇA | Bloco Parlamentar Aliança | 2023 |
| 357 | 2025-02-03 | BLVANG | Bloco Parlamentar Vanguarda | 2025 |
| 358 | 2025-02-18 | BLDEM | Bloco Parlamentar Democracia | 2025 |
| 359 | 2025-02-18 | BLPBR | Bloco Parlamentar Pelo Brasil | 2025 |

---

## main.blocos_camara

| id_bloco | nome | id_legislatura | uri | year_snapshot | rn |
|----------|------|----------------|-----|---------------|----|
| 586 | Federação PSOL REDE | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/586 | 0 | 1 |
| 585 | Federação PSDB CIDADANIA | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/585 | 0 | 1 |
| 590 | AVANTE, SOLIDARIEDADE, PRD | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/590 | 0 | 1 |
| 584 | Federação Brasil da Esperança - Fe Brasil | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/584 | 0 | 1 |
| 589 | PL, UNIÃO, PP, PSD, REPUBLICANOS, MDB, Federação PSDB CIDADANIA, PODE | 57 | https://dadosabertos.camara.leg.br/api/v2/blocos/589 | 0 | 1 |

---

## main.blocos_partidos_camara

| id_bloco_partido | id_bloco | id_partido | year_snapshot |
|------------------|----------|------------|---------------|
| 3 | 586 | 36886 | 2020 |
| 5 | 590 | 37904 | 2020 |
| 7 | 585 | 37905 | 2020 |
| 9 | 589 | 37904 | 2020 |
| 10 | 590 | 38010 | 2020 |
| 11 | 584 | 36779 | 2020 |
| 12 | 589 | 37908 | 2020 |
| 16 | 589 | 38010 | 2020 |
| 19 | 589 | 37906 | 2020 |
| 22 | 589 | 36898 | 2020 |

---

## main.bronze_camara_blocos_partidos

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| camara | blocos/partidos | 584 | https://dadosabertos.camara.leg.br/api/v2/blocos/584/partidos | {"dados":[{"id":36779,"nome":"Partido Comunista do Brasil","sigla":"PCdoB","uri":"https://dadosab... | c1402ccc6ef392ea8f2d6860b18bedd4e42344fd2f2d32ef33b05d9652db3320 | 2020 |
| camara | blocos/partidos | 585 | https://dadosabertos.camara.leg.br/api/v2/blocos/585/partidos | {"dados":[{"id":37905,"nome":"Cidadania","sigla":"CIDADANIA","uri":"https://dadosabertos.camara.l... | 3b167fa8779e00dfd667a4332dcfcb52398cb580d06aed9952a3679c13d58f4f | 2020 |
| camara | blocos/partidos | 586 | https://dadosabertos.camara.leg.br/api/v2/blocos/586/partidos | {"dados":[{"id":36839,"nome":"Partido Socialismo e Liberdade","sigla":"PSOL","uri":"https://dados... | 15ef31e3202a6a33140f4f77a7c4228e9f9a0ba78e4460964dc73874b5cec2e6 | 2020 |
| camara | blocos/partidos | 589 | https://dadosabertos.camara.leg.br/api/v2/blocos/589/partidos | {"dados":[{"id":36898,"nome":"Avante","sigla":"AVANTE","uri":"https://dadosabertos.camara.leg.br/... | f656c9ed44f153c1d6fbd3064687500a356669972587454017736960df0cda6e | 2020 |
| camara | blocos/partidos | 590 | https://dadosabertos.camara.leg.br/api/v2/blocos/590/partidos | {"dados":[{"id":36898,"nome":"Avante","sigla":"AVANTE","uri":"https://dadosabertos.camara.leg.br/... | ce9fa1ff31333290d873cad4548d17c34dc560a9ebf4cc9427e67b319ffdde90 | 2020 |

---

## main.bronze_camara_deputados_frentes

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| camara | deputados/frentes | 141470 | https://dadosabertos.camara.leg.br/api/v2/deputados/141470/frentes | {"dados":[{"id":55686,"idLegislatura":57,"titulo":"Frente Parlamentar Mista em Defesa da União Na... | 760217bee4f4e88828efa8dd53c8397cd72fdf8be64671407401b8cfccc22649 | 2020 |
| camara | deputados/frentes | 141485 | https://dadosabertos.camara.leg.br/api/v2/deputados/141485/frentes | {"dados":[{"id":55672,"idLegislatura":57,"titulo":"Frente Parlamentar da Baixada Fluminense do Ri... | 773082bec3c8e7d7f70281a55eca4a228dd16c9f71b931bb48b4bd759655db0c | 2020 |
| camara | deputados/frentes | 220588 | https://dadosabertos.camara.leg.br/api/v2/deputados/220588/frentes | {"dados":[{"id":55686,"idLegislatura":57,"titulo":"Frente Parlamentar Mista em Defesa da União Na... | 674b5cb899fffc2dda9631ee89aa46e2790fe4bc8df3149ffbc6ab946a4d5ecc | 2020 |
| camara | deputados/frentes | 73491 | https://dadosabertos.camara.leg.br/api/v2/deputados/73491/frentes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2021 |
| camara | deputados/frentes | 74211 | https://dadosabertos.camara.leg.br/api/v2/deputados/74211/frentes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2021 |
| camara | deputados/frentes | 74372 | https://dadosabertos.camara.leg.br/api/v2/deputados/74372/frentes | {"dados":[{"id":53845,"idLegislatura":55,"titulo":"Frente Parlamentar Mista em Defesa da Pesquisa... | b7724ac66e014aa2c0e44effe3c3695f2ca4b9c0d0d72a90332c68f59a3f816a | 2021 |
| camara | deputados/frentes | 74441 | https://dadosabertos.camara.leg.br/api/v2/deputados/74441/frentes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2021 |
| camara | deputados/frentes | 74269 | https://dadosabertos.camara.leg.br/api/v2/deputados/74269/frentes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2023 |
| camara | deputados/frentes | 74541 | https://dadosabertos.camara.leg.br/api/v2/deputados/74541/frentes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2023 |
| camara | deputados/frentes | 133854 | https://dadosabertos.camara.leg.br/api/v2/deputados/133854/frentes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2023 |

---

## main.bronze_camara_deputados_historico

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| camara | deputados/historico | 178929 | https://dadosabertos.camara.leg.br/api/v2/deputados/178929/historico | {"dados":[{"condicaoEleitoral":null,"dataHora":"2015-02-01T00:00","descricaoStatus":"Partido no i... | acac1fac1a85f9000f25e0ab0dd59125ad65941cab5f50a71b897362463db948 | 2022 |
| camara | deputados/historico | 204412 | https://dadosabertos.camara.leg.br/api/v2/deputados/204412/historico | {"dados":[{"condicaoEleitoral":null,"dataHora":"2019-02-01T00:00","descricaoStatus":"Nome no iníc... | a66a42fd97d56bfc3cc6e3973d81961ec7f16dc5f3140e645b1cc2c82da48c2a | 2022 |
| camara | deputados/historico | 204450 | https://dadosabertos.camara.leg.br/api/v2/deputados/204450/historico | {"dados":[{"condicaoEleitoral":null,"dataHora":"2019-02-01T00:00","descricaoStatus":"Nome no iníc... | 041af3645c19b7a5bf02b41bafe34f65b5de8eaa73606280a1482de6720039df | 2022 |
| camara | deputados/historico | 92776 | https://dadosabertos.camara.leg.br/api/v2/deputados/92776/historico | {"dados":[{"condicaoEleitoral":null,"dataHora":"2011-02-01T00:00","descricaoStatus":"Nome no iníc... | a6fbf436867139b4f9d0899f33d99c7526e68e304b12ecf21aed21c809684a05 | 2023 |
| camara | deputados/historico | 141458 | https://dadosabertos.camara.leg.br/api/v2/deputados/141458/historico | {"dados":[{"condicaoEleitoral":"Titular","dataHora":"2007-02-01T00:00","descricaoStatus":"Nome no... | 8978cabd9f84b912b1603589cd7540947692302056bbb4a8da58b0822775a8b9 | 2023 |
| camara | deputados/historico | 160559 | https://dadosabertos.camara.leg.br/api/v2/deputados/160559/historico | {"dados":[{"condicaoEleitoral":"Titular","dataHora":"2011-02-01T00:00","descricaoStatus":"Nome no... | 704385fab60a25a86eea451e2cdeccaf46f0b6cc7fc675e5e732af52a78826e1 | 2023 |
| camara | deputados/historico | 204387 | https://dadosabertos.camara.leg.br/api/v2/deputados/204387/historico | {"dados":[{"condicaoEleitoral":null,"dataHora":"2019-02-01T00:00","descricaoStatus":"Nome no iníc... | f406448c1f0e57cf612ae6f8c31038cb4b6403ec03862528fbeeaae08e56f2bd | 2023 |
| camara | deputados/historico | 220671 | https://dadosabertos.camara.leg.br/api/v2/deputados/220671/historico | {"dados":[{"condicaoEleitoral":null,"dataHora":"2023-02-01T00:00","descricaoStatus":"Nome no iníc... | 4134e1fadcbe85da6fb315c25d1a6c763a4bc3c070a70604d2e326c3fc5aa6f0 | 2023 |
| camara | deputados/historico | 220676 | https://dadosabertos.camara.leg.br/api/v2/deputados/220676/historico | {"dados":[{"condicaoEleitoral":null,"dataHora":"2023-02-01T00:00","descricaoStatus":"Nome no iníc... | c7e034371379b4f7f3fddfafc16fa098d375ebdc1dd63fef003c5807a1d3bdb2 | 2023 |
| camara | deputados/historico | 224117 | https://dadosabertos.camara.leg.br/api/v2/deputados/224117/historico | {"dados":[{"condicaoEleitoral":null,"dataHora":"2023-02-01T00:00","descricaoStatus":"Nome no iníc... | 60417b13fb8d2991a6806fc8642ed79989e5b77f9644a7cd3d10c46f26114943 | 2023 |

---

## main.bronze_camara_deputados_orgaos

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| camara | deputados/orgaos | 74043 | https://dadosabertos.camara.leg.br/api/v2/deputados/74043/orgaos | {"dados":[{"codTitulo":"101","dataFim":null,"dataInicio":"2023-11-02T00:00","idOrgao":539644,"nom... | 94b5115c1c3cc6b7e251c6a74b2e41a828a8ae8260eff3a4fac226300073126d | 2023 |
| camara | deputados/orgaos | 204445 | https://dadosabertos.camara.leg.br/api/v2/deputados/204445/orgaos | {"dados":[{"codTitulo":"2","dataFim":null,"dataInicio":"2023-05-31T00:00","idOrgao":539419,"nomeO... | 9df7f8c76608479e8c9e092f2ed9ce6550da349731af390aaf38c59fdb77da81 | 2023 |
| camara | deputados/orgaos | 204456 | https://dadosabertos.camara.leg.br/api/v2/deputados/204456/orgaos | {"dados":[{"codTitulo":"101","dataFim":null,"dataInicio":"2023-08-23T00:00","idOrgao":5973,"nomeO... | f95ea87e7cd7880017aa499f51b975963ba2757d5d504549715ac23262ee3318 | 2023 |
| camara | deputados/orgaos | 204560 | https://dadosabertos.camara.leg.br/api/v2/deputados/204560/orgaos | {"dados":[{"codTitulo":"102","dataFim":null,"dataInicio":"2023-08-23T00:00","idOrgao":5973,"nomeO... | 5477301d0c5747e2568aac191294ef8c439daff822ddfee114e9a7d73b283616 | 2023 |
| camara | deputados/orgaos | 220573 | https://dadosabertos.camara.leg.br/api/v2/deputados/220573/orgaos | {"dados":[{"codTitulo":"101","dataFim":null,"dataInicio":"2023-11-02T00:00","idOrgao":539644,"nom... | 20355d7d3956b5cd152a73d645a10ca7f7841cab0ccd0b43df33a4271b824acc | 2023 |
| camara | deputados/orgaos | 91228 | https://dadosabertos.camara.leg.br/api/v2/deputados/91228/orgaos | {"dados":[{"codTitulo":"101","dataFim":null,"dataInicio":"2024-02-07T00:00","idOrgao":539589,"nom... | beb63304e72353ebe86b1d07d8b6466ea63355029a04b26901bfbd752d41670c | 2024 |
| camara | deputados/orgaos | 163321 | https://dadosabertos.camara.leg.br/api/v2/deputados/163321/orgaos | {"dados":[{"codTitulo":"101","dataFim":null,"dataInicio":"2024-03-06T00:00","idOrgao":5973,"nomeO... | 04036693346f3f22db7bc6cf66c2e502b1d697a851cac68ef480c64b0c8df9ba | 2024 |
| camara | deputados/orgaos | 74585 | https://dadosabertos.camara.leg.br/api/v2/deputados/74585/orgaos | {"dados":[{"codTitulo":"102","dataFim":null,"dataInicio":"2025-03-18T00:00","idOrgao":537871,"nom... | 9340fc0a7ce9f2cdcf644cf11d81e8f61c2fc6df9dd7810201fdf8b2d4fdefa3 | 2025 |
| camara | deputados/orgaos | 141487 | https://dadosabertos.camara.leg.br/api/v2/deputados/141487/orgaos | {"dados":[{"codTitulo":"101","dataFim":null,"dataInicio":"2025-03-18T00:00","idOrgao":2016,"nomeO... | f2cf859d2c532fb5125f65119b0c33ea86ab3c0e56a25f4160257f814a46d7e8 | 2025 |
| camara | deputados/orgaos | 141555 | https://dadosabertos.camara.leg.br/api/v2/deputados/141555/orgaos | {"dados":[{"codTitulo":"102","dataFim":null,"dataInicio":"2025-03-18T00:00","idOrgao":2010,"nomeO... | bf652cbf5a7b43f9b85f0bb43a9af2b0350cd75848885a88090cc64997cb4790 | 2025 |

---

## main.bronze_camara_eventos_orgaos

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| camara | eventos/orgaos | 60044 | https://dadosabertos.camara.leg.br/api/v2/eventos/60044/orgaos | {"dados":[{"apelido":"Câmara dos Deputados - Decom","codTipoOrgao":12000,"id":102371,"nome":"Even... | 01d6ea590e472b6791d96f01d2cbfc3704a053bc033bd173ccf27adb9c430dc3 | 2020 |
| camara | eventos/orgaos | 62394 | https://dadosabertos.camara.leg.br/api/v2/eventos/62394/orgaos | {"dados":[{"apelido":"Meio Ambiente e Desenvolvimento Sustentável","codTipoOrgao":2,"id":6174,"no... | 59a815c5367af2e08cc47058cf93c647e34ed1f26c9ac98c916791bb6f2575f2 | 2021 |
| camara | eventos/orgaos | 63126 | https://dadosabertos.camara.leg.br/api/v2/eventos/63126/orgaos | {"dados":[{"apelido":"Educação","codTipoOrgao":2,"id":2009,"nome":"Comissão de Educação","nomePub... | e78dc5e978c1d454989c9dd5f507b759ab53a671fa3181542c8b96765b230070 | 2021 |
| camara | eventos/orgaos | 65460 | https://dadosabertos.camara.leg.br/api/v2/eventos/65460/orgaos | {"dados":[{"apelido":"Ciência, Tecnologia e Inovação","codTipoOrgao":2,"id":2002,"nome":"Comissão... | de630a3d983d6df5b6137415a3291827d0ceddbcc1a4edd207961979e12f7fb1 | 2022 |
| camara | eventos/orgaos | 67804 | https://dadosabertos.camara.leg.br/api/v2/eventos/67804/orgaos | {"dados":[{"apelido":"Cultura","codTipoOrgao":2,"id":536996,"nome":"Comissão de Cultura","nomePub... | 43aee3c2c0d106f200ebeec379abd05311f76532f1fd5f3555ec708eb0cfe30e | 2023 |
| camara | eventos/orgaos | 68551 | https://dadosabertos.camara.leg.br/api/v2/eventos/68551/orgaos | {"dados":[{"apelido":"Minas e Energia","codTipoOrgao":2,"id":2012,"nome":"Comissão de Minas e Ene... | 35fc97fdbbc6b593ee372200efefe93c908bb65011f78213a6dbc1c5af44b6d7 | 2023 |
| camara | eventos/orgaos | 68718 | https://dadosabertos.camara.leg.br/api/v2/eventos/68718/orgaos | {"dados":[{"apelido":"Esporte","codTipoOrgao":2,"id":537236,"nome":"Comissão do Esporte","nomePub... | 8181d8fd1a156fd3f6e081f650740666e64fcf38bb9a9a62e38da4bd23846ff8 | 2023 |
| camara | eventos/orgaos | 70016 | https://dadosabertos.camara.leg.br/api/v2/eventos/70016/orgaos | {"dados":[{"apelido":"Legislação Participativa","codTipoOrgao":2,"id":5438,"nome":"Comissão de Le... | 94b0969cd919dfe2d57a03caccba62f968ab505aeffdf134eea401fed18cc0b4 | 2023 |
| camara | eventos/orgaos | 72160 | https://dadosabertos.camara.leg.br/api/v2/eventos/72160/orgaos | {"dados":[{"apelido":"Defesa dos Direitos das Pessoas com Deficiência","codTipoOrgao":2,"id":5374... | bb8067c57a4cf1516fb07f3b5dc75488db5b14a438b1d8500e7642696d44495b | 2024 |
| camara | eventos/orgaos | 74402 | https://dadosabertos.camara.leg.br/api/v2/eventos/74402/orgaos | {"dados":[{"apelido":"Plenário","codTipoOrgao":26,"id":180,"nome":"Plenário","nomePublicacao":"Pl... | 8ce4459d770733a20b6a383d3d0e804c4a7d3d7f3ded64e6478afb452808065c | 2024 |

---

## main.bronze_camara_eventos_pauta

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| camara | eventos/pauta | 59353 | https://dadosabertos.camara.leg.br/api/v2/eventos/59353/pauta | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | eventos/pauta | 60245 | https://dadosabertos.camara.leg.br/api/v2/eventos/60245/pauta | {"dados":[{"codRegime":99,"ordem":1,"proposicaoRelacionada_":{"ano":"2020","codTipo":"139","ement... | e1846976f0195caefbfa9ee9ef4b3a7f3a9fc322aedb46de8cf63bd405a8a6c9 | 2020 |
| camara | eventos/pauta | 62337 | https://dadosabertos.camara.leg.br/api/v2/eventos/62337/pauta | {"dados":[{"codRegime":99,"ordem":1,"proposicaoRelacionada_":{"ano":"2021","codTipo":"147","ement... | 8bf5e47e8e739fb3fc9024bf9d9196bf33ef1c54ce08f33f79042f2b6ee5afe4 | 2021 |
| camara | eventos/pauta | 62957 | https://dadosabertos.camara.leg.br/api/v2/eventos/62957/pauta | {"dados":[{"codRegime":99,"ordem":1,"proposicaoRelacionada_":null,"proposicao_":{"ano":2021,"codT... | c060e7ba61f0e56b2612086fd6280eada22902719a8e5b2a8fe88065084bef79 | 2021 |
| camara | eventos/pauta | 64004 | https://dadosabertos.camara.leg.br/api/v2/eventos/64004/pauta | {"dados":[{"codRegime":14,"ordem":1,"proposicaoRelacionada_":{"ano":"2011","codTipo":"139","ement... | accf71d53bc27500cf7a5bd1f0d4f88b97a544c5b3f3f814aaa68c9b80f7ee2b | 2021 |
| camara | eventos/pauta | 64370 | https://dadosabertos.camara.leg.br/api/v2/eventos/64370/pauta | {"dados":[{"codRegime":99,"ordem":1,"proposicaoRelacionada_":null,"proposicao_":{"ano":2021,"codT... | 9965552c5a7eed769c9b2e0ea6f87646faead58f6eb2f43e62a4b1972174444b | 2021 |
| camara | eventos/pauta | 67740 | https://dadosabertos.camara.leg.br/api/v2/eventos/67740/pauta | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2023 |
| camara | eventos/pauta | 70111 | https://dadosabertos.camara.leg.br/api/v2/eventos/70111/pauta | {"dados":[{"codRegime":14,"ordem":1,"proposicaoRelacionada_":{"ano":"2022","codTipo":"139","ement... | 7fa403dd2787632f1e765a1821eabed8345f2e5fba5e0408ec21fd5274ae06e3 | 2023 |
| camara | eventos/pauta | 72240 | https://dadosabertos.camara.leg.br/api/v2/eventos/72240/pauta | {"dados":[{"codRegime":99,"ordem":1,"proposicaoRelacionada_":null,"proposicao_":{"ano":2024,"codT... | c007c14dde7fd80a25eecf99e302e9a9f779aff0969f5a5fe635f64f390020a1 | 2024 |
| camara | eventos/pauta | 72270 | https://dadosabertos.camara.leg.br/api/v2/eventos/72270/pauta | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2024 |

---

## main.bronze_camara_legislaturas_mesa

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| camara | legislaturas/mesa | 55 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/55/mesa | {"dados":[{"codTitulo":"7","dataFim":"2017-02-02","dataInicio":"2015-02-01","email":null,"id":160... | d4a6d9799672439bff37ef7173dcb0703136c8de0edf95821059e9dc9efe6a37 | 2015 |
| camara | legislaturas/mesa | 3 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/3/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | legislaturas/mesa | 20 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/20/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | legislaturas/mesa | 23 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/23/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | legislaturas/mesa | 27 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/27/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | legislaturas/mesa | 28 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/28/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | legislaturas/mesa | 35 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/35/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | legislaturas/mesa | 40 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/40/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | legislaturas/mesa | 42 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/42/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | legislaturas/mesa | 51 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/51/mesa | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |

---

## main.bronze_camara_votacoes

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| camara | votacoes | 2234674 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2234674/votacoes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | votacoes | 2247730 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2247730/votacoes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | votacoes | 2249775 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2249775/votacoes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | votacoes | 2264520 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2264520/votacoes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2020 |
| camara | votacoes | 2089686 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2089686/votacoes | {"dados":[{"aprovacao":1,"data":"2018-06-13","dataHoraRegistro":"2018-06-13T12:13:54","descricao"... | 5dffd898d8f5e95305a8d5cbb84adb74d7c8f36e1c9626ef3384cf53f8605602 | 2021 |
| camara | votacoes | 2219972 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2219972/votacoes | {"dados":[{"aprovacao":1,"data":"2019-10-09","dataHoraRegistro":"2019-10-09T12:05:25","descricao"... | 9dab5e986f5902e87fea5fb8fedffc777b6e0bc9fcbb210cd30733400f11266d | 2021 |
| camara | votacoes | 2279148 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2279148/votacoes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2021 |
| camara | votacoes | 2318226 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2318226/votacoes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2022 |
| camara | votacoes | 2324981 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2324981/votacoes | {"dados":[{"aprovacao":1,"data":"2022-11-23","dataHoraRegistro":"2022-11-23T10:29:47","descricao"... | f53692a89ad1f0bb2d94f6ae79f0e97a94d334cf53513f63ffe297684652c17d | 2022 |
| camara | votacoes | 2335001 | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2335001/votacoes | {"dados":[]} | e3f60f959291f48551b8f9a819aa280d6c26cb36048a77675fc4e4107d2f7b49 | 2022 |

---

## main.bronze_senado_colegiado

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| senado | colegiado | 34 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"34","CodigoTipoColegiado":"21","DataInicio":"1900-01-01","IndicadorDistrParti... | 78ed658e3085b205f0f04ba4a60012b4ffb82a4c940b9002175b607892541f8c | 1900 |
| senado | colegiado | 38 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"38","CodigoTipoColegiado":"21","DataInicio":"1900-01-01","IndicadorDistrParti... | 5b3ab8402aca0640913710c9d437529da92d924e0e88933cbdbcd76ad8c1f8e4 | 1900 |
| senado | colegiado | 40 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"40","CodigoTipoColegiado":"21","DataInicio":"1900-01-01","IndicadorDistrParti... | 35d4234190deb511703364728fb000edb326e0659b064c26d75149a5cba8fa0a | 1900 |
| senado | colegiado | 47 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"47","CodigoTipoColegiado":"21","DataInicio":"1900-01-01","IndicadorDistrParti... | 6f59be0b517199c781da41f2612350d986a34843c900d0d58cb10306a54b86bd | 1900 |
| senado | colegiado | 834 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"834","CodigoTipoColegiado":"21","DataInicio":"2002-12-13","IndicadorDistrPart... | 3933b8d7d84f0dec73573210fc43c78f44f01c90e741edd05a504f38e88303d4 | 2002 |
| senado | colegiado | 1306 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"1306","CodigoTipoColegiado":"21","DataInicio":"2005-02-18","IndicadorDistrPar... | 8507906f27e8343a1c19f1845e0673b1c9aa86d8c1b06e198bf3779351fb7f78 | 2005 |
| senado | colegiado | 1307 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"1307","CodigoTipoColegiado":"21","DataInicio":"2005-02-22","IndicadorDistrPar... | ffe2c98b2405762449e7e5f6769b3d37e9d58c31c3d9271ef145d731264ff1ed | 2005 |
| senado | colegiado | 2615 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"2615","CodigoTipoColegiado":"21","DataInicio":"2023-06-07","IndicadorDistrPar... | 45bcbb1ade1c713adffe799f060cbb59cf70698074e09c1246ee0c934b769440 | 2023 |
| senado | colegiado | 2617 | https://legis.senado.leg.br/dadosabertos/comissao/lista/permanente.json | {"CodigoColegiado":"2617","CodigoTipoColegiado":"21","DataInicio":"2023-06-07","IndicadorDistrPar... | 1a841b1b4067fc9177b1067ed51ca9f78e627cc192cc80572d74c7fac1879783 | 2023 |
| senado | colegiado | 2740 | https://legis.senado.leg.br/dadosabertos/comissao/lista/temporaria.json | {"CodigoColegiado":"2740","CodigoTipoColegiado":"121","DataInicio":"2025-04-08","DescricaoSubtitu... | 4b25ebfeaca181c82c948fb8ad24fc8bd6f480f9d8c8c33d8c5a503b4fd3cd3f | 2025 |

---

## main.bronze_senado_processo

| source | entity | id | url | payload_json | payload_sha256 | year |
|--------|--------|----|-----|--------------|----------------|------|
| senado | processo | 7933108 | https://legis.senado.leg.br/dadosabertos/processo/7933108 | {"ano":2020,"autoriaIniciativa":[{"autor":"José Serra","cargo":"Senador","casaEnte":"SF","codigoP... | 64876d3227a46a0c9190daf9330ec53c708a4b3d80d93d3ef1b78948c9b13fd3 | 2020 |
| senado | processo | 7934803 | https://legis.senado.leg.br/dadosabertos/processo/7934803 | {"ano":2020,"autoriaIniciativa":[{"autor":"Ciro Nogueira","cargo":"Líder","codigoParlamentar":739... | ea7f8085621bc0e8f0673fc0b8c741998f8affc2c589212bccf544f2ee79525e | 2020 |
| senado | processo | 7993083 | https://legis.senado.leg.br/dadosabertos/processo/7993083 | {"ano":2020,"autoriaIniciativa":[{"autor":"Presidência da República","descricaoTipo":"PRESIDENTE_... | 3cb1d27e23e212c1b579e8f2406676073887f57985335732302b38112f9f1bfa | 2020 |
| senado | processo | 8049766 | https://legis.senado.leg.br/dadosabertos/processo/8049766 | {"ano":2021,"autoriaIniciativa":[{"autor":"Eduardo Braga","cargo":"Líder","codigoParlamentar":499... | 1dc8059570cfe33df4bdf2fd4c73bd4751c3593480425d103169c8e831c5bc43 | 2021 |
| senado | processo | 8050433 | https://legis.senado.leg.br/dadosabertos/processo/8050433 | {"ano":2021,"autoriaIniciativa":[{"autor":"Marcos do Val","cargo":"Senador","casaEnte":"SF","codi... | 62d53336e0440ebd2235441dca943dafadde55903a32657578331f18643040cb | 2021 |
| senado | processo | 8097814 | https://legis.senado.leg.br/dadosabertos/processo/8097814 | {"ano":2021,"autoriaIniciativa":[{"autor":"Mara Gabrilli","cargo":"Senadora","casaEnte":"SF","cod... | 2ad27e24bd7db24fd0236767de48973f2cdb3b4481062711eaca8ec8280325bf | 2021 |
| senado | processo | 8170507 | https://legis.senado.leg.br/dadosabertos/processo/8170507 | {"ano":2021,"autoriaIniciativa":[{"autor":"Carlos Portinho","cargo":"Senador","casaEnte":"SF","co... | 81a0f630ab17efc7a4f622ee2cdb0260d5ec1b51fff2124f1d89408ddbbb680c | 2021 |
| senado | processo | 8195961 | https://legis.senado.leg.br/dadosabertos/processo/8195961 | {"ano":2022,"autoriaIniciativa":[{"autor":"Sérgio Petecão","cargo":"Senador","casaEnte":"SF","cod... | 57579bd1a9aeb7a12dedc3dab70055ea451296dd87e7743043bc971f42b5bc2a | 2022 |
| senado | processo | 8451268 | https://legis.senado.leg.br/dadosabertos/processo/8451268 | {"ano":2023,"autoriaIniciativa":[{"autor":"Carlos Portinho","cargo":"Senador","casaEnte":"SF","co... | 5eb70ef6f6d17eaa6b6479c5ff83ff337a4ccb681d875f782bd1d5fefaa43e7e | 2023 |
| senado | processo | 8705988 | https://legis.senado.leg.br/dadosabertos/processo/8705988 | {"ano":2024,"autoriaIniciativa":[{"autor":"Professora Dorinha Seabra","cargo":"Senadora","casaEnt... | a56ea72c89a6668666688ddf640b580de54fcd49c03dc60310e0b26570016da0 | 2024 |

---

## main.camara_authors

| id_proposicao | uri_kind | author_id_num |
|---------------|----------|---------------|
| 2242787 | deputados | 204412 |
| 2248899 |  | NULL |
| 2252409 | deputados | 74548 |
| 2252061 | deputados | 73701 |
| 2256766 | deputados | 74082 |
| 2260380 | deputados | 204509 |
| 2264960 | deputados | 204485 |
| 2217407 | deputados | 204570 |
| 2420550 | deputados | 178992 |
| 2462038 | deputados | 220559 |

---

## main.colegiado_senado

| codigo_colegiado | codigo_tipo_colegiado | data_inicio | indicador_distr_partidaria | nome_colegiado | sigla_colegiado | ordem | year_snapshot |
|------------------|-----------------------|-------------|----------------------------|----------------|-----------------|-------|---------------|
| 34 | 21 | 1900-01-01 | S | Comissão de Constituição, Justiça e Cidadania | CCJ | 3 | 1900 |
| 38 | 21 | 1900-01-01 | S | Comissão de Assuntos Econômicos | CAE | 1 | 1900 |
| 47 | 21 | 1900-01-01 | S | Comissão de Educação e Cultura | CE | 4 | 1900 |
| 54 | 21 | 1900-01-01 | S | Comissão de Relações Exteriores e Defesa Nacional | CRE | 7 | 1900 |
| 834 | 21 | 2002-12-13 | S | Comissão de Direitos Humanos e Legislação Participativa | CDH | 6 | 2002 |
| 1307 | 21 | 2005-02-22 | S | Comissão de Agricultura e Reforma Agrária | CRA | 10 | 2005 |
| 1956 | 21 | 2015-09-02 | S | Comissão de Transparência, Governança, Fiscalização e Controle e Defesa do Consumidor | CTFC | 5 | 2015 |
| 2429 | 21 | 2021-03-12 | S | Comissão de Segurança Pública | CSP | 14 | 2021 |
| 2615 | 21 | 2023-06-07 | S | Comissão de Esporte | CEsp | 16 | 2023 |
| 2617 | 21 | 2023-06-07 | S | Comissão de Defesa da Democracia | CDD | 12 | 2023 |

---

## main.correspondencia_proposicoes_processo

| id_proposicao_camara | id_processo_senado | identificacao |
|----------------------|--------------------|---------------|
| 2238527 | 8514010 | PL 557/2020 |
| 2242772 | 7886317 | MPV 940/2020 |
| 2277894 | 8147190 | PL 1374/2021 |
| 2314678 | 7718388 | PL 764/2019 |
| 2315066 | 8182071 | PL 4392/2021 |
| 2333775 | 7760352 | PL 3253/2019 |
| 2366765 | 7999332 | PL 5179/2020 |
| 2401138 | 8577406 | MPV 1192/2023 |
| 2405709 | 8517525 | PL 3954/2023 |
| 2416729 | 8638298 | PL 6233/2023 |

---

## main.deputados_camara

| id_deputado | nome_civil | uri | year_snapshot | rn | tag |
|-------------|------------|-----|---------------|----|-----|
| 73782 | ODILIO BALBINOTTI | https://dadosabertos.camara.leg.br/api/v2/deputados/73782 | 2023 | 1 | CD:73782 |
| 73732 | Fernando Antonio da Câmara Freire | https://dadosabertos.camara.leg.br/api/v2/deputados/73732 | 2023 | 1 | CD:73732 |
| 160570 | JERÔNIMO PIZZOLOTTO GOERGEN | https://dadosabertos.camara.leg.br/api/v2/deputados/160570 | 2020 | 1 | CD:160570 |
| 141506 | MAURÍCIO GONÇALVES TRINDADE | https://dadosabertos.camara.leg.br/api/v2/deputados/141506 | 2021 | 1 | CD:141506 |
| 73938 | EDUARDO VALVERDE ARAÚJO ALVES | https://dadosabertos.camara.leg.br/api/v2/deputados/73938 | 2020 | 1 | CD:73938 |
| 73764 | ABELARDO LUIZ LUPION MELLO | https://dadosabertos.camara.leg.br/api/v2/deputados/73764 | 2021 | 1 | CD:73764 |
| 160542 | MÁRCIO COSTA MACÊDO | https://dadosabertos.camara.leg.br/api/v2/deputados/160542 | 2020 | 1 | CD:160542 |
| 74161 | REGINALDO LÁZARO DE OLIVEIRA LOPES | https://dadosabertos.camara.leg.br/api/v2/deputados/74161 | 2020 | 1 | CD:74161 |
| 74752 | ODELMO LEÃO CARNEIRO SOBRINHO | https://dadosabertos.camara.leg.br/api/v2/deputados/74752 | 2020 | 1 | CD:74752 |
| 215361 | RACHEL XIMENES MARQUES | https://dadosabertos.camara.leg.br/api/v2/deputados/215361 | 2021 | 1 | CD:215361 |

---

## main.deputados_frentes_camara

| id_deputado_frente | id_deputado | id_frente | year_snapshot |
|--------------------|-------------|-----------|---------------|
| 4106 | 178991 | 53460 | 2021 |
| 10336 | 178860 | 53518 | 2020 |
| 13587 | 161440 | 54337 | 2020 |
| 15734 | 220573 | 54318 | 2020 |
| 125343 | 74585 | 53764 | 2020 |
| 126997 | 178986 | 54237 | 2020 |
| 131442 | 178947 | 54184 | 2020 |
| 134396 | 69871 | 54431 | 2020 |
| 140687 | 160559 | 55655 | 2020 |
| 143375 | 74371 | 54178 | 2020 |

---

## main.deputados_historico_camara

| id_deputado_historico | id_deputado | id_legislatura | data_hora | condicao_eleitoral | descricao_status | year_snapshot |
|-----------------------|-------------|----------------|-----------|--------------------|------------------|---------------|
| 130 | 204572 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2022 |
| 285 | 204407 | 57 | 2023-02-01 12:05:00 | Titular | Entrada - Posse de Eleito Titular - Posse na Sessão Preparatória | 2023 |
| 1263 | 178871 | 56 | 2023-01-31 23:59:00 | Titular | Saída - Afastamento definitivo - Término da Legislatura | 2023 |
| 1854 | 204444 | 56 | 2022-02-23 00:00:00 | Titular | Alteração de partido | 2022 |
| 2157 | 204368 | 56 | 2019-02-01 00:00:00 | NULL | Nome no início da legislatura / Partido no início da legislatura | 2022 |
| 2280 | 160588 | 55 | 2019-01-31 23:59:00 | Titular | Saída - Afastamento definitivo - Término da Legislatura | 2023 |
| 2428 | 178860 | 55 | 2019-01-31 23:59:00 | Titular | Saída - Afastamento definitivo - Término da Legislatura | 2022 |
| 3960 | 74856 | 56 | 2021-08-11 14:27:00 | Suplente | Diverso - Convocação Eleito ou Suplente - Aguardando Convocação de Suplente | 2021 |
| 3996 | 74550 | 50 | 1995-02-01 00:00:00 | Titular | Partido no início da legislatura / Nome no início da legislatura / Primeira posse na legislatura ... | 2023 |
| 4302 | 163321 | 55 | 2016-05-12 18:33:00 | Titular | Saída - Afastamento sem prazo determinado - Ministro de Estado - Ministro de Estado do Trabalho e... | 2023 |

---

## main.deputados_orgaos_camara

| id_deputado_orgao | id_deputado | id_orgao | cod_titulo | data_inicio | data_fim | year_snapshot |
|-------------------|-------------|----------|------------|-------------|----------|---------------|
| 35 | 107970 | 539677 | 102 | 2025-04-16 00:00:00 | NULL | 2023 |
| 335 | 221328 | 539771 | 101 | 2025-05-05 00:00:00 | NULL | 2024 |
| 667 | 220544 | 539731 | 4 | 2025-06-10 00:00:00 | NULL | 2023 |
| 1242 | 220691 | 537053 | 20 | 2025-04-09 00:00:00 | NULL | 2023 |
| 1803 | 160600 | 2012 | 102 | 2025-03-18 00:00:00 | NULL | 2025 |
| 1946 | 178964 | 539386 | 101 | 2025-03-18 00:00:00 | NULL | 2023 |
| 2082 | 220674 | 537870 | 101 | 2025-04-01 00:00:00 | NULL | 2023 |
| 2384 | 220618 | 2010 | 102 | 2025-04-23 00:00:00 | NULL | 2023 |
| 2890 | 221338 | 2018 | 101 | 2025-03-19 00:00:00 | NULL | 2023 |
| 3252 | 220650 | 4 | 102 | 2025-02-01 00:00:00 | NULL | 2025 |

---

## main.despachos_senado

| id_processo | id_despacho | data_despacho | cancelado | tipo_motivacao | sigla_tipo_motivacao | year_snapshot |
|-------------|-------------|---------------|-----------|----------------|----------------------|---------------|
| 507581 | 7950965 | 2019-05-08 | Não | Aprovação de requerimento | APROV_REQ | 2015 |
| 5051890 | 7763117 | 2017-02-22 | Não | Motivação não categorizada | NAO_CATEGORIZADO | 2017 |
| 5206199 | 7763265 | 2017-03-29 | Não | Motivação não categorizada | NAO_CATEGORIZADO | 2017 |
| 1402773 | 8098097 | 2020-04-15 | Não | Aprovação de requerimento | APROV_REQ | 2015 |
| 7878092 | 8083029 | 2020-04-01 | Não | Decisão da Presidência | DECISAO_PRESID | 2020 |
| 7870004 | 8075107 | 2020-03-12 | Não | Leitura da Matéria | LEITURA_DA_MATERIA | 2020 |
| 8287548 | 9185424 | 2022-07-12 | Não | Decisão da Presidência | DECISAO_PRESID | 2022 |
| 8183380 | 9071338 | 2022-02-16 | Não | Decisão da Presidência | DECISAO_PRESID | 2021 |
| 8308150 | 9204275 | 2022-10-06 | Não | Decisão da Presidência | DECISAO_PRESID | 2022 |
| 8647752 | 9585547 | 2024-04-16 | Não | Leitura da Matéria | LEITURA_DA_MATERIA | 2023 |

---

## main.documento_autoria_senado

| id_documento_autoria | id_processo | id_ente | autor | codigo_parlamentar | descricao_tipo | ente | ordem | outros_autores_nao_informados | sigla_ente | sigla_tipo | year_snapshot | tipo_autor | id_senador_ou_ente |
|----------------------|-------------|---------|-------|--------------------|----------------|------|-------|-------------------------------|------------|------------|---------------|------------|--------------------|
| 7936 | 8533500 | 2 | Câmara dos Deputados | NULL | CAMARA | Câmara dos Deputados | 1 | Não | CD | CAMARA | 2019 | ente | 2 |
| 8474 | 7879922 | 1 | Esperidião Amin | 22 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2020 | senador | 22 |
| 9813 | 7756290 | 1 | Humberto Costa | 5008 | SENADOR | Senado Federal | 9 | Não | SF | SENADOR | 2019 | senador | 5008 |
| 9917 | 7778476 | 1 | Paulo Rocha | 374 | SENADOR | Senado Federal | 45 | Não | SF | SENADOR | 2019 | senador | 374 |
| 11174 | 7926757 | 1 | Rose de Freitas | 2331 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2020 | senador | 2331 |
| 13853 | 7987889 | 55126 | Presidência da República | NULL | PRESIDENTE_REPUBLICA | Presidência da República | 1 | Não | PR | PRESIDENTE_REPUBLICA | 2020 | ente | 55126 |
| 17381 | 8066578 | 1 | Jayme Campos | 4531 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2021 | senador | 4531 |
| 20164 | 8169124 | 1 | Telmário Mota | 5535 | SENADOR | Senado Federal | 1 | Não | SF | SENADOR | 2021 | senador | 5535 |
| 21119 | 8083359 | 1 | Angelo Coronel | 5967 | SENADOR | Senado Federal | 19 | Não | SF | SENADOR | 2021 | senador | 5967 |
| 24640 | 8270618 | 1 | Mara Gabrilli | 5376 | SENADOR | Senado Federal | 29 | Não | SF | SENADOR | 2022 | senador | 5376 |

---

## main.emendas_senado

| id_emenda | id_ci_emenda | id_ci_emendado | id_documento_emenda | id_processo | identificacao | numero | autoria | descricao_documento_emenda | tipo_emenda | turno_apresentacao | casa | codigo_colegiado | sigla_colegiado | nome_colegiado | data_apresentacao | url_documento_emenda | year_snapshot |
|-----------|--------------|----------------|---------------------|-------------|---------------|--------|---------|----------------------------|-------------|--------------------|------|------------------|-----------------|----------------|-------------------|----------------------|---------------|
| 9449376 | 7541475 | 7540139 | 9449374 | 8525545 | EMENDA 127 - MPV 1184/2023 | 127 | Deputado Federal André Figueiredo (PDT/CE) | Dispõe sobre a tributação de aplicações em fundos de investimento no País. | EMENDA_PARCIAL | NORMAL | CN | 2631 | CMMPV 1184/2023 | Comissão Mista da Medida Provisória n° 1184, de 2023 | 2023-09-04 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9449374 | 2023 |
| 9606550 | 7568333 | 7556913 | 9606394 | 8611636 | EMENDA 1 / CE - PL 6207/2023 | 1 | Comissão de Educação e Cultura, Senador Romário (PL/RJ), Senador Flávio Arns (PSB/PR) | Da COMISSÃO DE EDUCAÇÃO E CULTURA, sobre o Projeto de Lei n° 6207, de 2023, que Declara o Municíp... | EMENDA_PARCIAL | NORMAL | SF | 47 | CE | Comissão de Educação e Cultura | 2024-05-14 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9606394 | 2024 |
| 9545755 | 7558952 | 7558404 | 9545753 | 8618228 | EMENDA 8 - MPV 1206/2024 | 8 | Senador Ciro Nogueira (PP/PI) | Emenda à MPV 1206/2024 - imposto de renda | EMENDA_PARCIAL | NORMAL | CN | 2654 | CMMPV 1206/2024 | Comissão Mista da Medida Provisória n° 1206, de 2024 | 2024-02-08 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9545753 | 2024 |
| 9547469 | 7559238 | 7558404 | 9547467 | 8618228 | EMENDA 31 - MPV 1206/2024 | 31 | Senador Mecias de Jesus (REPUBLICANOS/RR) | Emenda 3 à MPV 1206/2024 | EMENDA_PARCIAL | NORMAL | CN | 2654 | CMMPV 1206/2024 | Comissão Mista da Medida Provisória n° 1206, de 2024 | 2024-02-15 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9547467 | 2024 |
| 9610523 | 7568969 | 7567765 | 9610521 | 8659393 | EMENDA 66 - MPV 1216/2024 | 66 | Deputada Federal Luisa Canziani (PSD/PR) | Suprimam-se o art. 1º-B, o inciso IV do caput do art. 2º e o § 7º do art. 6º; e dê-se nova redaçã... | EMENDA_PARCIAL | NORMAL | CN | 2670 | CMMPV 1216/2024 | Comissão Mista da Medida Provisória n° 1216, de 2024 | 2024-05-15 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9610521 | 2024 |
| 9770930 | 7578760 | 7577647 | 9770928 | 8701679 | EMENDA 17-U - PLP 68/2024 | 17 | Senador Mecias de Jesus (REPUBLICANOS/RR) | Emenda 13 ao PLP 68/2024 | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2024-08-12 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9770928 | 2024 |
| 9780584 | 7579734 | 7577647 | 9780582 | 8701679 | EMENDA 322-U - PLP 68/2024 | 322 | Senador Luis Carlos Heinze (PP/RS) | Emenda 30 ao PLP 68/2024 - 01 M | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2024-08-14 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9780582 | 2024 |
| 9781920 | 7579930 | 7577647 | 9781918 | 8701679 | EMENDA 449-U - PLP 68/2024 | 449 | Senador Alessandro Vieira (MDB/SE) | Emenda  ao PLP 68/2024 (PCD) | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2024-08-15 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9781918 | 2024 |
| 9783316 | 7580181 | 7577647 | 9783314 | 8701679 | EMENDA 651-U - PLP 68/2024 | 651 | Senador Laércio Oliveira (PP/SE) | EM \| Emenda  ao PLP 68/2024_Dê-se a seguinte redação ao inciso I do art. 59 do PLP nº 68, de 2024 | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2024-08-15 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9783314 | 2024 |
| 9831542 | 7587086 | 7577647 | 9831540 | 8701679 | EMENDA 1473 - PLP 68/2024 | 1473 | Senador Weverton (PDT/MA) | Emenda 41 ao PLP 68/2024 - corrigir fantasy sport | EMENDA_PARCIAL | NORMAL | SF | 34 | CCJ | Comissão de Constituição, Justiça e Cidadania | 2024-10-23 | http://legis.senado.leg.br/sdleg-getter/documento?dm=9831540 | 2024 |

---

## main.encontro_legislativo_senado

| id_processo | id_despacho | id_encontro_legislativo | data_encontro | tipo_encontro | descricao_encontro | casa_encontro | numero_encontro | colegiado_casa | colegiado_codigo | colegiado_nome | colegiado_sigla | year_snapshot | rn |
|-------------|-------------|-------------------------|---------------|---------------|--------------------|---------------|-----------------|----------------|------------------|----------------|-----------------|---------------|----|
| 8617061 | 9620473 | 8671076 | 2024-05-28 | SES | Eventos Independentes de Sessão | SF | 1 | SF | 1998 | Plenário do Senado Federal | PLEN | 2024 | 1 |
| 8011172 | 8929229 | 8024992 | 2021-02-23 | SES | Sessão Deliberativa Ordinária | SF | 5 | SF | 1998 | Plenário do Senado Federal | PLEN | 2020 | 1 |
| 8293065 | 9342882 | 8436174 | 2023-04-27 | SES | Eventos Independentes de Sessão | SF | 1 | SF | 1998 | Plenário do Senado Federal | PLEN | 2022 | 1 |
| 7917285 | 8124848 | 7931829 | 2020-06-23 | SES | Sessão Deliberativa Remota | SF | 59 | SF | 1998 | Plenário do Senado Federal | PLEN | 2020 | 1 |
| 8208068 | 9190734 | 8289717 | 2022-07-13 | SES | Eventos Independentes de Sessão | SF | 1 | SF | 1998 | Plenário do Senado Federal | PLEN | 2022 | 1 |
| 7876822 | 8864755 | 7958921 | 2020-07-15 | SES | Sessão Deliberativa Remota | SF | 69 | SF | 1998 | Plenário do Senado Federal | PLEN | 2020 | 1 |
| 8199560 | 9169015 | 8269078 | 2022-06-07 | SES | Eventos Independentes de Sessão | SF | 1 | SF | 1998 | Plenário do Senado Federal | PLEN | 2022 | 1 |
| 7868372 | 8069358 | 7868746 | 2020-02-19 | SES | Sessão Deliberativa Ordinária | SF | 10 | SF | 1998 | Plenário do Senado Federal | PLEN | 2020 | 1 |
| 8470977 | 9397132 | 8482898 | 2023-06-26 | SES | Eventos Independentes de Sessão | SF | 1 | SF | 1998 | Plenário do Senado Federal | PLEN | 2023 | 1 |
| 8632160 | 9562322 | 8632227 | 2024-03-11 | SES | Eventos Independentes de Sessão | SF | 1 | SF | 1998 | Plenário do Senado Federal | PLEN | 2024 | 1 |

---

## main.ente_senado

| id_ente | sigla | nome | casa | sigla_tipo | descricao_tipo | data_inicio | data_fim | tag |
|---------|-------|------|------|------------|----------------|-------------|----------|-----|
| 7351588 | CMMPV 945/2020 | Comissão Mista da Medida Provisória n° 945/2020 | CN | COLEGIADO_LEGISLATIVO | Colegiado Legislativo | 2020-04-04 | NULL | SE:7351588 |
| 7357739 | CAM_MUN_SP_3350 | Câmara Municipal de Bragança Paulista - SP | NULL | CASA_LEGISLATIVA | Casa Legislativa | NULL | NULL | SE:7357739 |
| 7358618 | CAM_MUN_SC_4352 | Câmara Municipal de Braço do Norte - SC | NULL | CASA_LEGISLATIVA | Casa Legislativa | NULL | NULL | SE:7358618 |
| 7356328 | CAM_MUN_RS_4673 | Câmara Municipal de Campo Novo - RS | NULL | CASA_LEGISLATIVA | Casa Legislativa | NULL | NULL | SE:7356328 |
| 7354972 | CAM_MUN_CE_974 | Câmara Municipal de Itaitinga - CE | NULL | CASA_LEGISLATIVA | Casa Legislativa | NULL | NULL | SE:7354972 |
| 7355164 | CAM_MUN_PR_4218 | Câmara Municipal de Rio Negro - PR | NULL | CASA_LEGISLATIVA | Casa Legislativa | NULL | NULL | SE:7355164 |
| 7353587 | CAM_MUN_ES_3161 | Câmara Municipal de São Mateus - ES | NULL | CASA_LEGISLATIVA | Casa Legislativa | NULL | NULL | SE:7353587 |
| 7350375 | GSAOLIVE | Gabinete do Senador Arolde de Oliveira | SF | GABINETE_PARLAMENTAR | Gabinete de Parlamentar | 2018-10-26 | 2020-10-21 | SE:7350375 |
| 7361080 | NULL | Governo | NULL | UNIDADE_LIDERANCA | Unidade de liderança | NULL | NULL | SE:7361080 |
| 5377758 | NULL | Tribunal Regional Federal da 1ª Região | NULL | TRIBUNAL_REGIONAL_FEDERAL | Tribunal Regional Federal | NULL | NULL | SE:5377758 |

---

## main.eventos_camara

| id_evento | data_hora_inicio | data_hora_fim | descricao | descricao_tipo | fases | uri | year_snapshot | rn |
|-----------|------------------|---------------|-----------|----------------|-------|-----|---------------|----|
| 60717 | 2021-03-24 09:00:00 | 2021-03-24 10:47:00 | Discussão e Votação de Proposições  | Reunião Deliberativa | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/60717 | 2021 | 1 |
| 69346 | 2023-08-24 10:00:00 | 2023-08-24 13:01:00 | Recente aumento da tarifa de energia elétrica do Pará.  Em atendimento ao Requerimento nº 114/20... | Audiência Pública | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/69346 | 2023 | 1 |
| 72765 | 2024-05-16 09:30:00 | 2024-05-16 12:27:00 | Regulamentação da profissão de organizadores e gestores de eventos  Requerimento Nº 13/2024, da ... | Audiência Pública | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/72765 | 2024 | 1 |
| 74920 | 2024-11-19 15:00:00 | NULL | Discussão e votação de propostas legislativas  | Reunião Deliberativa | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/74920 | 2024 | 1 |
| 65084 | 2022-05-16 14:00:00 | 2022-05-16 16:27:00 | Privatização da Eletrobras  Expositores convidados:  1- ANDERSON MARCIO DE OLIVEIRA - Diretor ... | Audiência Pública | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/65084 | 2022 | 1 |
| 68822 | 2023-07-12 09:00:00 | NULL | Discussão e votação de propostas legislativas  | Reunião Deliberativa | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/68822 | 2023 | 1 |
| 67983 | 2023-05-10 10:00:00 | 2023-05-10 11:08:00 | Discussão e votação de propostas legislativas  | Reunião Deliberativa | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/67983 | 2023 | 1 |
| 68189 | 2023-05-24 14:00:00 | 2023-05-24 15:10:00 | Discussão e votação de propostas legislativas  Pauta a ser oportunamente divulgada. | Reunião Deliberativa | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/68189 | 2023 | 1 |
| 72676 | 2024-05-08 14:00:00 | 2024-05-08 15:07:00 | Discussão e votação de propostas legislativas  | Reunião Deliberativa | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/72676 | 2024 | 1 |
| 69829 | 2023-10-06 19:30:00 | 2023-10-06 21:00:00 | PL 2387/23 - Reconhecimento das educadoras infantis como professoras  REQ nº 196/2023, de autori... | Seminário | NULL | https://dadosabertos.camara.leg.br/api/v2/eventos/69829 | 2023 | 1 |

---

## main.eventos_orgaos_camara

| id_evento_orgao | id_evento | id_orgao | year_snapshot |
|-----------------|-----------|----------|---------------|
| 988 | 60804 | 2004 | 2021 |
| 2189 | 62286 | 2010 | 2021 |
| 2852 | 63097 | 2009 | 2021 |
| 4758 | 65432 | 2008 | 2022 |
| 6369 | 67682 | 5438 | 2023 |
| 6371 | 67685 | 100950 | 2023 |
| 9452 | 71712 | 2014 | 2023 |
| 9989 | 72505 | 537480 | 2024 |
| 10320 | 72960 | 2012 | 2024 |
| 11556 | 74721 | 2008 | 2024 |

---

## main.eventos_pauta_camara

| id_pauta | id_evento | cod_regime | ordem | id_proposicao | id_relator | year_snapshot |
|----------|-----------|------------|-------|---------------|------------|---------------|
| 11774 | 62365 | 14.0 | 24 | 2290933 | NULL | 2021 |
| 19075 | 63867 | 24.0 | 7 | 2304999 | 74160 | 2021 |
| 22922 | 64515 | 14.0 | 42 | 2305459 | 204412 | 2021 |
| 25330 | 65095 | 99.0 | 2 | 2320971 | NULL | 2022 |
| 30330 | 66141 | 99.0 | 1 | 2331626 | NULL | 2022 |
| 30873 | 66219 | 14.0 | 33 | 2330270 | 204455 | 2022 |
| 33677 | 66615 | 99.0 | 1 | 2326371 | NULL | 2022 |
| 35240 | 66902 | 99.0 | 1 | 2339409 | NULL | 2022 |
| 37953 | 67082 | 99.0 | 1794 | 2288237 | 204556 | 2022 |
| 40805 | 67680 | 14.0 | 14 | 2231339 | 160512 | 2023 |

---

## main.frentes_camara

| id_frente | id_deputado_coordenador | id_legislatura | titulo | uri | year_snapshot | rn |
|-----------|-------------------------|----------------|--------|-----|---------------|----|
| 53500 | 178963 | 55 | Frente Parlamentar Mista de Logística de Transportes e Armazenagem - FRENLOG | https://dadosabertos.camara.leg.br/api/v2/frentes/53500 | 0 | 1 |
| 460 | 160636 | 54 | Frente Parlamentar Mista em Defesa do Magistério | https://dadosabertos.camara.leg.br/api/v2/frentes/460 | 0 | 1 |
| 53388 | 129618 | 54 | Frente Parlamentar da Causa QESA | https://dadosabertos.camara.leg.br/api/v2/frentes/53388 | 0 | 1 |
| 55636 | 220620 | 57 | Frente Parlamentar Mista para a Defesa e Valorização das Polícias Institucionais | https://dadosabertos.camara.leg.br/api/v2/frentes/55636 | 0 | 1 |
| 53413 | 161907 | 54 | Frente Parlamentar Mista do Marketing Multinível | https://dadosabertos.camara.leg.br/api/v2/frentes/53413 | 0 | 1 |
| 53487 | 167493 | 55 | Frente Parlamentar em Defesa das Populações Atingidas por Áreas Protegidas (unidades de Conservaç... | https://dadosabertos.camara.leg.br/api/v2/frentes/53487 | 0 | 1 |
| 442 | 160592 | 54 | Frente Parlamentar Mista José Alencar para o Desenvolvimento da Indústria Têxtil e da Confecção d... | https://dadosabertos.camara.leg.br/api/v2/frentes/442 | 0 | 1 |
| 54333 | 204462 | 57 | Frente Parlamentar Mista contra o Aborto e em Defesa da Vida | https://dadosabertos.camara.leg.br/api/v2/frentes/54333 | 0 | 1 |
| 53679 | 160604 | 55 | Frente Parlamentar Mistas das Ferrovias | https://dadosabertos.camara.leg.br/api/v2/frentes/53679 | 0 | 1 |
| 53505 | 74400 | 55 | Frente Parlamentar Mista pela Competitividade da Cadeia Produtiva do Setor Químico, Petroquímico ... | https://dadosabertos.camara.leg.br/api/v2/frentes/53505 | 0 | 1 |

---

## main.informes_documentos_associados_senado

| id_documento_associado | id_processo | id_informe | id_documento | autuacao_ordem | informe_ordem | documento_ordem | sigla_tipo_documento | tipo_documento | identificacao | data_documento | autoria_documento | url_documento | year_snapshot |
|------------------------|-------------|------------|--------------|----------------|---------------|-----------------|----------------------|----------------|---------------|----------------|-------------------|---------------|---------------|
| 332 | 580351 | 2150649 | 9419085 | 0 | 201 | 0 | LISTAGEM_RELATORIO | Listagem ou relatório descritivo | Listagem ou relatório descritivo - SF236498359984 | 2023-08-05 00:00:00 | Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=9419085 | 2015 |
| 4578 | 7197009 | 2118334 | 9250359 | 0 | 83 | 0 | REQUERIMENTO | Requerimento | RQS 41/2023 | 2023-02-02 09:34:37 | Senador Romário (PL/RJ), Senador Flávio Bolsonaro (PL/RJ), Senador Eduardo Gomes (PL/TO), Senador... | http://legis.senado.leg.br/sdleg-getter/documento?dm=9250359 | 2017 |
| 10892 | 2922714 | 1857692 | 3628554 | 0 | 13 | 0 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária | Texto final - Projeto de Lei Ordinária | 2015-10-07 00:00:00 | Autoria não registrada. | http://legis.senado.leg.br/sdleg-getter/documento?dm=3628554 | 2015 |
| 14742 | 7729216 | 2052723 | 8960200 | 0 | 35 | 2 | OFICIO | Ofício | OFSF 179/2021 | 2021-05-03 00:00:00 | Primeiro-Secretário do Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=8960200 | 2019 |
| 24382 | 7829457 | 2101219 | 9218796 | 0 | 12 | 0 | PARECER | Parecer | P.S 119/2022 - CCT | 2022-12-01 00:00:00 | Comissão de Ciência, Tecnologia, Inovação, Comunicação e Informática, Senador Carlos Viana (PL/MG) | http://legis.senado.leg.br/sdleg-getter/documento?dm=9218796 | 2019 |
| 24591 | 7751229 | 2096967 | 9201741 | 0 | 25 | 0 | OFICIO | Ofício | Ofício - SF223859806055 | 2022-09-21 00:00:00 | Presidente de Comissão | http://legis.senado.leg.br/sdleg-getter/documento?dm=9201741 | 2019 |
| 34103 | 7958926 | 2167823 | 9492032 | 0 | 21 | 0 | OFICIO | Ofício | Ofício - SF235706948923 | 2023-10-31 13:02:32 | Presidente de Comissão | http://legis.senado.leg.br/sdleg-getter/documento?dm=9492032 | 2020 |
| 34923 | 7958151 | 2052890 | 8965950 | 0 | 13 | 0 | PARECER | Parecer | P.S 10/2021 - CDIR | 2021-05-05 00:00:00 | Comissão Diretora do Senado Federal | http://legis.senado.leg.br/sdleg-getter/documento?dm=8965950 | 2020 |
| 38884 | 7974395 | 2049309 | 8942989 | 0 | 39 | 1 | DECLARACAO_VOTO | Declaração de Voto | Declaração de Voto | 2021-03-17 07:21:17 | Deputado Federal João Maia (PL/RN) | http://legis.senado.leg.br/sdleg-getter/documento?dm=8942989 | 2020 |
| 39373 | 8003818 | 2043209 | 8911340 | 0 | 5 | 0 | OFICIO | Ofício | OFCN 450/2020 | 2020-12-09 00:00:00 | Diretor da Secretaria de Expediente | http://legis.senado.leg.br/sdleg-getter/documento?dm=8911340 | 2020 |

---

## main.informes_legislativos_senado

| id_informe_legislativo | id_processo | id_informe | data_informe | descricao | id_situacao_iniciada | sigla_situacao_iniciada | ente_adm_casa | ente_adm_id | ente_adm_nome | ente_adm_sigla | colegiado_casa | colegiado_codigo | colegiado_nome | colegiado_sigla | year_snapshot |
|------------------------|-------------|------------|--------------|-----------|----------------------|-------------------------|---------------|-------------|---------------|----------------|----------------|------------------|----------------|-----------------|---------------|
| 1153 | 7187694 | 2151179 | 2023-08-05 | A matéria vai ao arquivo. | NULL | NULL | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF | NULL | NULL | NULL | NULL | 2017 |
| 6846 | 502233 | 2060728 | 2021-08-09 | Devolvido pelo relator, Senador Ciro Nogueira, em virtude de não mais pertencer aos quadros desta... | 87 | AGDREL | SF | 13565 | Secretaria de Apoio à Comissão de Constituição, Justiça e Cidadania | SACCJ | SF | 34 | Comissão de Constituição, Justiça e Cidadania | CCJ | 2016 |
| 10032 | 7703136 | 2001403 | 2019-04-29 | Juntei, às fls. 3 a 9, o Parecer, a lista do registro de presença dos senadores e a decisão da Co... | NULL | NULL | SF | 55302 | Secretaria de Apoio à Comissão de Direitos Humanos e Legislação Participativa | SACDH | SF | 834 | Comissão de Direitos Humanos e Legislação Participativa | CDH | 2018 |
| 14870 | 2919419 | 2098858 | 2022-11-07 | Incluído em Ordem do Dia da Sessão Deliberativa Ordinária Semipresencial de 08/11/2022. Discussã... | 78 | INCLOD | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF | SF | 1998 | Plenário do Senado Federal | PLEN | 2015 |
| 16893 | 501256 | 1935209 | 2018-12-11 | Em reunião realizada em 11/12/2018, a apreciação da matéria foi adiada. | 42 | PRONTPAUT | SF | 13530 | Secretaria de Apoio à Comissão de Assuntos Econômicos | SACAE | SF | 38 | Comissão de Assuntos Econômicos | CAE | 2016 |
| 18758 | 2920795 | 2085773 | 2022-04-28 | Matéria constante da Pauta da 14ª Reunião da Comissão de Direitos Humanos e Legislação Participat... | 138 | INPAUTA | SF | 55302 | Secretaria de Apoio à Comissão de Direitos Humanos e Legislação Participativa | SACDH | SF | 834 | Comissão de Direitos Humanos e Legislação Participativa | CDH | 2015 |
| 21462 | 7407509 | 1992113 | 2018-07-12 | Esgotado o prazo regimental sem a apresentação de emendas, a matéria aguarda designação de Relato... | 87 | AGDREL | SF | 5225770 | Secretaria de Apoio à Comissão de Transparência, Governança, Fiscalização e Controle e Defesa do ... | SACTFC | SF | 1956 | Comissão de Transparência, Governança, Fiscalização e Controle e Defesa do Consumidor | CTFC | 2018 |
| 24335 | 5218045 | 1948449 | 2017-04-05 | Matéria sobre a Mesa desta Comissão aguardando abertura de prazo para apresentação de emendas, e ... | NULL | NULL | SF | 13565 | Secretaria de Apoio à Comissão de Constituição, Justiça e Cidadania | SACCJ | SF | 34 | Comissão de Constituição, Justiça e Cidadania | CCJ | 2017 |
| 25499 | 1330336 | 1910290 | 2015-12-15 | Este processo contém 02  ( duas  ) folha(s) numerada(s) e rubricada(s). | NULL | NULL | SF | 7217797 | PROTOCOLO LEGISLATIVO | PLEG | NULL | NULL | NULL | NULL | 2015 |
| 28793 | 7152001 | 1969842 | 2018-02-20 | Em reunião realizada em 20/02/2018, a apreciação da matéria foi adiada. | 42 | PRONTPAUT | SF | 55316 | Secretaria de Apoio à Comissão de Educação e Cultura | SACE | SF | 47 | Comissão de Educação e Cultura | CE | 2017 |

---

## main.legislaturas_camara

| id_legislatura | data_inicio | data_fim | uri | year_snapshot | rn |
|----------------|-------------|----------|-----|---------------|----|
| 41 | 1959-02-01 | 1963-01-31 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/41 | 0 | 1 |
| 53 | 2007-02-01 | 2011-01-31 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/53 | 0 | 1 |
| 24 | 1897-04-18 | 1900-04-17 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/24 | 0 | 1 |
| 10 | 1857-04-15 | 1861-04-14 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/10 | 0 | 1 |
| 17 | 1878-11-27 | 1881-06-30 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/17 | 0 | 1 |
| 31 | 1918-04-18 | 1921-04-14 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/31 | 0 | 1 |
| 32 | 1921-04-15 | 1924-04-14 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/32 | 0 | 1 |
| 52 | 2003-02-01 | 2007-01-31 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/52 | 0 | 1 |
| 11 | 1861-04-15 | 1863-05-12 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/11 | 0 | 1 |
| 55 | 2015-02-01 | 2019-01-31 | https://dadosabertos.camara.leg.br/api/v2/legislaturas/55 | 0 | 1 |

---

## main.legislaturas_lideres_camara

| id_lider | id_legislatura | nome_bancada | tipo_bancada | uri_bancada | data_inicio | data_fim | id_deputado | titulo | year_snapshot |
|----------|----------------|--------------|--------------|-------------|-------------|----------|-------------|--------|---------------|
| 3174 | 55 | PSB | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36832 | 2016-04-16 00:00:00 | 2016-04-16 00:00:00 | 178898 | Vice-Líder | 2015 |
| 3627 | 55 | PSDB | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36835 | 2017-03-07 00:00:00 | 2018-02-19 00:00:00 | 178856 | Vice-Líder | 2015 |
| 3960 | 55 | PT | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36844 | 2017-03-08 00:00:00 | 2019-01-31 00:00:00 | 113247 | Vice-Líder | 2015 |
| 5192 | 56 | NOVO | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/37901 | 2021-09-30 00:00:00 | 2021-11-09 00:00:00 | 204365 | Vice-Líder | 2020 |
| 5313 | 56 | NOVO | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/37901 | 2019-12-16 00:00:00 | 2019-12-17 00:00:00 | 204519 | Vice-Líder | 2020 |
| 6270 | 56 | PROS | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36763 | 2021-12-15 00:00:00 | 2022-02-15 00:00:00 | 178934 | Vice-Líder | 2020 |
| 7582 | 56 | PSOL | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36839 | 2021-08-06 00:00:00 | 2021-08-09 00:00:00 | 204509 | Vice-Líder | 2020 |
| 8810 | 56 | PT | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/36844 | 2020-04-07 00:00:00 | 2020-04-07 00:00:00 | 178986 | Vice-Líder | 2020 |
| 9542 | 56 | UNIÃO | Partido Político | https://dadosabertos.camara.leg.br/api/v2/partidos/38009 | 2022-12-22 00:00:00 | 2022-12-22 00:00:00 | 204451 | Vice-Líder | 2020 |
| 11811 | 57 | UNIÃO | Bloco Parlamentar | https://dadosabertos.camara.leg.br/api/v2/blocos/588 | 2024-07-03 00:00:00 | 2024-07-11 00:00:00 | 204494 | Vice-Líder | 2023 |

---

## main.legislaturas_mesa_camara

| id_legislatura_mesa | id_legislatura | id_deputado | cod_titulo | data_inicio | data_fim | year_snapshot |
|---------------------|----------------|-------------|------------|-------------|----------|---------------|
| 115 | 52 | 74563 | 10 | 2005-02-14 | 2007-01-31 | 2003 |
| 13 | 52 | 74520 | 2 | 2005-02-16 | 2007-01-31 | 2003 |
| 31 | 52 | 74313 | 3 | 2005-02-14 | 2007-01-31 | 2003 |
| 110 | 53 | 73433 | 1 | 2007-02-01 | 2009-02-02 | 2007 |
| 92 | 53 | 73552 | 1 | 2009-02-02 | 2010-12-16 | 2007 |
| 8 | 53 | 74163 | 9 | 2007-02-01 | 2009-02-02 | 2007 |
| 39 | 54 | 74374 | 9 | 2011-02-01 | 2013-02-04 | 2011 |
| 100 | 55 | 74693 | 1 | 2016-07-14 | 2017-02-02 | 2015 |
| 58 | 55 | 141427 | 2 | 2017-02-02 | 2019-01-31 | 2015 |
| 102 | 57 | 220669 | 6 | 2025-02-01 | NULL | 2023 |

---

## main.missing_orgaos

*Table is empty*


---

## main.movimentacoes_senado

| id_processo | autuacao_idx | movimentacao_idx | id_movimentacao | data_envio | data_recebimento | ente_origem_casa | ente_origem_id | ente_origem_nome | ente_origem_sigla | ente_destino_casa | ente_destino_id | ente_destino_nome | ente_destino_sigla | colegiado_destino_casa | colegiado_destino_codigo | colegiado_destino_nome | colegiado_destino_sigla | year_snapshot |
|-------------|--------------|------------------|-----------------|------------|------------------|------------------|----------------|------------------|-------------------|-------------------|-----------------|-------------------|--------------------|------------------------|--------------------------|------------------------|-------------------------|---------------|
| 1394793 | 0 | 8 | 9930674 | 2025-04-08 15:46:24 | 2025-04-08 15:48:24 | SF | 55290 | Serviço de Protocolo Legislativo | SEPRTL | SF | 55299 | Coordenação de Arquivo | COARQ | NULL | NULL | NULL | NULL | 2016 |
| 573418 | 0 | 19 | 9273701 | 2022-12-22 02:27:07 | 2022-12-22 14:48:38 | SF | 13565 | Secretaria de Apoio à Comissão de Constituição, Justiça e Cidadania | SACCJ | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF | SF | 1998 | Plenário do Senado Federal | PLEN | 2016 |
| 1329918 | 0 | 7 | 9271739 | 2016-06-15 16:43:56 | 2016-06-15 16:57:11 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 13565 | Secretaria de Apoio à Comissão de Constituição, Justiça e Cidadania | SACCJ | NULL | NULL | NULL | NULL | 2016 |
| 2602049 | 0 | 35 | 8669010 | 2020-03-31 09:43:13 | 2020-09-24 17:29:21 | SF | 4892928 | Coordenação de Apoio à Mesa | COAME | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 1998 | Plenário do Senado Federal | PLEN | 2014 |
| 7703122 | 0 | 3 | 9269595 | 2018-12-19 09:02:54 | 2018-12-20 15:42:45 | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF | SF | 13594 | Secretaria de Atas e Diários | SEADI | NULL | NULL | NULL | NULL | 2018 |
| 5000887 | 0 | 0 | 8752252 | 2017-02-14 17:11:11 | 2017-02-14 18:53:51 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55313 | Secretaria de Apoio à Comissão de Assuntos Sociais | SACAS | SF | 40 | Comissão de Assuntos Sociais | CAS | 2017 |
| 7756896 | 0 | 4 | 8832407 | 2020-03-26 18:38:15 | 2020-06-04 11:27:07 | SF | 4892928 | Coordenação de Apoio à Mesa | COAME | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 |
| 7876139 | 0 | 6 | 9162431 | 2022-05-25 12:23:28 | 2023-01-16 08:36:50 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55299 | Coordenação de Arquivo | COARQ | NULL | NULL | NULL | NULL | 2020 |
| 8659115 | 0 | 8 | 9640391 | 2024-06-18 15:28:10 | 2024-06-18 16:14:31 | SF | 13594 | Secretaria de Atas e Diários | SEADI | SF | 55304 | Secretaria de Expediente | SEXPE | NULL | NULL | NULL | NULL | 2019 |
| 7814962 | 0 | 18 | 9222588 | 2022-12-13 07:53:03 | 2022-12-13 09:34:20 | SF | 7359809 | Núcleo de Redação Legislativa | NRELE | SF | 55312 | Secretaria Legislativa do Senado Federal | SLSF | SF | 1998 | Plenário do Senado Federal | PLEN | 2019 |

---

## main.orgaos_camara

| id_orgao | nome | cod_tipo_orgao | uri | year_snapshot | rn | tag |
|----------|------|----------------|-----|---------------|----|-----|
| 100846 | CENTRO DE INFORMÁTICA | 12000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/100846 | 0 | 1 | CO:100846 |
| 102602 | Comissão Mista da MPV 1155/2023 | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/102602 | 0 | 1 | CO:102602 |
| 101899 | Comissão Mista da MPV 832/2018 | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/101899 | 0 | 1 | CO:101899 |
| 102384 | Comissão Mista da MPV 994/2020 | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/102384 | 2020 | 1 | CO:102384 |
| 102574 | Comissão Mista da MPV 1133/2022 | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/102574 | 2022 | 1 | CO:102574 |
| 102931 | Comissão Mista da MPV 1276/2024 | 9 | https://dadosabertos.camara.leg.br/api/v2/orgaos/102931 | 0 | 1 | CO:102931 |
| 539775 | Grupo de Trabalho destinado a elaborar e propor à Mesa Diretora solução tecnológica de identifica... | 10 | https://dadosabertos.camara.leg.br/api/v2/orgaos/539775 | 0 | 1 | CO:539775 |
| 537804 | Comissão Especial destinada a proferir parecer ao Projeto de Lei nº 6299, de 2002, do Senado Fede... | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537804 | 2020 | 1 | CO:537804 |
| 537349 | Comissão Especial destinada a proferir parecer ao Projeto de Lei nº 4.238, de 2012, do Senado Fed... | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537349 | 2021 | 1 | CO:537349 |
| 382 | Tribunal de Justiça do Distrito Federal e dos Territórios | 50000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/382 | 2020 | 1 | CO:382 |

---

## main.orgaos_camara_hotfix

| id_orgao | nome | cod_tipo_orgao | uri | year_snapshot | rn |
|----------|------|----------------|-----|---------------|----|
| 6726 | Comissão Especial destinada ao exame e a avaliação da Crise Econômico-Financeira e, ao final, for... | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/6726 | 2020 | 1 |
| 81 | Superior Tribunal de Justiça | 50000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/81 | 2020 | 1 |
| 57 | MINISTÉRIO PÚBLICO DA UNIÃO | 50000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/57 | 2020 | 1 |
| 102133 | P50 SERVIÇOS INTEGRADOS | 70000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/102133 | 2020 | 1 |
| 102346 | Dep. João H. Campos | 70000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/102346 | 2020 | 1 |
| 9140 | Comissão Parlamentar de Inquérito destinada a apurar denúncias de turismo sexual e exploração sex... | 4 | https://dadosabertos.camara.leg.br/api/v2/orgaos/9140 | 2020 | 1 |
| 537487 | Comissão Parlamentar de Inquérito destinada a investigar a Cartelização na Fixação de Preços e Di... | 4 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537487 | 2020 | 1 |
| 101772 | MPF - PGR - Procuradoria Geral da República | 70000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/101772 | 2020 | 1 |
| 101798 | Iniciativa Popular | 70000 | https://dadosabertos.camara.leg.br/api/v2/orgaos/101798 | 2020 | 1 |
| 537939 | Comissão Especial para análise, estudo e formulação de proposições relacionadas à Reforma Política | 3 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537939 | 2020 | 1 |

---

## main.orientacoes_camara

| id_orientacao | id_votacao | sigla_partido_bloco | orientacao_voto | cod_partido_bloco | cod_tipo_lideranca | uri_partido_bloco | year_snapshot |
|---------------|------------|---------------------|-----------------|-------------------|--------------------|-------------------|---------------|
| 5308 | 2205645-77 | Governo | Sim | NULL | B | NULL | 2020 |
| 9299 | 2260971-117 | NOVO | Não | 37901 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/37901 | 2020 |
| 16735 | 2266115-55 | REDE | Sim | 36886 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36886 | 2020 |
| 19707 | 2266116-68 | Minoria | Liberado | NULL | B | NULL | 2020 |
| 27403 | 2270800-172 | PDT |  | 36786 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36786 | 2021 |
| 29738 | 2272137-266 | PROS | Sim | 36763 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36763 | 2021 |
| 30987 | 2279513-118 | PATRIOTA | Não | 37907 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/37907 | 2021 |
| 34874 | 2291898-73 | PP | Sim | 37903 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/37903 | 2021 |
| 37937 | 2283436-57 | PSL | Não | 36837 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36837 | 2021 |
| 40168 | 2309053-95 | REDE |  | 36886 | P | https://dadosabertos.camara.leg.br/api/v2/partidos/36886 | 2021 |

---

## main.outros_numeros_senado

| id_outro_numero | id_processo | id_outro_processo | ano | casa_identificadora | ente_identificador | sigla | numero | sigla_ente_identificador | externa_ao_congresso | tramitando | year_snapshot |
|-----------------|-------------|-------------------|-----|---------------------|--------------------|-------|--------|--------------------------|----------------------|------------|---------------|
| 232 | 5009694 | 7892018 | 2020 | CD | Câmara dos Deputados | PL | 01586 | CD | Não | Sim | 2017 |
| 1250 | 8524448 | 8524447 | 2019 | CD | Câmara dos Deputados | PL | 03811 | CD | Não | Sim | 2019 |
| 1380 | 7885017 | 7885016 | 2020 | CD | Câmara dos Deputados | PL | 00864 | CD | Não | Não | 2020 |
| 1695 | 7973302 | 7922056 | 2020 | NULL | Presidência da República | MSG | 00316 | PR | Sim | Não | 2020 |
| 1781 | 7992741 | 7992741 | 2020 | NULL | Presidência da República | MSG | 00606 | PR | Sim | Não | 2020 |
| 2660 | 8276003 | 8276002 | 2021 | CD | Câmara dos Deputados | PDL | 00949 | CD | Não | Sim | 2021 |
| 2961 | 8268926 | 8268926 | 2022 | NULL | Presidência da República | MSG | 00277 | PR | Sim | Não | 2022 |
| 3509 | 8524306 | 8524306 | 2023 | NULL | Presidência da República | MSG | 00414 | PR | Sim | Não | 2023 |
| 3533 | 8538700 | 8538700 | 2023 | NULL | Presidência da República | MSG | 00440 | PR | Sim | Não | 2023 |
| 3843 | 8502522 | 8541572 | 2023 | CD | Câmara dos Deputados | PL | 03696 | CD | Não | Não | 2023 |

---

## main.parlamentar_senado

| codigo_parlamentar | codigo_publico_leg_atual | nome_completo | nome_parlamentar | sexo_parlamentar | sigla_partido | uf_parlamentar | email_parlamentar | data_nascimento | endereco_parlamentar | naturalidade | uf_naturalidade | year_snapshot | rn |
|--------------------|--------------------------|---------------|------------------|------------------|---------------|----------------|-------------------|-----------------|----------------------|--------------|-----------------|---------------|----|
| 5621 | NULL | Rudson Leite da Silva | Rudson Leite | Masculino | PV | NULL | sen.rudsonleite@senado.leg.br | 1963-07-29 | Senado Federal Anexo 2   Ala Ruy Carneiro Gabinete 03 | Boa Vista | RR | 2023 | 1 |
| 5611 | NULL | Severino Nunes de Araujo | Severino Araujo | Masculino | PSB | NULL | NULL | 1939-01-17 | NULL | Limoeiro | PE | 2023 | 1 |
| 5972 | 915 | Julio Ventura Neto | Julio Ventura | Masculino | PDT | NULL | NULL | 1959-01-24 | Senado Federal Anexo 1  10º Pavimento   | Fortaleza | CE | 2024 | 1 |
| 6355 | NULL | Emerson Luiz Santana | Tenente Emerson | Masculino | PTB | NULL | NULL | 1974-01-17 | NULL | NULL | NULL | 2024 | 1 |
| 6001 | NULL | Arlindo Penha da Silva | Arlindo Silva | Masculino | NULL | NULL | NULL | 1958-10-15 | NULL | Rio de Janeiro | RJ | 2024 | 1 |
| 375 | NULL | Valdir Ganzer | Valdir Ganzer | Masculino | PT | NULL | NULL | 1955-06-01 | NULL | NULL | NULL | 2023 | 1 |
| 5591 | NULL | Manoel Francisco de Vasconcelos Motta | Manoel Motta | Masculino | PCB | NULL | NULL | 1949-12-21 | NULL | Recife | PE | 2023 | 1 |
| 5900 | NULL | Gil Marques de Medeiros | Gil Paraibano | Masculino | NULL | NULL | NULL | 1947-08-10 | NULL | Malta | PB | 2024 | 1 |
| 5923 | NULL | Alberto da Silva David | Alberto David | Masculino | NULL | NULL | NULL | 1972-01-23 | NULL | NULL | NULL | 2024 | 1 |
| 6365 | NULL | Leny May da Silva Campêlo | Leny Campêlo | Feminino | NULL | NULL | NULL | 1962-10-18 | NULL | NULL | NULL | 2024 | 1 |

---

## main.partido_senado

| codigo_partido | data_criacao | nome | sigla | year_snapshot |
|----------------|--------------|------|-------|---------------|
| 500 | 1928-03-03 | Partido Libertador | PL_RS | 1928 |
| 527 | 1932-01-01 | Liga Eleitoral Católica | LEC | 1932 |
| 555 | 1935-01-01 | Oposições Coligadas | OPCOL | 1935 |
| 498 | 1945-07-09 | Partido Democrata Cristão | PDC | 1945 |
| 20 | 1980-09-16 | Partido Democrático Trabalhista | PDT | 1980 |
| 89 | 1987-10-22 | Partido Social Democrático | PSD | 1987 |
| 91 | 1987-01-18 | Partido Verde | PV | 1987 |
| 66 | 1988-06-01 | Partido da Social Democracia Brasileira | PSDB | 1988 |
| 92 | 1989-02-22 | Partido da Reconstrução Nacional | PRN | 1989 |
| 38 | 1993-01-31 | Partido Progressista | PP | 1993 |

---

## main.partidos_camara

| id_partido | nome | sigla | uri | year_snapshot | rn |
|------------|------|-------|-----|---------------|----|
| 36851 | Partido Verde | PV | https://dadosabertos.camara.leg.br/api/v2/partidos/36851 | 0 | 1 |
| 37901 | Partido Novo | NOVO | https://dadosabertos.camara.leg.br/api/v2/partidos/37901 | 0 | 1 |
| 38010 | Partido Renovação Democrática | PRD | https://dadosabertos.camara.leg.br/api/v2/partidos/38010 | 0 | 1 |
| 36779 | Partido Comunista do Brasil | PCdoB | https://dadosabertos.camara.leg.br/api/v2/partidos/36779 | 0 | 1 |
| 36899 | Movimento Democrático Brasileiro | MDB | https://dadosabertos.camara.leg.br/api/v2/partidos/36899 | 0 | 1 |
| 36832 | Partido Socialista Brasileiro | PSB | https://dadosabertos.camara.leg.br/api/v2/partidos/36832 | 0 | 1 |
| 37905 | Cidadania | CIDADANIA | https://dadosabertos.camara.leg.br/api/v2/partidos/37905 | 0 | 1 |
| 36786 | Partido Democrático Trabalhista | PDT | https://dadosabertos.camara.leg.br/api/v2/partidos/36786 | 0 | 1 |
| 36896 | Podemos | PODE | https://dadosabertos.camara.leg.br/api/v2/partidos/36896 | 0 | 1 |
| 36844 | Partido dos Trabalhadores | PT | https://dadosabertos.camara.leg.br/api/v2/partidos/36844 | 0 | 1 |

---

## main.partidos_lideres_camara

| id_partido_lider | id_partido | cod_titulo | data_inicio | data_fim | id_deputado | year_snapshot |
|------------------|------------|------------|-------------|----------|-------------|---------------|
| 1 | 36834 | 1001 | 2023-02-01 | NULL | 160553 | 2023 |
| 4 | 36899 | 1001 | 2023-02-01 | NULL | 204436 | 2023 |
| 7 | 37908 | 1001 | 2025-02-04 | NULL | 204491 | 2023 |
| 12 | 36832 | 1002 | 2025-09-24 | NULL | 220686 | 2025 |
| 15 | 37906 | 1001 | 2025-02-01 | NULL | 178947 | 2025 |
| 16 | 38009 | 1001 | 2025-02-01 | NULL | 122974 | 2025 |
| 19 | 36899 | 1 | 2023-02-01 | NULL | 178975 | 2023 |
| 23 | 36832 | 1003 | 2025-09-16 | NULL | 204534 | 2025 |
| 24 | 36786 | 1002 | 2025-09-17 | NULL | 220607 | 2025 |
| 26 | 36786 | 1002 | 2025-09-17 | NULL | 220578 | 2025 |

---

## main.partidos_membros_camara

| id_partido_membro | id_partido | id_deputado | id_legislatura | year_snapshot |
|-------------------|------------|-------------|----------------|---------------|
| 109 | 37903 | 228616 | NULL | 2020 |
| 235 | 36896 | 220529 | NULL | 2020 |
| 362 | 36899 | 204456 | NULL | 2020 |
| 378 | 37906 | 220611 | NULL | 2020 |
| 478 | 38009 | 204398 | NULL | 2020 |
| 484 | 37908 | 160531 | NULL | 2020 |
| 504 | 37906 | 220526 | NULL | 2020 |
| 528 | 36834 | 92776 | NULL | 2020 |
| 540 | 36834 | 74574 | NULL | 2020 |
| 736 | 37906 | 204472 | NULL | 2020 |

---

## main.processo_senado

| id_processo | codigo_materia | id_processo_casa_inicial | identificacao | identificacao_processo_inicial | identificacao_externa | ano | casa_identificadora | sigla_casa_iniciadora | sigla_ente_identificador | descricao_sigla | sigla | numero | objetivo | tramitando | id_conteudo | id_tipo_conteudo | sigla_tipo_conteudo | tipo_conteudo | tipo_norma_indicada | ementa | explicacao_ementa | deliberacao_id_destino | deliberacao_sigla_destino | deliberacao_tipo | deliberacao_sigla_tipo | deliberacao_data | deliberacao_destino | id_documento | documento_sigla_tipo | documento_tipo | documento_indexacao | documento_resumo_autoria | documento_data_apresentacao | documento_data_leitura | norma_codigo | norma_numero | norma_sigla_tipo | norma_tipo | norma_descricao | norma_sigla_veiculo | norma_veiculo | norma_numero_int | norma_ano_assinatura | norma_data_assinatura | norma_data_publicacao | year_snapshot | tag |
|-------------|----------------|--------------------------|---------------|--------------------------------|-----------------------|-----|---------------------|-----------------------|--------------------------|-----------------|-------|--------|----------|------------|-------------|------------------|---------------------|---------------|---------------------|--------|-------------------|------------------------|---------------------------|------------------|------------------------|------------------|---------------------|--------------|----------------------|----------------|---------------------|--------------------------|-----------------------------|------------------------|--------------|--------------|------------------|------------|-----------------|---------------------|---------------|------------------|----------------------|-----------------------|-----------------------|---------------|-----|
| 7857901 | 140343 | 7857901 | PL 6539/2019 | PL 6539/2019 | {} | 2019 | SF | SF | SF | Projeto de Lei | PL | 6539 | Iniciadora | Não | 7404579 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 12.187, de 29 de dezembro de 2009, que institui a Política Nacional sobre Mudança... | Define a Contribuição Nacionalmente Determinada (NDC); inclui nas diretrizes da Política Nacional... | 1 | CAMARA | Aprovada pelo Plenário | APROVADA_NO_PLENARIO | 2021-11-03 | À Câmara dos Deputados | 8057880 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  LEI FEDERAL ,  POLITICA NACIONAL ,  MUDANÇA CLIMATICA ,  ATUALIZAÇÃO ,  CORRELAÇÃO ... | Comissão de Meio Ambiente | 2019-12-18 | 2019-12-18 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2019 | SP:7857901 |
| 7864669 | 140637 | 7864669 | PL 242/2020 | PL 242/2020 | {} | 2020 | SF | SF | SF | Projeto de Lei | PL | 242 | Iniciadora | Não | 7405695 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera o Decreto-Lei nº 5.452, de 1º de maio de 1943, que aprova a Consolidação das Leis do Traba... | Estabelece que o tempo de licença-maternidade será prorrogado por 180 dias, assim como também a e... | 4 | ARQUIVO | Retirada pelo autor | RETIRADO_PELO_AUTOR | 2023-08-08 | Ao arquivo | 8063196 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  CONSOLIDAÇÃO DAS LEIS DO TRABALHO (CLT) ,  PRORROGAÇÃO ,  PRAZO ,  PERIODO ,  ESTAB... | Senadora Mara Gabrilli (PSDB/SP) | 2020-02-06 | 2020-02-11 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2020 | SP:7864669 |
| 7905996 | 141752 | 7905996 | PL 2308/2020 | PL 2308/2020 | {} | 2020 | SF | SF | SF | Projeto de Lei | PL | 2308 | Iniciadora | Não | 7417830 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 13.979, de 6 de fevereiro de 2020, para dispor sobre uso compulsório de leitos pr... | Estabelece o uso compulsório de leitos em hospitais privados pelo poder público, para internações... | 4 | ARQUIVO | Prejudicada | PREJUDICADO | 2023-05-11 | Ao arquivo | 8101627 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  CRIAÇÃO ,  LEI FEDERAL ,  EMERGENCIA ,  CALAMIDADE PUBLICA ,  PANDEMIA ,  EPIDEMIA ,  CRITERIOS ... | Senador Rogério Carvalho (PT/SE), Senador Humberto Costa (PT/PE), Senadora Zenaide Maia (PROS/RN)... | 2020-04-29 | 2020-04-29 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2020 | SP:7905996 |
| 7922175 | 142272 | 7922175 | PLN 12/2020 | PLN 12/2020 | {"ano":2020,"identificacao":"MSG 315/2020","nomeEnte":"Presidência da República","numero":"315","... | 2020 | CN | CN | Mesa | Projeto de Lei do Congresso Nacional | PLN | 12 | NULL | Não | 7423026 | 11 | NORMA_GERAL | Norma Geral | LEI | Abre aos Orçamentos Fiscal e da Seguridade Social da União, em favor de diversos órgãos do Poder ... | Propõe recomposição parcial de dotações orçamentárias das despesas com Pessoal e Encargos Sociais... | 3 | SANCAO | Aprovada pelo Plenário | APROVADA_NO_PLENARIO | 2020-11-04 | À sanção | 8117208 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  CRIAÇÃO ,  LEI FEDERAL ,  CREDITO SUPLEMENTAR ,  ORÇAMENTO FISCAL ,  ORÇAMENTO DA SEGURIDADE SOC... | Presidência da República | 2020-06-02 | NULL | 32929146 | 14081 | LEI-n | Lei Numerada | Lei nº 14.081 de 17/11/2020 | DOU | [Diário Oficial da União  de 18/11/2020] (p. 3, col. 1) | 14081 | 2020 | 2020-11-17 | 2020-11-18 | 2020 | SP:7922175 |
| 7934836 | 143127 | 7934836 | PL 3557/2020 | PL 3557/2020 | {} | 2020 | SF | SF | SF | Projeto de Lei | PL | 3557 | Iniciadora | Não | 7425896 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 13.586, de 28 de dezembro de 2017, para dar diferente tratamento fiscal às ativid... | Revoga benefícios fiscais destinados a empresas petrolíferas relativos ao Imposto de Renda e à Co... | 4 | ARQUIVO | Retirada pelo autor | RETIRADO_PELO_AUTOR | 2024-03-21 | Ao arquivo | 8127431 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ALTERAÇÃO ,  LEI FEDERAL ,  REDUÇÃO ,  BENEFICIO FISCAL ,  EMPRESA DE PETROLEO ,  CONTRIBUIÇÃO S... | Senador Rogério Carvalho (PT/SE) | 2020-06-30 | 2020-06-30 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2020 | SP:7934836 |
| 8310943 | 154926 | 8310942 | PL 5310/2020 | PL 5310/2020 | {} | 2020 | SF | CD | SF | Projeto de Lei | PL | 5310 | Revisora | Não | 7503333 | 11 | NORMA_GERAL | Norma Geral | LEI | Denomina Viaduto Francisco Pereira Netto o viaduto situado sobre a rodovia BR-116, nas proximidad... | NULL | 3 | SANCAO | Aprovada por Comissão em decisão terminativa | APROVADA_EM_COMISSAO_TERMINATIVA | 2023-11-07 | À sanção | 9205865 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  CRIAÇÃO ,  LEI FEDERAL ,  DENOMINAÇÃO ,  VIADUTO ,  TRECHO ,  RODOVIA ,  MUNICIPIO ,  CURITIBA (... | Câmara dos Deputados | 2022-10-19 | 2022-10-19 | 37876812 | 14739 | LEI-n | Lei Numerada | Lei nº 14.739 de 28/11/2023 | DOU | [Diário Oficial da União  de 29/11/2023] (p. 1, col. 2) | 14739 | 2023 | 2023-11-28 | 2023-11-29 | 2020 | SP:8310943 |
| 8151190 | 151020 | 8151189 | PL 2058/2021 | PL 2058/2021 | {} | 2021 | SF | CD | SF | Projeto de Lei | PL | 2058 | Revisora | Não | 7468091 | 11 | NORMA_GERAL | Norma Geral | LEI | Altera a Lei nº 14.151, de 12 de maio de 2021, para disciplinar o afastamento da empregada gestan... | NULL | 1 | CAMARA | Aprovada pelo Plenário | APROVADA_NO_PLENARIO | 2021-12-16 | À Câmara dos Deputados | 9026873 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  POSSIBILIDADE ,  TRABALHO ,  DISTANCIA ,  ALTERAÇÃO ,  ATIVIDADE ,  MANUTENÇÃO ,  REMUNERAÇÃO . ... | Câmara dos Deputados | 2021-10-13 | 2021-11-29 | 35544457 | 14311 | LEI-n | Lei Numerada | Lei nº 14.311 de 09/03/2022 | DOU | [Diário Oficial da União  de 10/03/2022] (p. 1, col. 1) | 14311 | 2022 | 2022-03-09 | 2022-03-10 | 2021 | SP:8151190 |
| 8283075 | 153889 | 8283075 | PLN 15/2022 | PLN 15/2022 | {"ano":2022,"identificacao":"MSG 334/2022","nomeEnte":"Presidência da República","numero":"334","... | 2022 | CN | CN | Mesa | Projeto de Lei do Congresso Nacional | PLN | 15 | NULL | Não | 7497247 | 11 | NORMA_GERAL | Norma Geral | LEI | Abre ao Orçamento de Investimento da União, em favor da Companhia Docas do Ceará, crédito supleme... | A suplementação visa o reforço de dotação orçamentária da ação “20HL - Estudos e Projetos para In... | 3 | SANCAO | Aprovada pelo Plenário | APROVADA_NO_PLENARIO | 2022-12-16 | À sanção | 9180289 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  CRIAÇÃO ,  LEI FEDERAL ,  CREDITO SUPLEMENTAR ,  ORÇAMENTO DE INVESTIMENTO ,  UNIÃO FEDERAL ,  D... | Presidência da República | 2022-06-30 | NULL | 36622000 | 14485 | LEI-n | Lei Numerada | Lei nº 14.485 de 21/12/2022 | DOU | [Diário Oficial da União  de 22/12/2022] (p. 12, col. 1) | 14485 | 2022 | 2022-12-21 | 2022-12-22 | 2022 | SP:8283075 |
| 8356901 | 155688 | 8356901 | MPV 1158/2023 | MPV 1158/2023 | {"ano":2023,"identificacao":"MSG 34/2023","nomeEnte":"Presidência da República","numero":"34","si... | 2023 | CN | CN | PLEN | Medida Provisória | MPV | 1158 | NULL | Não | 7508997 | 11 | NORMA_GERAL | Norma Geral | NULL | Altera a Lei nº 9.069, de 29 de junho de 1995, a Lei nº 9.613, de 3 de março de 1998, e a Lei nº ... | A Medida Provisória tem a finalidade de modificar a vinculação da Unidade de Inteligência Finance... | 4 | ARQUIVO | Perda de eficácia, em decorrência do término do prazo para sua votação no Congresso | PERDA_EFICACIA | 2023-06-01 | Ao arquivo | 9248152 | MEDIDA_PROVISORIA | Medida Provisória |  ALTERAÇÃO ,  LEI FEDERAL ,  COMPOSIÇÃO ,  CONSELHO MONETARIO NACIONAL (CMN) ,  COMISSÃO TECNICA ... | Presidência da República | 2023-01-12 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2023 | SP:8356901 |
| 8647136 | 163089 | 8647136 | PLN 3/2024 | PLN 3/2024 | {"ano":2024,"identificacao":"MSG 145/2024","nomeEnte":"Presidência da República","numero":"145","... | 2024 | CN | CN | Mesa | Projeto de Lei do Congresso Nacional | PLN | 3 | NULL | Não | 7565228 | 11 | NORMA_GERAL | Norma Geral | LEI | Dispõe sobre as diretrizes para a elaboração e a execução da Lei Orçamentária de 2025 e dá outras... | Por determinação do §2º, art. 165 da CF/88, o projeto compreende as metas e prioridades da admini... | 3 | SANCAO | Aprovada pelo Plenário | APROVADA_NO_PLENARIO | 2024-12-18 | À sanção | 9586941 | PROJETO_LEI_ORDINARIA | Projeto de Lei Ordinária |  ENCAMINHAMENTO ,  CONGRESSO NACIONAL ,  PROJETO DE LEI ,  LEI DE DIRETRIZES ORÇAMENTARIAS (LDO) ... | Presidência da República | 2024-04-17 | NULL | 40035025 | 15080 | LEI-n | Lei Numerada | Lei nº 15.080 de 30/12/2024 | DOU | [Diário Oficial da União  de 31/12/2024] (p. 1, col. 1) | 15080 | 2024 | 2024-12-30 | 2024-12-31 | 2024 | SP:8647136 |

---

## main.processos_relacionados_senado

| id_processo_relacionado | id_processo | id_outro_processo | ano | casa_identificadora | ente_identificador | sigla | numero | sigla_ente_identificador | tipo_relacao | tramitando | year_snapshot |
|-------------------------|-------------|-------------------|-----|---------------------|--------------------|-------|--------|--------------------------|--------------|------------|---------------|
| 303 | 565984 | 7952665 | 2018 | SF | Plenário do Senado Federal | RQS | 343 | PLEN | REFERENCIA | Não | 2016 |
| 756 | 584069 | 8256841 | 2022 | SF | Plenário do Senado Federal | RQS | 346 | PLEN | REFERENCIA | Não | 2015 |
| 1686 | 7837421 | 7861446 | 2019 | CN | Mesa Diretora do Congresso Nacional | PDN | 5 | Mesa | CONCLUSAO_PARECER_GERAL | Não | 2019 |
| 2371 | 7933657 | 7979088 | 2020 | SF | Plenário do Senado Federal | RQS | 2164 | PLEN | REFERENCIA | Não | 2019 |
| 2485 | 7857969 | 7865663 | 2020 | CN | Plenário do Congresso Nacional | RQN | 6 | PLEN | REFERENCIA | Não | 2019 |
| 4507 | 7983756 | 7983791 | 2020 | SF | Plenário do Senado Federal | RQS | 2278 | PLEN | REFERENCIA | Não | 2020 |
| 5523 | 8060173 | 8049788 | 2021 | SF | Plenário do Senado Federal | RQS | 1065 | PLEN | REFERENCIA | Não | 2021 |
| 6332 | 8134482 | 8192042 | 2022 | SF | Plenário do Senado Federal | RQS | 16 | PLEN | REFERENCIA | Não | 2021 |
| 6501 | 8202637 | 8202784 | 2022 | SF | Plenário do Senado Federal | RQS | 95 | PLEN | REFERENCIA | Não | 2022 |
| 6596 | 8289788 | 8416740 | 2023 | SF | Senado Federal | PL | 1969 | SF | CONCLUSAO_PARECER_GERAL | Sim | 2022 |

---

## main.proposicoes_camara

| id_proposicao | sigla_tipo | numero | ano | ementa | uri | year_snapshot | prop_tag | prop_label | prop_category |
|---------------|------------|--------|-----|--------|-----|---------------|----------|------------|---------------|
| 2230650 | PL | 6163 | 2019 | Institui o Plano Regional de Desenvolvimento do Nordeste para o período de 2020-2023. | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2230650 | 2020 | CP:2230650 | PL 6163/2019 | PL |
| 2237261 | PL | 308 | 2020 | Altera a Lei nº 12.587, de 3 de janeiro de 2012, para dispor sobre o cadastro de motoristas e usu... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2237261 | 2020 | CP:2237261 | PL 308/2020 | PL |
| 2241672 | PL | 813 | 2020 | Dispõe sobre a execução do Programa Nacional de Assistência Estudantil - PNAES em caso de pandemi... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2241672 | 2020 | CP:2241672 | PL 813/2020 | PL |
| 2253009 | PL | 2767 | 2020 | Dispõe sobre o pagamento do adicional de insalubridade no percentual de 30% ao profissional de sa... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2253009 | 2020 | CP:2253009 | PL 2767/2020 | PL |
| 2299908 | PL | 5582 | 2019 | Altera a Consolidação das Leis do Trabalho (CLT), aprovada pelo Decreto-Lei nº 5.452, de 1º de ma... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2299908 | 2021 | CP:2299908 | PL 5582/2019 | PL |
| 2350412 | PL | 950 | 2023 | Institui a licença remunerada às vítimas de violência doméstica e familiar, "Licença Maria da Pen... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2350412 | 2023 | CP:2350412 | PL 950/2023 | PL |
| 2372070 | PLP | 135 | 2023 | "Estabelece o número total de Deputados, bem como a representação por Estado e pelo Distrito Fede... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2372070 | 2023 | CP:2372070 | PLP 135/2023 | PL |
| 2418048 | PL | 303 | 2024 | Altera o art. 6º da Lei nº 9.279, de 14 de maio de 1996, para dispor sobre a titularidade de inve... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2418048 | 2024 | CP:2418048 | PL 303/2024 | PL |
| 2441159 | PL | 2412 | 2024 | Altera a Lei no 6.015, de 31 de dezembro de 1973, que “dispõe sobre os registros públicos, e dá o... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2441159 | 2024 | CP:2441159 | PL 2412/2024 | PL |
| 2468642 | PL | 4355 | 2024 | Altera a redação da Lei nº 9.504, de 30 de setembro de 1997 e da Lei nº 8.429, de 02 de junho de ... | https://dadosabertos.camara.leg.br/api/v2/proposicoes/2468642 | 2024 | CP:2468642 | PL 4355/2024 | PL |

---

## main.providencias_senado

| id_processo | id_despacho | id_providencia | descricao | tipo | analise_conteudo | analise_tempo | ordem | reexame | year_snapshot |
|-------------|-------------|----------------|-----------|------|------------------|---------------|-------|---------|---------------|
| 578193 | 7950965 | 7751073 | Análise | ANALISE | MATERIA | SUCESSIVA | 1 | Não | 2015 |
| 5297730 | 7763794 | 7420886 | Análise | ANALISE | NULL | SUCESSIVA | 1 | Não | 2017 |
| 7621131 | 9021876 | 8145210 | Tramitação Conjunta | TRAMITACAO_CONJUNTA | MATERIA | SUCESSIVA | 1 | Não | 2018 |
| 582581 | 7765576 | 7426486 | Análise | ANALISE | NULL | SUCESSIVA | 2 | Não | 2015 |
| 7704774 | 9037833 | 8164104 | Análise | ANALISE | MATERIA | SUCESSIVA | 2 | Não | 2018 |
| 7872006 | 8072051 | 7872010 | Análise | ANALISE | MATERIA | SUCESSIVA | 1 | Não | 2020 |
| 7970554 | 9030550 | 8155398 | Ao Plenário, nos termos do Ato da Comissão Diretora nº 8, de 2021 | AO_PLENARIO_ATO_8_2021 | NULL | SUCESSIVA | 1 | Não | 2020 |
| 8145463 | 9026886 | 8151216 | Análise | ANALISE | NULL | SUCESSIVA | 1 | Não | 2021 |
| 8274415 | 9173599 | 8275183 | Análise | ANALISE | MATERIA | SUCESSIVA | 1 | Não | 2021 |
| 8565467 | 9510098 | 8590506 | Análise | ANALISE | MATERIA | SUCESSIVA | 1 | Não | 2023 |

---

## main.relatorias_senado

| id_relatoria | id_processo | codigo_materia | codigo_parlamentar | codigo_colegiado | codigo_tipo_colegiado | sigla_colegiado | nome_colegiado | autoria_processo | identificacao_processo | ementa_processo | numero_autuacao | tramitando | sigla_casa | casa_relator | descricao_tipo_relator | id_tipo_relator | descricao_tipo_encerramento | forma_tratamento_parlamentar | nome_parlamentar | nome_completo | sigla_partido_parlamentar | uf_parlamentar | sexo_parlamentar | email_parlamentar | url_foto_parlamentar | url_pagina_parlamentar | data_apresentacao_processo | data_designacao | data_destituicao | data_fim_colegiado | year_snapshot |
|--------------|-------------|----------------|--------------------|------------------|-----------------------|-----------------|----------------|------------------|------------------------|-----------------|-----------------|------------|------------|--------------|------------------------|-----------------|-----------------------------|------------------------------|------------------|---------------|---------------------------|----------------|------------------|-------------------|----------------------|------------------------|----------------------------|-----------------|------------------|--------------------|---------------|
| 7880976 | 5229349 | 128728 | 3634 | 1363 | 21 | CCT | Comissão de Ciência, Tecnologia, Inovação e Informática | Câmara dos Deputados | PDS 56/2017 | Aprova o ato que outorga autorização à ASSOCIAÇÃO BENEFICENTE, CULTURAL E DE RADIODIFUSÃO COMUNIT... | 1 | N | SF | SF | Relator Ad hoc | 3 | Deliberação da matéria | Senador | Flexa Ribeiro | Fernando de Souza Flexa Ribeiro | PSDB | PA | M | flexa.ribeiro@senador.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador3634.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/3634 | 2017-04-11 18:05:27 | 2018-10-31 09:40:00 | 2018-10-31 18:18:23 | NULL | 2018 |
| 8049756 | 7806174 | 138787 | 5967 | 1363 | 21 | CCT | Comissão de Ciência, Tecnologia, Inovação e Informática | Câmara dos Deputados | PDL 628/2019 | Aprova o ato que outorga autorização à Associação Nova Barra para executar serviço de radiodifusã... | 1 | N | SF | SF | Relator | 1 | Fim de Legislatura | Senador | Angelo Coronel | Angelo Mario Coronel de Azevedo Martins | PSD | BA | M | sen.angelocoronel@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador5967.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/5967 | 2019-09-13 16:42:38 | 2019-11-29 09:54:28 | 2022-12-21 00:10:00 | NULL | 2019 |
| 9296844 | 3012974 | 121265 | 6009 | 1363 | 21 | CCT | Comissão de Ciência, Tecnologia, Inovação e Informática | Câmara dos Deputados | PDS 119/2015 | Aprova o ato que outorga autorização à ASSOCIAÇÃO MÃOS UNIDAS para executar serviço de radiodifus... | 1 | N | SF | SF | Relator | 1 | Criação de nova comissão | Senador | Astronauta Marcos Pontes | Marcos Cesar Pontes | PL | SP | M | sen.astronautamarcospontes@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador6009.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/6009 | 2015-05-19 00:00:00 | 2023-03-23 17:01:05 | 2023-06-23 10:30:58 | NULL | 2023 |
| 9284132 | 7759092 | 137049 | 5895 | 59 | 21 | CI | Comissão de Serviços de Infraestrutura | Senador Chico Rodrigues (DEM/RR) | PL 3221/2019 | Altera a Lei nº 9.432, de 8 de janeiro de 1997, que dispõe sobre a ordenação do transporte aquavi... | 1 | N | SF | SF | Relator | 1 | Redistribuição | Senador | Jorge Kajuru | Jorge Kajuru Reis da Costa Nasser | PSB | GO | M | sen.jorgekajuru@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador5895.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/5895 | 2019-05-29 15:13:02 | 2023-03-10 14:44:17 | 2023-04-17 09:54:39 | NULL | 2023 |
| 9447078 | 8282994 | 153884 | 5967 | 2614 | 21 | CCDD | Comissão de Comunicação e Direito Digital | Câmara dos Deputados | PDL 676/2021 | Aprova o ato que renova a autorização outorgada à Associação da Rádio Comunitária Liberdade FM pa... | 1 | N | SF | SF | Relator | 1 | Substituído por "ad hoc" | Senador | Angelo Coronel | Angelo Mario Coronel de Azevedo Martins | PSD | BA | M | sen.angelocoronel@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador5967.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/5967 | 2022-06-30 18:51:26 | 2023-09-01 15:38:35 | 2024-09-04 19:29:04 | NULL | 2023 |
| 9418692 | 8324326 | 155318 | 285 | 50 | 21 | CMA | Comissão de Meio Ambiente | Senador Mecias de Jesus (REPUBLICANOS/RR) | PL 2910/2022 | Altera a Lei nº 11.445, de 05 de janeiro de 2007, que estabelece as diretrizes nacionais para o s... | 1 | N | SF | SF | Relator | 1 | Deliberação da matéria | Senador | Marcio Bittar | Marcio Miguel Bittar | UNIÃO | AC | M | sen.marciobittar@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador285.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/285 | 2022-12-01 17:17:48 | 2023-08-04 14:29:37 | 2024-04-10 19:20:51 | NULL | 2023 |
| 9475808 | 8537620 | 159879 | 4560 | 59 | 21 | CI | Comissão de Serviços de Infraestrutura | Senador Alan Rick (UNIÃO/AC) | PL 4392/2023 | Altera a Lei nº 7.565, de 19 de dezembro de 1986, que dispõe sobre o Código Brasileiro de Aeronáu... | 1 | N | SF | SF | Relator | 1 | Redistribuição | Senador | Sérgio Petecão | Sérgio de Oliveira Cunha | PSD | AC | M | sen.sergiopetecao@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador4560.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/4560 | 2023-09-12 10:26:49 | 2023-10-04 14:47:50 | 2024-05-14 13:47:13 | NULL | 2023 |
| 9561683 | 8302058 | 154642 | 5793 | 34 | 21 | CCJ | Comissão de Constituição, Justiça e Cidadania | Senadora Margareth Buzetti (PP/MT) | PL 2390/2022 | Altera o Decreto-Lei nº 2.848, de 7 de dezembro de 1940, para criar causas de aumento de pena par... | 1 | N | SF | SF | Relator | 1 | Deliberação da matéria | Senador | Dr. Hiran | Hiran Manuel Gonçalves da Silva | PP | RR | M | sen.drhiran@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador5793.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/5793 | 2022-08-31 15:16:20 | 2024-03-08 12:13:31 | 2024-05-22 12:01:04 | NULL | 2024 |
| 9589403 | 8524407 | 159484 | 5895 | 50 | 21 | CMA | Comissão de Meio Ambiente | Câmara dos Deputados | PL 1970/2019 | Institui a Política Nacional para o Manejo Sustentável, Plantio, Extração, Consumo, Comercializaç... | 1 | N | SF | SF | Relator | 1 | Deliberação da matéria | Senador | Jorge Kajuru | Jorge Kajuru Reis da Costa Nasser | PSB | GO | M | sen.jorgekajuru@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador5895.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/5895 | 2023-08-25 16:30:27 | 2024-04-19 15:39:20 | 2024-06-12 15:08:22 | NULL | 2024 |
| 9873980 | 8773980 | 166669 | 5967 | 38 | 21 | CAE | Comissão de Assuntos Econômicos | Presidência da República | MSF 77/2024 | Submete à apreciação do Senado Federal, nos termos do art. 52, incisos V, VII e VIII, da Constitu... | 1 | N | SF | SF | Relator | 1 | Deliberação da matéria | Senador | Angelo Coronel | Angelo Mario Coronel de Azevedo Martins | PSD | BA | M | sen.angelocoronel@senado.leg.br | http://www.senado.leg.br/senadores/img/fotos-oficiais/senador5967.jpg | http://www25.senado.leg.br/web/senadores/senador/-/perfil/5967 | 2024-12-12 19:07:33 | 2024-12-13 20:17:25 | 2024-12-17 16:12:15 | NULL | 2024 |

---

## main.situacoes_senado

| id_situacao | id_processo | numero_autuacao | id_tipo_situacao | sigla_situacao | descricao_situacao | data_inicio | data_fim | year_snapshot |
|-------------|-------------|-----------------|------------------|----------------|--------------------|-------------|----------|---------------|
| 1802 | 7695125 | 1 | 95 | AGINCL(RQ) | AGUARDANDO INCLUSÃO ORDEM DO DIA DE REQUERIMENTO | 2023-03-09 | 2025-04-07 | 2018 |
| 13464 | 2922834 | 1 | 91 | RELATOR | MATÉRIA COM A RELATORIA | 2019-05-09 | 2019-06-05 | 2015 |
| 14979 | 572890 | 1 | 87 | AGDREL | AGUARDANDO DESIGNAÇÃO DO RELATOR | 2018-10-10 | 2018-10-10 | 2016 |
| 18447 | 5373953 | 1 | 138 | INPAUTA | INCLUÍDA NA PAUTA DA REUNIÃO | 2018-02-23 | 2018-02-28 | 2017 |
| 24379 | 7327703 | 1 | 91 | RELATOR | MATÉRIA COM A RELATORIA | 2019-02-27 | 2019-06-25 | 2017 |
| 24994 | 585221 | 1 | 42 | PRONTPAUT | PRONTA PARA A PAUTA NA COMISSÃO | 2018-09-04 | 2018-10-04 | 2015 |
| 32925 | 8050675 | 1 | 57 | RMSAN | REMETIDA À SANÇÃO | 2021-04-16 | 2021-05-06 | 2019 |
| 36680 | 7834311 | 1 | 146 | APRCD(DT) | APRECIADA EM DECISÃO TERMINATIVA PELAS COMISSÕES | 2021-08-19 | 2021-08-23 | 2019 |
| 37787 | 7849367 | 1 | 16 | AGMESA | AGUARDANDO DECISÃO DA MESA | 2019-12-11 | 2019-12-12 | 2019 |
| 40039 | 7811720 | 1 | 91 | RELATOR | MATÉRIA COM A RELATORIA | 2021-09-23 | 2022-12-21 | 2019 |

---

## main.temas_camara

| id_tema | descricao |
|---------|-----------|
| 34 | Administração Pública |
| 39 | Esporte e Lazer |
| 43 | Direito Penal e Processual Penal |
| 53 | Processo Legislativo e Atuação Parlamentar |
| 55 | Relações Internacionais e Comércio Exterior |
| 60 | Turismo |
| 66 | Indústria, Comércio e Serviços |
| 68 | Direito Constitucional |
| 74 | Política, Partidos e Eleições |
| 76 | Direito e Justiça |

---

## main.tipo_colegiado_senado

| codigo_tipo_colegiado | codigo_natureza_colegiado | descricao_tipo_colegiado | indicador_ativo | sigla_casa | sigla_tipo_colegiado | year_snapshot |
|-----------------------|---------------------------|--------------------------|-----------------|------------|----------------------|---------------|
| 21 | 1 | Comissão Permanente | S | SF | PERMANENTE | 2023 |
| 121 | 2 | Comissão Temporária Externa | S | SF | CT | 2025 |

---

## main.tipo_conteudo_senado

| id_tipo_conteudo | sigla_tipo_conteudo | descricao_tipo_conteudo | tipo_norma_indicada | year_snapshot |
|------------------|---------------------|-------------------------|---------------------|---------------|
| 162 | RISF | Regimento Interno do Senado Federal e Normas Conexas | RSF | 2023 |
| 1066 | RELATORIO_FUNDO_CONSTITUCIONAL | Relatórios dos fundos constitucionais | NULL | 2017 |
| 38 | AUDIENCIA_PUBLICA | Audiência Pública | NULL | 2023 |
| 32 | INDICACAO_AUTORIDADE | Indicação de Autoridade | NULL | 2024 |
| 701 | AVALIACAO_PP | Avaliação de Políticas Públicas  | NULL | 2021 |
| 705 | CONVITE_AUTORIDADE | Convite a autoridades | NULL | 2022 |
| 7230824 | RELATORIO_RECEITAS_DESPESAS | Relatório de Avaliação de Receitas e Despesas | NULL | 2020 |
| 146 | DESAPENSAMENTO_MATERIA | Desapensamento de matérias  | NULL | 2024 |
| 2013 | VETO_CONSTITUCIONAL | Veto Constitucional | NULL | 2024 |
| 7351409 | LICENCA_NOJO | Licença Nojo | NULL | 2024 |

---

## main.tipo_deliberacao_senado

| sigla_tipo_deliberacao | descricao_tipo_deliberacao | id_destino | sigla_destino | destino | year_snapshot |
|------------------------|----------------------------|------------|---------------|---------|---------------|
| ARQUIVADO_FIM_LEGISLATURA | Arquivada ao final da Legislatura (art. 332 do RISF) | 4 | ARQUIVO | Ao arquivo | 2022 |
| DEFERIDO_CDIR | Deferida pela Comissão Diretora | 4 | ARQUIVO | Ao arquivo | 2024 |
| TRANSF_IND | Transformada em Indicação | NULL | NULL | NULL | 2023 |
| REJEITADO_COMISSAO_NAO_TERM | Rejeitada por Comissão em decisão não terminativa (art. 254 do RISF) | 4 | ARQUIVO | Ao arquivo | 2022 |
| APROVADA_PARCIALMENTE | Aprovada parcialmente pelo Plenário | 3 | SANCAO | À sanção | 2021 |
| APROVADO_NA_INTEGRA | Aprovada na íntegra | 2 | PROMULGACAO | À promulgação | 2024 |
| RECEBIDO | Recebido | NULL | NULL | NULL | 2024 |
| PUBLICADO | Publicada | NULL | NULL | NULL | 2024 |
| SEM_EFICACIA | Sem eficácia (art. 48, II e XI, do RISF) | 4 | ARQUIVO | Ao arquivo | 2020 |
| DEFERIDO_PRESIDENCIA_ART_199_RISF | Deferida pela Presidência (art. 199 do RISF) | NULL | NULL | NULL | 2022 |

---

## main.tipo_emendas_senado

| tipo_emenda | year_snapshot |
|-------------|---------------|
| EMENDA_PARCIAL | 2024 |
| EMENDA_TOTAL | 2024 |

---

## main.tramitacoes_camara

| id_tramitacao | id_proposicao | ambito | apreciacao | cod_situacao | cod_tipo_tramitacao | data_hora | descricao_situacao | descricao_tramitacao | despacho | regime | sequencia | sigla_orgao | uri_orgao | uri_ultimo_relator | year_snapshot |
|---------------|---------------|--------|------------|--------------|---------------------|-----------|--------------------|----------------------|----------|--------|-----------|-------------|-----------|--------------------|---------------|
| 3319 | 2078107 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II | 923 | 502 | 2019-01-31 00:00:00 | Arquivada | Arquivamento | Arquivado nos termos do Artigo 105 do Regimento Interno da Câmara dos Deputados. | Ordinário (Art. 151, III, RICD) | 35 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/129618 | 2020 |
| 492606 | 593788 | Regimental | Proposição Sujeita à Apreciação do Plenário | NULL | 504 | 2013-10-09 14:39:00 | NULL | Notificação de Apensação | Apense-se a este(a) o(a) PL-1965/2007. | Prioridade (Art. 151, II, RICD) | 12 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | NULL | 2022 |
| 494212 | 532249 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II | NULL | 431 | 2018-05-02 17:42:00 | NULL | Declaração de Voto em Separado | Apresentação do Voto em Separado n. 1 CSPCCO, pela Deputada Laura Carneiro (DEM-RJ). | Ordinário (Art. 151, III, RICD) | 97 | CSPCCO | https://dadosabertos.camara.leg.br/api/v2/orgaos/5503 | https://dadosabertos.camara.leg.br/api/v2/deputados/160642 | 2022 |
| 497023 | 553029 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II | NULL | 100 | 2012-08-09 14:48:00 | NULL | Apresentação de Proposição | Apresentação do Projeto de Lei n. 4303/2012, pelo Deputado Laercio Oliveira (PR-SE), que: "Altera... | Ordinário (Art. 151, III, RICD) | 1 | PLEN | https://dadosabertos.camara.leg.br/api/v2/orgaos/180 | NULL | 2022 |
| 498520 | 515917 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II | NULL | 605 | 2011-08-31 00:00:00 | NULL | Publicação de Despacho | Publicação do despacho no DCD do dia 01/09/11 PAG 46841 COL 02. | Ordinário (Art. 151, III, RICD) | 14 | CCP | https://dadosabertos.camara.leg.br/api/v2/orgaos/186 | NULL | 2022 |
| 499904 | 328385 | Regimental | Proposição Sujeita à Apreciação do Plenário | NULL | 240 | 2007-10-03 00:00:00 | NULL | Aprovação | Aprovado por Unanimidade o Parecer com Complementação de Voto | Especial (Art. 202 c/c 191, I, RICD) | 41 | CCJC | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/deputados/73434 | 2022 |
| 502563 | 2315175 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II | NULL | 505 | 2022-06-29 00:00:00 | NULL | Notificação de Desapensação | Deferido o Requerimento n. 1.025/2022, conforme despacho do seguinte teor: Defiro o Requerimento ... | Ordinário (Art. 151, III, RICD) | 25 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | NULL | 2022 |
| 504755 | 2314914 | Regimental | Proposição Sujeita à Apreciação Conclusiva pelas Comissões - Art. 24 II | NULL | 336 | 2023-08-30 10:30:00 | NULL | Aprovação do Parecer | Aprovado o Parecer. | Ordinário (Art. 151, III, RICD) | 28 | CINDRE | https://dadosabertos.camara.leg.br/api/v2/orgaos/2017 | https://dadosabertos.camara.leg.br/api/v2/deputados/220641 | 2022 |
| 739256 | 2383019 | Regimental | Proposição Sujeita à Apreciação do Plenário | 939 | 192 | 2025-05-14 18:11:00 | Aguardando Apreciação do Veto | Apresentação de Recurso | Apresentação do REC n. 2/2025 (Recurso contra decisão do Presidente da CD em Questao de Ordem (Ar... | Urgência (Art. 155, RICD) | 66 | MESA | https://dadosabertos.camara.leg.br/api/v2/orgaos/4 | https://dadosabertos.camara.leg.br/api/v2/deputados/74467 | 2023 |
| 864171 | 2463150 | Regimental | Proposição Sujeita à Apreciação do Plenário | NULL | 1005 | 2025-04-04 00:00:00 | NULL | Notificações | Designado Relator, Dep. Bruno Farias (AVANTE-MG), para o PL 6749/2016, ao qual esta proposição es... | Urgência (Art. 155, RICD) | 16 | PLEN | https://dadosabertos.camara.leg.br/api/v2/orgaos/180 | NULL | 2024 |

---

## main.unidades_destinatarias_senado

| id_unidade_destinataria | id_processo | id_despacho | id_providencia | colegiado_casa | colegiado_codigo | colegiado_nome | colegiado_sigla | ordem | tipo_analise_deliberacao | year_snapshot |
|-------------------------|-------------|-------------|----------------|----------------|------------------|----------------|-----------------|-------|--------------------------|---------------|
| 1733 | 7695107 | 7882574 | 7695118 | SF | 47 | Comissão de Educação e Cultura | CE | 1 | TERMINATIVA | 2018 |
| 3919 | 7752899 | 7952614 | 7752904 | SF | 834 | Comissão de Direitos Humanos e Legislação Participativa | CDH | 1 | TERMINATIVA | 2019 |
| 4265 | 7798962 | 8006847 | 7801412 | SF | 2015 | Comissão Diretora do Senado Federal | CDIR | 1 | NAO_TERMINATIVA | 2019 |
| 4487 | 7837763 | 8040027 | 7837765 | SF | 38 | Comissão de Assuntos Econômicos | CAE | 2 | TERMINATIVA | 2019 |
| 5642 | 7780985 | 7981251 | 7781248 | SF | 1363 | Comissão de Ciência, Tecnologia, Inovação e Informática | CCT | 1 | TERMINATIVA | 2019 |
| 6517 | 8101185 | 9191222 | 8295200 | SF | 1998 | Plenário do Senado Federal | PLEN | 1 | NAO_TERMINATIVA | 2020 |
| 7427 | 8302804 | 9397888 | 8483680 | SF | 2614 | Comissão de Comunicação e Direito Digital | CCDD | 1 | TERMINATIVA | 2021 |
| 8149 | 8303508 | 9198012 | 8303766 | SF | 1363 | Comissão de Ciência, Tecnologia, Inovação e Informática | CCT | 1 | TERMINATIVA | 2021 |
| 8721 | 8516534 | 9432737 | 8516599 | SF | 2015 | Comissão Diretora do Senado Federal | CDIR | 1 | NAO_TERMINATIVA | 2023 |
| 9118 | 8655845 | 9606275 | 8661618 | CN | 1664 | Comissão Mista de Planos, Orçamentos Públicos e Fiscalização | CMO | 1 | NAO_TERMINATIVA | 2024 |

---

## main.votacoes_camara

| id_votacao | id_proposicao | data | descricao | aprovacao | uri_evento | uri_orgao | uri | year_snapshot | rn |
|------------|---------------|------|-----------|-----------|------------|-----------|-----|---------------|----|
| 1732982-57 | 1732982 | 2023-12-13 | Aprovado o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/71611 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1732982-57 | 2021 | 1 |
| 2167716-66 | 2167716 | 2019-10-10 | Aprovadas as Emendas de Redação. Aprovada a Redação Final. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/57906 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/2167716-66 | 2023 | 1 |
| 1279371-34 | 1279371 | 2016-12-07 | Aprovado por Unanimidade o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/46006 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2015 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1279371-34 | 2020 | 1 |
| 529820-104 | 529820 | 2015-04-23 | Aprovado o Requerimento. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/38744 | https://dadosabertos.camara.leg.br/api/v2/orgaos/180 | https://dadosabertos.camara.leg.br/api/v2/votacoes/529820-104 | 2024 | 1 |
| 2435743-22 | 2435743 | 2025-05-20 | Aprovado o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/76365 | https://dadosabertos.camara.leg.br/api/v2/orgaos/539384 | https://dadosabertos.camara.leg.br/api/v2/votacoes/2435743-22 | 2024 | 1 |
| 1672576-120 | 1672576 | 2019-03-20 | Rejeitado o Requerimento. Sim: 17; não: 269; abstenção: 2; total: 288. | False | https://dadosabertos.camara.leg.br/api/v2/eventos/54771 | https://dadosabertos.camara.leg.br/api/v2/orgaos/180 | https://dadosabertos.camara.leg.br/api/v2/votacoes/1672576-120 | 2024 | 1 |
| 2415323-26 | 2415323 | 2024-10-30 | Aprovado o Parecer. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/74550 | https://dadosabertos.camara.leg.br/api/v2/orgaos/537870 | https://dadosabertos.camara.leg.br/api/v2/votacoes/2415323-26 | 2023 | 1 |
| 2423023-32 | 2423023 | 2024-07-03 | Aprovada a Redação Final. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/73678 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/2423023-32 | 2024 | 1 |
| 2318399-50 | 2318399 | 2024-10-09 | Aprovado o Parecer, com o seguinte resultado:  36 votos "Sim", 14 votos "Não". Quórum de votação:... | True | https://dadosabertos.camara.leg.br/api/v2/eventos/74412 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/2318399-50 | 2022 | 1 |
| 2476187-36 | 2476187 | 2025-09-16 | Aprovada a Redação Final. | True | https://dadosabertos.camara.leg.br/api/v2/eventos/79148 | https://dadosabertos.camara.leg.br/api/v2/orgaos/2003 | https://dadosabertos.camara.leg.br/api/v2/votacoes/2476187-36 | 2024 | 1 |

---

## main.votacoes_senado

| id_votacao | id_materia | id_processo | identificacao | sigla | numero | ano | codigo_sessao | numero_sessao | sequencial_sessao | sigla_tipo_sessao | casa_sessao | codigo_sessao_legislativa | data_apresentacao | data_sessao | descricao_votacao | ementa | resultado_votacao | total_votos_sim | total_votos_nao | total_votos_abstencao | votacao_secreta | id_informe | id_evento | codigo_colegiado | nome_colegiado | sigla_colegiado | data_informe | texto_informe | year_snapshot |
|------------|------------|-------------|---------------|-------|--------|-----|---------------|---------------|-------------------|-------------------|-------------|---------------------------|-------------------|-------------|-------------------|--------|-------------------|-----------------|-----------------|-----------------------|-----------------|------------|-----------|------------------|----------------|-----------------|--------------|---------------|---------------|
| 6121 | 141437 | 7891117 | PL 1543/2020 | PL | 1543 | 2020 | 175280 | 48 | 2 | SDR | SF | 863 | 2020-04-06 00:00:00 | 2020-05-26 00:00:00 | Votação do Projeto de Lei nº 1.543, de 2020 e Emendas, nos termos do parecer. | Autoriza a prorrogação de dívidas rurais em decorrência da pandemia do coronavírus (Covid-19). | A | NULL | NULL | NULL | N | 2032381 | 10093567 | 1998 | Plenário do Senado Federal | PLEN | 2020-05-26 00:00:06 | (Sessão Deliberativa Remota realizada em 26/05/2020) Aprovado o Substitutivo – Emenda nº 28-PLEN... | 2020 |
| 6187 | 142947 | 7915985 | MSF 11/2020 | MSF | 11 | 2020 | 196263 | 86 | 6 | DOR | SF | 863 | 2020-05-18 00:00:00 | 2020-09-22 00:00:00 | Votação da Mensagem nº 11, de 2020 - Norberto Moretti (OACI). | Submete à apreciação do Senado Federal a escolha do Senhor NORBERTO MORETTI, Ministro de Primeira... | A | 39 | 3 | 1 | S | 2039768 | 10121867 | 1998 | Plenário do Senado Federal | PLEN | 2020-09-22 20:20:41 | (Sessão Deliberativa Ordinária Semipresencial realizada em 22/09/2020)  Aprovada a indicação, no... | 2020 |
| 6210 | 142950 | 7932499 | MSF 14/2020 | MSF | 14 | 2020 | 196750 | 87 | 18 | DEX | SF | 863 | 2020-06-24 00:00:00 | 2020-09-23 00:00:00 | Votação da Mensagem nº 14, de 2020 - Colbert Soares Pinto Junior (Cabo Verde). | Submete à apreciação do Senado Federal, de conformidade com o art. 52, inciso IV, da Constituição... | A | 36 | 4 | 2 | S | 2039847 | 10122146 | 1998 | Plenário do Senado Federal | PLEN | 2020-09-23 14:12:21 | (Sessão Deliberativa Extraordinária Semipresencial realizada em 23/09/2020)   Aprovada a indicaç... | 2020 |
| 6208 | 144629 | 7982702 | MSF 46/2020 | MSF | 46 | 2020 | 196750 | 87 | 16 | DEX | SF | 863 | 2020-09-10 00:00:00 | 2020-09-23 00:00:00 | Votação da Mensagem nº 46, de 2020 - José Carlos de Araújo Leitão (Costa do Marfim). | Submete à apreciação do Senado Federal, de conformidade com o art. 52, inciso IV, da Constituição... | A | 37 | 3 | 1 | S | 2039843 | 10122134 | 1998 | Plenário do Senado Federal | PLEN | 2020-09-23 13:54:43 | (Sessão Deliberativa Extraordinária Semipresencial realizada em 23/09/2020)   Aprovada a indicaç... | 2020 |
| 6515 | 152144 | 8109014 | PL 1360/2021 | PL | 1360 | 2021 | 282237 | 21 | 1 | DOR | SF | 866 | 2021-07-19 00:00:00 | 2022-03-22 00:00:00 | Votação nominal do PL 1.360/2021. | Cria mecanismos para a prevenção e o enfrentamento da violência doméstica e familiar contra a cri... | A | NULL | NULL | NULL | N | 2081588 | 10259679 | 1998 | Plenário do Senado Federal | PLEN | 2022-03-22 20:26:20 | (Sessão Deliberativa Ordinária - Semipresencial, realizada em 22/02/2022)  Encaminhadas à public... | 2022 |
| 6628 | 152560 | 8236047 | MPV 1112/2022 | MPV | 1112 | 2022 | 304487 | 83 | 3 | DOR | SF | 866 | 2022-04-01 00:00:00 | 2022-08-03 00:00:00 | Votação nominal da Emenda nº 59 à Medida Provisória nº 1.112, de 2022, destacada. | Institui o Programa de Aumento da Produtividade da Frota Rodoviária no País - Renovar e altera a ... | R | NULL | NULL | NULL | N | 2094845 | 10340988 | 1998 | Plenário do Senado Federal | PLEN | 2022-08-03 20:19:39 | (Sessão Deliberativa Ordinária - Semipresencial, realizada em 03/08/2022)  Encaminhado à publica... | 2022 |
| 6657 | 155164 | 8317962 | MSF 80/2022 | MSF | 80 | 2022 | 312400 | 113 | 11 | DOR | SF | 866 | 2022-11-17 00:00:00 | 2022-11-23 00:00:00 | Votação nominal da Mensagem nº 80, de 2022 - Caio César Farias Leôncio (ANTAQ). | Submete à consideração do Senado Federal, nos termos do art. 52, inciso III, alínea "f", da Const... | A | 38 | 1 | 2 | S | 2100477 | 10360057 | 1998 | Plenário do Senado Federal | PLEN | 2022-11-23 19:36:05 | (Sessão Deliberativa Ordinária-Semipresencial, realizada em 23/11/2022)  Aprovada a indicação co... | 2022 |
| 6671 | 155594 | 8333764 | PEC 32/2022 (fase 2) | PEC | 32 | 2022 | 317954 | 123 | 4 | DOR | SF | 866 | 2022-12-21 00:00:00 | 2022-12-20 00:00:00 | Votação nominal da PEC nº 32/2022, nos termos do Parecer, ressalvado o destaque (1º Turno). | Altera a Constituição Federal, para dispor sobre as emendas individuais ao projeto de lei orçamen... | A | NULL | NULL | NULL | N | 2104041 | 10373023 | 1998 | Plenário do Senado Federal | PLEN | 2022-12-21 23:12:12 | (Continuação da Sessão Deliberativa Ordinária - Semipresencial, iniciada em 20/12/2022)     Prof... | 2022 |
| 6767 | 159983 | 8538700 | MSF 61/2023 | MSF | 61 | 2023 | 366154 | 161 | 6 | DOR | SF | 868 | 2023-09-12 00:00:00 | 2023-10-25 00:00:00 | Votação nominal da Mensagem nº 61, de 2023 - Teodoro Silva Santos (STJ). | Submete à apreciação do Senado Federal, nos termos do art. 104, parágrafo único, inciso I, da Con... | A | 63 | 0 | 1 | S | 2167158 | 10612658 | 1998 | Plenário do Senado Federal | PLEN | 2023-10-25 20:51:15 | (Sessão Deliberativa Ordinária, realizada em 25/10/2023)¿ Aprovada a indicação, nos termos do Pa... | 2023 |
| 6891 | 166356 | 8760023 | MSF 59/2024 | MSF | 59 | 2024 | 430896 | 179 | 9 | DOR | SF | 871 | 2024-12-04 00:00:00 | 2024-12-10 00:00:00 | Votação nominal Mensagem nº 59, de 2024 - Izabela Moreira Correa (Banco Central do Brasil). | Submete à apreciação do Senado Federal, nos termos do art. 52, inciso III, alínea "d", da Constit... | A | 48 | 3 | 0 | S | 2222235 | 10977065 | 1998 | Plenário do Senado Federal | PLEN | 2024-12-10 18:40:54 | (Sessão Deliberativa Ordinária, realizada em 10/12/2024) Aprovada a indicação, com o seguinte re... | 2024 |

---

## main.votos_camara

| id_voto | id_votacao | id_deputado | tipo_voto | data_hora | year_snapshot |
|---------|------------|-------------|-----------|-----------|---------------|
| 297 | 1050795-6 | 178854 | Sim | 2015-03-24 18:10:21 | 2021 |
| 3528 | 1197773-99 | 138286 | Não | 2023-08-09 19:42:12 | 2021 |
| 370294 | 2265631-116 | 204545 | Sim | 2022-02-16 20:50:01 | 2020 |
| 371580 | 2265679-30 | 74165 | Não | 2022-12-14 14:37:02 | 2020 |
| 373422 | 2266116-87 | 160570 | Sim | 2021-08-19 16:12:51 | 2020 |
| 375018 | 2266304-9 | 204575 | Sim | 2020-12-09 19:50:03 | 2020 |
| 499022 | 2279513-106 | 204506 | Não | 2021-08-12 12:39:34 | 2021 |
| 507288 | 2279744-57 | 204432 | Não | 2021-07-15 22:56:45 | 2021 |
| 616398 | 2305189-27 | 178983 | Não | 2021-12-08 19:05:21 | 2021 |
| 739126 | 2331282-8 | 220657 | Sim | 2023-08-29 18:58:20 | 2022 |

---

## main.votos_senado

| id_voto | codigo_votacao_sve | codigo_sessao_votacao | codigo_materia | identificacao_materia | codigo_parlamentar | nome_parlamentar | sexo_parlamentar | sigla_partido_parlamentar | sigla_uf_parlamentar | sigla_voto_parlamentar | descricao_voto_parlamentar | year_snapshot |
|---------|--------------------|-----------------------|----------------|-----------------------|--------------------|------------------|------------------|---------------------------|----------------------|------------------------|----------------------------|---------------|
| 1508 | 3853 | 6554 | 152599 | MSF 33/2022 | 5411 | Weverton | M | PDT | MA | P-NRV | Presente – Não registrou voto | 2022 |
| 4010 | 3995 | 6674 | 155773 | PDL 2/2023 | 5899 | Vanderlan Cardoso | M | PSD | GO | Votou | NULL | 2023 |
| 7681 | 4033 | 6712 | 157945 | MSF 29/2023 | 6331 | Sergio Moro | M | UNIÃO | PR | Votou | NULL | 2023 |
| 8846 | 4005 | 6683 | 157158 | MSF 6/2023 | 5352 | Rogério Carvalho | M | PT | SE | Votou | NULL | 2023 |
| 14565 | NULL | 6161 | 141417 | MPV 945/2020 | 5523 | Otto Alencar | M | PSD | BA | AP | Atividade parlamentar | 2020 |
| 31429 | NULL | 6172 | 142693 | PLP 170/2020 (Substitutivo-CD) | 4770 | Izalci Lucas | M | PSDB | DF | Sim | NULL | 2020 |
| 33610 | 4005 | 6683 | 157158 | MSF 6/2023 | 5953 | Fabiano Contarato | M | PT | ES | Votou | NULL | 2023 |
| 36596 | 3971 | 6653 | 155171 | MSF 84/2022 | 5953 | Fabiano Contarato | M | PT | ES | P-NRV | Presente – Não registrou voto | 2022 |
| 37167 | 3913 | 6601 | 152861 | MSF 41/2022 | 5898 | Eliane Nogueira | F | PP | PI | Votou | NULL | 2022 |
| 39749 | 4128 | 6811 | 160915 | OFS 26/2023 | 6335 | Damares Alves | F | REPUBLICANOS | DF | Votou | NULL | 2023 |

---

