import os
from collections import defaultdict
import copy


def main():
    with open((os.path.join(os.getcwd(),'test_input.txt')), 'r') as f:
        # read the data from 'input.txt' or 'test_input.txt'
        # data = [line.strip() for line in f.readlines()]
        # data = [item.strip('\n') for item in f.readlines()]
        stacks = {}
        instructions = []
        stacks_str, commands = f.read().split("\n\n")
        stacks_list = stacks_str.split("\n")
        # print('stacks_str: ', stacks_str)
        # print('type of stacks_str: ', type(stacks_str))
        # print('commands: ', commands)
        # print('stacks_list: ', stacks_list)


        def answer_1():

            """
            DESCRIPTION: 
            In this example, there are three stacks of crates. 
            Stack 1 contains two crates: crate Z is on the bottom, 
            and crate N is on top. Stack 2 contains three crates; 
            from bottom to top, they are crates M, C, and D. Finally, 
            stack 3 contains a single crate, P.

            Then, the rearrangement procedure is given. In each 
            step of the procedure, a quantity of crates is moved 
            from one stack to a different stack. In the first step of 
            the above rearrangement procedure, one crate is moved from 
            stack 2 to stack 1

            OBJECTIVE: 
            The Elves just need to know which crate 
            will end up on top of each stack; in this example, 
            the top crates are C in stack 1, M in stack 2, 
            and Z in stack 3, so you should combine these 
            together and give the Elves the message CMZ.

            After the rearrangement procedure completes, 
            what crate ends up on top of each stack?

            """

            stacks: dict[int, list[str]] = defaultdict(list)
            # print(stacks)
            for stack in stacks_list[-2::-1]: # `stacks_list[-2::-1]` = start at 2nd to last item, increment backwards 
                                              # by 1 through the entire list
                for i, box in enumerate(stack[1::4]): # `stack[1::4]` = start at index 1 (2nd item in list), increment 
                                                      # by 4 through the entire list
                    if box != " ":
                        stacks[i + 1].append(box)
                        # print(stacks)

           
            for command in commands.strip().split('\n'):
                _, box_num, _, origin, _, destination = command.split()
                instructions.append(list(map(int, [box_num, origin, destination])))

            print(instructions)
            print(stacks)
            # process instructions
            new_stacks = copy.deepcopy(stacks)
            for count, start, end in instructions:
                for _ in range(count):
                    new_stacks[end].append(new_stacks[start].pop())
            print(new_stacks)

            # return your answer here         
            print("     ")
            return "still working on it..."


        def answer_2():

            """
            DESCRIPTION: 


            OBJECTIVE: 
            

            """
            # your code goes here


            # return your answer here         
            return "still working on it..."


        # clearly print your answers
        print('Answer 1: ', answer_1())
        print('Answer 2: ', answer_2())
        print("     ")


if __name__ == "__main__":
    main()