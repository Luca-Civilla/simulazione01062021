from dataclasses import dataclass
from model.gene import Gene
@dataclass
class Interazione:
    GeneID1:Gene
    GeneID2:Gene
    Type:str
    Expression_Corr:float

    def __str__(self):
        return f'{self.gene1.GeneID}-{self.gene2.GeneID}'
