from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def accueil():
    return {"message": "Bienvenue dans l'Agent IA"}


@app.get("/bonjour")
def bonjour():
    return {"message": "Bonjour"}


@app.get("/status")
def status():
    return {"status": "OK"}


@app.get("/info")
def info():
    return {"application": "Agent IA", "version": "1.0"}


@app.get("/utilisateur/{nom}")
def utilisateur(nom):
    return {"message": f"Bonjour {nom}"}