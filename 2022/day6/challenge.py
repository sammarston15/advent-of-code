import os


def main():
    with open((os.path.join(os.getcwd(),'input.txt')), 'r') as f:
        # read the data from 'input.txt' or 'test_input.txt'
        data = f.read()
        # data = [item.strip('\n') for item in f.readlines()]


        def answer_1():

            """
            DESCRIPTION: 


            OBJECTIVE: 
            

            """
            # your code goes here
            new_data = list(data)
            fourteen = []
            check = 0
            found = 0
            result = 0
            for i, char in enumerate(new_data):
                # print('   ')
                # print(f"-----index {i}-----")


                if i < 4:
                    fourteen.append(char)

                else:
                    # drop first char then add next char to the end
                    fourteen.pop(0)
                    fourteen.append(char)

                # check for multiples
                check = [fourteen.count(item) for item in fourteen]
                # print('check: ', len(check))
                if sum(check) == 4 and len(check) == 4:
                    result = i + 1
                    break
                else:
                    continue


            # return your answer here    
            print("     ")     
            return result


        def answer_2():

            """
            DESCRIPTION: 


            OBJECTIVE: 
            

            """
            # your code goes here
            new_data = list(data)
            fourteen = []
            check = 0
            found = 0
            result = 0
            for i, char in enumerate(new_data):
                # print('   ')
                # print(f"-----index {i}-----")


                if i < 14:
                    fourteen.append(char)

                else:
                    # drop first char then add next char to the end
                    fourteen.pop(0)
                    fourteen.append(char)

                # check for multiples
                check = [fourteen.count(item) for item in fourteen]
                if sum(check) == 14 and len(check) == 14:
                    result = i + 1
                    break
                else:
                    continue


            # return your answer here    
            print("     ")     
            return result


        # clearly print your answers
        print('Answer 1: ', answer_1())
        print('Answer 2: ', answer_2())
        print("     ")


if __name__ == "__main__":
    main()