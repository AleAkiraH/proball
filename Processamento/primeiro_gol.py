import sqlite3

def cnfrt_casa(valor_aposta_ganha, valor_aposta_perdida, confronto_casa, liga, data_confronto_min, data_confronto_max):
    qtd_total_jogos = c.execute("select count(1) from Proball_confrontos where CONFRONTO_CASA = '"+confronto_casa+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchone()
    com_placar_o_o = c.execute("select count(1) from Proball_confrontos where CONFRONTO_CASA = '"+confronto_casa+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"') and (PLACAR_CASA = 0 and PLACAR_FORA = 0)").fetchone()
    gol_menor_10_min = c.execute("select count(1) from Proball_confrontos where CONFRONTO_CASA = '"+confronto_casa+"' AND LIGA = '"+str(liga)+"' and id in (select id_Proball_confrontos from Proball_confrontos_eventos where evento = '1st Goal' and cast(tempo AS INTEGER) <= 10) AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchone()

    try:
        resultado = 100 -(((int(gol_menor_10_min[0])/int(qtd_total_jogos[0])))*100)

        jogos = c.execute("select * from Proball_confrontos where CONFRONTO_CASA = '"+confronto_casa+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchall()

        for jg in jogos:
            print(jg)
        print("Total de jogos pesquisados: " + str(qtd_total_jogos[0]) + " / " +str(gol_menor_10_min[0]))
        print(str(round(resultado)) + "%")
        lucro = (int(qtd_total_jogos[0]) - int(gol_menor_10_min[0])) * float(valor_aposta_ganha)
        prejuizo = float((int(gol_menor_10_min[0])) * float(valor_aposta_perdida))
        print("em uma aposta simulada, considerando o valor de entrada de R$3,00 para um lucro de R$0,50;\nR$: " + str(lucro - prejuizo))
    except:
        print("Não encontrado...")

def cnfrt_fora(valor_aposta_ganha, valor_aposta_perdida, confronto_fora, liga, data_confronto_min, data_confronto_max):
    qtd_total_jogos = c.execute("select count(1) from Proball_confrontos where CONFRONTO_FORA = '"+confronto_fora+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchone()
    com_placar_o_o = c.execute("select count(1) from Proball_confrontos where CONFRONTO_FORA = '"+confronto_fora+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"') and (PLACAR_CASA = 0 and PLACAR_FORA = 0)").fetchone()
    gol_menor_10_min = c.execute("select count(1) from Proball_confrontos where CONFRONTO_FORA = '"+confronto_fora+"' AND LIGA = '"+str(liga)+"' and id in (select id_Proball_confrontos from Proball_confrontos_eventos where evento = '1st Goal' and cast(tempo AS INTEGER) <= 10) AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchone()

    try:
        resultado = 100 -(((int(gol_menor_10_min[0])/int(qtd_total_jogos[0])))*100)

        jogos = c.execute("select * from Proball_confrontos where CONFRONTO_FORA = '"+confronto_fora+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchall()

        for jg in jogos:
            print(jg)
        print("Total de jogos pesquisados: " + str(qtd_total_jogos[0]) + " / " +str(gol_menor_10_min[0]))
        print(str(round(resultado)) + "%")
        lucro = (int(qtd_total_jogos[0]) - int(gol_menor_10_min[0])) * float(valor_aposta_ganha)
        prejuizo = float((int(gol_menor_10_min[0])) * float(valor_aposta_perdida))
        print("em uma aposta simulada, considerando o valor de entrada de R$3,00 para um lucro de R$0,50;\nR$: " + str(lucro - prejuizo))
    except:
        print("Não encontrado...")

def cnfrt_liga(valor_aposta_ganha, valor_aposta_perdida, liga, data_confronto_min, data_confronto_max):
    qtd_total_jogos = c.execute("select count(1) from Proball_confrontos where LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchone()
    com_placar_o_o = c.execute("select count(1) from Proball_confrontos where LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"') and (PLACAR_CASA = 0 and PLACAR_FORA = 0)").fetchone()
    gol_menor_10_min = c.execute("select count(1) from Proball_confrontos where LIGA = '"+str(liga)+"' and id in (select id_Proball_confrontos from Proball_confrontos_eventos where evento = '1st Goal' and cast(tempo AS INTEGER) <= 10) AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchone()

    try:
        resultado = 100 -(((int(gol_menor_10_min[0])/int(qtd_total_jogos[0])))*100)

        jogos = c.execute("select * from Proball_confrontos where LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchall()

        for jg in jogos:
            print(jg)
        print("Total de jogos pesquisados: " + str(qtd_total_jogos[0]) + " / " +str(gol_menor_10_min[0]))
        print(str(round(resultado)) + "%")
        lucro = (int(qtd_total_jogos[0]) - int(gol_menor_10_min[0])) * float(valor_aposta_ganha)
        prejuizo = float((int(gol_menor_10_min[0])) * float(valor_aposta_perdida))
        print("em uma aposta simulada, considerando o valor de entrada de R$3,00 para um lucro de R$0,50;\nR$: " + str(lucro - prejuizo))
    except:
        print("Não encontrado...")

def cnfrt_direto(valor_aposta_ganha, valor_aposta_perdida, confronto_casa, confronto_fora, liga, data_confronto_min, data_confronto_max):
    qtd_total_jogos = c.execute("select count(1) from Proball_confrontos where CONFRONTO_CASA = '"+confronto_casa+"' AND CONFRONTO_FORA = '"+confronto_fora+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchone()
    com_placar_o_o = c.execute("select count(1) from Proball_confrontos where CONFRONTO_CASA = '"+confronto_casa+"' AND CONFRONTO_FORA = '"+confronto_fora+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"') and (PLACAR_CASA = 0 and PLACAR_FORA = 0)").fetchone()
    gol_menor_10_min = c.execute("select count(1) from Proball_confrontos where CONFRONTO_CASA = '"+confronto_casa+"' AND CONFRONTO_FORA = '"+confronto_fora+"' AND LIGA = '"+str(liga)+"' and id in (select id_Proball_confrontos from Proball_confrontos_eventos where evento = '1st Goal' and cast(tempo AS INTEGER) <= 10) AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchone()

    try:
        resultado = 100 -(((int(gol_menor_10_min[0])/int(qtd_total_jogos[0])))*100)

        jogos = c.execute("select * from Proball_confrontos where CONFRONTO_CASA = '"+confronto_casa+"' AND CONFRONTO_FORA = '"+confronto_fora+"' AND LIGA = '"+str(liga)+"' AND DATA_CONFRONTO >= ('"+str(data_confronto_min)+"') and DATA_CONFRONTO < ('"+str(data_confronto_max)+"')").fetchall()

        for jg in jogos:
            print(jg)
        print("Total de jogos pesquisados: " + str(qtd_total_jogos[0]) + " / " +str(gol_menor_10_min[0]))
        print(str(round(resultado)) + "%")
        lucro = (int(qtd_total_jogos[0]) - int(gol_menor_10_min[0])) * float(valor_aposta_ganha)
        prejuizo = float((int(gol_menor_10_min[0])) * float(valor_aposta_perdida))
        print("em uma aposta simulada, considerando o valor de entrada de R$3,00 para um lucro de R$0,50;\nR$: " + str(lucro - prejuizo))
    except:
        print("Não encontrado...")

conn = sqlite3.connect(r'C:\Users\AleAkiraH\Desktop\Projetos\ProBall\proball.db')
c = conn.cursor()

liga = 'BRASIL - SÉRIE A'
data_confronto_min = '2020-01-01 00:00:00'
data_confronto_max = '2020-12-31 23:59:59'
confronto_casa = ''
confronto_fora = ''

# Simulando cotação de 7
valor_aposta_ganha   = 0.50
valor_aposta_perdida = 3.00

if (confronto_casa == '' and confronto_fora == ''):
    cnfrt_liga(valor_aposta_ganha, valor_aposta_perdida, liga, data_confronto_min, data_confronto_max)
elif (confronto_casa != '' and confronto_fora == ''):
    cnfrt_casa(valor_aposta_ganha, valor_aposta_perdida, confronto_casa, liga, data_confronto_min, data_confronto_max)
elif (confronto_casa == '' and confronto_fora != ''):
    cnfrt_fora(valor_aposta_ganha, valor_aposta_perdida, confronto_fora, liga, data_confronto_min, data_confronto_max)
elif (confronto_casa != '' and confronto_fora != ''):
    cnfrt_direto(valor_aposta_ganha, valor_aposta_perdida, confronto_casa, confronto_fora, liga, data_confronto_min, data_confronto_max)
else:
    print('ERRO')


var = 'a'