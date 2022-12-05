class Solution:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def part1(cls, input_file):
        total_sum = 0
        with open(input_file) as file:

            for line in file:
                char_dict = {}

                middle = int((len(line) / 2))
                first_half = line[:middle]
                second_half = line[middle:]

                for index, char in enumerate(second_half):
                    char_dict[char] = index

                for char in first_half:
                    if char in second_half:
                        total_sum += cls.ALPHABET.index(char) + 1
                        break

        return total_sum

    @classmethod
    def part2(cls, input_file):
        total_sum = 0
        with open(input_file) as file:
            lines = file.readlines()
            line_groups = []


            for n in range(3, len(lines), 3):
                print(lines[:n])
