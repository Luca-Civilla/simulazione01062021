from database.DB_connect import DBConnect
from model.gene import Gene
from model.interazione import Interazione


class DAO():

    @staticmethod
    def getAllGenes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query ="""SELECT DISTINCT g.GeneID, g.Essential, g.Chromosome
                FROM genes g
                WHERE  Essential = 'Essential'
                ORDER BY GeneID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(u,v,idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select i.*
                from interactions i
                where i.GeneID1 = %s and i.GeneID2 =%s
                """

        cursor.execute(query,(u,v,))

        for row in cursor:
            result.append(Interazione(idMap[row["GeneID1"]],idMap[row["GeneID2"]],row["Type"],row["Expression_Corr"]))

        cursor.close()
        conn.close()
        return result

