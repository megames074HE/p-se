from colorama import Fore, Style

run = True
print(Fore.BLUE, 'vällkommen till påsen 💰', Style.RESET_ALL)
bag = []

while run:
    print(Fore.YELLOW, '\nVisa innehållet i påsen  [V]')
    print('Spara i påsen [S]')
    print('Ta bort nåt ur påsen [D]')
    print('Sök nåt i påsen och ändra/ta bort den [F]')
    print('Avsluta [Q]', Style.RESET_ALL)
    choice = input('\nVälj: ').lower()
    if choice == 'q':
        run = False
    elif choice == 'v':
        if len(bag) == 0:
            print(Fore.RED, '\nJodu det verkar lite tomt här. Testa adda grejer till påsen', Style.RESET_ALL)
        else:
            bag_sorted = sorted(bag)
            for thing in bag_sorted:
                print(Fore.GREEN, thing, Style.RESET_ALL)
    elif choice == 's':
        
        if len(bag) > 10:
            print(Fore.RED, '\nDu har inte en sånt stor påse', Style.RESET_ALL)
        else:
            bag.append(input('\nskriv vad du vill spara: ').lower())
            print(Fore.GREEN, f'\ndu har {10 - len(bag)} platser kvar', Style.RESET_ALL)
    elif choice == 'f':
        query = input('\nVad vill du söka efter: ')
        if query.lower() in bag:
            print(Fore.GREEN, f'\nHittade: "{query}" in bag', Style.RESET_ALL)
            choice = input(f'Vill du ta bort eller ändra {query}? [D]/[C]/[NEJ] ').lower()
            
            if choice == 'd':
                bag.remove(query)
                print(Fore.GREEN, 'Den blev bortagen', Style.RESET_ALL)
            elif choice == 'c':
                new_query = input(f'Till vad vill du ändra {query}? ').lower()
                bag.remove(query)
                bag.append(new_query)
                print(Fore.GREEN, 'Den har ändrats nu!', Style.RESET_ALL)

        
    elif choice == 'd':
        for thing in bag:
            print(thing)
        try:
            bag.remove(input('\nskriv vad du vill ta bort: ').lower())
            print(Fore.GREEN, 'Den blev bortagen', Style.RESET_ALL)
        except ValueError:
            print(Fore.RED, '\nNaah den finns inte i listan testa igen.', Style.RESET_ALL)
    else:
        print(Fore.RED, '\nFel kommando, testa igen', Style.RESET_ALL)
    