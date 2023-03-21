from PCA_utils.PCA_methods import perform_PCA, add_back_data
from PCA_utils.graphs import get_plain_PCA, scree_graph, loadings_graph, FG_graph, getPCA_plot, optimised_PCA_plot
from PCA_utils.reactionT import reactionT
from PCA_utils.ReactionClass import reaction_class

# get reaction class
RC, dict_desc = reaction_class()

Descriptors = dict_desc[RC]

# PCA, Mean Impute, Standardisation

# get data
data, principalDf, cum_scree, loadings = perform_PCA("solvent_exp_data.csv", Descriptors)
add_back_data(principalDf, data)

# get reaction temp- - figure out how to grey out instead of not include
T = reactionT()
principalDf = principalDf[principalDf["BP /degC"] > T]


# plot PCA graph
get_plain_PCA(principalDf)

# plot scree graph
scree_graph(cum_scree)

# plot loading graph
loadings_graph(loadings)

# plot validation graphs
# plot with functional groups highlighted
FG_graph(principalDf)

# plot optimised PCA graphs - title with user input?
optimised_PCA_plot(principalDf, "Optimised PCA")

# show plot with yield data for specified reaction class
getPCA_plot(principalDf, "PCA", RC)
