import os


def main():
    with open((os.path.join(os.getcwd(),'input.txt')), 'r') as f:
        data = [line.strip() for line in f.readlines()] # read the data for answer 1
        # data = [item.strip('\n') for item in f.readlines()] # read the data for answer 2


        def answer_1():

            """
            For the first few pairs, this list means:

            Within the first pair of Elves, the first Elf was assigned sections 2-4 
            (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
            The Elves in the second pair were each assigned two sections.
            The Elves in the third pair were each assigned three sections: 
            one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

            Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.

            Objective: 
            In how many assignment pairs does one range fully contain the other?

            """
            # print(data) # output: ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']


            fully_contained_pairs = 0

            for pair_of_elves in data:
                elf_1_sections = []
                elf_2_sections = []

                # split the line of text to get a list of each elves range of sections
                split_pair_of_elves = pair_of_elves.split(',')

                # find each elf's start and end sections
                elf_1 = split_pair_of_elves[0].split('-')
                elf_2 = split_pair_of_elves[1].split('-')

                elf_1_start = int(elf_1[0])
                elf_1_end = int(elf_1[-1])
                elf_2_start = int(elf_2[0])
                elf_2_end = int(elf_2[-1])

                # get the actual range/section numbers listed out
                for section in range(elf_1_start, elf_1_end + 1):
                    elf_1_sections.append(section)

                for section in range(elf_2_start, elf_2_end + 1):
                    elf_2_sections.append(section)

                # check if elf_1_sections contains elf_2_sections and the other way around 
                check = set(elf_2_sections).issubset(elf_1_sections) or set(elf_1_sections).issubset(elf_2_sections)  

                # add up the fully contained pairs
                if check == True:
                    fully_contained_pairs += 1
                else:
                    pass

                            
            return fully_contained_pairs


        def answer_2():

            """
            the Elves would like to know the number of pairs that overlap at all.

            In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the 
            remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

            5-7,7-9 overlaps in a single section, 7.
            2-8,3-7 overlaps all of the sections 3 through 7.
            6-6,4-6 overlaps in a single section, 6.
            2-6,4-8 overlaps in sections 4, 5, and 6.
            So, in this example, the number of overlapping assignment pairs is 4.

            In how many assignment pairs do the ranges overlap?
            
            """
            # print(data) # output: ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']


            overlapped_pairs = 0

            for pair_of_elves in data:
                elf_1_sections = []
                elf_2_sections = []

                # split the line of text to get a list of each elves range of sections
                split_pair_of_elves = pair_of_elves.split(',')

                # find each elf's start and end sections
                elf_1 = split_pair_of_elves[0].split('-')
                elf_2 = split_pair_of_elves[1].split('-')

                elf_1_start = int(elf_1[0])
                elf_1_end = int(elf_1[-1])
                elf_2_start = int(elf_2[0])
                elf_2_end = int(elf_2[-1])

                # get the actual range/section numbers listed out
                for section in range(elf_1_start, elf_1_end + 1):
                    elf_1_sections.append(section)

                for section in range(elf_2_start, elf_2_end + 1):
                    elf_2_sections.append(section)


                # check if elf_1_sections contains elf_2_sections and the other way around 
                common = list(set(elf_2_sections).intersection(elf_1_sections)) 


                if common != []:
                    overlapped_pairs += 1
                else:
                    pass


                
            return overlapped_pairs


        print("   ")
        print('Answer 1: ', answer_1())
        print('Answer 2: ', answer_2())
        print("   ")


if __name__ == "__main__":
    main()