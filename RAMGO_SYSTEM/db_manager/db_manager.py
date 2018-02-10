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

    def read_all(self):
        pass
    #
    # def get_product_id(self, nombre_producto):
    #     query = "SELECT Producto.Id FROM Producto WHERE Producto.Nombre = '{nombre}'".format(nombre=nombre_producto)
    #     id_producto = self.cur.execute(query)
    #     return str(id_producto)

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
            return db_response
        except NameError:
            self.db.rollback()
            print("Exception")

    def modify_product(self, **kwargs):
        # UPDATE Producto SET Nombre='MDF 18mm', Costo=120, Precio=200, Stock=28 WHERE Nombre='MDF 16mm'
        query = "UPDATE Producto SET Nombre='{nombre}', Costo='{costo}', Precio='{precio}', Stock='{stock}' " \
                "WHERE Id='{id_producto}'".format(id_producto=kwargs.get('id_producto'),
                                                  nombre=kwargs.get('nombre'),
                                                  precio=kwargs.get('precio'),
                                                  costo=kwargs.get('costo'),
                                                  stock=kwargs.get('stock'))
        try:
            self.cur.execute(query)
            self.db.commit()
            print("Product updated")
            return self.consular_producto(nombre_producto=kwargs.get('nombre'))
        except NameError:
            self.db.rollback()
            print("Exception")

    def delete_product(self, id_producto):
        query = "DELETE FROM Producto WHERE Id='{0}'".format(id_producto)
        try:
            self.cur.execute(query)
            self.db.commit()
            print("Product deleted")
        except NameError:
            self.db.rollback()
            print("Exception")


if __name__ == "__main__":
    DBManager().consular_producto("Polin 4x5")

