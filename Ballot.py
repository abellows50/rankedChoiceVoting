class Ballot:
    def __init__(self, ballot_choices:list, rankings:list):
        choices = [0 for c in ballot_choices]
        for i in range(len(rankings)):
            r = rankings[i]
            choices[r-1] = ballot_choices[i]
        
        self.choices = choices

    def pop_up(self, choice):

