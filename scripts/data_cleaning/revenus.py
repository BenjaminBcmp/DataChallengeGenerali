import pandas as pd
import numpy as np

mypath = "/Users/Benjamin/Documents/MATHAPPLI/APST-ML/DataChallenge/DataChallengeGenerali/data/revenus/"

def load_data(year):
    """Charge les données de revenu de l'année year dans un dataframe, seulement
    pour les codes INSEE. Ne garde que les colonnes :
        -code géographique
        -revenu médian"""
    file = pd.ExcelFile(mypath+"revenus_%s.xls"%(year))
    revenus = file.parse('COM', skiprows=np.arange(5))
    suff = str(year)[-2:] #suffixe pour les libellés de colonnes
    list_cols = ['CODGEO', 'MED'+suff]
    revenus = revenus.loc[:,list_cols]
    revenus.rename(columns={'MED'+suff:'MED'}, inplace=True)
    revenus = revenus.dropna(axis=0)
    return revenus

def load_data_dep(year):
    """Charge les données de revenu de l'année year dans un dataframe, seulement
    pour les départements. Ne garde que les colonnes :
        -code géographique (numéro de département)
        -revenu médian"""
    file = pd.ExcelFile(mypath+"revenus_%s.xls"%(year))
    revenus = file.parse('DEP', skiprows=np.arange(5))
    suff = str(year)[-2:] #suffixe pour les libellés de colonnes
    list_cols = ['CODGEO', 'MED'+suff]
    revenus = revenus.loc[:,list_cols]
    revenus.rename(columns={'MED'+suff:'MED'}, inplace=True)
    revenus = revenus.dropna(axis=0)
    return revenus

rev2012 = load_data(2012)
rev2013 = load_data(2013)
rev2014 = load_data(2014)
rev2015 = load_data(2015)
rev2012_dep = load_data_dep(2012)
rev2013_dep = load_data_dep(2013)
rev2014_dep = load_data_dep(2014)
rev2015_dep = load_data_dep(2015)

rev2012.to_csv(mypath+"revenus_2012_propre.csv")
rev2013.to_csv(mypath+"revenus_2013_propre.csv")
rev2014.to_csv(mypath+"revenus_2014_propre.csv")
rev2015.to_csv(mypath+"revenus_2015_propre.csv")
rev2012_dep.to_csv(mypath+"revenus_2012_dep_propre.csv")
rev2013_dep.to_csv(mypath+"revenus_2013_dep_propre.csv")
rev2014_dep.to_csv(mypath+"revenus_2014_dep_propre.csv")
rev2015_dep.to_csv(mypath+"revenus_2015_dep_propre.csv")