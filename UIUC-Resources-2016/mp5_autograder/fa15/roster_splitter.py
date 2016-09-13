import sys


def write_file(filename, content):
    print 'writing ' + filename
    with open(filename, 'w') as f:
        for netid in content:
            f.write(netid)

def main():
    if not (sys.argv[1] and sys.argv[2]):
        print "Usage: python roster_splitter.py roster_file_path num_graders"
	exit()

    roster_file_path = sys.argv[1]
    num_graders = int(sys.argv[2])
    
    # read netids from roster file
    with open(roster_file_path, 'r') as f:
        student_list = f.readlines()

    # write them to outputs
    student_per_grader = len(student_list)/num_graders
    out_filename = "./grader_{0}_list.txt"
    for i in range(num_graders):
        if i == num_graders - 1:
            write_file(out_filename.format(i), student_list[i*student_per_grader:])
        else:
            write_file(out_filename.format(i), student_list[i*student_per_grader:(i+1)*student_per_grader])

if __name__ == "__main__":
    main()
