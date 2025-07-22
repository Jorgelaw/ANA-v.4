# Script de busca de similaridade
def buscar_modelos_similares(pdf_path, X, nomes):
    import PyPDF2
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import TfidfVectorizer

    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        texto = ""
        for page in reader.pages:
            texto += page.extract_text() or ""

    vetorizar = TfidfVectorizer()
    vetor_caso = vetorizar.fit_transform([texto])
    similaridades = cosine_similarity(vetor_caso, X)

    indice = similaridades.argmax()
    return {"modelos": nomes[indice], "minuta": "Conteúdo da minuta correspondente"}