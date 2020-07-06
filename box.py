#!/usr/bin/env python

NUM_SLOTS = 30
NUM_ROWS = 5
NUM_COLUMNS = 6


def box_loc(dex_num):
    _row = NUM_ROWS
    _col = NUM_COLUMNS - 1
    _box, _r = divmod(dex_num, NUM_SLOTS)
    if _r:
        _row, _col = divmod(_r, NUM_ROWS)
    _col += 1
    return f"Box {_box}, Row {_row}, Col {_col}"


def box():
    print("Reply with \"done\" or \"exit\" at any point to end")
    while True:
        try:
            user_input = input("\nPokemon's NationalDex number: ")
            if user_input.lower() in ["done", "exit"]:
                return
            dex_val = int(user_input)
            print(box_loc(dex_val))
        except ValueError:
            print("That's not a number!")


if __name__ == "__main__":
    box()
