import requests


def poser_question(modele, prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": modele, "prompt": prompt, "stream": False}
    response = requests.post(url, json=data)
    return response.json()["response"]


print(poser_question("gemma3", "Explique le RAG."))
