import sys

def main():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    
    scores = dict()

    with open(filename1) as f:
        for line in f:
            line = line.strip().translate(None, '"')
            line = line.split(',')
            netid = line[0]
            score = int(line[1])
            if (netid in scores) :
                raise NameError(netid)
            else:
                scores[netid] = score

    with open(filename2) as f:
        for line in f:
            line = line.strip().translate(None, '"')
            line = line.split(',')
            netid = line[0]
            score = int(line[1])
            if (netid in scores) :
                    scores[netid] += score
            else:
                if score != 0:
                    raise NameError(netid+','+str(score))
                scores[netid] = score


    for key, value in scores.iteritems():
        print key + "," + str(value)


if __name__ == '__main__':
    main()