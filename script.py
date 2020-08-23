from flask import Flask, render_template, request
import sqlite3 as sql

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
    

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/index/')
def index():
    return render_template("index.html")    #carousel
    
@app.route('/lil')      # Lista lokacija za novu sadnju
def lil():
   con = sql.connect("janda.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT lokacija.id, lokacija.oznaka, lokacija.status, status_lok.opis, sorta.naziv, cokot.poreklo, godinasadnje FROM cokot \
JOIN lokacija \
	ON lokacija.id = cokot.lokacija_id \
JOIN sorta\
	ON sorta.id = cokot.sorta_id \
JOIN status_lok \
	ON lokacija.status = status_lok.status \
WHERE lokacija.status NOT LIKE 'F' AND lokacija.status NOT LIKE 'K' \
ORDER BY  lokacija.id;		") 
   rows = cur.fetchall()
   return render_template("lil.html",rows = rows)
   
@app.route('/lic')  # čokoti po lokaciji
def lic():
   con = sql.connect("janda.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT lokacija.id, lokacija.oznaka, sorta.naziv, epoha.period, lokacija.status, cokot.poreklo, godinasadnje FROM cokot \
JOIN lokacija \
	ON lokacija.id = cokot.lokacija_id \
JOIN sorta\
	ON sorta.id = cokot.sorta_id \
JOIN epoha \
	ON epoha.id = sorta.epoha_id \
WHERE lokacija.status NOT LIKE 'F' \
ORDER BY  lokacija.id;	") 
   rows = cur.fetchall()
   return render_template("lic.html",rows = rows)    
      
@app.route('/lis')      # lista sorti
def lis():
   con = sql.connect("janda.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT  sorta.id, sorta.naziv, COUNT(sorta.id) AS cokota FROM cokot \
JOIN lokacija \
	ON lokacija.id = cokot.lokacija_id \
JOIN sorta\
	ON sorta.id = cokot.sorta_id \
WHERE lokacija.status NOT LIKE 'F' \
GROUP BY sorta.id \
ORDER BY  sorta.id;	") 
   rows = cur.fetchall()
   return render_template("lis.html",rows = rows)   

@app.route('/lib')      # lista berbi
def lib():
   con = sql.connect("janda.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT  godina.godina, datum_berbe, sorta.naziv, most_lit, secer FROM berba \
JOIN godina \
	ON godina.id = berba.godina_id \
JOIN sorta\
	ON sorta.id = berba.sorta_id \
ORDER BY  godina.godina;	") 
   rows = cur.fetchall()
   return render_template("lib.html",rows = rows)    
   
@app.route('/lir')      # lista rizlinga
def lir():
   con = sql.connect("janda.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT  godina.godina, datum_berbe, ubrano_kg, secer, berba.komentar, most_lit, sira_lit, vina_lit, vina_kom FROM berba \
JOIN godina \
	ON godina.id = berba.godina_id \
JOIN sorta\
	ON sorta.id = berba.sorta_id \
WHERE sorta.id LIKE 1 \
ORDER BY  godina.godina;	") 
   rows = cur.fetchall()
   return render_template("lir.html",rows = rows)      
   
@app.route('/lim')      # lista muskata
def lim():
   con = sql.connect("janda.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT  godina.godina, datum_berbe, ubrano_kg, secer, berba.komentar, most_lit, sira_lit, vina_lit, vina_kom FROM berba \
JOIN godina \
	ON godina.id = berba.godina_id \
JOIN sorta\
	ON sorta.id = berba.sorta_id \
WHERE sorta.id LIKE 2 \
ORDER BY  godina.godina;	") 
   rows = cur.fetchall()
   return render_template("lim.html",rows = rows)      

@app.route('/lip')      # lista prokupca 
def lip():
   con = sql.connect("janda.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT  godina.godina, datum_berbe, ubrano_kg, secer, berba.komentar, most_lit, sira_lit, vina_lit, vina_kom FROM berba \
JOIN godina \
	ON godina.id = berba.godina_id \
JOIN sorta\
	ON sorta.id = berba.sorta_id \
WHERE sorta.id LIKE 4 \
ORDER BY  godina.godina;	") 
   rows = cur.fetchall()
   return render_template("lip.html",rows = rows)   
 

@app.route('/lik')      # lista kabernea 
def lik():
   con = sql.connect("janda.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT  godina.godina, datum_berbe, ubrano_kg, secer, berba.komentar, most_lit, sira_lit, vina_lit, vina_kom FROM berba \
JOIN godina \
	ON godina.id = berba.godina_id \
JOIN sorta\
	ON sorta.id = berba.sorta_id \
WHERE sorta.id LIKE 15 \
ORDER BY  godina.godina;	") 
   rows = cur.fetchall()
   return render_template("lik.html",rows = rows)   
 


 
if __name__=="__main__":
    app.run(debug=True)
