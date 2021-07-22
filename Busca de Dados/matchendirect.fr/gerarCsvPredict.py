# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:35:32 2021

@author: alexsander.ferreira
"""

import sqlite3
import pandas as pd
import os

try:
    os.remove("massa ML\\csvTeste.csv")
except:
    pass

f = open("massa ML\\csvTeste.csv","a")
f.write("\"CONFRONTO_CASA\",\"CONFRONTO_FORA\",\"média_posse_casa\",\"média_posse_fora\",\"média_ataques_casa\",\"média_ataques_fora\",\"média_ataques_perigosos_casa\",\"média_ataques_perigosos_fora\"\n")
f.close()
lst_predict_times = pd.read_csv('massa ML\\listatimesPredict.csv', encoding = "ANSI")

for linha in range(0,len(lst_predict_times)):
    time_casa = lst_predict_times.values[linha][0]
    time_fora = lst_predict_times.values[linha][1]

    conn = sqlite3.connect(r'C:\Users\alexsander.ferreira\Desktop\trabalho\proball\dtproball.db')
    c = conn.cursor()

    c.execute("CREATE TEMP TABLE _Variables(Name TEXT PRIMARY KEY, RealValue REAL, IntegerValue INTEGER, BlobValue BLOB, TextValue TEXT);")
    conn.commit()

    c.execute("INSERT INTO _Variables (Name) VALUES ('time_casa');")
    c.execute("INSERT INTO _Variables (Name) VALUES ('time_fora');")
    conn.commit()

    c.execute("UPDATE _Variables SET IntegerValue = '"+time_casa+"' WHERE Name = 'time_casa';")
    c.execute("UPDATE _Variables SET IntegerValue = '"+time_fora+"' WHERE Name = 'time_fora';")
    conn.commit()

    time_casa = c.execute("SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_casa' LIMIT 1").fetchall()[0][0]
    conn.commit()

    time_fora = c.execute("SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_fora' LIMIT 1").fetchall()[0][0]
    conn.commit()

    query_media_previsores = "SELECT (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_casa' LIMIT 1) 'CONFRONTO_CASA',(SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_fora' LIMIT 1) 'CONFRONTO_FORA',cast((select sum(ce.posse_casa)/(select count(1) from Proball_confrontos where liga = 'BRASIL SERIE A' and CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_casa' LIMIT 1)) FROM Proball_confrontos c inner join Proball_confrontos_estastiticas ce on c.id = ce.id_proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_casa' LIMIT 1)) as integer) 'média_posse_casa',cast((select sum(ce.posse_casa)/(select count(1) from Proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_fora' LIMIT 1)) FROM Proball_confrontos c inner join Proball_confrontos_estastiticas ce on c.id = ce.id_proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_fora' LIMIT 1)) as integer) 'média_posse_fora',cast((select sum(ce.ataques_casa)/(select count(1) from Proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_casa' LIMIT 1)) FROM Proball_confrontos c inner join Proball_confrontos_estastiticas ce on c.id = ce.id_proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_casa' LIMIT 1)) as integer) 'média_ataques_casa',cast((select sum(ce.ataques_casa)/(select count(1) from Proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_fora' LIMIT 1)) FROM Proball_confrontos c inner join Proball_confrontos_estastiticas ce on c.id = ce.id_proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_fora' LIMIT 1)) as integer) 'média_ataques_fora',cast((select sum(ce.ataques_perigosos_casa)/(select count(1) from Proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_casa' LIMIT 1)) FROM Proball_confrontos c inner join Proball_confrontos_estastiticas ce on c.id = ce.id_proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_casa' LIMIT 1)) as integer) 'média_ataques_perigosos_casa',cast((select sum(ce.ataques_perigosos_casa)/(select count(1) from Proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_fora' LIMIT 1)) FROM Proball_confrontos c inner join Proball_confrontos_estastiticas ce on c.id = ce.id_proball_confrontos where liga = 'BRASIL SERIE A' and  CONFRONTO_CASA = (SELECT coalesce(RealValue, IntegerValue, BlobValue, TextValue) FROM _Variables WHERE Name = 'time_fora' LIMIT 1)) as integer) 'média_ataques_perigosos_fora'"
    previsores = c.execute(query_media_previsores).fetchall()

    csv = ""

    for i in range(0, len(previsores[0])):
        
        csv = csv + str(previsores[0][i]) + ","
        
    csv = csv [0:len(csv)-1]
        
    f = open("massa ML\\csvTeste.csv","a")
    f.write(csv + "\n")
    f.close()    