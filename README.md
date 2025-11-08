# tramita

## Instalação:

```
pip install -U pip setuptools wheel
pip install .
```

## Comandos:

### Fase Bronze:

```
tramita bronze all
```

Obs.: Se o comando for rodado com as configurações padrão, isso sobrescreverá os dados na pasta `./data/bronze`.

### Fase Prata:

```
tramita silver all
```

A execução da frase prata requer uma sequência de arquivos Python e SQL conforme o conteúdo da pasta `./data/silver/pipelines/`.


### Fase Ouro:

Todo o trabalho está realizado em um sequência de arquivos `.ipynb` na pasta `./gold`. A fase ouro não foi implementada no módulo em nível de linha de comando.
