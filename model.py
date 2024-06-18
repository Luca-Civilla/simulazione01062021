import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._geni = DAO.getAllGenes()
        self._idMap = {}




    def build_graph(self):
        self._grafo.add_nodes_from(self._geni)
        for gene in self._geni:
            self._idMap[gene.GeneID] = gene
        for u in self._grafo.nodes:
            for v in self._grafo.nodes:
                if u!= v:#QUI PASSO 2 VERTICI DELLA CLASSE GENE
                    tabella = DAO.getArchi(u.GeneID,v.GeneID,self._idMap)#RESTITUISCE UN OGGETTO DI CLASSE INTERAZIONE
                    if tabella:#OGGETTO ESISTE---> QUINDI CORRELAZIONE TRA I 2 VERTICI
                        #IMPOSTO IL PESO DELL'ARCO
                        if u.Chromosome == v.Chromosome:#VERIFICO SE ELEMENTI DELLA CLASSE GENE appartengono allo stesso cromosoma
                            peso = abs(tabella[0].Expression_Corr)*2
                            self._grafo.add_edge(u,v,weight=peso)
                        else:
                            peso1 = abs(tabella[0].Expression_Corr)
                            self._grafo.add_edge(u, v, weight=peso1)

    def _vicini(self,gene):
        archi = []
        for vicino in self._grafo.neighbors(gene):
            distanza = self._grafo[gene][vicino]["weight"]
            archi.append((vicino,distanza))
        archi.sort(key=lambda x:x[1], reverse=True)#ORDINO ARCHI CON PESO DECRESCENTE
        return archi





    def graphDetails(self):
        return len(self._grafo.nodes),len(self._grafo.edges)