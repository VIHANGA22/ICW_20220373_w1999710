import pandas as pd
import streamlit as st
import plotly.express as px
# Setting page configuration
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)
# Custom CSS to style the dashboard
st.markdown(
    """
    <style>
        /* Center align the main header and subheader */
        .center {
            text-align: center;
        }
        
        /* Ad padding to the bordered container */
        .bordered {
            b

