class Numbers:
    def print_numbers(self):
        numbers = list(range(1, 8))
        for n in numbers:
            print(n)
            if n == 5:
                break
numbers = Numbers() #объект создается обязательно, чтобы вызвать метод print_
numbers.print_numbers()
