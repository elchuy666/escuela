entrada = input("escribe una letra. ").lower()
vocales = "aeiou"

if entrada in vocales:
    print("vocal")
else:
    print("consonante")