
class Coffee:
    @staticmethod
    def is_hot(temperature):
        return temperature > 50

print(f"Acesso a método de classe {Coffee.is_hot(49)}")
