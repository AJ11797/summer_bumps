import summer_bumps.settings as settings
import random


class Div():
    def __init__(self, division: list):
        self.division = division

    def __str__(self):
        return str([str(rower) for rower in self.division])

    def get_next_bump(self) -> list:
        """Works out between who the next bump will occur"""
        ranked_division = list(enumerate(self.division))
        possible_bumps = []
        for i in range(len(ranked_division)):
            if i > 0:
                if ranked_division[i][1].active and ranked_division[i-1][1].active and (ranked_division[i][1].points - ranked_division[i-1][1].points) > settings.bumps_diff:
                    possible_bumps.append(
                        (i, i-1, ranked_division[i][1].points - ranked_division[i-1][1].points))
            if i > 2:
                if ranked_division[i][1].active and not ranked_division[i-1][1].active and not ranked_division[i-2][1].active and ranked_division[i-3][1].active and (ranked_division[i][1].points - ranked_division[i-3][1].points) > settings.nbump_diff[1]:
                    possible_bumps.append(
                        (i, i-3, ranked_division[i][1].points - ranked_division[i-3][1].points))
            if i > 4:
                if ranked_division[i][1].active and not ranked_division[i-1][1].active and not ranked_division[i-2][1].active and not ranked_division[i-3][1].active and not ranked_division[i-2][1].active and not ranked_division[i-4][1].active and not ranked_division[i-2][1].active and ranked_division[i-5][1].active and (ranked_division[i][1].points - ranked_division[i-5][1].points) > settings.nbump_diff[2]:
                    possible_bumps.append(
                        (i, i-5, ranked_division[i][1].points - ranked_division[i-5][1].points))
        if possible_bumps == []:
            return None
        else:
            return max(possible_bumps, key=(lambda x: x[2]))

    def find_bump_location(self, loc: float, max_diff: list) -> str:
        """Returns the location where a bump occured when input with percentage course completion"""
        locations = [[93, "the P&E"], [90, "Peter's Posts"], [74.3, "the Railway Bridge"], [59.7, "the Railings"], [42.7, "the Reach"], [36, "Ditton"], [
            30.7, "Plough Reach"], [25.7, "Grassy"], [22.3, "the Gut"], [19.3, "First Post Corner"], [8, "the Gunshed"], [6, "the Motorway Bridge"], [0, "the Little Bridge"]]
        if self.division[max_diff[1]].points != 0:
            for location in locations:
                if loc > location[0]:
                    return f" at {location[1]}"
        else:
            return " on station as they " + settings.zero_point_msgs[random.randint(0, len(settings.zero_point_msgs)-1)]

    def perform_bump(self) -> str:
        max_diff = self.get_next_bump()
        self.division[max_diff[0]].active = False
        self.division[max_diff[1]].active = False
        self.division[max_diff[0]
                      ].finish_position = self.division[max_diff[1]].start_position
        self.division[max_diff[1]
                      ].finish_position = self.division[max_diff[0]].start_position
        positional_change = self.division[max_diff[0]
                                          ].start_position - self.division[max_diff[1]].start_position

        if positional_change == 1:
            loc = round(settings.bumps_diff / max_diff[2], 3) * 100
            note = (self.division[max_diff[0]].name + " has bumped " +
                    self.division[max_diff[1]].name + self.find_bump_location(loc, max_diff))
        elif positional_change == 3:
            loc = round(settings.nbump_diff[1] / max_diff[2], 3) * 100
            note = (self.division[max_diff[0]].name + " has overbumped " +
                    self.division[max_diff[1]].name + self.find_bump_location(loc, max_diff))
        elif positional_change == 5:
            loc = round(settings.nbump_diff[2] / max_diff[2], 3) * 100
            note = (self.division[max_diff[0]].name + " has double overbumped " +
                    self.division[max_diff[1]].name + self.find_bump_location(loc, max_diff))
        else:
            print("Warning mega overbump has occured")

        note += "\n" + self.division[max_diff[0]].name + ": " + str(
            self.division[max_diff[0]].start_position) + "->" + str(self.division[max_diff[0]].finish_position)
        note += ", " + self.division[max_diff[1]].name + ": " + str(
            self.division[max_diff[1]].start_position) + "->" + str(self.division[max_diff[1]].finish_position)

        self.division[max_diff[0]], self.division[max_diff[1]
                                                  ] = self.division[max_diff[1]], self.division[max_diff[0]]
        return note

    def detect_finish(self) -> bool:
        """Detects where the division should finish"""
        if self.get_next_bump() is None:
            return True
        else:
            return False

    def race(self) -> str:
        report = ""
        for i in range(len(self.division)):
            if self.detect_finish():
                break
            report += self.perform_bump() + "\n"
        return report

    def report(self) -> str:
        report = "\nNet Bumps Standings\n"
        for rower in self.division:
            if rower.sort_by > rower.finish_position:
                report += rower.name + \
                    " (+" + str(rower.sort_by - rower.finish_position) + ")\n"
            else:
                report += rower.name + \
                    " (" + str(rower.sort_by - rower.finish_position) + ")\n"
        return report

    def get_finish_order(self) -> tuple:
        print_order = sorted(self.division, key=(lambda x: x.sort_by))
        names = ""
        start_order = ""
        finish_order = ""

        for rower in print_order:
            names += rower.name + ","
            start_order += str(rower.start_position) + ","
            finish_order += str(rower.finish_position) + ","

        return names, start_order, finish_order
