import csv
import sys
from summer_bumps.rower import Rower


def readFile(file_name: str) -> list:
    start_pos_total = 0
    sort_by_total = 0
    try:
        division = []
        with open(f"input/{file_name}.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    division.append(Rower(
                        name=row["name"], points=row["points"], start_pos=row["pos"], sort_by=row["sortby"]))
                    start_pos_total += int(row["pos"])
                    sort_by_total += int(row["sortby"])
                except KeyError as e:
                    print(f"Field {str(e)} doesn't exist")
                    sys.exit()
    except FileNotFoundError:
        print("Input file doesn't exist")
        sys.exit()

    # Sum of the natural numbers up to the number of people competing
    correct_total = int(len(division)*(len(division)+1)/2)

    if start_pos_total != correct_total:
        raise ValueError("Error in start positions")
    if sort_by_total != correct_total:
        raise ValueError("Error in sorting positions")

    return division


def writeTextFile(file_name: str, message: str):
    f = open(f"output/output_{file_name}.txt", "w")
    f.write(message)
    f.close()
