import pandas as pd

from src.embeddings import (
    generate_embeddings,
    model
)

from src.retriever import Retriever

from src.analytics import (
    analytics_query
)

from src.llm import (
    generate_answer
)

df = pd.read_csv(
    "C:\\Users\\gva\\Desktop\\QA-System\\data\\organizations.csv"
)

documents = []

for _, row in df.iterrows():

    text = f"""
Organization Name:
{row['org_name']}

Location:
{row['location']}

Employees:
{row['employees']}

Revenue:
{row['revenue']} crore

"""

    documents.append(text)

embeddings = generate_embeddings(
    documents
)

retriever = Retriever(
    embeddings
)

print("System Ready")

while True:

    question = input(
        "\nAsk Question: "
    )

    if question.lower() == "exit":
        break

    result = analytics_query(
        question,
        df
    )

    if result:
        print("\nAnswer:")
        print(result)
        continue

    query_embedding = model.encode(
        [question]
    )

    indices = retriever.search(
        query_embedding
    )

    context = ""

    for idx in indices:
        context += (
            documents[idx]
            + "\n"
        )

    answer = generate_answer(
        question,
        context
    )

    print("\nAnswer:")
    print(answer)