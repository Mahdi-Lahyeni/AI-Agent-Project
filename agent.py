from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

class AgentState(TypedDict):
    question: str
    reponse: str
    type_question: str

def analyse_node(state):
    print("Analyse de la question...")
    return state

def reponse_node(state):
    question = state["question"]
    state["reponse"] = (
    f"Votre question est : {question}"
    )
    return state


def decision_node(state):
    question = state[
    "question"
    ].lower()
    if "bonjour" in question:
        state["type_question"] = (
    "salutation"
    )
    elif (
    "+" in question
    or "-" in question
    or "*" in question
    or "/" in question
    ):

        state["type_question"] = (
    "calcul"
    )
    elif "lis" in question:
        state["type_question"] = (
    "lecture"
    )
    else:
        state["type_question"] = (
    "documentation"
    )
    return state

def calculatrice_node(state):
    state["reponse"] = (
    "Résultat du calcul"
    )
    return state

def documentation_node(state):
    state["reponse"] = (
    "Réponse documentaire"
    )
    return state


def greeting_node(state):
    state["reponse"] = (
    "Bonjour ! Comment puis-je vous aider ?"
    )
    return state

def txt_reader(chemin_fichier):
    with open(
    chemin_fichier,
    "r",
    encoding="utf-8"
    ) as fichier:
        contenu = fichier.read()
    return contenu

def route_question(state):
    return state[
"type_question"
]

def txt_reader_node(state):
    contenu = txt_reader(
    "documents/rh.txt"
    )
    state["reponse"] = contenu
    return state

workflow = StateGraph(
    AgentState
    )

workflow.add_node(
    "analyse",
    analyse_node
)

workflow.add_node(
    "reponse",
    reponse_node
    )

workflow.add_node(
"salutation",
greeting_node
)

workflow.add_node(
"decision",
decision_node
)
workflow.add_node(
"calculatrice",
calculatrice_node
)
workflow.add_node(
"documentation",
documentation_node
)



workflow.add_node(
"txt_reader",
txt_reader_node
)




workflow.add_conditional_edges(
"decision",
route_question,
{
"calcul":
"calculatrice",
"lecture":
"txt_reader",
"documentation":
"documentation"
}
)

workflow.set_entry_point(
    "analyse"
)

workflow.add_edge(
    "analyse",
    "decision"
)

workflow.add_edge(
    "documentation",
    END
)

workflow.add_edge(
    "calculatrice",
    END
)


workflow.add_edge(
"salutation",
END
)

workflow.add_edge(
"txt_reader",
END
)

agent = workflow.compile()

resultat = agent.invoke(
{
"question":
"Lis le fichier RH ?"
}
)
print(
txt_reader("documents/rh.txt")
)
print(resultat)