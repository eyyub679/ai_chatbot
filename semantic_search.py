import chromadb
def run_search():
    client=chromadb.Client()
    collection=client.create_collection(name="test_collection")
    collection.add(
        ids=[f"id{i}" for i in range(1,6)],
        documents=[
            "Kevin De Bruyne delivered a perfectly weighted cross into the penalty box, allowing the striker to head it home.",
            "The veteran defender made a crucial sliding tackle to stop the counter-attack.",
            "The goalkeeper was named Man of the Match after saving three penalties in the shootout.",
            "Lionel Messi controlled the ball with his chest before firing a shot into the top left corner.",
            "Despite running over 11 kilometers, the midfielder maintained a passing accuracy of 92%."
        ]
    )
    query="Strikers love to turn good crosses into brilliant goals"
    res=collection.query(
        query_texts=query,
        n_results=2
    )
    print(f"Query: {query}\n")
    print("Most Relevant Results:")
    for idx, doc in enumerate(res["documents"][0], 1):
        print(f"{idx}. {doc}")

if __name__ == "__main__":
    run_search()