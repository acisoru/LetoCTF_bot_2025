from Crypto.Util.number import getPrime


class SimpleLcg:
    def __init__(self, flag: bytes):
        self.a = 0x4242
        self.p = getPrime(0x400)
        self.b = getPrime(0x400)
        self.seed = int.from_bytes(flag, byteorder='big')

    def calc_state(self, n: int) -> int:
        state = self.seed
        for i in range(0x2 ** n):
            state = (state * self.a + self.b) % self.p
        return state

    def __str__(self):
        return f"{self.p, self.b = }"


def main():
    flag = ...
    lcg = SimpleLcg(flag)
    state = lcg.calc_state(0x100)
    print(lcg)
    print(f'{state = }')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
