gyujtes = input("Mire gyűjti Anna a pénzt?")
hanyKutya = int(input("Hány kutyát sétáltat a hétvégén?"))
ido = hanyKutya*20
if hanyKutya*700 < 5000:
    print(f"Anna {hanyKutya} kutyát sétáltatott {ido/60} óra alatt, ezért {hanyKutya*700} Ft-ot kapott és ez nem elegendő egy {gyujtes}(-ra/re).")
else:
    print(f"Anna {hanyKutya} kutyát sétáltatott {ido/60} óra alatt, ezért {hanyKutya*700} Ft-ot kapott és ez elegendő egy {gyujtes}(-ra/re).")




























def main():
    pass
main()