import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_explore_page():
    st.title("Explora sueldos de ingeniero de software")

    st.write(
        """
    ### Stack Overflow Developer Survey 2022
    """
    )


    fig1, ax1 = plt.subplots()
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Número de datos de diferentes países""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Salario promedio basado en el país
    """
    )



    st.write(
        """
    #### Salario promedio basado en la experiencia
    """
    )

