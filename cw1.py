# Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia, oraz nazwisko, a następnie zwróci te wartości połączone kropką. Przykładowe wyjście: J. Kowalski.
def zad1(first_name_letter, surname):
    return first_name_letter + '. ' + surname


# Przygotować funkcję, która przyjmie w parametrach imię i nazwisko, oraz zwróci pierwszą literę imienia i nazwisko połączone kropką. Funkcja powinna również dbać o poprawność wielkich liter.
# Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.
def zad2(name, surname):
    return "{}. {}".format(name[0:1].upper(), surname.capitalize())


# Przygotować funkcję, która przyjmie 3 argumenty: 2 pierwsze cyfry aktualnego roku, 2 ostatnie cyfry aktualnego roku, wiek użytkownika, a następnie zwróci jego rok urodzenia.
def zad3(two_first_year_number, two_last_year_number, age):
    return int(str(two_first_year_number) + str(two_last_year_number)) - age


# Przygotować funkcję, która przyjmie 3 parametry: imię, nazwisko i funkcję przetwarzającą te dane, a następnie zwróci wynik działania funkcji przyjętej w 3. parametrze.
# Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2), wyjście: J. Kowalski.
def zad4(name, surname, function):
    return function(name, surname)


# Przygotować funkcję, która przyjmie 2 argumenty, a następnie zwróci wynik ich dzielenia. Należy sprawdzić w jednej instrukcji if (bez użycia elif i else),
# czy obydwie liczby są dodatnie oraz czy druga liczba jest różna od 0.
def zad5(number_1, number_2):
    if number_1 > 0 and number_2 > 0 and number_2 != 0:
        return number_1 / number_2

    return "Nieprawidłowe dane."


# Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby w pętli, dopóki suma wszystkich podanych do tej pory liczb nie osiągnie wartości 100.
def zad6():
    suma = 0
    while suma < 100:
        a = input("Wprowadź wartość:")
        suma += int(a)


# Przygotować funkcję, która przyjmie 1 argument w postaci listy, a następnie zwróci te elementy w postaci krotki.
def zad7(input_list):
    return tuple(input_list)


# Przygotować skrypt, w którym użytkownik będzie wprowadzał do listy wartości używając pętli, a następnie wartości z tej zostanią zrzutowane do krotki.
def zad8():
    l = list()
    for i in range(10):
        a = input("Wprowadź wartość:")

        l.append(int(a))

    l = tuple(l)
    print(l)


# Przygotować funkcję, która przyjmie 1 argument całkowitoliczbowy, a następnie zwróci nazwę dnia tygodnia odpowiadającą przekazanemu argumentowi.
# Nie należy w tym zadaniu używać instrukcji warunkowych! Przykładowo, wejście: 6, wyjście: sobota.
def zad9(number):
    week_name = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

    return week_name[number - 1]


# Przygotować funkcję, która przyjmie argument w postaci łańcucha znaków, a następnie zwróci wartość logiczną informującą o tym czy przekazany tekst jest palindromem.
def zad10(string):
    return string == string[::-1]

print(zad10("test"))