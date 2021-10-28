import pandas as pd
import plotly.express as px

data = pd.read_csv("CovidCasesData.csv")
figure = px.line(data, x="date", y="cases", color="country")
figure.show()