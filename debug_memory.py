import chromadb
import os

def check_memory():
    db_path = "backend/data/chroma"
    if not os.path.exists(db_path):
        print(f"Database path {db_path} does not exist.")
        return

    try:
        client = chromadb.PersistentClient(path=db_path)
        print("Collections:", client.list_collections())
        
        collection = client.get_collection("health_episodes")
        count = collection.count()
        print(f"Collection 'health_episodes' has {count} items.")
        
        if count > 0:
            peek = collection.peek(limit=5)
            print("Peek IDs:", peek['ids'])
            print("Peek Metadatas:", peek['metadatas'])
    except Exception as e:
        print(f"Error inspecting ChromaDB: {e}")

if __name__ == "__main__":
    check_memory()
