def converter():
    phrase = str(input("input phrase"))
    phrase.lower()
    output = phrase.replace(" ", "_")
    print(output)


converter()
