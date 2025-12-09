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
    supplier: str = Field(description="Nome do fornecedor")
    date: str = Field(description="Data da proposta. Ex: '2025-12-09' ")
    city: str = Field(description="Cidade")
    state: str = Field(description="Estado")
    contact: str = Field(description="Informações de contato, como telefone ou email")
    other_info: str = Field(description='Outras informações qualitativas da proposta, como frete, observações de parcelamentos, descontos, etc.')