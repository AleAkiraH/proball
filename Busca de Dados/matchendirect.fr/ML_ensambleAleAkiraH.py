# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:29:24 2020

@author: AleAkiraH
"""

import pandas as pd

base = pd.read_csv('massa ML\\treino.csv', encoding = "ANSI")
base = base.drop(['CONFRONTO_CASA','CONFRONTO_FORA'], axis=1)
previsores = base.iloc[:, 0:6].values
classe = base.iloc[:, 6].values
# classe = base.iloc[:, 22:24].values
                
from sklearn.preprocessing import LabelEncoder

labelencoder_previsores = LabelEncoder()
# previsores[:, 0] = labelencoder_previsores.fit_transform(previsores[:, 0])
# previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:, 1])

labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)
# classe[:,0] = labelencoder_classe.fit_transform(classe[:,0])
# classe[:,1] = labelencoder_classe.fit_transform(classe[:,1])

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classificador = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
classificador.fit(previsores_treinamento.astype(int), classe_treinamento.astype(int))
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)


previsao_base = pd.read_csv('massa ML\\csvTeste.csv', encoding = "ANSI")
# previsao_base = previsao_base.drop(['ResultFT'], axis=1)
previsao_base = previsao_base.drop(['CONFRONTO_FORA'], axis=1)
previsao_base = previsao_base.drop(['CONFRONTO_CASA'], axis=1)
previsao = pd.read_csv('massa ML\\csvTeste.csv', encoding = "ANSI")
# previsao = previsao.drop(['ResultFT'], axis=1)
previsao = previsao.drop(['CONFRONTO_FORA'], axis=1)
previsao = previsao.drop(['CONFRONTO_CASA'], axis=1)

labelencoder_previsores = LabelEncoder()
previsao = previsao.iloc[:, 0:6].values

# previsao[:, 0] = labelencoder_previsores.fit_transform(previsao[:, 0])
# previsao[:, 1] = labelencoder_previsores.fit_transform(previsao[:, 1])

resultado = classificador.predict(previsao)

resultado