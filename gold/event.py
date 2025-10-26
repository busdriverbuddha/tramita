from enum import Enum

class Event(Enum):
    APRESENTADO = 'apresentado'
    DISTRIBUIDO = 'distribuido'
    RECEBIDO_COMISSAO = 'recebido_comissao'
    DESIGNADO_RELATOR_COMISSAO = 'designado_relator_comissao'
    RETIRADO_PAUTA_COMISSAO = 'retirado_pauta_comissao'
    RETIRADO_PAUTA_PLENARIO = 'retirado_pauta_plenario'
    APROVADA_URGENCIA = 'aprovada_urgencia'
    DESIGNADO_RELATOR_PLENARIO = 'designado_relator_plenario'
    REMETIDO_AO_SENADO = 'remetido_ao_senado'
    REMETIDO_A_CAMARA = 'remetido_a_camara'
    REMETIDO_A_SANCAO = 'remetido_a_sancao'
    REMETIDO_A_PROMULGACAO = 'remetido_a_promulgacao'
    APROVADO_PLENARIO = 'aprovado_plenario'
    REJEITADO_PLENARIO = 'rejeitado_plenario'
    ARQUIVADO = 'arquivado'
    DESARQUIVADO = 'desarquivado'


    # funções de comparação para o pivot table
    def __gt__(self, other):
        order = list(Event)
        return order.index(self) > order.index(other)
    
    def __le__(self, other):
        order = list(Event)
        return order.index(self) <= order.index(other)
    
    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)
