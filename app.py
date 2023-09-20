# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to generate random data (simulate some computational workload)
@st.cache_data
def generate_random_data(n_rows=100):
    return pd.DataFrame({
        'A': np.random.rand(n_rows),
        'B': np.random.randn(n_rows)
    })

# Main app
def main():
    st.title("Streamlit Showcase App")

    st.markdown("### Introduction")
    st.write("This app showcases some of Streamlit's abilities, including widgets, caching, displaying data, and plotting graphs.")

    st.markdown("### Generate Random Data")
    n_rows = st.slider("Select the number of rows:", min_value=10, max_value=1000, value=100, step=10)
    data = generate_random_data(n_rows)
    
    st.markdown("### Display Data")
    if st.checkbox("Show data"):
        st.dataframe(data)

    st.markdown("### Visualize Data")
    plot_choice = st.selectbox("Choose a type of plot:", ["Line", "Scatter"])
    
    fig, ax = plt.subplots()
    
    if plot_choice == "Line":
        ax.plot(data.index, data['A'], label='Column A')
        ax.plot(data.index, data['B'], label='Column B')
    elif plot_choice == "Scatter":
        ax.scatter(data.index, data['A'], label='Column A')
        ax.scatter(data.index, data['B'], label='Column B')
    
    ax.legend()
    st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    main()
