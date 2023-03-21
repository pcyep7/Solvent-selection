import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import impute
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.decomposition import PCA

def perform_PCA(file, Descriptors, missing_data="mean", scaling="standard"):
    # get data from file
    data = pd.read_csv(file)
    # get the descriptors
    data_df = data[Descriptors]
    # missing data
    if missing_data == "iterative":
        # set up imputation
        imp = IterativeImputer(max_iter=10)
    else:
        # set up imputation
        imp = impute.SimpleImputer(missing_values=np.nan, strategy='mean')
    # fit to data
    imp.fit(data_df)
    # transform data
    data_df_impute = imp.transform(data_df)
    # scaling
    if scaling == "min_max":
        scaler = preprocessing.MinMaxScaler().fit(data_df_impute)
    else:
        scaler = preprocessing.StandardScaler().fit(data_df_impute)
    data_df_impute = scaler.transform(data_df_impute)
    #set up PCA with n_comp=n_desc
    pca = PCA(n_components = len(data_df_impute[0]))
    # get components
    principalComponents = pca.fit_transform(data_df_impute)
    # make into dataframe
    columns=[]
    for x in range(len(data_df_impute[0])):
        columns.append("PC" + str(x + 1))
    principalDf = pd.DataFrame(data=principalComponents, columns=columns)
    # get the cumulative variance
    cum_scree=np.cumsum(pca.explained_variance_ratio_)*100
    # get the loadings for each PC
    loadings = pd.DataFrame(pca.components_.T, columns=columns, index=Descriptors)
    loadings["Descriptor"] = Descriptors
    # return info
    return data, principalDf, cum_scree, loadings

def add_back_data(principalDf, data):
    # add back in green rating and experimental data
    principalDf["Solvent"] = data["Solvent"]
    principalDf["CHEM21 (0=bad, 0.5 = acceptable, 1=good)"] = data["CHEM21 (0=bad, 0.5 = acceptable, 1=good)"]
    principalDf["% enol"] = data["% enol"]
    principalDf["Thioester"] = data["Thioester"]
    principalDf["Esterification"] = data["Esterification"]
    principalDf["Delapine"] = data["Delapine"]
    principalDf["Functional Group"] = data["Functional Group"]
    principalDf["CHEM21 Numerical"] = data["CHEM21 Numerical"]
    principalDf["Grignard"] = data["Grignard"]
    principalDf["Amide Coupling"] = data["Amide Coupling"]
    principalDf["Heck C-C"] = data["Heck C-C"]
    principalDf["Baylis-Hillman"] = data["Baylis-Hillman"]
    principalDf["Suzuki-Miyaura"] = data["Suzuki-Miyaura"]
    principalDf["Buchwald-Hartwig"] = data["Buchwald-Hartwig"]
    principalDf["Alkene Metathesis"] = data["Alkene Metathesis"]
    principalDf["Suzuki-Miyaura Ni"] = data["Suzuki-Miyaura Ni"]
    principalDf["SN2/SNAr"] = data["SN2/SNAr"]
    principalDf["Alcohol Oxidation"] = data["Alcohol Oxidation"]
    principalDf["Ester Hydrolysis"] = data["Ester Hydrolysis"]
    principalDf["BP /degC"] = data["BP /degC"]
    principalDf["cost £/L"] = data["cost £/L"]
