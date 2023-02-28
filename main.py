from PCA_utils.PCA_methods import perform_PCA, add_back_data
from PCA_utils.graphs import get_plain_PCA, scree_graph, loadings_graph, FG_graph, getPCA_plot
from PCA_utils.reactionT import reactionT
from PCA_utils.budget import budget

Descriptors= ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"]

dict_desc = {"one": 1, "two": 2}
print(dict_desc["one"])
# PCA, Mean Impute, Standardisation

# get data
data, principalDf, cum_scree, loadings = perform_PCA("solvent_exp_data.csv", Descriptors)
add_back_data(principalDf, data)

# get reaction temp
T=reactionT()
principalDf = principalDf[principalDf["BP /degC"] > T]

# get solvent budget
C=budget()
principalDf = principalDf[principalDf["cost £/L"] < C]


# plot PCA graph
get_plain_PCA(principalDf)

# plot scree graph
scree_graph(cum_scree)

# plot loading graph
loadings_graph(loadings)

# plot validation graphs
# plot with functional groups highlighted
FG_graph(principalDf)
# plot of experimental data
getPCA_plot(principalDf, "PCA", "% enol")
# plot of experimental data
getPCA_plot(principalDf, "PCA", "Thioester")
# plot of experimental data
getPCA_plot(principalDf, "PCA", "Esterification")
# plot of experimental data
getPCA_plot(principalDf, "PCA", "Delapine")
# plot of experimental data
getPCA_plot(principalDf, "PCA", "Grignard")
getPCA_plot(principalDf, "PCA", "Amide")
getPCA_plot(principalDf, "PCA", "C-C Heck")
getPCA_plot(principalDf, "PCA", "C-C Bayliss")
getPCA_plot(principalDf, "PCA", "Suzuki-Miyaura Pd")
getPCA_plot(principalDf, "PCA", "Buchwald-Hartwig")
getPCA_plot(principalDf, "PCA", "Alkene metathesis")
getPCA_plot(principalDf, "PCA", "Suzuki-Miyaura Ni")
getPCA_plot(principalDf, "PCA", "Alcohol oxidation")
getPCA_plot(principalDf, "PCA", "Sn2/SnAr")
getPCA_plot(principalDf, "PCA", "Ester hydrolysis")