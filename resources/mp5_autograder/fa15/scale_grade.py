import sys

def main():
    filename = sys.argv[1]
    scores = dict()

    with open(filename) as f:
        for line in f:
            line = line.strip().translate(None, '"')
            # line = line.split('\t')
            if line[0] == "#":
                continue
            else:
                line = line.split(',')
                netid = line[0]
                score = float(line[1])
                scores[netid] = score

    for key, value in scores.iteritems():
        print key + "," + str("{0:.2f}".format(value * 100 / 110))


if __name__ == '__main__':
    main()
