# coding=utf-8
import MySQLdb
import ipdb


class DBManager():
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="Pass.word0",
                             db="RAMGO_1")
        self.cur = self.db.cursor()

    """
    def _get_columns_names(self, table_name):
        query = "select column_name from information_schema.columns where table_name='{0}'".format(table_name)
        self.cur.execute(query)
        columns = self.cur.fetchall()
        return columns
    """

    def read_all(self):
        pass

    def insert_product(self, **kwargs):
        """
        Inserts an element into "Producto" table
        :param kwargs:
            nombre: descripción del producto
            precio: precio de venta del producto
            costo: costo de compra del producto
            stock: cantidad del producto a registrar
        """
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
            print("Product inserted")
        except NameError:
            self.db.rollback()
            print("Exception")

    def consular_producto(self, nombre_producto):
        query = "SELECT * FROM Producto WHERE Producto.Nombre = '{0}'".format(nombre_producto)
        try:
            self.cur.execute(query)
            db_response = self.cur.fetchone()
            ipdb.set_trace()
        except NameError:
            self.db.rollback()
            print("Exception")


if __name__ == "__main__":
    # DBManager().consular_producto("Polin 4x5")

    DBManager().insert_product(nombre="Tabla 6x8 2a",
                               precio="90",
                               costo="55",
                               stock="200")
