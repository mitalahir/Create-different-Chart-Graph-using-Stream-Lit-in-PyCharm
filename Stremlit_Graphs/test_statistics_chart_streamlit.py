import time
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_data = load_iris()

data = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
fig = plt.figure()
sns.histplot(data=data, bins=20)
st.pyplot(fig)

fig = plt.figure()
sns.boxplot(data=data)
st.pyplot(fig)

fig = plt.figure()
sns.scatterplot(data=data)
st.pyplot(fig)

rows = np.random.randn(1, 1)
chart = st.line_chart(rows)

'Growing Line Chart:'
for i in range(1, 100):
    new_rows = rows[0] + np.random.randn(1, 1)
    chart.add_rows(new_rows)
    rows = new_rows
    time.sleep(0.05)

values = np.random.rand(10)
'Maxplotlibs Line Chart:'
fig, ax = plt.subplots()
ax.plot(values)
st.pyplot(fig)

animals = ['Cat', 'Cow', 'Dog']
heights = [30, 150, 80]
'Pie Charts:'
fig, ax = plt.subplots()
ax.pie(heights, labels=animals)
st.pyplot(fig)


col_names = ['column1', 'column2', 'column3']
data = pd.DataFrame(np.random.randint(30, size=(30, 3)), columns=col_names)
'Line Graph:'
st.line_chart(data)

'Bar Graph:'
st.bar_chart(data)


