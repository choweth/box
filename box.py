#!/usr/bin/env python

NUM_SLOTS = 30
NUM_ROWS = 5
NUM_COLUMNS = 6


def box_loc(dex_num):
    dex_num -= 1
    _box, _r = divmod(dex_num, NUM_SLOTS)
    _row, _col = divmod(_r, NUM_COLUMNS)
    return f"Box {_box+1}, Row {_row+1}, Col {_col+1}"


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
