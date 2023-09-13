Player1 = input("Введите значение: ")
Player2 = input("Введите значение: ")

Winner = None

choices = {"Камень": "Ножницы", "Ножницы": "Бумага", "Бумага": "Камень"}

if Player1 == Player2:
    Winner = "Ничья"
elif choices.get(Player1) == Player2:
    Winner = "Выиграл первый игрок!"
elif choices.get(Player2) == Player1:
    Winner = "Выиграл второй игрок!"

print(Winner)