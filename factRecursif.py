def factRecursif(n) :
    if n == 0:
        return 1;
    else:
        return n * factRecursif(n - 1);




# Exemple d'utilisation
if __name__ == "__main__":
    print(factRecursif(4))