class Ballot:
    def __init__(self, ballot_choices:list, rankings:list):
        choices = [0 for c in ballot_choices]
        for i in range(len(rankings)):
            r = rankings[i]
            choices[r-1] = ballot_choices[i]
        
        self.choices = choices

    def pop_up(self, choice):
        if choice in self.choices:
            self.choices.remove(choice)
            return True
        return False
    
    def vote(self):
        if len(self.choices) > 0:
            return self.choices[0]
        return None
    
    def __str__(self):
        return str(self.choices)


