def main(input: list):

    limits = {"r": 12, "g": 13, "b": 14}
    lines = []
    sum = 0
    for line in input:
        
        step1 = line.replace(";", ",").replace(", ", ".").replace("red", "r").replace("green", "g").replace("blue", "b")
        step2 = step1.split(": ")
        step3 = step2[1].split(".")
        game_id = step2[0].split(" ")[1]
        line_values = {"r": 0, "g": 0, "b": 0, "id": int(game_id)}
        for value in step3:
            for key in line_values.keys():
                if key in value:
                    line_values[key] += int(value.split(" ")[0])
        lines.append(line_values)
    print(lines)
    for line in lines:
        valid = True
        for key in limits.keys():
            if limits[key] < line[key]:
                valid = False
                break
        if valid:
            sum += line["id"]
            print(line)
    return sum

    

if __name__ == "__main__":
    with open("day2.txt") as f:
        input = f.readlines()
    print(main(input))