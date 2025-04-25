import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# df = pd.read_csv('great_lakes.csv')
# metrics = ['area', 'depth', 'vol', 'shoreline_ft', 'elevation_ft']

# st.title = ("Great Lakes Comparison")

# lake = st.selectbox('Select a Lake', df['lake'].unique())
# option = st.selectbox('Select a Metric', metrics)

# data = df.set_index('lake')[metrics]

# for metric in metrics:
#     fig, ax = plt.subplots()
#     colors = ['orange' if idx == lake else 'skyblue' for idx in data.index]
#     ax.bar(data.index, data[metric], color=colors)
#     ax.set_title(f"{metric.title()} Comparison")
#     ax.set_xlabel("Lake")
#     ax.set_ylabel(metric.title())
#     ax.tick_params(axis='x', rotation=45)
#     st.pyplot(fig, use_container_width=True)



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('great_lakes.csv')

# Metrics available for comparison
metrics = ['area', 'depth', 'vol', 'shoreline_ft', 'elevation_ft']

st.title("Great Lakes Comparison Dashboard")

# User selects lake and metric
selected_lake = st.selectbox("Select a Lake to Highlight", df['lake'].unique())
selected_metric = st.selectbox("Select a Metric to Compare", metrics)

# Prepare data
data = df.set_index('lake')[metrics]

# Generate a single bar chart based on selected metric
fig, ax = plt.subplots()
colors = ['orange' if lake == selected_lake else 'skyblue' for lake in data.index]
ax.bar(data.index, data[selected_metric], color=colors)
ax.set_title(f"{selected_metric.title()} of the Great Lakes")
ax.set_xlabel("Lake")
ax.set_ylabel(selected_metric.title())
ax.tick_params(axis='x', rotation=45)

# Display the chart
st.pyplot(fig, use_container_width=True)