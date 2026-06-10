from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL
from retriever import retrieve

_client = Groq(api_key=GROQ_API_KEY)

def generateAnswer(question):
    chunks = retrieve(question)
    #chunks = [c for c in chunks if c["distance"] <= 0.5]
    if not chunks:
        return{
            "answer": "Not enough information.",
            "sources": []
        }

    context = ""

    for chunk in chunks:
        context += f"\nSOURCE: {chunk['source']}\n"
        context += chunk["text"]
        context += "\n\n"

        prompt = f"""
            Answer using ONLY the provided context.

            If the answer is not contained in the context, say:
            "I don't have enough information on that."

Context:
{context}

Question:
{question}
"""

    response = _client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": "Answer only from retrieved documents."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    sources = list(set(chunk["source"] for chunk in chunks))

    return {
        "answer": answer,
        "sources": sources
    }