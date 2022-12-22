import os


def main():
    with open((os.path.join(os.getcwd(),'input.txt')), 'r') as f:
        # read the data from 'input.txt' or 'test_input.txt'
        data = [line.strip() for line in f.readlines()]
        # data = [item.strip('\n') for item in f.readlines()]


        def answer_1():

            """
            DESCRIPTION: 


            OBJECTIVE: 
            

            """
            # your code goes here


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