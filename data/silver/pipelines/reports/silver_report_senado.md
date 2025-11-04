| Nome do arquivo | Descrição                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------|
| step_0001.py    | Importação de bibliotecas; configuração de conexão DuckDB e parâmetros de memória               |
| step_0002.sql   | Definição de macro SQL jget1 para extrair strings de JSON                                       |
| step_0003.sql   | Criação de view bronze_senado_bloco sobre dados brutos de blocos parlamentares                  |
| step_0005.sql   | Extração e criação da tabela bloco_senado com dados dimensionais de blocos                      |
| step_0006.sql   | Criação de view bronze_senado_colegiado sobre dados brutos de colegiados                        |
| step_0007.sql   | Extração e criação das tabelas colegiado_senado e tipo_colegiado_senado com dados dimensionais  |
| step_0008.sql   | Criação de view bronze_senado_parlamentar sobre dados brutos de parlamentares                   |
| step_0009.sql   | Extração e criação da tabela parlamentar_senado com dados dimensionais de parlamentares         |
| step_0010.sql   | Criação de view bronze_senado_partido sobre dados brutos de partidos políticos                  |
| step_0011.sql   | Extração e criação da tabela partido_senado com dados dimensionais de partidos                  |
| step_0012.sql   | Criação de view bronze_senado_processo sobre dados brutos de processos legislativos             |
| step_0013.sql   | Extração e criação da tabela processo_senado com dados dimensionais de processos                |
| step_0014.sql   | Criação de view bronze_senado_emendas sobre dados brutos de emendas                             |
| step_0015.sql   | Extração e criação da tabela emendas_senado com dados factuais de emendas                       |
| step_0016.sql   | Criação da tabela tipo_emendas_senado a partir de tipos de emendas únicos                       |
| step_0017.sql   | Remoção da view bronze_senado_emendas                                                           |
| step_0018.sql   | Criação de view bronze_senado_relatorias sobre dados brutos de relatorias                       |
| step_0019.sql   | Extração e criação da tabela relatorias_senado com dados factuais de relatorias                 |
| step_0020.sql   | Criação de view bronze_senado_votacoes sobre dados brutos de votações                           |
| step_0021.sql   | Extração e criação da tabela votacoes_senado com dados factuais de votações                     |
| step_0022.sql   | Extração e criação da tabela votos_senado explodindo votos individuais das votações             |
| step_0023.sql   | Remoção da view bronze_senado_votacoes                                                          |
| step_0024.sql   | Recriação de view bronze_senado_processo para extração de relacionamentos                       |
| step_0025.sql   | Extração e criação da tabela autoria_iniciativa_senado com autoria de iniciativas               |
| step_0026.sql   | Extração e criação da tabela autoria_documento_senado com autoria de documentos                 |
| step_0027.sql   | Extração e criação da tabela situacoes_senado com situações de processos                        |
| step_0028.sql   | Extração e criação da tabela despachos_senado com despachos de processos                        |
| step_0029.sql   | Extração e criação da tabela outros_numeros_senado com números alternativos de processos        |
| step_0030.sql   | Extração e criação da tabela processos_relacionados_senado com relações entre processos         |
| step_0031.sql   | Extração e criação da tabela documento_autoria_senado com autoria de documentos                 |
| step_0032.sql   | Extração e criação da tabela autuacoes_senado com autuações de processos                        |
| step_0033.sql   | Extração e criação da tabela informes_legislativos_senado com informes legislativos             |
| step_0034.sql   | Extração e criação da tabela informes_documentos_associados_senado com documentos de informes   |
| step_0035.sql   | Extração e criação da tabela movimentacoes_senado com movimentações de processos                |
| step_0036.sql   | Extração e criação da tabela providencias_senado com providências de despachos                  |
| step_0037.sql   | Extração e criação da tabela unidades_destinatarias_senado com unidades destinatárias           |
| step_0038.sql   | Extração e criação da tabela encontro_legislativo_senado com encontros legislativos             |
| step_0039.sql   | Definição de chave primária para bloco_senado                                                   |
| step_0040.sql   | Deduplicação da tabela parlamentar_senado por codigo_parlamentar mantendo registro mais recente |
| step_0041.sql   | Definição de chave primária para parlamentar_senado                                             |
| step_0042.sql   | Definição de chave primária para partido_senado                                                 |
| step_0043.sql   | Definição de chave primária para processo_senado                                                |
| step_0044.sql   | Definição de chave primária para emendas_senado                                                 |
| step_0045.sql   | Definição de chave primária para relatorias_senado                                              |
| step_0046.sql   | Definição de chave primária para votacoes_senado                                                |
| step_0047.sql   | Definição de chave primária para votos_senado                                                   |
| step_0048.sql   | Definição de chave primária para autoria_iniciativa_senado                                      |
| step_0049.sql   | Definição de chave primária para situacoes_senado                                               |
| step_0050.sql   | Análise de duplicatas na tabela despachos_senado                                                |
| step_0051.sql   | Definição de chave primária composta para despachos_senado                                      |
| step_0052.sql   | Definição de chave primária para outros_numeros_senado                                          |
| step_0053.sql   | Definição de chave primária para documento_autoria_senado                                       |
| step_0054.sql   | Definição de chave primária para processos_relacionados_senado                                  |
| step_0055.sql   | Definição de chave primária composta para autuacoes_senado                                      |
| step_0056.sql   | Definição de chave primária para informes_legislativos_senado                                   |
| step_0057.sql   | Definição de chave primária para informes_documentos_associados_senado                          |
| step_0058.sql   | Definição de chave primária composta para providencias_senado                                   |
| step_0059.sql   | Definição de chave primária composta para movimentacoes_senado                                  |
| step_0060.sql   | Definição de chave primária para unidades_destinatarias_senado                                  |
| step_0061.sql   | Análise de duplicatas na tabela encontro_legislativo_senado                                     |
| step_0062.sql   | Deduplicação da tabela encontro_legislativo_senado mantendo registro mais recente               |
| step_0063.sql   | Definição de chave primária para encontro_legislativo_senado                                    |
| step_0064.sql   | Análise de duplicatas na tabela informes_legislativos_senado                                    |
| step_0065.sql   | Contagem de duplicatas em informes_legislativos_senado                                          |
| step_0066.sql   | Deduplicação da tabela informes_legislativos_senado mantendo primeira ocorrência                |
| step_1009.py    | Fetch da API de entes do Senado e criação da tabela ente_senado com tags                        |
| step_1014.sql   | Remoção de processos anteriores a 2019 e originados de proposições anteriores a 2019            |
| step_1015.sql   | Filtragem de processos por tipo (projetos de lei, complementares, PEC e MP)                     |
| step_1016.sql   | Adição de coluna tag em processo_senado para construção de grafos                               |
| step_1017a.sql  | Remoção de linhas órfãs em documento_autoria_senado referentes a processos deletados            |
| step_1017b.sql  | Adição de coluna tipo_autor em documento_autoria_senado                                         |
| step_1017c.sql  | Adição de coluna id_senador_ou_ente em documento_autoria_senado                                 |
| step_1017d.sql  | Preenchimento das colunas tipo_autor e id_senador_ou_ente em documento_autoria_senado           |
| step_1017e.sql  | Remoção de registros com id_senador_ou_ente nulo em documento_autoria_senado                    |
| step_1018.sql   | Criação de tabela correspondencia_proposicoes_processo relacionando Câmara e Senado             |
| step_1019.py    | Fechamento da conexão DuckDB e limpeza final                                                    |