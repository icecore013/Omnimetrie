import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show


df = pd.read_csv('./streamlit/data.csv')
x = df["tensiometre"]
y = df["lse_humidite"]

print(df.corr())


sns.set_theme()

print(sns.lineplot(x="tensiometre", y="lse_humidite", data=df))

p = figure()
r = p.vbar(x=x, top=y, width=0.9)
h = Hovertool(renderers = [r],
              tooltips = [("(x,y)","($x,$y)")])

p.add_tools(h)
st.bokeh_chart(p, use_container_width=True)
