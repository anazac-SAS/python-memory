import random

def generate_numbers():
    numbers = list(range(1, 13))
    random.shuffle(numbers)
    return numbers

def play_memory():
    numbers = generate_numbers()
    print('Kom ihåg ordningen på siffrorna: ')
    print(numbers)
    
    input('Tryck Enter för att fortsätta')

    shuffled = numbers[:]
    random.shuffle(shuffled)
    print('Nu är ordningen omblandad: ')
    print(shuffled)

    while True:
        guess = input('Skriv in siffrorna i rätt ordning, separerade med mellanslag: ')
        guess_list = [int(x) for x in guess.split()]

        if guess_list == numbers:
            print('Rätt! Bra memorerat')
            break
        else:
            print('Testa igen')

play_memory()
