import maria as M
import irene as I 

def main():
    a = 1
    b = 2
    c = M.sumaA(a,b)
    print(f"El resultado de la suma de a y b es {c}")

    d = I.resta(a, b)
    print(f"El valor de la resta de a y b es: {d}")

if __name__ == "__main__":
    main() 
