import plotly.express as px
import pandas as pd
import numpy as np

config = {
  'toImageButtonOptions': {
    'format': 'svg', # one of png, svg, jpeg, webp
    'filename': 'custom_image',
    'height': 400,
    'width': 600,
    'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
  }
}

def get_plain_PCA(principalDf):
    fig = px.scatter(principalDf, x="PC1", y="PC2", hover_name="Solvent", hover_data={"PC1":False,"PC2":False},
                     title="PCA First Two PCs")
    fig.update_traces(marker=dict(size=12,
                                  opacity=0.6),
                      selector=dict(mode='markers'))
    fig.update_layout(
        font=dict(
            family="Calibri",
            size=14,
        )
    )
    fig.show(config=config)
    
def scree_graph(cum_scree):
    # round cum_scree data
    cum_scree = [round(x, 2) for x in cum_scree]
    # prepare data to plot scree plot
    df_data = np.array([np.arange(1, len(cum_scree) + 1), cum_scree]).transpose()
    cum_scree_df = pd.DataFrame(df_data, columns=["Component", "Variance"])
    # make bar chart
    fig = px.bar(cum_scree_df, x='Component', y='Variance', title="Cumulative Variance by Successive PCs",
                 hover_name="Variance", hover_data={"Component": False, "Variance": False}, height=600, width=700)
    fig.update_xaxes(dtick=1)
    fig.update_yaxes(range=[0, 100])
    fig.update_layout(
        font=dict(
            family="Calibri",
            size=14,
        )
    )
    fig.show(config=config)
    
def loadings_graph(loadings_df):
    # make loadings scatter chart
    fig = px.scatter(loadings_df, x='PC1', y='PC2', title="Loading of Descriptors in First Two PCs",
                     hover_name="Descriptor")
    fig.update_traces(marker=dict(size=12,
                                  opacity=0.6),
                  selector=dict(mode='markers'))
    fig.update_layout(
        font=dict(
            family="Calibri",
            size=14,
        )
    )
    fig.show(config=config)
    
def FG_graph(principalDf):
    fig = px.scatter(principalDf, x="PC1", y="PC2", color="Functional Group",
                     color_discrete_sequence=px.colors.qualitative.G10, hover_name="Solvent", 
                     hover_data={"PC1":False,"PC2":False})
    fig.update_traces(marker=dict(size=12,
                                  opacity=0.6),
                      selector=dict(mode='markers'))
    fig.update_layout(
        font=dict(
            family="Calibri",
            size=14,
        )
    )
    fig.show(config=config)
    

def getPCA_plot(Data,title,colour_by):
    fig = px.scatter(Data, x='PC1', y='PC2', title=title, hover_name="Solvent", hover_data={"PC1":False,"PC2":False},
                     color=colour_by, color_continuous_scale='Bluered_r')
    fig.update_traces(marker=dict(size=12,
                                  opacity=0.6),
                  selector=dict(mode='markers'))
    fig.update_layout(
        font=dict(
            family="Calibri",
            size=14,
        )
    )
    fig.show(config=config)

def optimised_PCA_plot(Data,title):
    fig = px.scatter(Data, x='PC1', y='PC2', title=title, hover_name="Solvent", hover_data={"PC1":False,"PC2":False, "cost £/L":True},
                     color="CHEM21 (0=bad, 0.5=acceptable, 1=good)", color_continuous_scale=[(0, "red"), (0.5, "orange"), (1, "green")])
    fig.update_traces(marker=dict(size=12,
                                  opacity=0.8),
                  selector=dict(mode='markers'))
    fig.update_layout(
        font=dict(
            family="Calibri",
            size=14,
        )
    )
    fig.show(config=config)