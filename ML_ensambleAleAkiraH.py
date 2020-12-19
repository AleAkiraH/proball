# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:29:24 2020

@author: AleAkiraH
"""

import pandas as pd

base = pd.read_csv('BRASIL SERIE A.csv', encoding = "ISO-8859-1")
previsores = base.iloc[:, 0:3].values
classe = base.iloc[:, 5].values
                
from sklearn.preprocessing import LabelEncoder

labelencoder_previsores = LabelEncoder()
previsores[:, 0] = labelencoder_previsores.fit_transform(previsores[:, 0])
previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 2] = labelencoder_previsores.fit_transform(previsores[:, 2])


labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classificador = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)





previsao = pd.read_csv('Predict.csv', encoding = "ISO-8859-1")
labelencoder_previsores = LabelEncoder()
previsao = previsao.iloc[:, 0:3].values

previsao[:, 0] = labelencoder_previsores.fit_transform(previsao[:, 0])
previsao[:, 1] = labelencoder_previsores.fit_transform(previsao[:, 1])
previsao[:, 2] = labelencoder_previsores.fit_transform(previsao[:, 2])

resultado = classificador.predict(previsao)