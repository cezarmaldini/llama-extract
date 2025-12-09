from pydantic import BaseModel, Field
from typing import List

class Item(BaseModel):
    description: str = Field(description="Descrição detalhada do item. Ex: 'PORTA CORTA FOGO P90 900X2100'")
    quantity: float = Field(description="Quantidade do item. Ex: '26,0000'")
    unit_price: float = Field(description="Valor unitário do item (coluna 'VI. Unit'). Ex: '1.610,00'")
    total_price: float = Field(description="Valor total do item (coluna 'VI. Total'). Ex: '41.860,00'")
    unt: str = Field(description="Unidade de medida do item. Ex: 'UN'")
    
class Itens(BaseModel):
    itens: List[Item]= Field(description="Uma lista de todos os itens do pedido encontrados na proposta")
    
class ResumeProposal(BaseModel):
    supplier: str = Field(description="Nome da empresa fornecedora.")
    date: str = Field(description="Data da proposta no formato YYYY-MM-DD.")
    city: str = Field(description="Cidade onde o fornecedor está localizado.")
    state: str = Field(description="Estado onde o fornecedor está localizado.")
    contact: str = Field(description="Informações de contato: telefone, e-mail ou responsável.")
    other_info: str = Field(description="Informações adicionais relevantes: frete, condições, prazos, descontos ou observações gerais.")