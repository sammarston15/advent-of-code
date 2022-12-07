import os
import string

def main():
    with open((os.path.join(os.getcwd(),'input.txt')), 'r') as f:
        # data = [line.strip() for line in f.readlines()] # read the data for answer 1
        data = [item.strip('\n') for item in f.readlines()] # read the data for answer 2


        def answer_1():

            """
            each rucksack is split in half, the first half is one compartment of the rucksack
            the second half is the second compartment

            Objective:
            In the above example, the priority of the item type that appears in both compartments 
            of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

            Find the item type that appears in both compartments of each rucksack. 
            What is the sum of the priorities of those item types?
            
            """
            common_type_number_values = []

            def get_common_type_value(common_type_letter):

                # setting the priority value
                for count, letter in enumerate(string.ascii_letters):
                    if letter == common_type_letter:
                        # print(f"{count + 1}, {letter}")
                        return count + 1

            for line in data: 
                new_list = list(line)
                list_length = len(new_list)
                middle_index = int(list_length / 2)
                first_half = new_list[:middle_index]
                second_half = new_list[middle_index:]
                common_type_list = [item for item in first_half if item in second_half] # returns list of matching items
                common_type = common_type_list[0] # select only the first item in common_type_list
                common_tyoe_number_value = get_common_type_value(common_type)
                common_type_number_values.append(common_tyoe_number_value)

            
            # print(common_type_number_values)
            # print(sum(common_type_number_values))



            return sum(common_type_number_values)


        def answer_2():

            """
            In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. 
            In the second group, their badge item type must be Z. Priorities for these items must still be 
            found to organize the sticker attachment efforts: here, they are 18 (r) for the first 
            group and 52 (Z) for the second group. The sum of these is 70.

            Objective:
            Find the item type that corresponds to the badges of each three-Elf group. 
            What is the sum of the priorities of those item types?
            
            """
            badge_sum_value_list = []

            def get_common_type_value(common_type_letter):

                # setting the priority value
                for count, letter in enumerate(string.ascii_letters):
                    if letter == common_type_letter:
                        # print(f"{count + 1}, {letter}")
                        return count + 1


            groups_of_elves = [data[n:n+3] for n in range(0, len(data), 3)]



            for group_count, elf_group in enumerate(groups_of_elves): 
                print(f"Elf group #{group_count + 1}, {elf_group}")
                common_letter_list = [letter for letter in elf_group[0] if letter in elf_group[1] and letter in elf_group[2]]
                print('common letter: ', common_letter_list[0])
                common_letter_value = get_common_type_value(common_letter_list[0])
                badge_sum_value_list.append(common_letter_value)
               

            return sum(badge_sum_value_list)


        print("   ")
        print('Answer 1: ', answer_1())
        print('Answer 2: ', answer_2())
        print("   ")

if __name__ == "__main__":
    main()