data =[{"time": 41, "distance": 249}, {"time": 77, "distance": 1362},{"time": 70, "distance": 1127},{"time": 96, "distance": 1011}]


def main() -> int:
    possibles = 1
    for game in data:
        total_t = game["time"]
        hold_ts = []
        hold_t = 0
        while (hold_t * (total_t - hold_t) < game["distance"]):
            hold_t += 1

        while (hold_t * (total_t - hold_t) > game["distance"] and hold_t < total_t):
            hold_ts.append(hold_t)
            hold_t += 1

        possibles  *= len(hold_ts)
    return possibles


if __name__ == "__main__":
        print(main())