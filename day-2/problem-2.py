#!/usr/bin/env python3


ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSOR_SCORE = 3

# the losing pairs are everything that's left

SAMPLE_GAME = "C Z"


def score_round(matchup):
    rocks = "A X"
    papers = "B Y"
    scissors = "C Z"
    scores = {'X': 1, 'Y': 2, 'Z': 3}

    winning_pairs = ["C X", "A Y", "B Z"]
    drawing_pairs = [rocks, papers, scissors]
    score = scores[matchup[2]]
    if matchup in winning_pairs:
        score += 6
    elif matchup in drawing_pairs:
        score += 3

    return score

def part_2(matchup):
    draw = 'Y'
    lose = 'X'
    win = 'Z'

    rps_scores = {"rock": 1, "paper": 2, "scissors": 3}
    end_scores = {"Z": 6, "Y": 3, "X": 0}

    # there's probably a more elegant way of deriving this but... eh
    draws = {"A": "rock", "B": "paper", "C": "scissors"}
    wins = {"A": "paper", "B": "scissors", "C": "rock"}
    loses = {"A": "scissors", "B": "rock", "C": "paper"}


    score = end_scores[matchup[2]]

    if matchup[2] == win:
        score += rps_scores[wins[matchup[0]]]
    elif matchup[2] == draw:
        score += rps_scores[draws[matchup[0]]]
    elif matchup[2] == lose:
        score += rps_scores[loses[matchup[0]]]

    return score

with open("input", "r") as f:
    total_score_p1 = 0
    total_score_p2 = 0
    for line in f:
        total_score_p1 += score_round(line.rstrip())
        total_score_p2 += part_2(line.rstrip())

    print("part 1: " + str(total_score_p1))
    print("part 2: " + str(total_score_p2))
