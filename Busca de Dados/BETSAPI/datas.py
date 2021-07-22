f = open('crawler.txt', 'a')
f.write('')
f.close()

for x in range(1,700):
    d = datetime.today() - timedelta(days=x)
    
    ano = str(d.year)
    mes = str(d.month)
    dia = str(d.day)

    f = open('datas.txt','a')
    f.write(ano+'-'+mes+'-'+dia+'\n')
    f.close()