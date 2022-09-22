import stat
import mysql.connector
class Connection:
      @staticmethod
      def createConnection():
            mydb = mysql.connector.connect(host="localhost", user="root",passwd="",database="dukan")
            return mydb