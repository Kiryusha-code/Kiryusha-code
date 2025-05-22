class Clock:
    DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.DAY

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return False
        return self.seconds == other.seconds

    def __hash__(self):
        return hash(self.seconds)


class Fraction:
    def __init__(self, numerator, denominator=1):
        if not all(isinstance(x, int) for x in (numerator, denominator)):
            raise TypeError("Числитель и знаменатель должны быть целыми числами")
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулем")
        
        # Приводим дробь к простейшему виду
        gcd_value = self._gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd_value
        self.denominator = denominator // gcd_value

    @staticmethod
    def _gcd(a, b):
        """Вычисление наибольшего общего делителя"""
        while b:
            a, b = b, a % b
        return a

    # Операции сравнения
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return (self.numerator == other.numerator and 
                self.denominator == other.denominator)

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator * other.denominator < 
                other.numerator * self.denominator)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __hash__(self):
        return hash((self.numerator, self.denominator))

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Проверка работы Clock
c1 = Clock(1000)
c2 = Clock(1000)
print(c1 == c2)  # True
print(hash(c1) == hash(c2))  # True

# Проверка работы Fraction
f1 = Fraction(2, 4)
f2 = Fraction(1, 2)
f3 = Fraction(3, 4)

print(f1 == f2)  # True (2/4 == 1/2)
print(f1 < f3)   # True (1/2 < 3/4)
print(f3 > f2)   # True (3/4 > 1/2)
print(hash(f1) == hash(f2))  # True
