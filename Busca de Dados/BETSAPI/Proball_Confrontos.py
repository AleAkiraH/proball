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
import betsapi_siteafterlogin
import bus_odd

def ultimos_jogos_10_min():

    data = str(datetime.datetime.now().year) + '-' + str(round(datetime.datetime.now().month,2)) + '-' + str(round(datetime.datetime.now().day,2))

    try:
        os.remove('crawler.txt')
    except:
        pass

    urlbase = "https://pt.betsapi.com/"
    urlresultado_10min = urlbase + "le/22821/Esoccer-Live-Arena--10-mins-play/"
    logado = False

    f = open('crawler.txt', 'a')
    f.write('Liga;dia;mes;hr;minuto;confronto;placar_casa;placar_fora;player_casa;player_fora;url_odds\n')
    f.close()
    pg = 1
    
    while True:
        if (pg == 1):
            pagina = urlresultado_10min
        else:
            pagina = urlresultado_10min+"/p." + str(pg)


        htmlPagina = gets_posts_requests.get_list_series_availables(pagina).text

        soup = BeautifulSoup(htmlPagina, 'html.parser')

        tabela_results = soup.find_all('tr')

        for trs in tabela_results:            
            infos = trs.text.split('\n')
            
            try:
                mes = str(infos[1].split('/')[0])
            except:
                continue
                            
            link_confronto_placar = trs.find_all('a')
            link_confronto_placar = link_confronto_placar[2].get('href').replace('/r/','/rs/')
            url_odds = urlbase + link_confronto_placar
            
            if not (logado):
                result = betsapi_login.make_requests()
                result = facebook_login_get.make_requests()
                result = facebook_login_post.make_requests()
                logado = True

            while True:
                try:
                    result = bus_odd.make_requests(url_odds)
                    break
                except:
                    continue

            if not ("Bet365" in result):
                continue
            

            dia = str(infos[1].split('/')[1].split(' ')[0])
            hr = str(int(str(infos[1].split('/')[1].split(' ')[1]).split(":")[0])-3)
            if ("-" in hr):
                dia = str(int(dia) -  1)
                hr = str(24 + int(hr))
            minuto = str(infos[1].split('/')[1].split(' ')[1]).split(":")[1]

            confronto = str(infos[4]).strip()

            placar_casa = str(infos[7]).strip().split('-')[0]
            try:
                placar_fora = str(infos[7]).strip().split('-')[1]
            except:
                continue
            

            player_casa = infos[4].split('(')[1].split(')')[0]
            player_fora = infos[4].split('(')[2].split(')')[0]

            f = open('crawler.txt', 'a')
            f.write(str("Esoccer Live Arena - 10 Minutos de Jogo").strip()+";"+dia+";"+mes+";"+hr+";"+minuto+";"+confronto+";"+placar_casa+";"+placar_fora+";"+str(player_casa)+";"+str(player_fora)+";"+str(url_odds)+"\n")
            f.close()
        
        print(pg)
        
        pg = pg + 1

def buscar_jogos_por_data(data, d, x):

    urlbase = "https://pt.betsapi.com/cs/soccer/"+data+"?skipE=1"
    logado = False

    for pg in range(1,20):
        
        if (pg == 1):
            pagina = urlbase+"/"
        else:
            pagina = urlbase+data+"/p." + str(pg)
        
        if not (logado):
            result = betsapi_login.make_requests()
            result = facebook_login_get.make_requests()
            result = facebook_login_post.make_requests()
            result = betsapi_siteafterlogin.make_requests()
            logado = True

        htmlPagina = gets_posts_requests.get_list_series_availables(pagina)

        soup = BeautifulSoup(htmlPagina, 'html.parser')

        tabela_results = soup.find_all('tr')

        for trs in tabela_results:
            infos = trs.text.split('\n')

            hr = str(int(str(infos[2].split('/')[1].split(' ')[1]).split(":")[0])-2).zfill(2)
            ano = str(data.split('-')[0])

            link_confronto_placar = trs.find_all('a')
            link_confronto_placar = str(link_confronto_placar[len(link_confronto_placar)-2].get('href'))
            dia = str(d.day).zfill(2)
            mes = str(d.month).zfill(2)

            if ("-" in hr):
                dia = str((d - timedelta(days=1)).day).zfill(2)
                mes = str((d - timedelta(days=1)).month).zfill(2)
                ano = str((d - timedelta(days=1)).year).zfill(2)
                hr = str(24+int(hr)).zfill(2)

            
            minuto = str(infos[2].split('/')[1].split(' ')[1]).split(":")[1].zfill(2)

            confronto = str(infos[5].encode('utf-8')).strip()

            placar_casa = str(infos[11]).strip().split('-')[0]
            try:
                placar_fora = str(infos[11]).strip().split('-')[1]
            except:
                continue
            

            player_casa = infos[5].split(' v ')[0]
            player_fora = player_casa = infos[5].split(' v ')[1]

            f = open('crawler.txt', 'a')
            f.write(infos[1].encode("utf-8") + ";"+dia+";"+mes+";"+ano+";"+hr+";"+minuto+";"+confronto+";"+placar_casa+";"+placar_fora+";"+link_confronto_placar+"\n")
            f.close()

        pg = pg + 1



try:
    os.remove('crawler.txt')
except:
    pass

f = open('crawler.txt', 'a')
f.write('Liga;dia;mes;ano;hr;minuto;confronto;casa;fora;link\n')
f.close()

i = 1

for x in range(i,3660):
    d = datetime.today() - timedelta(days=x)
    
    ano = str(d.year)
    mes = str(d.month)
    dia = str(d.day)
    buscar_jogos_por_data((ano+'-'+mes+'-'+dia), d, x)