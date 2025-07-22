# Script de vetorização de modelos
def vetorizar_modelos(csv_path):
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer

    df = pd.read_csv(csv_path)
    nomes = df['nome'].tolist()
    textos = df['conteudo'].fillna("").tolist()

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)

    return X, nomes