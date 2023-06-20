player1 = input("Nombre del jugador 1 (figura = ⭕): ")
player2 = input("Nombre del jugador 2 (figura = ❌): ")
figure_player1 = "⭕"
figure_player2 = "❌"
# Establecemos una condición para cambiar turnos entre jugadores
player_flow = True
# Definimos un contador que recogerá cada movimiento
moves_count = 0
# Definimos los movimientos límite o máximos
moves_limit = 9
board = [["⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛"]]
# Variables que representan posibles errores
occupied_square = "Casilla ocupada, prueba de nuevo"
out_of_range = "Valores fuera del rango permitido, introduce unos nuevos"
# Variables que van tomando valores dentro del bucle
error_message = ""
playing = True
victory = ""
while playing:
    # Bucle que va a mostrar el tablero
    for line in board:
        for column in line:
            print(column, end=" ")
        print()
    if player_flow:
        print(
            "Turno de",
            player1,
            "⭕ selecciona una linea (1,2 o 3) y una columna (1,2, o 3)",
        )
        line = int(input("Linea: "))
        column = int(input("Columna: "))
        # Restamos uno al tamaño del board ya que empezamos en 0
        if 1 <= line <= 3 and 1 <= column <= 3 and board[line - 1][column - 1] == "⬛":
            board[line - 1][column - 1] = figure_player1
            moves_count += 1
            player_flow = not player_flow
        else:
            if 1 > line or line > 3 or 1 > column or column > 3:
                error_message = out_of_range
            elif board[line - 1][column - 1] != "⬛":
                error_message = occupied_square
            print(error_message)
    else:
        print(
            "Turno de",
            player2,
            "❌ selecciona una linea (1,2 o 3) y una columna (1,2, o 3)",
        )
        line = int(input("Linea: "))
        column = int(input("Columna: "))
        if 1 <= line <= 3 and 1 <= column <= 3 and board[line - 1][column - 1] == "⬛":
            board[line - 1][column - 1] = figure_player2
            moves_count += 1
            player_flow = not player_flow
        else:
            if 1 > line or line > 3 or 1 > column or column > 3:
                error_message = out_of_range
            elif board[line - 1][column - 1] != "⬛":
                error_message = occupied_square
            print(error_message)

    # Definimos las condiciones de victoria
    for line in range(3):
        if board[line][0] == board[line][1] == board[line][2] != "⬛":
            victory = f"¡¡{board[line][0]} ha ganado!!"
            playing = not playing
            break
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != "⬛":
            victory = f"¡¡{board[0][column]} ha ganado!!"
            playing = not playing
            break
    if board[0][0] == board[1][1] == board[2][2] != "⬛":
        victory = f"¡¡{board[0][0]} ha ganado!!"
        playing = not playing
    elif board[0][2] == board[1][1] == board[2][0] != "⬛":
        victory = f"¡¡{board[0][2]} ha ganado!!"
        playing = not playing
    else:
        if moves_count == moves_limit:
            victory = "El juego ha quedado en empate"
            playing = not playing

# Tablero final con victoria
for line in board:
    for column in line:
        print(column, end=" ")
    print()
print(victory)