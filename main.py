from logicengine import Carta

def main():
    cartaA = Carta(1, "Carta A", 10, 5, 3, 2, [1, 0, 0, 0])
    cartaB = Carta(2, "Carta B", 8, 7, 4, 1, [0, 1, 0, 0])

    print(cartaA)  # Output: (1) Carta A (AP: 10, AT: 5, PD: 3, MD: 2, Flechas: [1, 0, 0, 0])
    print(cartaB)  # Output: (2) Carta B (AP: 8, AT: 7, PD: 4, MD: 1, Flechas: [0, 1, 0, 0])

if __name__ == "__main__":
    main()