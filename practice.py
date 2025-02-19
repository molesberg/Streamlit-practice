import numpy as np
import streamlit as st
import pytest
import requests
import pylint

st.title("Completely arbitrary data")

mySeed = st.slider('Generate Seed', 0, 100, 42)

def func(mySeed):
    np.random.seed(mySeed)
    array = np.random.rand(10, 10)
    maxColumn = np.argmax(np.sum(array, axis = 0))
    minColumn = np.argmin(np.sum(array, axis = 0))
    return array, maxColumn, minColumn

array, maxColumn, minColumn = func(mySeed)
st.subheader('Raw Data')
st.write(array)

st.text(f'Max Column: {maxColumn}. Min Column: {minColumn}')
st.success(f'Sum of max column > Sum of min column: {np.sum(array[:, maxColumn])} > {np.sum(array[:, minColumn])}')
st.error(f'Sum of max column < Sum of min column: {np.sum(array[:, maxColumn])} < {np.sum(array[:, minColumn])}')

