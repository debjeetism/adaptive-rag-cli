from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from model import llm_model

class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "websearch", "llm_fallback"] = Field(
        ...,
        description=(
            "Given a user question, choose to route it to either 'vectorstore' (for "
            "domain-specific/document questions), 'websearch' (for recent/current events or "
            "open web information), or 'llm_fallback' (for general chit-chat, greetings, "
            "or questions outside the other two categories)."
        )
    )

llm = llm_model

structured_llm_router = llm.with_structured_output(RouteQuery)

system = """
You are an expert at routing user questions to vectorstore, websearch, or llm_fallback.
- Use **vectorstore** for questions about agents, prompt engineering, adversarial attacks, or any topics specifically covered in the stored documents.
- Use **websearch** if the user needs very recent, newsworthy, or open web information (facts/events not in your stored documents).
- Use **llm_fallback** for general conversation, greetings, or queries outside the scope of stored documents and open web searches—for example, jokes, chit-chat, or very broad/general info needs.
Choose one route ONLY for each question.
"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router