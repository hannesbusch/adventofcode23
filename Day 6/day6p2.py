def main() -> int:
    game = {"time":41777096, "distance": 249136211271011}
    total_t = game["time"]
    hold_ts = []
    hold_t = 0
    while (hold_t * (total_t - hold_t) < game["distance"]):
        hold_t += 1

    while (hold_t * (total_t - hold_t) > game["distance"] and hold_t < total_t):
        hold_ts.append(hold_t)
        hold_t += 1

    return len(hold_ts)

print(main())