from sqlite3 import Cursor
from models.connection import Connection
class UserDbUtility:
      @staticmethod
      def getAllUsers():
            con = Connection.createConnection()
            cursor = con.cursor()
            cursor.execute("select * from users")
            users = [dict((cursor.description[i][0], value) \
                  for i, value in enumerate(row)) for row in cursor.fetchall()]
            con.close()
            return users

      def changeUserStatus(user,oper):
            con = Connection.createConnection()
            cursor = con.cursor()
            if oper=='block':
                  qry = 'update users set status = 0 where email=%s '
            else:
                  qry = 'update users set status = 1 where email=%s '
            arg = (user,)
            cursor.execute(qry,arg)
            con.commit()
            con.close()