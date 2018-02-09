import MySQLdb


class DBManager():
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="Pass.word0",
                             db="RAMGO_1")
        self.cur = self.db.cursor()

    def read_all(self):
        pass

    def insert_element(self, **kwargs):
        insert_producto = "INSERT INTO `Producto` (`Nombre`, `Precio`, `Costo`, `Stock`) VALUES"
        query = "{operation} ('{nombre}', '{precio}', '{costo}', '{stock}')".format(
            operation=insert_producto,
            nombre=kwargs.get('nombre'),
            precio=kwargs.get('precio'),
            costo=kwargs.get('costo'),
            stock=kwargs.get('stock'))
        try:
            self.cur.execute(query)
            self.db.commit()
        except:
            self.db.rollback()


if __name__ == "__main__":
    DBManager().insert_element(nombre="Polin 4x5",
                               precio="125",
                               costo="85",
                               stock="50")
