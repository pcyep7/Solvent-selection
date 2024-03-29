from PCA_utils.PCA_methods import perform_PCA, add_back_data
from PCA_utils.graphs import scree_graph, loadings_graph, getPCA_plot, optimised_PCA_plot
from PCA_utils.reactionT import reactionT
from PCA_utils.ReactionClass import reaction_class
from PCA_utils.budget import budget

# get reaction class
RC, dict_desc, dict_ref = reaction_class()

# Set descriptors used in PCA to match reaction class user inputted
Descriptors = dict_desc[RC]

# get data
data, principalDf, cum_scree, loadings = perform_PCA("solvent_exp_data.csv", Descriptors)
add_back_data(principalDf, data)

# get reaction temp
T = reactionT()
principalDf = principalDf[principalDf["BP /degC"] > T]

# get solvent budget
C = budget()
principalDf = principalDf[principalDf["cost £/L"] < C]

# print references for chosen reaction class
print(dict_ref[RC])

# plot scree graph
scree_graph(cum_scree)

# plot loading graph
loadings_graph(loadings)

# plot optimised PCA graphs - title with user input?
optimised_PCA_plot(principalDf, RC)

# show plot with yield data for specified reaction class
getPCA_plot(principalDf, "PCA", RC)
