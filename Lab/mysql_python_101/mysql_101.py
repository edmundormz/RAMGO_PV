from RAMGO_SYSTEM.db_manager.db_manager import *
# Queries
# INSERT INTO `Producto` (`Id`, `Nombre`, `Precio`, `Costo`, `Stock`) VALUES ('8796', 'Polin 4x4', '115', '85', '100')



db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="Pass.word0",
                     db="RAMGO_1")


insert_producto = "INSERT INTO `Producto` (`Id`, `Nombre`, `Precio`, `Costo`, `Stock`) VALUES"
values_to_insert = {"id":"1235","nombre":"Tabla 4x8 1a","precio":89,"costo":58, "stock":326}

query = "{operation} ('{id}', '{nombre}', '{precio}', '{costo}', '{stock}')".format(
    operation=insert_producto,
    id=values_to_insert["id"],
    nombre=values_to_insert["nombre"],
    precio=values_to_insert["precio"],
    costo=values_to_insert["costo"],
    stock=values_to_insert["id"])


cur = db.cursor()
try:
    cur.execute(query)
    db.commit()
except:
    db.rollback()

"""
for row in cur.fetchall():
    print(row)
"""

db.close()
