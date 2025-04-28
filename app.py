import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('Sales Dataset.csv')

# State abbreviations
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

# ---------- U.S. Sales Heatmaps (ONLY) ----------
st.header("U.S. Sales Heatmaps")

# Create two tabs: one for Quantity, one for Profit
tab1, tab2 = st.tabs([" Quantity Sold", " Profit"])

# ------------ TAB 1: Quantity Heatmap ------------
with tab1:
    st.subheader("Total Products Sold by State")

    view_all_qty = st.checkbox("View All Categories (Quantity)", key="qty_all")

    if view_all_qty:
        qty_df = df.groupby('State')['Quantity'].sum().reset_index()
        title_qty = "Total Quantity Sold by State (All Categories)"
    else:
        col1, col2 = st.columns(2)
        with col1:
            selected_cat_qty = st.selectbox("Select Category", df['Category'].unique(), key="qty_cat")
        with col2:
            subcats_qty = df[df['Category'] == selected_cat_qty]['Sub-Category'].unique()
            selected_subcat_qty = st.selectbox("Select Sub-Category", subcats_qty, key="qty_sub")

        filtered_qty = df[(df['Category'] == selected_cat_qty) &
                          (df['Sub-Category'] == selected_subcat_qty)]
        qty_df = filtered_qty.groupby('State')['Quantity'].sum().reset_index()
        title_qty = f"Quantity of {selected_subcat_qty} Sold by State"

    qty_df = qty_df[qty_df['State'].isin(state_abbrev)]
    qty_df['State Code'] = qty_df['State'].map(state_abbrev)

    fig_qty = px.choropleth(
        qty_df,
        locations='State Code',
        locationmode='USA-states',
        color='Quantity',
        scope='usa',
        color_continuous_scale='YlGnBu',
        title=title_qty,
        labels={'Quantity': 'Quantity Sold'}
    )
    st.plotly_chart(fig_qty, use_container_width=True)

# ------------ TAB 2: Profit Heatmap ------------
with tab2:
    st.subheader("Total Profit by State")

    view_all_profit = st.checkbox("View All Categories (Profit)", key="profit_all")

    if view_all_profit:
        profit_df = df.groupby('State')['Profit'].sum().reset_index()
        title_profit = "Total Profit by State (All Categories)"
    else:
        col3, col4 = st.columns(2)
        with col3:
            selected_cat_profit = st.selectbox("Select Category", df['Category'].unique(), key="profit_cat")
        with col4:
            subcats_profit = df[df['Category'] == selected_cat_profit]['Sub-Category'].unique()
            selected_subcat_profit = st.selectbox("Select Sub-Category", subcats_profit, key="profit_sub")

        filtered_profit = df[(df['Category'] == selected_cat_profit) &
                             (df['Sub-Category'] == selected_subcat_profit)]
        profit_df = filtered_profit.groupby('State')['Profit'].sum().reset_index()
        title_profit = f"Profit from {selected_subcat_profit} by State"

    profit_df = profit_df[profit_df['State'].isin(state_abbrev)]
    profit_df['State Code'] = profit_df['State'].map(state_abbrev)

    fig_profit = px.choropleth(
        profit_df,
        locations='State Code',
        locationmode='USA-states',
        color='Profit',
        scope='usa',
        color_continuous_scale='YlOrRd',
        title=title_profit,
        labels={'Profit': 'Total Profit'}
    )
    st.plotly_chart(fig_profit, use_container_width=True)
