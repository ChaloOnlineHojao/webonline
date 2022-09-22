from models.connection import Connection
class LoginDbUtility:
      @staticmethod
      def checkForUser(username,password):
            con = Connection.createConnection()
            cursor = con.cursor()
            cursor.execute("select email,password from admin")
            admins =  cursor.fetchall()
            con.close()
            for admin in admins:
                  if username == admin[0] and password == admin[1]:
                        return 1
            return 0