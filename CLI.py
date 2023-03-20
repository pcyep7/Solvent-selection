from PCA_utils.PCA_methods import perform_PCA, add_back_data
from PCA_utils.graphs import get_plain_PCA, scree_graph, loadings_graph, FG_graph, getPCA_plot
from PCA_utils.reactionT import reactionT
from PCA_utils.budget import budget

Descriptors= ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"]


dict_desc = {
    "Grignard": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
    "Alkene metathesis": ["Alpha", "Beta", "H Bonding", "Dispersion"],
    "Heck C-C": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
    "Buchwald-Hartwig": ["Dipole moment (D)", "Dielectric constant", "Alpha",
              "Pi", "Polarity", "H Bonding"],
    "SN2/SNAr": ["Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Polarity", "H Bonding"],
    "Amide Coupling": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
    "Suzuki-Miyaura": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
    "Alcohol Oxidation": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
    "Baylis-Hillman": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
    "Ester Hydrolysis": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"],
    "Other": ["Molecular Weight", "BP /degC", "Density g/cm3", "Viscosity /cP", "Vapour Pressure /mmHg",
              "Refractive index", "logP", "Dipole moment (D)", "Dielectric constant", "Alpha", "Beta",
              "Pi", "Dispersion", "Polarity", "H Bonding", "Molar Vol"]
}

#print(dict_desc["one"])
chosen_user_input = input("Choose reaction class: Grignard, Alkene metathesis, Heck C-C, Buchwald-Hartwig, SN2/SNAr, "
                          "Amide Coupling, Suzuki-Miyaura, Alcohol Oxidation, Baylis-Hillman, Ester Hydrolysis, Other")
print(dict_desc[chosen_user_input])
exit()

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
getPCA_plot(principalDf, "PCA", "C-C Baylis")
getPCA_plot(principalDf, "PCA", "Suzuki-Miyaura Pd")
getPCA_plot(principalDf, "PCA", "Buchwald-Hartwig")
getPCA_plot(principalDf, "PCA", "Alkene metathesis")
getPCA_plot(principalDf, "PCA", "Suzuki-Miyaura Ni")
getPCA_plot(principalDf, "PCA", "Alcohol oxidation")
getPCA_plot(principalDf, "PCA", "Sn2/SnAr")
getPCA_plot(principalDf, "PCA", "Ester hydrolysis")