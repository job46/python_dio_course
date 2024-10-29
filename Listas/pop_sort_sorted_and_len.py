linguagens = ["Python", "Java", "C", "C#"]

# linguagens.extend(["Php", "Js"])

# linguagens.pop()
# linguagens.sort(reverse =True)

# linguagens.sort(key=lambda x: len(x), reverse = True)

linguagens.sort(key=lambda x: len(x))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))