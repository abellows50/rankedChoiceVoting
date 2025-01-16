from Ballot import Ballot
import sys
import time

JUNK = "Order the following improvement projects according to your preference. Number 1 is your most preferred choice. You cannot select more than one option for each rank."

def getData(ballots:list):
    with open(sys.argv[1], "r") as file:
        headers = file.readline().strip().split(",")[1:]
        # clean up the headers
        for i in range(len(headers)):
            while JUNK in headers[i]:
                headers[i] = headers[i].replace(JUNK, "").strip()

        for line in file.readlines():
            data = line.strip().split(",")[1:]
            rankings = [int(d) for d in data]
            ballots.append(Ballot(headers, rankings))

    return headers


def run_election(ballots:list, headers:list, n):
    print(f"""-------------------------------------\nRunning election round {n}""")
    time.sleep(1)
    current = {}
    total = 0
    for h in headers:
        current[h] = 0
    
    for b in ballots:
        vote = b.vote()
        current[vote] += 1
        total += 1
    
    worst = 100
    best = -100
    best_cs = []
    worst_cs = []

    for c in current.keys():
        current[c] /= total
        if current[c] < worst:
            worst = current[c]
        if current[c] > best:
            best = current[c]
   
    for c in current.keys():
        if current[c] == best:
            best_cs.append(c)
        if current[c] == worst:
            worst_cs.append(c)
    
    
    print(f"Eliminating {worst_cs} with score {worst}")
    print(f"current leader is {best_cs} with score {best}")
    print(f"Current standings: {current}")
    print("-------------------------------------------------")
    
    if best > 0.5:
        return best_cs
        # END OF RANKED CHOICE VOTING

    if best == worst:
        print("Tie")
        return "TIE"

    newc = current.copy()
    for c in current.keys():
        if current[c] == worst:
            del newc[c]
            for b in ballots:
                b.pop_up(c)
    
    current = newc
    
    return run_election(ballots, list(current), n+1)
    


def main():
    ballots = []
    headers = getData(ballots)
    print("Headers: ", headers)
    print("Ballots: ")
    for b, i in enumerate(ballots):
        print(i, end=" - ")
        print(b)
    print("the winner is: ",run_election(ballots, headers, 0))

if __name__ == "__main__":
    main()