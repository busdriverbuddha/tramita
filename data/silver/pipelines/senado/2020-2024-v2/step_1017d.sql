
UPDATE documento_autoria_senado
SET
  tipo_autor = CASE
                 WHEN sigla_tipo = 'SENADOR' THEN 'senador'
                 ELSE 'ente'
               END,
  id_senador_ou_ente = CASE
                         WHEN sigla_tipo = 'SENADOR'
                           THEN TRY_CAST(codigo_parlamentar AS BIGINT)
                         ELSE TRY_CAST(id_ente AS BIGINT)
                       END;
