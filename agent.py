from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

class AgentState(TypedDict):
    question: str
    reponse: str

def analyse_node(state):
    print("Analyse de la question...")
    return state

def reponse_node(state):
    question = state["question"]
    state["reponse"] = (
    f"Votre question est : {question}"
    )
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

workflow.set_entry_point(
    "analyse"
)

workflow.add_edge(
    "analyse",
    "reponse"
)

workflow.add_edge(
    "reponse",
    END
)

agent = workflow.compile()

resultat = agent.invoke(
    {
        "question": "Quels sont les congés annuels ?"
    }
)

print(resultat)