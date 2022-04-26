import random
import json

def main():
    with open('encrypted_names.json', 'r') as openfile:
        json_object = json.load(openfile)
    candidates = json_object["names"]
    votes = []
    for i in range(1000):
        votes.append( candidates[random.randint(0,len(candidates)-1)] )

    
    with open('vote_list.txt', 'w') as f:
        for vote in votes:
            f.write("%s\n" % vote)

if __name__ == "__main__":
    main()