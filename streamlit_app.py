import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Créer les onglets principaux
main_tab1, main_tab2, main_tab3, main_tab4 = st.tabs([
    "Présentation de l'écosystème", 
    "La SciPy Stack", 
    "Librairies de visualisation", 
    "Fichiers volumineux"
])

# ==============================
# Main Tab 1: Présentation de l'écosystème Python scientifique avec sous-onglets
# ==============================
with main_tab1:
    # Créer des sous-onglets pour l'écosystème
    sub_tab1, sub_tab2, sub_tab3 = st.tabs(["Guide", "Quiz sur venv", "Voir les réponses"])

    # ==============================
    # Sub Tab 1: Guide de l'écosystème
    # ==============================
    with sub_tab1:
        st.header("Guide de Gestion des Environnements Python avec venv")

        st.markdown("""
        Ce guide vous permettra de comprendre comment créer, gérer et utiliser des environnements virtuels Python avec `venv`, un outil intégré à Python.

        ## **Qu'est-ce qu'un environnement virtuel ?**
        Un environnement virtuel est un espace isolé où vous pouvez installer des bibliothèques spécifiques pour un projet, sans interférer avec les autres projets ou la configuration globale de Python sur votre machine.
        
        ## **Étapes pour gérer les environnements virtuels avec venv**
        - **Création d'un Environnement avec venv**
        - **Activation de l'Environnement**
        - **Installation de Bibliothèques avec pip**
        - **Utilisation du fichier requirements.txt**
        - **Désactivation de l'Environnement**
        """)

    # ==============================
    # Sub Tab 2: Quiz interactif sur venv
    # ==============================
    with sub_tab2:
        st.header("Quiz : Gestion des Environnements avec venv")
        st.markdown("Répondez aux questions suivantes pour tester vos connaissances sur `venv`.")

        # Question 1
        q1 = st.radio(
            "1. Quelle commande est utilisée pour créer un environnement virtuel avec `venv` dans un dossier appelé `mon_env` ?",
            ("A) python -m pyvenv mon_env", 
             "B) python -m venv mon_env", 
             "C) virtualenv mon_env", 
             "D) pip install venv mon_env")
        )

        # Question 2
        q2 = st.radio(
            "2. Comment activer un environnement virtuel avec `venv` sur Windows ?",
            ("A) .\\venv_env\\Scripts\\activate", 
             "B) venv_env\\bin\\activate", 
             "C) activate venv_env", 
             "D) venv start venv_env")
        )

        # Question 3
        q3 = st.radio(
            "3. Quelle est la commande pour installer des dépendances à partir d'un fichier `requirements.txt` ?",
            ("A) pip installer -r requirements.txt", 
             "B) pip install -r requirements.txt", 
             "C) conda install --file requirements.txt", 
             "D) pip get -r requirements.txt")
        )

        # Vérification des réponses
        if st.button("Vérifier mes réponses"):
            correct_answers = {
                "q1": "B) python -m venv mon_env",
                "q2": "A) .\\venv_env\\Scripts\\activate",
                "q3": "B) pip install -r requirements.txt"
            }

            user_answers = {
                "q1": q1,
                "q2": q2,
                "q3": q3
            }

            score = 0
            for question, correct in correct_answers.items():
                if user_answers[question] == correct:
                    score += 1

            st.write(f"Votre score : {score} / 3")

            if score == 3:
                st.success("Félicitations, vous avez tout juste !")
            else:
                st.warning("Vous avez fait quelques erreurs. Allez voir l'onglet des réponses pour plus de détails.")

    # ==============================
    # Sub Tab 3: Voir les réponses du quiz
    # ==============================
    with sub_tab3:
        st.header("Voir les réponses")
        st.write("""
        1. **Quelle commande est utilisée pour créer un environnement virtuel avec `venv` dans un dossier appelé `mon_env` ?**
           - Réponse correcte : **B) python -m venv mon_env**

        2. **Comment activer un environnement virtuel avec `venv` sur Windows ?**
           - Réponse correcte : **A) .\\venv_env\\Scripts\\activate**

        3. **Quelle est la commande pour installer des dépendances à partir d'un fichier `requirements.txt` ?**
           - Réponse correcte : **B) pip install -r requirements.txt**
        """)

# ==============================
# Main Tab 2: La SciPy Stack
# ==============================
with main_tab2:
    st.header("2. La SciPy Stack: le socle des librairies incontournables en analyse des données")
    st.markdown("""
    ### Les librairies fondamentales :
    - **Numpy** : Manipulation de tableaux multi-dimensionnels.
    - **Scipy** : Outils scientifiques avancés.
    - **Pandas** : Analyse et manipulation de données.
    - **Matplotlib** et **Seaborn** : Visualisation de données.
    - **Scikit-learn** : Machine Learning.
    """)

    st.subheader("TP2 : Manipulation de tableaux avec NumPy et Pandas")
    st.markdown("Voici un exemple de création et manipulation de tableaux avec NumPy :")

    # Exemple NumPy
    st.code("""
    import numpy as np

    # Créer un tableau NumPy
    tableau = np.array([1, 2, 3, 4, 5])

    # Opération : calculer la somme
    somme = np.sum(tableau)
    print("La somme du tableau est :", somme)
    """)

# ==============================
# Main Tab 3: Librairies de visualisation
# ==============================
with main_tab3:
    st.header("3. Librairies de visualisation")
    st.markdown("""
    Les principales librairies de visualisation que nous avons étudiées sont :
    - **Matplotlib** et **Seaborn** pour les visualisations statiques.
    - **Plotly** et **Bokeh** pour des visualisations interactives.
    """)

    st.subheader("Exemple : Visualisation avec Seaborn")
    st.markdown("Voici un exemple de visualisation d'une distribution de données avec **Seaborn** :")

    # Exemple Seaborn
    if st.button("Afficher la visualisation"):
        # Générer des données aléatoires
        data = np.random.randn(1000)
        sns.histplot(data, kde=True)
        plt.title("Distribution de données")
        st.pyplot(plt)

# ==============================
# Main Tab 4: Fichiers volumineux
# ==============================
with main_tab4:
    st.header("4. Formats de fichiers volumineux et leur manipulation")

    st.markdown("""
    Dans cette partie, nous avons couvert :
    - Les différents types de fichiers volumineux comme **HDF5**, **Parquet**, et **CSV**.
    - Comment manipuler ces fichiers avec **Pandas** et **Dask**.
    """)

    st.subheader("TP4 : Manipulation de fichiers volumineux")
    st.markdown("""
    Exercice pratique :
    1. Charger un fichier CSV volumineux avec Pandas.
    2. Utiliser **Dask** pour traiter un fichier Parquet trop grand pour tenir en mémoire.
    """)

    st.markdown("Voici un exemple d'utilisation de Dask pour charger un fichier volumineux :")

    st.code("""
    import dask.dataframe as dd

    # Lire un fichier CSV volumineux avec Dask
    df = dd.read_csv('path_to_large_file.csv')

    # Afficher les premières lignes
    df.head()
    """)

    # Conclusion et projet final
    st.header("Projet final :")
    st.markdown("""
    Le projet final consiste à réaliser une **étude complète** en utilisant toutes les compétences apprises :
    1. Analyse des données avec Pandas.
    2. Visualisation des résultats.
    3. Manipulation de fichiers volumineux.
    """)
