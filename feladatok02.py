lista = []
with open("kutyusok.txt", encoding="UTF-8") as f:
    for i in f:
        sor = i.strip()
        lista.append(sor.capitalize())
print(f"A listában {len(lista)} darab elem szerepel.")
print("Kutyanevek amik i betűre végződnek:")
for i in lista:
    if i[-1] == "i":
        print(i)
with open("kutyusok_nagy.txt", "w", encoding="UTF-8")as f:
    for i in lista:
        f.write(i)
        f.write("\n")


