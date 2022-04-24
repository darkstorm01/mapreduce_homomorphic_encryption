import random

def main():
    candidates = ["id1","id2","id3","id4","id5"]
    votes = []
    for i in range(1000):
        votes.append( candidates[random.randint(0,len(candidates)-1)] )

    
    with open('vote_list.txt', 'w') as f:
        for vote in votes:
            f.write("%s\n" % vote)

if __name__ == "__main__":
    main()