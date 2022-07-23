import streamlit as st
import pickle
import numpy as np


def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### Necesitamos información para predecir el salario""")

    countries = (
        "Estados Unidos",
        "India",
        "Inglaterra",
        "Perú",
        "Alemania",
        "Canada",
        "Brazil",
        "Francia",
        "España",
        "Australia",
        "Holanda",
        "Polonoa",
        "Italia",
        "Rusia",
        "Suecia",
    )

    education = (
        "Bachiller",
        "Licenciatura",
        "Maestría",
        "Postgrado",
    )

    country = st.selectbox("País", countries)
    education = st.selectbox("Nivel de educación", education)

    expericence = st.slider("Años de experiencia", 0, 50, 3)

    ok = st.button("Calcular salario")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"El salario estimado es ${salary[0]:.2f}")