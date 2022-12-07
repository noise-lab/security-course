import sys

def main():
    filename = sys.argv[1]

    with open(filename) as f:
        for line in f:
            score = int(line.strip().translate(None, '"').split(',')[1])
            if score == 0 or score == 20:
                continue
            print line.strip()




if __name__ == '__main__':
    main()