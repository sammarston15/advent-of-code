import os

def main():
    with open((os.path.join(os.getcwd(),'input.txt')), 'r') as f:
        data = [line.strip() for line in f.readlines()]

        total_calories_by_elf = []
        elf_calories = 0
        for entry in data:
            if entry == '':
                total_calories_by_elf.append(elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(entry)


        print('Answer 1: ', max(total_calories_by_elf))
        print('Answer 2: ', sum(sorted(total_calories_by_elf, reverse=True)[:3]))

if __name__ == "__main__":
    main()