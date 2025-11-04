| Nome do arquivo | Descrição                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------|
| step_0001.py    | Importação de bibliotecas; configuração de conexão DuckDB e parâmetros de memória                       |
| step_0002.sql   | Definição de macro SQL jget1 para extrair strings de JSON                                               |
| step_0003.sql   | Criação de view bronze_camara_blocos sobre dados brutos de blocos parlamentares                         |
| step_0004.sql   | Extração e criação da tabela blocos_camara com dados dimensionais de blocos                             |
| step_0005.sql   | Criação de view bronze_camara_deputados sobre dados brutos de deputados                                 |
| step_0006.sql   | Extração e criação da tabela deputados_camara com dados dimensionais de deputados                       |
| step_0007.sql   | Criação de view bronze_camara_eventos sobre dados brutos de eventos legislativos                        |
| step_0008.sql   | Extração e criação da tabela eventos_camara com dados dimensionais de eventos                           |
| step_0009.sql   | Criação de view bronze_camara_frentes sobre dados brutos de frentes parlamentares                       |
| step_0010.sql   | Extração e criação da tabela frentes_camara com dados dimensionais de frentes                           |
| step_0011.sql   | Criação de view bronze_camara_legislaturas sobre dados brutos de legislaturas                           |
| step_0012.sql   | Extração e criação da tabela legislaturas_camara com dados dimensionais de legislaturas                 |
| step_0013.sql   | Criação de view bronze_camara_orgaos sobre dados brutos de órgãos legislativos                          |
| step_0014.sql   | Extração e criação da tabela orgaos_camara com dados dimensionais de órgãos                             |
| step_0015.sql   | Criação de view bronze_camara_partidos sobre dados brutos de partidos políticos                         |
| step_0016.sql   | Extração e criação da tabela partidos_camara com dados dimensionais de partidos                         |
| step_0017.sql   | Criação de view bronze_camara_proposicoes sobre dados brutos de proposições legislativas                |
| step_0018.sql   | Extração e criação da tabela proposicoes_camara com dados dimensionais de proposições                   |
| step_0019.sql   | Criação de view bronze_camara_temas sobre dados brutos de temas legislativos                            |
| step_0020.sql   | Extração e criação da tabela temas_camara com dados dimensionais de temas                               |
| step_0021.sql   | Criação de view bronze_camara_autores sobre dados brutos de autoria de proposições                      |
| step_0022.sql   | Extração e criação da tabela autores_camara com dados factuais de autoria                               |
| step_0023.sql   | Criação de view bronze_camara_orientacoes sobre dados brutos de orientações de voto                     |
| step_0024.sql   | Extração e criação da tabela orientacoes_camara com dados factuais de orientações                       |
| step_0025.sql   | Criação de view e tabela tramitacoes_camara com dados factuais de tramitações                           |
| step_0026.sql   | Criação de view bronze_camara_votacoes sobre dados brutos de votações                                   |
| step_0027.sql   | Extração e criação da tabela votacoes_camara com dados factuais de votações                             |
| step_0028.py    | Processamento de dados brutos de votos com Python/Pandas e criação da tabela votos_camara               |
| step_0029.sql   | Criação de view bronze_camara_blocos_partidos sobre relação blocos-partidos                             |
| step_0030.sql   | Extração e criação da tabela blocos_partidos_camara com relação blocos-partidos                         |
| step_0031.sql   | Criação de view bronze_camara_deputados_frentes sobre relação deputados-frentes                         |
| step_0032.sql   | Extração e criação da tabela deputados_frentes_camara com relação deputados-frentes                     |
| step_0033.sql   | Criação de view bronze_camara_deputados_historico sobre histórico de deputados                          |
| step_0034.sql   | Extração e criação da tabela deputados_historico_camara com histórico de status                         |
| step_0035.sql   | Criação de view bronze_camara_deputados_orgaos sobre relação deputados-órgãos                           |
| step_0036.sql   | Extração e criação da tabela deputados_orgaos_camara com participação em órgãos                         |
| step_0037.sql   | Criação de view bronze_camara_eventos_orgaos sobre relação eventos-órgãos                               |
| step_0038.sql   | Extração e criação da tabela eventos_orgaos_camara com relação eventos-órgãos                           |
| step_0039.sql   | Criação de view bronze_camara_eventos_pauta sobre pautas de eventos                                     |
| step_0040.py    | Processamento de pautas de eventos com Python/Pandas e criação da tabela eventos_pauta_camara           |
| step_0041.py    | Processamento de líderes legislativos com Python/Pandas e criação da tabela legislaturas_lideres_camara |
| step_0042.sql   | Criação de view bronze_camara_legislaturas_mesa sobre composição das mesas diretoras                    |
| step_0043.sql   | Extração e criação da tabela legislaturas_mesa_camara com membros das mesas                             |
| step_0044.sql   | Criação de view bronze_partidos_lideres sobre líderes partidários                                       |
| step_0045.sql   | Extração e criação da tabela partidos_lideres_camara com dados de lideranças                            |
| step_0046.sql   | Criação de view bronze_partidos_membros sobre membros de partidos                                       |
| step_0047.sql   | Extração e criação da tabela partidos_membros_camara com filiações partidárias                          |
| step_0048.sql   | Início da seção de regularização - normalização de chaves primárias                                     |
| step_0049.sql   | Deduplicação da tabela blocos_camara por id_bloco mantendo registro mais recente                        |
| step_0050.sql   | Definição de chave primária e tipo de coluna para blocos_camara                                         |
| step_0051.sql   | Deduplicação da tabela deputados_camara por id_deputado mantendo registro mais recente                  |
| step_0052.sql   | Definição de chave primária e tipo de coluna para deputados_camara                                      |
| step_0053.sql   | Deduplicação da tabela eventos_camara por id_evento mantendo registro mais recente                      |
| step_0054.sql   | Definição de chave primária e tipo de coluna para eventos_camara                                        |
| step_0055.sql   | Deduplicação da tabela frentes_camara por id_frente mantendo registro mais recente                      |
| step_0056.sql   | Definição de chave primária e tipo de coluna para frentes_camara                                        |
| step_0057.sql   | Deduplicação da tabela legislaturas_camara por id_legislatura mantendo registro mais recente            |
| step_0058.sql   | Definição de chave primária e tipo de coluna para legislaturas_camara                                   |
| step_0059.sql   | Deduplicação da tabela orgaos_camara por id_orgao mantendo registro mais recente                        |
| step_0060.sql   | Definição de chave primária e tipo de coluna para orgaos_camara                                         |
| step_0061.sql   | Deduplicação da tabela partidos_camara por id_partido mantendo registro mais recente                    |
| step_0062.sql   | Definição de chave primária e tipo de coluna para partidos_camara                                       |
| step_0063.sql   | Definição de chave primária e tipo de coluna para proposicoes_camara                                    |
| step_0064.sql   | Definição de chave primária e tipo de coluna para temas_camara                                          |
| step_0065.sql   | Análise de duplicatas na tabela autores_camara                                                          |
| step_0066.sql   | Definição de chave primária e tipo de coluna para autores_camara                                        |
| step_0067.sql   | Definição de chave primária e tipo de coluna para tramitacoes_camara                                    |
| step_0068.sql   | Definição de chave primária e tipo de coluna para votacoes_camara                                       |
| step_0069.sql   | Definição de chave primária e tipo de coluna para blocos_partidos_camara                                |
| step_0070.sql   | Definição de chave primária e tipo de coluna para deputados_frentes_camara                              |
| step_0071.sql   | Definição de chave primária e tipo de coluna para deputados_historico_camara                            |
| step_0072.sql   | Definição de chave primária e tipo de coluna para deputados_orgaos_camara                               |
| step_0073.sql   | Definição de chave primária e tipo de coluna para eventos_orgaos_camara                                 |
| step_0074.sql   | Definição de chave primária e tipo de coluna para partidos_lideres_camara                               |
| step_0075.sql   | Definição de chave primária e tipo de coluna para partidos_membros_camara                               |
| step_0076.sql   | Análise de duplicatas na tabela orientacoes_camara por votação e partido/bloco                          |
| step_0077.sql   | Continuação da análise de duplicatas em orientacoes_camara                                              |
| step_0078.sql   | Deduplicação da tabela orientacoes_camara mantendo primeira ocorrência                                  |
| step_0079.sql   | Recriação da tabela orientacoes_camara sem duplicatas                                                   |
| step_0080.sql   | Definição de chave primária composta para orientacoes_camara                                            |
| step_0081.sql   | Análise de duplicatas na tabela tramitacoes_camara                                                      |
| step_0082.sql   | Deduplicação da tabela tramitacoes_camara mantendo primeira ocorrência                                  |
| step_0083.sql   | Recriação da tabela tramitacoes_camara sem duplicatas                                                   |
| step_0084.sql   | Análise de duplicatas na tabela votos_camara                                                            |
| step_0085.sql   | Deduplicação da tabela votos_camara mantendo primeira ocorrência de voto por votação/deputado           |
| step_0086.sql   | Recriação da tabela votos_camara sem duplicatas                                                         |
| step_0087.sql   | Análise de duplicatas na tabela deputados_frentes_camara                                                |
| step_0088.sql   | Deduplicação da tabela deputados_frentes_camara mantendo primeira ocorrência                            |
| step_0089.sql   | Recriação da tabela deputados_frentes_camara sem duplicatas                                             |
| step_0090.sql   | Análise de duplicatas na tabela eventos_pauta_camara                                                    |
| step_0091.sql   | Deduplicação da tabela eventos_pauta_camara mantendo primeira ocorrência                                |
| step_0092.sql   | Recriação da tabela eventos_pauta_camara sem duplicatas                                                 |
| step_1003.sql   | Remoção de proposições anteriores a 2019 (antes da unificação dos códigos de projetos)                  |
| step_1004.sql   | Remoção de linhas de autoria órfãs referentes a proposições deletadas                                   |
| step_1005.sql   | Adição e preenchimento de colunas tipo_autor e id_deputado_ou_orgao em autores_camara                   |
| step_1006.py    | Fetch da API de órgãos faltantes com retry e backoff exponencial                                        |
| step_1007.sql   | Criação de tags identificadoras para deputados, órgãos e proposições para construção de grafos          |
| step_1008.sql   | Remoção de registros específicos incorretos em autores_camara (João Alberto e P50)                      |
| step_1009.py    | Fechamento da conexão DuckDB e limpeza final                                                            |