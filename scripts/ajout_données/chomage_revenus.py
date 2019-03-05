#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:51:03 2019

@author: Benjamin
"""

import numpy as np
import pandas as pd

data_path = "/Users/Benjamin/Documents/MATHAPPLI/APST-ML/DataChallenge/DataChallengeGenerali/data/"

#Importation de X (train ou test)
filename_input = "X_train.csv"
filename_output = "X_train_chomage_revenus.csv"
X = pd.read_csv(data_path+filename_input, header=0, index_col=0)
#Juste pour vérifier qu'on n'ajoute pas de NaN
X=X.dropna(axis=0)
X.index = range(len(X))

#Importation des données à ajouter
chomage = pd.read_csv(data_path+"chomage/chomage_propre.csv", header=0, index_col=0)

revenus = []
for annee in range(2012,2016):
    revenus.append(pd.read_csv(data_path+"revenus/revenus_%s_propre.csv"%(annee), header=0, index_col=0))

revenus_dep = []
for annee in range(2012,2016):
    revenus_dep.append(pd.read_csv(data_path+"revenus/revenus_%s_dep_propre.csv"%(annee), header=0, index_col=0))


#Ajout des colonnes chomage
#Pas de problème de code insee car on travaille par département
def ajout_chomage(X, chomage):
    departements = np.array(chomage['Code'])
    X['chomage'] = [chomage[str(annee)][departements==insee[:2]].values[0] \
                     for annee,insee in zip(X.ft_2_categ, X.Insee)]
    return X

    
#Ajout du revenu médian
#On utilise pred_revenu_2016 si l'année est 2016
#On met le revenu du departement si le code Insee n'est pas dans la liste 
#des codes de revenus
def ajout_revenu(X, revenus, revenus_dep):
    """Ajoute le revenu médian pour les années où l'on dispose des données"""
    codes = [np.array(revenus[annee-2012].CODGEO) for annee in range(2012,2016)]
    n = len(X)
    rev_med = np.zeros(n)
    for k in range(n):
        annee = int(X.ft_2_categ[k])
        if annee == 2016:
            rev_med[k] = pred_revenu_2016(X.Insee[k], revenus, revenus_dep)
        elif X.Insee[k] not in codes[annee-2012]:
            rev_med[k] = revenus_dep[annee-2012].MED[revenus_dep[annee-2012].CODGEO==X.Insee[k][:2]]
        else:
            rev_med[k] = revenus[annee-2012].MED[revenus[annee-2012].CODGEO==X.Insee[k]]

    X['rev_med'] = rev_med
    return X

def pred_revenu_2016(code, revenus, revenus_dep):
    """Prédit le revenu médian en 2016 pour le code INSEE.
    Prédiction = moyenne des revenus médians des deux années précédentes pour le
    code INSEE quand ils sont disponibles, sinon on utilise les revenus du 
    département"""
    rev14, rev15 = revenus[2], revenus[3]
    if code in np.array(rev14.CODGEO) and code in np.array(rev15.CODGEO):
        return (rev14.MED[rev14.CODGEO==code].values[0] + 
                rev15.MED[rev15.CODGEO==code].values[0] ) / 2
    else:
        revdep14, revdep15 = revenus_dep[2], revenus_dep[3]
        return (revdep14.MED[revdep14.CODGEO==code[:2]].values[0] + 
                revdep15.MED[revdep15.CODGEO==code[:2]].values[0] ) / 2


#Mise à jour de X
X = ajout_chomage(X, chomage)
    
X = ajout_revenu(X, revenus, revenus_dep)

X.to_csv(data_path+filename_output)

        







