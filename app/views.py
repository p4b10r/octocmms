#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from io import BytesIO as StringIO
import os
import csv
import io
import sys

import sys
reload(sys)
sys.setdefaultencoding('utf8')

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="p4b10r"
app.config["MYSQL_PASSWORD"]="P4b10r"
app.config["MYSQL_DB"]="mydb"
mysql=MySQL(app)
app.secret_key="secret_key"

@app.route("/")
def Index():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM correctivo ORDER BY id DESC LIMIT 1")
    data=cur.fetchall()
    cur.execute("SELECT * FROM inspeccion_previa ORDER BY id DESC LIMIT 1")
    data2=cur.fetchall()
    return render_template('ingresodatos.html',tipomant=data,inspeccion=data2)


@app.route("/ingresodatos",methods=["GET","POST"])
def IngresarDatos():
    if request.method=="POST":
        mantenimiento=request.form["mantenimiento"]
        sistema=request.form["sistema"]
        falla=request.form["falla"]

        estado=str("En proceso")
        cur=mysql.connection.cursor()
        mtbf="mtbf"
        cur.execute("INSERT INTO correctivo (Mantenimiento, Sistema, Falla, Estado, mtbf) VALUES(%s,%s,%s,%s,%s) ",(mantenimiento,sistema,falla,estado,mtbf))
        mysql.connection.commit()





        cur=mysql.connection.cursor()
        cur.execute("SELECT id, tiempo, Mantenimiento, Sistema, Falla, Estado FROM correctivo WHERE estado='En proceso'")
        results=cur.fetchall()
        with open("app/comenzados.csv","w") as file:
            for row in results:
                csv.writer(file).writerow(row)




        flash("Mantenimiento Iniciado. Al finalizar marque la actividad como terminada")
    return redirect(url_for("Index"))

@app.route("/eliminar/<string:id>")
def EliminarMantenimiento(id):
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM correctivo WHERE id= %s ", [id])
    mysql.connection.commit()
    flash("Mantenimiento Removido")
    return redirect(url_for("Index"))

@app.route("/terminar",methods=["POST"])
def TerminarMantenimiento():
    if request.method=="POST":

        cur=mysql.connection.cursor()
        cur.execute("SELECT Mantenimiento FROM correctivo ORDER BY Mantenimiento DESC LIMIT 1")
        mantenimiento=cur.fetchone()
        cur.execute("SELECT Falla FROM correctivo ORDER BY Falla DESC LIMIT 1")
        falla=cur.fetchone()
        cur.execute("SELECT Sistema FROM correctivo ORDER BY Falla DESC LIMIT 1")
        sistema=cur.fetchone()
        estado=str("Terminado")
        mtbf="mtbf"
        cur.execute("INSERT INTO correctivo (Mantenimiento, Sistema, Falla, Estado, mtbf) VALUES (%s, %s,%s,%s, %s)",(mantenimiento,sistema, falla,estado, mtbf))
        mysql.connection.commit()
        cur=mysql.connection.cursor()
        cur.execute("SELECT id, tiempo, Mantenimiento, Sistema, Falla, Estado FROM correctivo WHERE estado='Terminado'")
        results=cur.fetchall()
        with open("app/terminados.csv","w") as file:
            for row in results:
                csv.writer(file).writerow(row)
        flash("Mantenimiento Terminado")
    return redirect(url_for("Index"))

@app.route("/inspeccionprevia", methods=["POST"])
def InspeccionPrevia():
    if request.method=="POST":
        cur=mysql.connection.cursor()
        inspeccionlista="Realizada"
        cur.execute("INSERT INTO inspeccion_previa (inspeccion_diaria) VALUES (%s)",(inspeccionlista,))
        mysql.connection.commit()
    flash("Inspeccion Previa Realizada")
    return redirect(url_for("Index"))
