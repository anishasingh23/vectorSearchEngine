from search_engine import search

print("🔍 Welcome to AnishaSearchEngine!")
query = input("Enter your query: ")

results = search(query)

print("\nTop results:\n")
for result in results:
    print(f"📄 ID: {result['id']}")
    print(f"📌 Title: {result['title']}")
    print(f"📝 Content: {result['content'][:200]}...\n")
