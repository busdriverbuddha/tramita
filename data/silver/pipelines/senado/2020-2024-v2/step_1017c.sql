
ALTER TABLE documento_autoria_senado
  ADD COLUMN IF NOT EXISTS id_senador_ou_ente BIGINT;
