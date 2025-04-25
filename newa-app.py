import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt





# Load data
df = pd.read_csv('Sales Dataset.csv')



import plotly.express as px





# ---------- HEATMAP SECTION ----------
st.header("U.S. Sales Quantity Heatmap")

view_all = st.checkbox("View Total Products Sold (All Categories)", value=False)

if view_all:
    # No filters applied
    state_quantity = df.groupby('State')['Quantity'].sum().reset_index()
    title = "Total Products Sold by State (All Categories)"
else:
    # Inline filter placement (not sidebar)
    col1, col2 = st.columns(2)
    with col1:
        selected_category = st.selectbox("Select Category", df['Category'].unique())
    with col2:
        subcategory_options = df[df['Category'] == selected_category]['Sub-Category'].unique()
        selected_subcategory = st.selectbox("Select Sub-Category", subcategory_options)

    filtered_df = df[(df['Category'] == selected_category) &
                     (df['Sub-Category'] == selected_subcategory)]
    state_quantity = filtered_df.groupby('State')['Quantity'].sum().reset_index()
    title = f"Quantity of {selected_subcategory} Sold by State"

# Mapping state names to abbreviations
state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY'
}

# Apply mapping
state_quantity = state_quantity[state_quantity['State'].isin(state_abbrev)]
state_quantity['State Code'] = state_quantity['State'].map(state_abbrev)

# Heatmap creation
fig2 = px.choropleth(
    state_quantity,
    locations='State Code',
    locationmode='USA-states',
    color='Quantity',
    scope='usa',
    color_continuous_scale='YlOrRd',
    title=title,
    labels={'Quantity': 'Quantity Sold'}
)

st.plotly_chart(fig2, use_container_width=True)