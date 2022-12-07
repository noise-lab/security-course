from string import whitespace
from datetime import datetime
import os
import sys

'''
Note: Every student's svn directory should be updated to the revision just before
      the duedate before this script is run using 

      svn up -r "{2015-12-04 18:10:00}"

'''

# for grading
def read_student_solution(filepath):
    try:
        with open (filepath, "r") as myfile:
            data = myfile.read()
    except:
        data = ''
        
    return data

def get_score_string(partners, score):
    ret = ''
    for partner in partners:
        ret += partner.strip() + ',' + str(score) + '\n'

    return ret

def main():
    if len(sys.argv) < 3:
        print "Usage: python " + sys.argv[0] + " <svn_base_dir> <grader_list_file>\n"
        exit(0)

    svn_basedir = sys.argv[1]
    netid_list_path = sys.argv[2]

    curr_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    individual_grade_file_path = svn_basedir + "/{0}/mp5/grade_5.2_manual_"+str(curr_time)+".txt"
    partner_file_path = svn_basedir + "/{0}/mp5/partners.txt"
    suspect_file_path = svn_basedir + "/{0}/mp5/suspect_vm.txt"
    solution_file_paths = [svn_basedir + "/{0}/mp5/5.2.1_behavior.txt", 
                           svn_basedir + "/{0}/mp5/5.2.3_relationship.txt", 
                           svn_basedir + "/{0}/mp5/5.2.4_method.txt"]

    # instructor grade report file
    gr=open("part_5.2_manual_grades_"+str(curr_time)+".txt","w",0);

    # read student list into a list
    with open(netid_list_path, 'r') as f:
        netid_list = f.readlines()

    # grade students
    for netid in netid_list:
        netid = netid.strip()

        # manage partner
        partners = [netid]
        try:
            with open(partner_file_path.format(netid)) as f:
                content = f.readlines()
                if content == []:
                    partners = [netid]
                else:
                    partners = content
        except:
            pass

        print '\nGrading ' + str(partners)

        # printing suspect case
        with open(suspect_file_path.format(netid)) as f:
            suspect = f.read()
            suspect = suspect.strip()
            sus_ind = suspect.find('suspect')
            suspect = suspect[sus_ind:len(suspect)]
            print "Case: " + suspect + "\n"

        # initialization
        final_score = 0
        message = ''

        # start grading
        for path in solution_file_paths:
            subpart_name = path[path.find('mp5'):]
            print '\n\nGrading ' + subpart_name
            if '5.2.1' in subpart_name or '5.2.4' in subpart_name:
                total_score = 5
            elif '5.2.3' in subpart_name:
                total_score = 10
            student_sol = read_student_solution(path.format(netid))
            if student_sol == '':
                score = 0
            else:
                print student_sol
                score = input('\nEnter score (/{0} points): '.format(total_score))
                # print '='*80
            final_score += int(score)
            message += (subpart_name + ": " + str(score) + "\n")

        grade = get_score_string(partners, final_score)
        gr.write(grade)

        # create and add individual student's grade report to svn
        with open(individual_grade_file_path.format(netid), 'w') as indv_grade_file:
            indv_grade_file.write("Grade: " + str(final_score) + "\n" + message)

        os.system("svn add "+individual_grade_file_path.format(netid))

if __name__ == "__main__":
    main()
