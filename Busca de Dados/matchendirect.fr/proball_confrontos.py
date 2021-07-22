import gets_posts_requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect(r'C:\Users\alexsander.ferreira\Desktop\trabalho\proball\dtproball.db')
c = conn.cursor()

url = "https://www.matchendirect.fr/allemagne/bundesliga-1/"
ano = 2020

# variaveis_estatisticas = ['Possession','Attaques','Attaques dangereuses','Coups francs','Coups de pied arrêtés','Buts','Tirs cadrés','Tirs non cadrés','Tirs arrêtés','Touches','Corners','Hors-jeu','Fautes','Carton jaune','Remplacements','Remplacements']

for semana in range(1, 99):
    print(semana)
    pagina = url+str(ano)+"-"+str(semana).zfill(2)+"/"
    htmlPagina = gets_posts_requests.get_list_series_availables(pagina)

    soup = BeautifulSoup(htmlPagina, 'html.parser')
    lin_tb_rod = 0
    
    try:
        tabela_rodadas = soup.find_all('table')[0]

        liga = 'BUNDESLIGA-1'

        while True:
        
            qtd_confrontos_rodada = len(tabela_rodadas.find_all('tr'))

            if (lin_tb_rod == qtd_confrontos_rodada):
                break
            
            try:
                ano = tabela_rodadas.find_all('tr')[lin_tb_rod].contents[1].text.split(' ')[3]
                mes = tabela_rodadas.find_all('tr')[lin_tb_rod].contents[1].text.split(' ')[2]
                dia = tabela_rodadas.find_all('tr')[lin_tb_rod].contents[1].text.split(' ')[1]
            except:
                confrontos_horario = tabela_rodadas.find_all('tr')[lin_tb_rod].find_all('td', {'class','lm1'})[0].text
                
                dataconfronto = str(ano) +"-"+ str(mes.replace("janvier","1").replace("février","2").replace("mars","3").replace("avril","4").replace("mai","5").replace("juin","6").replace("juillet","7").replace("août","8").replace("septembre","9").replace("octobre","10").replace("novembre","11").replace("décembre","12").zfill(2)) +"-"+ str(dia.zfill(2)) +" "+ str(confrontos_horario) +":00"
                confronto_casa = tabela_rodadas.find_all('tr')[lin_tb_rod].find_all('td', {'class','lm3'})[0].contents[1].contents[0].text
                confronto_fora = tabela_rodadas.find_all('tr')[lin_tb_rod].find_all('td', {'class','lm3'})[0].contents[1].contents[2].text
                placar_casa = tabela_rodadas.find_all('tr')[lin_tb_rod].find_all('td', {'class','lm3'})[0].contents[1].contents[1].text.split(' - ')[0]
                placar_fora = tabela_rodadas.find_all('tr')[lin_tb_rod].find_all('td', {'class','lm3'})[0].contents[1].contents[1].text.split(' - ')[1]
                link = "https://www.matchendirect.fr" + str(tabela_rodadas.find_all('tr')[lin_tb_rod].find_all('a')[0].attrs['href'])
                print(confronto_casa + " x " + confronto_fora)
                verificar_existencia = "SELECT EXISTS (SELECT * FROM [Proball_confrontos] WHERE [LIGA] = '" + liga + "' AND [DATA_CONFRONTO] = '" + dataconfronto + "' AND [CONFRONTO_CASA] = '" + confronto_casa + "' AND [CONFRONTO_FORA] = '" + confronto_fora + "' AND [PLACAR_CASA] = '" + placar_casa + "' AND [PLACAR_FORA] = '" + placar_fora + "' AND [LINK_EVENTOS] = '" + link + "')"
                res = c.execute(verificar_existencia).fetchone()
                if (res[0] == 0):
                    # Abrir link e buscar eventos
                    htmlPagina_eventos = gets_posts_requests.get_list_series_availables(link)

                    soup_eventos = BeautifulSoup(htmlPagina_eventos, 'html.parser')

                    tabela_rodadas_eventos = soup_eventos.find_all('table')
                    div_estatisticas = soup_eventos.find('div')
                    
                    
                    finalHT_casa = ''
                    finalHT_fora = ''
                    finalFT_casa = ''
                    finalFT_fora = ''
                
                    finalHT_casa = tabela_rodadas_eventos[0].contents[1].contents[3].text.split(' - ')[0]
                    finalHT_fora = tabela_rodadas_eventos[0].contents[1].contents[3].text.split(' - ')[1]
                    finalFT_casa = tabela_rodadas_eventos[0].contents[3].contents[3].text.split(' - ')[0]
                    finalFT_fora = tabela_rodadas_eventos[0].contents[3].contents[3].text.split(' - ')[1]
                    
                    posse_casa = ''
                    posse_fora = ''
                    indexvariaveis = 1
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == "Possession"):
                            posse_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            posse_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                        
                    ataques_casa = ''
                    ataques_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Attaques'):
                            ataques_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            ataques_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    ataques_perigosos_casa = ''
                    ataques_perigosos_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Attaques dangereuses'):
                            ataques_perigosos_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            ataques_perigosos_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                        
                    chutes_livres_casa = ''
                    chutes_livres_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Coups francs'):
                            chutes_livres_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            chutes_livres_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                            
                    conjunto_de_pecas_casa = ''
                    conjunto_de_pecas_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Coups de pied arrêtés'):
                            conjunto_de_pecas_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            conjunto_de_pecas_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    metas_casa = ''
                    metas_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Buts'):
                            metas_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            metas_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    penaltis_casa = ''
                    penaltis_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Tirs cadrés'):
                            penaltis_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            penaltis_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    tiros_fora_do_alvo_casa = ''
                    tiros_fora_do_alvo_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Tirs non cadrés'):
                            tiros_fora_do_alvo_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            tiros_fora_do_alvo_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    tiros_parados_casa = ''
                    tiros_parados_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Tirs arrêtés'):
                            tiros_parados_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            tiros_parados_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    tiros_na_postagem_casa = ''
                    tiros_na_postagem_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Tirs sur le poteau'):
                            tiros_na_postagem_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            tiros_na_postagem_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    penaltys_casa = ''
                    penaltys_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Pénaltys'):
                            penaltys_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            penaltys_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    chaves_casa = ''
                    chaves_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Touches'):
                            chaves_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            chaves_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    cantos_casa = ''
                    cantos_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Corners'):
                            cantos_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            cantos_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    off_side_casa = ''
                    off_side_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Hors-jeu'):
                            off_side_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            off_side_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    faltas_casa = ''
                    faltas_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Fautes'):
                            faltas_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            faltas_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    cartao_amarelo_casa = ''
                    cartao_amarelo_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Carton jaune'):
                            cartao_amarelo_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            cartao_amarelo_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    cartao_vermelho_direto_casa = ''
                    cartao_vermelho_direto_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Carton rouge direct'):
                            cartao_vermelho_direto_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            cartao_vermelho_direto_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                    
                    substituicoes_casa = ''
                    substituicoes_fora = ''
                    try:
                        if (tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[7].text == 'Remplacements'):
                            substituicoes_casa = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[1].contents[0]
                            substituicoes_fora = tabela_rodadas_eventos[3].contents[1].contents[indexvariaveis].contents[11].contents[0]
                            indexvariaveis = indexvariaveis + 1
                    except:
                        pass
                        
                    # Registrar estatisticas
                    
                    insert = "INSERT INTO [Proball_confrontos] ([LIGA],[DATA_CONFRONTO],[CONFRONTO_CASA],[CONFRONTO_FORA],[PLACAR_CASA],[PLACAR_FORA],[LINK_EVENTOS],[robo_event]) VALUES ('" + liga + "','" + dataconfronto + "','" + confronto_casa + "','" + confronto_fora + "','" + placar_casa + "','" + placar_fora + "','" + link + "','1')"
                    id_proball_confrontos = c.execute(insert).lastrowid
                    conn.commit()
                    print('novo registro')
                    res = c.execute("SELECT EXISTS (SELECT * FROM [Proball_confrontos_estastiticas] WHERE [id_Proball_confrontos] = ?)", [id_proball_confrontos]).fetchone()
                
                    if (res[0] == 0):     
                        c.execute("INSERT INTO [Proball_confrontos_estastiticas] (id_proball_confrontos,finalHT_casa,finalHT_fora,finalFT_casa,finalFT_fora,posse_casa,posse_fora,ataques_casa,ataques_fora,ataques_perigosos_casa,ataques_perigosos_fora,chutes_livres_casa,chutes_livres_fora,conjunto_de_peças_casa,conjunto_de_peças_fora,metas_casa,metas_fora,penaltis_casa,penaltis_fora,tiros_fora_do_alvo_casa,tiros_fora_do_alvo_fora,tiros_parados_casa,tiros_parados_fora,tiros_na_postagem_casa,tiros_na_postagem_fora,penaltys_casa,penaltys_fora,chaves_casa,chaves_fora,cantos_casa,cantos_fora,off_side_casa,off_side_fora,faltas_casa,faltas_fora,cartao_amarelo_casa,cartao_amarelo_fora,cartao_vermelho_direto_casa,cartao_vermelho_direto_fora,substituicoes_casa,substituicoes_fora) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(id_proball_confrontos,finalHT_casa,finalHT_fora,finalFT_casa,finalFT_fora,posse_casa,posse_fora,ataques_casa,ataques_fora,ataques_perigosos_casa,ataques_perigosos_fora,chutes_livres_casa,chutes_livres_fora,conjunto_de_pecas_casa,conjunto_de_pecas_fora,metas_casa,metas_fora,penaltis_casa,penaltis_fora,tiros_fora_do_alvo_casa,tiros_fora_do_alvo_fora,tiros_parados_casa,tiros_parados_fora,tiros_na_postagem_casa,tiros_na_postagem_fora,penaltys_casa,penaltys_fora,chaves_casa,chaves_fora,cantos_casa,cantos_fora,off_side_casa,off_side_fora,faltas_casa,faltas_fora,cartao_amarelo_casa,cartao_amarelo_fora,cartao_vermelho_direto_casa,cartao_vermelho_direto_fora,substituicoes_casa,substituicoes_fora))
                        conn.commit()
                        print('novo registro Proball_confrontos_estastiticas')
                    else:
                        print('ja existente Proball_confrontos_estastiticas')
                    
                else:
                    print('ja existente')
                    
            lin_tb_rod = lin_tb_rod + 1 
    except:
        print("ERRO")
    
    lin_tb_rod = lin_tb_rod + 1    
