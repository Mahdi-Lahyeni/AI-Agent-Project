
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
    question = state["question"]
    if "bonjour" in question.lower():
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
    else:
        state["type_question"] = (
    "documentation"
    )
    return state

def calculatrice_node(state):
    question = state["question"]
    resultat = calculatrice(
    question
    )
    state["reponse"] = str(
    resultat
    )
    return state

def documentation_node(state):
    state["reponse"] = (
    "Réponse documentaire"
    )
    return state
def calculatrice(expression):
    return eval(expression)
def calculatrice_node(state):
    question = state["question"]
    resultat = calculatrice(
    question
    )
    state["reponse"] = str(
    resultat
    )
    return state

def greeting_node(state):
    state["reponse"] = (
    "Bonjour ! Comment puis-je vous aider ?"
    )
    return state



def route_question(state):
    return state[
"type_question"
]



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

workflow.add_conditional_edges(
"decision",
route_question,
{
"salutation":
"salutation",
"calcul":
"calculatrice",
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


agent = workflow.compile()

resultat = agent.invoke(
{
"question":
"5//5 "
}
)

print(
resultat["reponse"]
)


