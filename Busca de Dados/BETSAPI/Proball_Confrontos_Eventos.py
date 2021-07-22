import gets_posts_requests
from bs4 import BeautifulSoup
import string
import re
import os
from datetime import datetime, timedelta
import time
import betsapi_login
import facebook_login_get
import facebook_login_post
import betsapi_home
import bus_odd
import sqlite3
import betsapi_events
import cfscrape
import requests

while True:
    try:   

        VariaveisFT = ["Golos","Corners","Amarelo","Cart?es Amarelo/Vermelho","Cart?o Vermelho","Penaliza??es","Bola segura","Lesionados","Substitui??es","Ataques","Ataques Perigosos","Baliza","Ao Lado","de Posse"]
        VariaveisHT = ["Golos","Corners","Amarelo","Cart?o Vermelho","Penaliza??es","Substitui??es","Ataques","Ataques Perigosos","Baliza","Ao Lado","de Posse"]

        conn = sqlite3.connect(r'C:\Users\AleAkiraH\Desktop\Projetos\ProBall\proball.db')
        c = conn.cursor()

        oq = c.execute("SELECT * FROM [Proball_confrontos] where (LIGA = 'BRASIL - SÉRIE B' or LIGA = 'BRASIL - SÉRIE A') and robo_event is null order by DATA_CONFRONTO desc").fetchall()

        for row in oq:
            golsFT_casa = "sem info"
            golsFT_fora = "sem info"
            escanteiosFT_casa = "sem info"
            escanteiosFT_fora = "sem info"
            cartoesAFT_casa = "sem info"
            cartoesAFT_fora = "sem info"
            cartoesAVFT_casa = "sem info"
            cartoesAVFT_fora = "sem info"
            cartoesVFT_casa = "sem info"
            cartoesVFT_fora = "sem info"
            penalizacoesFT_casa = "sem info"
            penalizacoesFT_fora = "sem info"
            bola_seguraFT_casa = "sem info"
            bola_seguraFT_fora = "sem info"
            lesionadosFT_casa = "sem info"
            lesionadosFT_fora = "sem info"
            substituicoes_casa = "sem info"
            substituicoes_fora = "sem info"
            ataquesFT_casa = "sem info"
            ataquesFT_fora = "sem info"
            ataques_perigososFT_casa = "sem info"
            ataques_perigososFT_fora = "sem info"
            chute_a_golFT_casa = "sem info"
            chute_a_golFT_fora = "sem info"
            chute_ao_ladoFT_casa = "sem info"
            chute_ao_ladoFT_fora = "sem info"
            posse_de_bolaFT_casa = "sem info"
            posse_de_bolaFT_fora = "sem info"
            golsHT_casa = "sem info"
            golsHT_fora = "sem info"
            escanteiosHT_casa = "sem info"
            escanteiosHT_fora = "sem info"
            cartoesAHT_casa = "sem info"
            cartoesAHT_fora = "sem info"
            cartoesVHT_casa = "sem info"
            cartoesVHT_fora = "sem info"
            penalizacoesHT_casa = "sem info"
            penalizacoesHT_fora = "sem info"
            substituicoesHT_casa = "sem info"
            substituicoesHT_fora = "sem info"
            ataquesHT_casa = "sem info"
            ataquesHT_fora = "sem info"
            ataques_perigososHT_casa = "sem info"
            ataques_perigososHT_fora = "sem info"
            chute_a_golHT_casa = "sem info"
            chute_a_golHT_fora = "sem info"
            chute_ao_ladoHT_casa = "sem info"
            chute_ao_ladoHT_fora = "sem info"
            posse_de_bolaHT_casa = "sem info"
            posse_de_bolaHT_fora = "sem info"

            print(str('http://pt.betsapi.com'+row[7]))
            pagina = str('http://pt.betsapi.com'+row[7])

            time.sleep(1)
            htmlPagina = gets_posts_requests.get_list_series_availables(pagina)
            
            soup = BeautifulSoup(htmlPagina, 'html.parser')

            tabela_estatisticas = soup.findAll('table', {"class": "table table-sm"}) 
            tabela_estatisticasHT = tabela_estatisticas[1]
            tabela_estatisticas = tabela_estatisticas[0]
            
            linha = 1
            try:
                if ("                    ?                    " in tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip()):
                    confronto_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split('                    ?                    ')[0].strip()
                    confronto_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split('                    ?                    ')[1].strip()
                    print(str(confronto_casa)+" x "+str(confronto_fora))
                    linha = linha +2
                else:
                    print("SEM REGISTRO")
            except:
                print("SEM REGISTRO")

            # for vft in VariaveisFT:
            #     if (vft in tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip()):
            #         funcao_salva_variavelFT(vft, linha)            
            index = 0
            
            while True:        
                
                if (linha == len(tabela_estatisticas.contents)):
                    index = index + 1
                    linha = 3

                if (index == len(VariaveisFT)):
                    break

                if (VariaveisFT[index] in tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip()):
                    if (VariaveisFT[index] == "Golos"):
                        golsFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Golos")[0].strip()
                        golsFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Golos")[1].strip()
                        print(str(golsFT_casa)+" x "+str(golsFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Corners"):
                        escanteiosFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Corners")[0].strip()
                        escanteiosFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Corners")[1].strip()
                        print(str(escanteiosFT_casa)+" x "+str(escanteiosFT_fora))
                        linha = linha +2      
                        index = index +1
                    elif (VariaveisFT[index] == "Amarelo"):  
                        cartoesAFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Amarelo")[0].strip()
                        cartoesAFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Amarelo")[1].strip()
                        print(str(cartoesAFT_casa)+" x "+str(cartoesAFT_fora))
                        linha = linha +2   
                        index = index +1
                    elif (VariaveisFT[index] == "Cart?es Amarelo/Vermelho"):  
                        cartoesAVFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Cart?es Amarelo/Vermelho")[0].strip()
                        cartoesAVFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Cart?es Amarelo/Vermelho")[1].strip()
                        print(str(cartoesAVFT_casa)+" x "+str(cartoesAVFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Cart?o Vermelho"):
                        cartoesVFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Cart?o Vermelho")[0].strip()
                        cartoesVFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Cart?o Vermelho")[1].strip()
                        print(str(cartoesVFT_casa)+" x "+str(cartoesVFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Penaliza??es"):
                        penalizacoesFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Penaliza??es")[0].strip()
                        penalizacoesFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Penaliza??es")[1].strip()
                        print(str(penalizacoesFT_casa)+" x "+str(penalizacoesFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Bola segura"):
                        bola_seguraFT_casa= tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Bola segura")[0].strip()
                        bola_seguraFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Bola segura")[1].strip()
                        print(str(bola_seguraFT_casa)+" x "+str(bola_seguraFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Lesionados"):
                        lesionadosFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Lesionados")[0].strip()
                        lesionadosFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Lesionados")[1].strip()
                        print(str(lesionadosFT_casa)+" x "+str(lesionadosFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Substitui??es"):
                        substituicoes_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Substitui??es")[0].strip()
                        substituicoes_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Substitui??es")[1].strip()
                        print(str(substituicoes_casa)+" x "+str(substituicoes_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Ataques"):
                        ataquesFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        ataquesFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(ataquesFT_casa)+" x "+str(ataquesFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Ataques Perigosos"):
                        ataques_perigososFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        ataques_perigososFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(ataques_perigososFT_casa)+" x "+str(ataques_perigososFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Baliza"):
                        chute_a_golFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        chute_a_golFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(chute_a_golFT_casa)+" x "+str(chute_a_golFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "Ao Lado"):
                        chute_ao_ladoFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        chute_ao_ladoFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(chute_ao_ladoFT_casa)+" x "+str(chute_ao_ladoFT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisFT[index] == "de Posse"):
                        posse_de_bolaFT_casa = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        posse_de_bolaFT_fora = tabela_estatisticas.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(posse_de_bolaFT_casa)+" x "+str(posse_de_bolaFT_fora))
                        index = index +1
                else:
                    linha = linha +2   

            
            linha = 3
            index = 0
            
            while True:        
                
                if (linha == len(tabela_estatisticasHT.contents)):
                    index = index + 1
                    linha = 3

                if (index >= len(VariaveisHT)):
                    break

                if (VariaveisHT[index] in tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip()):
                    if (VariaveisHT[index] == "Golos"):
                        golsHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Golos")[0].strip()
                        golsHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Golos")[1].strip()
                        print(str(golsHT_casa)+" x "+str(golsHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "Corners"):
                        escanteiosHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Corners")[0].strip()
                        escanteiosHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Corners")[1].strip()
                        print(str(escanteiosHT_casa)+" x "+str(escanteiosHT_fora))
                        linha = linha +2     
                        index = index +1
                    elif (VariaveisHT[index] == "Amarelo"):
                        cartoesAHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Amarelo")[0].strip()
                        cartoesAHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Amarelo")[1].strip()
                        print(str(cartoesAHT_casa)+" x "+str(cartoesAHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "Cart?o Vermelho"):
                        cartoesVHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Cart?o Vermelho")[0].strip()
                        cartoesVHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Cart?o Vermelho")[1].strip()
                        print(str(cartoesVHT_casa)+" x "+str(cartoesVHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "Penaliza??es"):
                        penalizacoesHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Penaliza??es")[0].strip()
                        penalizacoesHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Penaliza??es")[1].strip()
                        print(str(penalizacoesHT_casa)+" x "+str(penalizacoesHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "Substitui??es"):
                        substituicoesHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Substitui??es")[0].strip()
                        substituicoesHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("Substitui??es")[1].strip()
                        print(str(substituicoesHT_casa)+" x "+str(substituicoesHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "Ataques"):
                        ataquesHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        ataquesHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(ataquesHT_casa)+" x "+str(ataquesHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "Ataques Perigosos"):
                        ataques_perigososHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        ataques_perigososHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(ataques_perigososHT_casa)+" x "+str(ataques_perigososHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "Baliza"):
                        chute_a_golHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        chute_a_golHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(chute_a_golHT_casa)+" x "+str(chute_a_golHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "Ao Lado"):
                        chute_ao_ladoHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        chute_ao_ladoHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(chute_ao_ladoHT_casa)+" x "+str(chute_ao_ladoHT_fora))
                        linha = linha +2
                        index = index +1
                    elif (VariaveisHT[index] == "de Posse"):
                        posse_de_bolaHT_casa = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[0].strip()
                        posse_de_bolaHT_fora = tabela_estatisticasHT.contents[linha].text.encode('ascii','replace').replace('\n','').strip().split("              ")[3].strip()
                        print(str(posse_de_bolaHT_casa)+" x "+str(posse_de_bolaHT_fora))
                        linha = linha +2
                        index = index +1
                else:
                    linha = linha +2 
                
            # trs_tabela_estatisticas = soup.find_all('td', {"class": "text-right"}) 

            # for trs in tabela_results:
            #     print(trs)

            # ATE AQUI TUDO BEM
            time.sleep(1)
            # htmlPagina = gets_posts_requests.get_list_series_availables(pagina)
            
            soup = BeautifulSoup(htmlPagina, 'html.parser')

            tabela_results = soup.find_all('li', {"class": "list-group-item"})
            id_Proball_confrontos = str(row[0])
            for trs in tabela_results:
                print(trs)
                try:
                    if ("bl-away" in str(trs.attrs['class'][1])):
                        casaoufora = 'FORA'
                    else:
                        casaoufora = 'CASA'
                except:
                    casaoufora = 'CASA'
                
                try:
                    tempo = str(trs.text.split('-')[0]).strip()
                except:
                    tempo =  trs.text

                try:
                    evento = str(trs.text.split('-')[1]).strip()
                except:
                    evento = ''
                
                try:
                    observacao = str(trs.text.split('-')[2]).strip()
                except:
                    observacao = ''

                res = c.execute("SELECT EXISTS (SELECT * FROM [Proball_confrontos_estastiticas] WHERE [id_Proball_confrontos] = ?)", [id_Proball_confrontos]).fetchone()
                if (res[0] == 0):           
                    c.execute("INSERT INTO [Proball_confrontos_estastiticas] (id_Proball_confrontos,golsFT_casa,golsFT_fora,escanteiosFT_casa,escanteiosFT_fora,cartoesAFT_casa,cartoesAFT_fora,cartoesAVFT_casa,cartoesAVFT_fora,cartoesVFT_casa,cartoesVFT_fora,penalizacoesFT_casa,penalizacoesFT_fora,bola_seguraFT_casa,bola_seguraFT_fora,lesionadosFT_casa,lesionadosFT_fora,substituicoes_casa,substituicoes_fora,ataquesFT_casa,ataquesFT_fora,ataques_perigososFT_casa,ataques_perigososFT_fora,chute_a_golFT_casa,chute_a_golFT_fora,chute_ao_ladoFT_casa,chute_ao_ladoFT_fora,posse_de_bolaFT_casa,posse_de_bolaFT_fora,golsHT_casa,golsHT_fora,escanteiosHT_casa,escanteiosHT_fora,cartoesAHT_casa,cartoesAHT_fora,cartoesVHT_casa,cartoesVHT_fora,penalizacoesHT_casa,penalizacoesHT_fora,substituicoesHT_casa,substituicoesHT_fora,ataquesHT_casa,ataquesHT_fora,ataques_perigososHT_casa,ataques_perigososHT_fora,chute_a_golHT_casa,chute_a_golHT_fora,chute_ao_ladoHT_casa,chute_ao_ladoHT_fora,posse_de_bolaHT_casa,posse_de_bolaHT_fora) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(id_Proball_confrontos,golsFT_casa,golsFT_fora,escanteiosFT_casa,escanteiosFT_fora,cartoesAFT_casa,cartoesAFT_fora,cartoesAVFT_casa,cartoesAVFT_fora,cartoesVFT_casa,cartoesVFT_fora,penalizacoesFT_casa,penalizacoesFT_fora,bola_seguraFT_casa,bola_seguraFT_fora,lesionadosFT_casa,lesionadosFT_fora,substituicoes_casa,substituicoes_fora,ataquesFT_casa,ataquesFT_fora,ataques_perigososFT_casa,ataques_perigososFT_fora,chute_a_golFT_casa,chute_a_golFT_fora,chute_ao_ladoFT_casa,chute_ao_ladoFT_fora,posse_de_bolaFT_casa,posse_de_bolaFT_fora,golsHT_casa,golsHT_fora,escanteiosHT_casa,escanteiosHT_fora,cartoesAHT_casa,cartoesAHT_fora,cartoesVHT_casa,cartoesVHT_fora,penalizacoesHT_casa,penalizacoesHT_fora,substituicoesHT_casa,substituicoesHT_fora,ataquesHT_casa,ataquesHT_fora,ataques_perigososHT_casa,ataques_perigososHT_fora,chute_a_golHT_casa,chute_a_golHT_fora,chute_ao_ladoHT_casa,chute_ao_ladoHT_fora,posse_de_bolaHT_casa,posse_de_bolaHT_fora))
                    conn.commit()
                    print('novo registro Proball_confrontos_estastiticas')
                else:
                    print('ja existente Proball_confrontos_estastiticas')

                res = c.execute("SELECT EXISTS (SELECT * FROM [Proball_confrontos_eventos] WHERE [id_Proball_confrontos] = ? AND [casaoufora] = ? AND [tempo] = ? AND [evento] = ? AND [observacao] = ?)", [id_Proball_confrontos,casaoufora, tempo.replace("'",""), evento, observacao]).fetchone()
                if (res[0] == 0):           
                    c.execute("INSERT INTO [Proball_confrontos_eventos] ([id_Proball_confrontos],[casaoufora],[tempo],[evento],[observacao]) VALUES (?,?,?,?,?)",(id_Proball_confrontos, casaoufora, tempo.replace("'",""), evento, observacao))
                    conn.commit()
                    print('novo registro Proball_confrontos_eventos')
                else:
                    print('ja existente Proball_confrontos_eventos')
            
            c.execute("update [Proball_confrontos] set robo_event = 1 where id = ?",[id_Proball_confrontos])
            conn.commit()

            time.sleep(1)
            try:
                res = res
            except:
                pass
    except:
        time.sleep(300)