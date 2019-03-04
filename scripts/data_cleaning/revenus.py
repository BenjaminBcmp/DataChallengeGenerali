import pandas as pd
import numpy as np

mypath = "/Users/Benjamin/Documents/MATHAPPLI/APST-ML/DataChallenge/data/revenus/"

def load_data(year):
    """Charge les données de revenu de l'année year dans un dataframe. Ne garde
    que les colonnes :
        -code géographique
        -revenu médian"""
    file = pd.ExcelFile(mypath+"revenus_%s.xls"%(year))
    revenus = file.parse('COM', skiprows=np.arange(5))
    suff = str(year)[-2:] #suffixe pour les libellés de colonnes
    list_cols = ['CODGEO', 'MED'+suff]
    return revenus.loc[:,list_cols]

rev2012 = load_data(2012)
rev2013 = load_data(2013)
rev2014 = load_data(2014)
rev2015 = load_data(2015)

rev2012.to_csv(mypath+"revenus_2012_propre.csv")
rev2013.to_csv(mypath+"revenus_2013_propre.csv")
rev2014.to_csv(mypath+"revenus_2014_propre.csv")
rev2015.to_csv(mypath+"revenus_2015_propre.csv")