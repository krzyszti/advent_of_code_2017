from libs import pyoeis


puzzle_input = 361527

data = pyoeis.load_oeis_sequence_table("A141481")
for index in data:
    if data[index] > puzzle_input:
        print(data[index])
        break
