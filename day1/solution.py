def calories_per_elf(file):
    total_calories_per_elf = []

    with open(file) as f:
        running_sum = 0

        for line in f:
            if line.strip() == "":
                total_calories_per_elf.append(running_sum)
                running_sum = 0
            else:
                running_sum += int(line)

    return total_calories_per_elf


def sum_top_three(calorie_list):
    calorie_list.sort(reverse=True)

    return sum(calorie_list[:3])
