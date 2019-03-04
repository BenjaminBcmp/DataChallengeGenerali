import pandas as pd
import numpy as np


mypath = "/Users/Benjamin/Documents/MATHAPPLI/APST-ML/DataChallenge/data/chomage/"
sheet = 'Département'

file = pd.ExcelFile(mypath+'chomage.xls')
chomage = file.parse(sheet)

def moyenne_annuelle(cols):
    """cols est un np.array, chaque ligne est un trimestre"""
    return cols.sum(axis=0)/len(cols)

#Ajout des moyennes anuelles, avec 3 chiffres après la virgule
chomage['2012'] = moyenne_annuelle(np.array([chomage.T1_2012, chomage.T2_2012, 
       chomage.T3_2012, chomage.T4_2012])).round(3)
chomage['2013'] = moyenne_annuelle(np.array([chomage.T1_2013, chomage.T2_2013, 
       chomage.T3_2013, chomage.T4_2013])).round(3)
chomage['2014'] = moyenne_annuelle(np.array([chomage.T1_2014, chomage.T2_2014, 
       chomage.T3_2014, chomage.T4_2014])).round(3)
chomage['2015'] = moyenne_annuelle(np.array([chomage.T1_2015, chomage.T2_2015, 
       chomage.T3_2015, chomage.T4_2015])).round(3)
chomage['2016'] = moyenne_annuelle(np.array([chomage.T1_2016, chomage.T2_2016, 
       chomage.T3_2016, chomage.T4_2016])).round(3)
 
#Exportation vers un nouveau fichier .csv
chomage_propre = chomage.loc[:,['Code', '2012', '2013', '2014', '2015', '2016']]
chomage_propre.to_csv(mypath+'chomage_propre.csv')