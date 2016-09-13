import sys

def main():
    filename = sys.argv[1]
    scores = dict()

    with open(filename) as f:
        for line in f:
            line = line.strip().translate(None, '"')
            line = line.split(',')
            netid = line[0]
            score = int(line[1])
            if (netid in scores) :
                if (scores[netid] < score) :
                    scores[netid] = score
            else:
                scores[netid] = score



    for key, value in scores.iteritems():
        print key + "," + str(value)


if __name__ == '__main__':
    main()