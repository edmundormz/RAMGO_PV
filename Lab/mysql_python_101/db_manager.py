import MySQLdb
import ipdb


class DBManager():
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="Pass.word0",
                             db="RAMGO_1")
        self.cur = self.db.cursor()

    def _get_columns_names(self,table_name):
        query = "select column_name from information_schema.columns where table_name='{0}'".format(table_name)
        self.cur.execute(query)
        columns = self.cur.fetchall()
        return columns

    def read_all(self):
        pass

    def insertar_producto(self, **kwargs):
        insert_into = "INSERT INTO `Producto` (`Nombre`, `Precio`, `Costo`, `Stock`) VALUES"
        query = "{operation} ('{nombre}', '{precio}', '{costo}', '{stock}')".format(
            operation=insert_into,
            nombre=kwargs.get('nombre'),
            precio=kwargs.get('precio'),
            costo=kwargs.get('costo'),
            stock=kwargs.get('stock'))
        try:
            self.cur.execute(query)
            self.db.commit()
            print "Product inserted"
        except:
            self.db.rollback()
            print "Exception"
    
    def consular_producto(self):
        columns = self._get_columns_names(table_name="Producto")
        query = "SELECT * FROM Producto WHERE Producto.Nombre = 'Polin 4x5'"
        self.cur.execute(query)
        db_response = self.cur.fetchone()
        ipdb.set_trace()

    
    
    
    


if __name__ == "__main__":
    DBManager().consular_producto()
    """
    DBManager().insertar_producto(nombre="Polin 4x5",
                               precio="125",
                               costo="85",
                               stock="50")
    """
