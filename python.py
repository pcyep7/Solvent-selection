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
df=pd.read_csv("solvent_exp_data.csv")
fig=px.scatter(df, x="Polarity", y="Dipole moment (D)")
fig.update_traces(marker=dict(size=12,
                              opacity=0.6),
                  selector=dict(mode='markers'))
fig.update_layout(
        font=dict(
            family="Arial",
            size=14,
        )
    )
fig.update_xaxes(title_font_family="Arial")
fig.show(config=config)