greeting = input("Greeting: ").strip()

lowercase_greeting = greeting.lower()

if lowercase_greeting.startswith("hello"):
    print("$0")
elif lowercase_greeting[0] == "h":
    print("$20")
else:
    print("$100")