import pymysql
from datetime import datetime

def conexion():
    
    db = pymysql.connect(host='145.14.151.1',user='u989932990_simova',password='~IiQcM&>L3',database='u989932990_simova')
    
    return db

def set(db,id,total):
    '''Actualiza con imagen +1'''          
    cursor = db.cursor()      
    sql = "INSERT INTO `estado` (`id`,`total`, `actual`) VALUES (%s, %s, %s)"
    val = (id, total, 0)
    cursor.execute(sql,val)      
    db.commit()     
    cursor.close()     
    return

def actualiza_estado(db,id):
    '''Actualiza con imagen +1'''          
    cursor = db.cursor()      
    sql = "UPDATE `estado`SET `actual` = `actual`+1 WHERE `id`= %s"      
    cursor.execute(sql,(id))      
    db.commit()     
    cursor.close()     
    return 

def consulta_id(db):
    
    cursor = db.cursor()

    sql = "SELECT MAX(id) FROM estado"

    cursor.execute(sql)

    resultados = cursor.fetchall()

    for row in resultados:
        id_bd = row[0]
        
    return id_bd

def consulta_estado(db,id):
    
    cursor = db.cursor()

    sql = "SELECT `actual` FROM estado WHERE `id`= %s"

    cursor.execute(sql,(id))

    resultados = cursor.fetchall()

    for row in resultados:
        estado = row[0]
        
    return estado
    

def cerrar_conexion(db):
    db.close()
    return
