import pandas as pd
import plotly.figure_factory as ff



df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

k=ff.create_distplot([data]  ,["heightsplot"]  ,show_hist=False    )
k.show()