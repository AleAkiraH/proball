import gets_posts_requests
from bs4 import BeautifulSoup
import string

def busca_series():
	htmlPagina = gets_posts_requests.get_list_series_availables("http://netcine.us/tvshows/").text

	soup = BeautifulSoup(htmlPagina, 'html.parser')

	box_series_list = soup.find('div', id="box_movies")
	box_series_list_items = box_series_list.find_all('a')

	seriados = []

	for serie in box_series_list_items:
		seriados.append(str(serie.get('href')).split('/')[4])
		print(str(serie.get('href')).split('/')[4])

	return seriados

def busca_temporadas(nome_seriado):

	htmlPagina = gets_posts_requests.get_list_series_availables("http://netcine.us/tvshows/"+ nome_seriado).text

	soup = BeautifulSoup(htmlPagina, 'html.parser')

	sinopse_seriado = soup.find('div', id="dato-2")

	boxTemporadas_list = soup.find('div', id="cssmenu")
	boxTemporadas_list_items = boxTemporadas_list.find_all('li')

	for temporada_episodio in boxTemporadas_list_items:

		# link = temporada_episodio.find_all('a')[0].get('href')

		if "Temporada" in temporada_episodio.text:
			print(temporada_episodio.contents[0].text.replace('\t','').replace('\r','').replace('\n','').strip())

def busca_episodios(nome_seriado, temporada):

	htmlPagina = gets_posts_requests.get_list_series_availables("http://netcine.us/tvshows/"+ nome_seriado)

	soup = BeautifulSoup(htmlPagina.text, 'html.parser')

	# sinopse_seriado = soup.find('div', id="dato-2")

	boxTemporadas_list = soup.find('div', id="cssmenu")
	boxTemporadas_list_items = boxTemporadas_list.find_all('li')

	for temporada_episodio in boxTemporadas_list_items:

		if (temporada in temporada_episodio.text):
			links = temporada_episodio.find_all('a')		
			for link_episodio in links:                                
				s = link_episodio.text.translate(str.maketrans("\n\t\r", "   "))
				if not "Temporada" in s:
					link_netcine = link_episodio.get('href')
					htmlPagina = gets_posts_requests.get_list_series_availables(link_netcine)
					soup = BeautifulSoup(htmlPagina.text, 'html.parser')

					# sinopse_seriado = soup.find('div', id="dato-2")

					video_play_leg = soup.find('div', id="play-1")
					video_play_leg_items = video_play_leg.find_all('iframe')

					htmlPagina = gets_posts_requests.get_list_series_availables(video_play_leg_items[0].get('src'))
					soup = BeautifulSoup(htmlPagina.text, 'html.parser')
					div_campanha = soup.find_all('iframe')

					htmlPagina = gets_posts_requests.get_list_series_availables(div_campanha[0].get('src'))
					soup = BeautifulSoup(htmlPagina.text, 'html.parser')
					div_campanha = soup.find_all('a')
					link_div_campanha = div_campanha[0].get('href').replace('http://p.netcine.us/redirecionar.php?data=','')

					htmlPagina = gets_posts_requests.get_list_series_availables(link_div_campanha)
					soup = BeautifulSoup(htmlPagina.text, 'html.parser')

					link_video_final_leg_baixo = soup.find('div', id="demo")
					lista_arquivos_site = link_video_final_leg_baixo.parent.text.split('\n')

					for arquivos in lista_arquivos_site:
						if  "file: \"" in arquivos:
							print(s.strip() + '\n')
							if  "BAIXO" in arquivos:
								print('LEGENDADO - BAIXO: ' + arquivos.replace('       file: ','').replace('\r','').replace('\"',''))
							if  "ALTO" in arquivos:
								print('LEGENDADO - ALTO: ' + arquivos.replace('       file: ','').replace('\r','').replace('\"',''))
# ANOTAÇÕES: DEVERÁ SER DIVIDO AS FUNCOES DE BUSCAR NOME DO EPISODIO DAS QUE NECESSITAM BUSCAR O LINK A FIM DE MINIMAR O TEMPO GASTO

					
print("Olá, sou o \"catalogador\":), o que você deseja fazer?\n"
        "1 - Deseja visualizar o nosso catalogo de seriados?\n"
        "2 - Deseja buscar uma de nossas series?\n"
        )
# opcao_selecionada = '2' # input("Digite a opção selecionada: ")
opcao_selecionada = input("Digite a opção selecionada: ")

if (opcao_selecionada == '1'):
	seriados = busca_series()
	for serie in seriados:
		print(serie)
		opcao_selecionada = '2'

if (opcao_selecionada == '2'):
	# serie = 'the-100'# input("Informe o nome do seriado: ")
	serie = input("Informe o nome do seriado: ")
	busca_temporadas(serie)
	# temporada = 'Temporada 4' # input("Informe a temporada: ")
	temporada = input("Informe a temporada: ")
	busca_episodios(serie, temporada)

input("Press enter to exit ;)")

# seriados = busca_series()
# for serie in seriados:
#         print(serie)
#         busca_temporadas(serie)
#         busca_episodios(serie, "Temporada")
