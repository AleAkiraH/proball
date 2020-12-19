import sqlite3
conn = sqlite3.connect(r'C:\Users\AleAkiraH\Desktop\Projetos\ProBall\proball.db')
c = conn.cursor()

f = open('crawler.txt', encoding="utf8")

for line in f.readlines():
    if (line.upper().split(';')[0] == 'LIGA'):
        pass
    else:
        pass
        liga = line.upper().split(';')[0]
        dataconfronto = line.upper().split(';')[3] +"-"+line.upper().split(';')[2] + "-" + line.upper().split(';')[1] + " " + line.upper().split(';')[4] + ":" + line.upper().split(';')[5] + ":00"
        confronto_casa = line.upper().split(';')[6].split(' V ')[0].replace("'","")
        confronto_fora = line.upper().split(';')[6].split(' V ')[1].replace("'","")
        placar_casa = line.upper().split(';')[7]
        placar_fora = line.upper().split(';')[8]
        link = line.upper().split(';')[9].replace("/R/","/r/").replace("\n","")
        # print("INSERT INTO [Proball_confrontos] ([LIGA],[DATA_CONFRONTO],[CONFRONTO_CASA],[CONFRONTO_FORA],[PLACAR_CASA],[PLACAR_FORA],[LINK_EVENTOS]) VALUES ('" + liga + "','" + dataconfronto + "','" + confronto_casa + "','" + confronto_fora + "','" + placar_casa + "','" + placar_fora + "','" + link + "')")

        verificar_existencia = "SELECT EXISTS (SELECT * FROM [Proball_confrontos] WHERE [LIGA] = '" + liga + "' AND [DATA_CONFRONTO] = '" + dataconfronto + "' AND [CONFRONTO_CASA] = '" + confronto_casa + "' AND [CONFRONTO_FORA] = '" + confronto_fora + "' AND [PLACAR_CASA] = '" + placar_casa + "' AND [PLACAR_FORA] = '" + placar_fora + "' AND [LINK_EVENTOS] = '" + link + "')"
        res = c.execute(verificar_existencia).fetchone()
        if (res[0] == 0):
            insert = "INSERT INTO [Proball_confrontos] ([LIGA],[DATA_CONFRONTO],[CONFRONTO_CASA],[CONFRONTO_FORA],[PLACAR_CASA],[PLACAR_FORA],[LINK_EVENTOS]) VALUES ('" + liga + "','" + dataconfronto + "','" + confronto_casa + "','" + confronto_fora + "','" + placar_casa + "','" + placar_fora + "','" + link + "')"
            c.execute(insert)
            conn.commit()
            print('novo registro')
        else:
            print('ja existente')
        


f.close()


c.execute("")



conn.close()

