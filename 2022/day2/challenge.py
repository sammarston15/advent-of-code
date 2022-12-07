import os

def main():
    with open((os.path.join(os.getcwd(),'input.txt')), 'r') as f:
        data = [line.strip() for line in f.readlines()]

        def answer_1():

            """
            A is rock
            B is paper
            C is scissors

            X is rock
            Y is paper
            Z is scissors
            """

            score_legend = {
                "X": 1,
                "Y": 2,
                "Z": 3,
                "win": 6,
                "lose": 0,
                "draw": 3
            }
            total_score = 0
            game_score = 0
            for game in data:
                game = game.split(' ')
                if game[0] == "A" and game[1] == "Y":
                    game_score = score_legend['Y'] + score_legend['win']
                if game[0] == "A" and game[1] == "X":
                    game_score = score_legend['X'] + score_legend['draw']
                if game[0] == "A" and game[1] == "Z":
                    game_score = score_legend['Z'] + score_legend['lose']
                if game[0] == "B" and game[1] == "Y":
                    game_score = score_legend['Y'] + score_legend['draw']
                if game[0] == "B" and game[1] == "X":
                    game_score = score_legend['X'] + score_legend['lose']
                if game[0] == "B" and game[1] == "Z":
                    game_score = score_legend['Z'] + score_legend['win']
                if game[0] == "C" and game[1] == "Y":
                    game_score = score_legend['Y'] + score_legend['lose']
                if game[0] == "C" and game[1] == "X":
                    game_score = score_legend['X'] + score_legend['win']
                if game[0] == "C" and game[1] == "Z":
                    game_score = score_legend['Z'] + score_legend['draw']

                # add game's score to the total score
                total_score += game_score

                # reset the game score to 0 for the next game
                game_score = 0

            return total_score


        def answer_2():

            """
            A is rock
            B is paper
            C is scissors

            X means you need to lose
            Y means you need to draw
            Z means you need to win
            """

            score_legend_2 = {
                "rock": 1,
                "paper": 2,
                "scissors": 3,
                "win": 6,
                "lose": 0,
                "draw": 3
            }
            total_score_2 = 0
            game_score_2 = 0
            for game in data:
                game = game.split(' ')
                if game[0] == "A" and game[1] == "Y":
                    game_score_2 = score_legend_2['rock'] + score_legend_2['draw']
                if game[0] == "A" and game[1] == "X":
                    game_score_2 = score_legend_2['scissors'] + score_legend_2['lose']
                if game[0] == "A" and game[1] == "Z":
                    game_score_2 = score_legend_2['paper'] + score_legend_2['win']
                if game[0] == "B" and game[1] == "Y":
                    game_score_2 = score_legend_2['paper'] + score_legend_2['draw']
                if game[0] == "B" and game[1] == "X":
                    game_score_2 = score_legend_2['rock'] + score_legend_2['lose']
                if game[0] == "B" and game[1] == "Z":
                    game_score_2 = score_legend_2['scissors'] + score_legend_2['win']
                if game[0] == "C" and game[1] == "Y":
                    game_score_2 = score_legend_2['scissors'] + score_legend_2['draw']
                if game[0] == "C" and game[1] == "X":
                    game_score_2 = score_legend_2['paper'] + score_legend_2['lose']
                if game[0] == "C" and game[1] == "Z":
                    game_score_2 = score_legend_2['rock'] + score_legend_2['win']

                # add game's score to the total score
                total_score_2 += game_score_2

                # reset the game score to 0 for the next game
                game_score_2 = 0

            return total_score_2


        print("   ")
        print('Answer 1: ', answer_1())
        print('Answer 2: ', answer_2())
        print("   ")

if __name__ == "__main__":
    main()