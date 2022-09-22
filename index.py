from altair.vegalite.v4.api import Chart
from altair.vegalite.v4.schema.channels import Tooltip
from altair.vegalite.v4.schema.core import LayoutAlign
from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
import js2py

from google.cloud import firestore

db = firestore.Client()

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import csv

# from plotly import graph_objs as go
import altair as alt
from streamlit_webrtc import webrtc_streamer


st.sidebar.header("Navigation")
rad = st.sidebar.radio("Choose: ", ["Client Side", "Database"])


if rad == "Client Side":
    st.title("Client")
    st.header("Live Video")
    webrtc_streamer(key="sample")

if rad == "Database":
    st.title("Backend")
    st.table()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .h{
                color:red;
                # padding:0px;
                margin:0px
                
            }
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# webrtc_streamer(key="example")
# st.header("OUTPUT")
# header = ["Car number", "Timestamp"]
# data = ["MH 09 RT 2536", "56:34578:434"]

# with open("LPlate.csv", "w", encoding="UTF8") as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)
# st.text(data)
