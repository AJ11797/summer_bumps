#!/usr/bin/env python3

import fileParser
from division import Div

file_names = ["wk1", "wk2", "wk3", "wk4",
              "wk5", "wk6", "wk7", "wk8", "wk9", "wk10"]

if __name__ == "__main__":
    report = ""
    finish_order = ""
    for week in file_names:
        if week != file_names[0]:
            report += "\n"
        report += f"Running week {week[2:]}\n"
        division = Div(sorted(fileParser.readFile(week)))
        report += division.race()

        if week == file_names[-1]:
            report += division.report() + "\n"
            report += division.get_finish_order()[0] + "\n"

        if week == file_names[0]:
            finish_order += "1," + division.get_finish_order()[1] + "\n"
        finish_order += str(int(week[2])+1) + "," + \
            division.get_finish_order()[2] + "\n"
    report += finish_order
    fileParser.writeTextFile(week, report)
