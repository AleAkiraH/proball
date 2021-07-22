from selenium import webdriver
driver = webdriver.PhantomJS(executable_path=r"C:\Users\AleAkiraH\Desktop\Projetos\ProBall\Busca de Dados\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get("http://betsapi.com/r/2213954/AMERICA-MG-V-CRUZEIRO")
p_element = driver.find_element_by_id(id_='intro-text')
print(p_element.text)
# result:
'Yay! Supports javascript'