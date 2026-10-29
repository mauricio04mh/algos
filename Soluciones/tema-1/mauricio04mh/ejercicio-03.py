"""Ejercicio 3. Pila con mínimo en O(1)."""
import random


class PilaMin:
    def __init__(self):
        self.v = []      # valores
        self.m = []      # m[i] = mínimo de v[0..i]
        self.operaciones = 0

    def push(self, x):
        self.v.append(x)
        self.m.append(x if not self.m else min(x, self.m[-1]))
        self.operaciones += 3          # comparación + dos append

    def pop(self):
        self.m.pop()
        self.operaciones += 2
        return self.v.pop()

    def minimo(self):
        self.operaciones += 1
        return self.m[-1]

    def invariante(self):
        return (len(self.v) == len(self.m) and
                all(self.m[i] == min(self.v[:i + 1]) for i in range(len(self.v))))


if __name__ == "__main__":
    # Ejemplo del enunciado
    p = PilaMin()
    for x in [5, 2, 7, 2]:
        p.push(x)
    print("v =", p.v, " m =", p.m, " minimo() =", p.minimo())
    for _ in range(3):
        p.pop()
    print("tras tres pop: v =", p.v, " m =", p.m, " minimo() =", p.minimo())

    # Prueba aleatoria contra una pila ingenua, con el invariante vigilado
    random.seed(3)
    pasos, malos = 0, 0
    for _ in range(2000):
        p, ref = PilaMin(), []
        for _ in range(random.randint(1, 40)):
            if ref and random.random() < 0.4:
                assert p.pop() == ref.pop()
            else:
                x = random.randint(-20, 20)
                p.push(x)
                ref.append(x)
            assert p.invariante()
            if ref:
                malos += p.minimo() != min(ref)
            pasos += 1
    print(f"operaciones comprobadas: {pasos}, respuestas incorrectas de minimo(): {malos}")

    # Costo: operaciones elementales por operación, no depende del tamaño
    for n in [10, 1_000, 100_000]:
        p = PilaMin()
        for i in range(n):
            p.push(i)
        antes = p.operaciones
        p.minimo()
        print(f"n = {n:>7}: minimo() cuesta {p.operaciones - antes} operación elemental")
