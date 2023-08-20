import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import json

df = pd.read_csv("HIST_PAINEL_COVIDBR_2021_Parte2_18ago2023.csv",sep=";")
df_states = df[~df['estado'].isna() & (df['codmun'].isna())]
df_brasil = df[df['regiao']=='Brasil']
df_brasil