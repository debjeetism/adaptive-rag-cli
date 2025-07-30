from model import llm_model

def llm_fallback(state):
    question = state.get("question")
    # print("[llm_fallback] Received question:", question)
    try:
        response = llm_model.invoke(question)
        # Most LLMs return a ChatMessage with .content
        answer = getattr(response, "content", str(response))
        # print("[llm_fallback] LLM content answer:", answer)
        state["generation"] = answer
        return state
    except Exception as e:
        print("[llm_fallback] Error:", e)
        state["generation"] = f"Sorry, there was an error: {e}"
        return state