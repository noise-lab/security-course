import sys
import os
import subprocess
import csv

script_path = './3.2.2.py'
if not os.path.exists(script_path):
    print "0\tUnable to find your solution file(s).  Aborting."
else:
    # init values
    svn_base = sys.argv[1]
    netid = sys.argv[2]
    PCAP_COUNT = 10
    SOLUTION_BASE_PATH = svn_base + "/_class/_private/mp4/solutions/cp2_pcap/{0}.txt"
    PCAP_BASE_PATH = svn_base + "/_class/_private/mp4/solutions/cp2_pcap/{0}.pcap"

    score = 0
    message = '\n'

    with open(script_path) as f:
        script_content = f.read()
        if script_content == '':
            message += 'empty submission'
            print str(score)+'\t'+message
            exit(0)

    for i in range(0,PCAP_COUNT,1):
        solution_path = SOLUTION_BASE_PATH.format(i)
        pcap_path = PCAP_BASE_PATH.format(i)

        with open(solution_path) as expected_file:
            expected = [line.strip()for line in expected_file]

        try:        
            result = subprocess.check_output(['python', script_path , pcap_path])

        #print results
        except KeyboardInterrupt:
            message += "Hit crtl+c, Stopping"
            print 0+"\t"+message
            exit(0)
        except:
            print "Exception encountered for netid: " + netid
            message +=  "Exception encountered for netid: " + netid +" for file cap" + str(i) + ".pcap\n"
            continue

        #add results to report
        results = result.split('\n')
        results = filter(None, results) # remove empty strings from set if present
        temp_set = set(results).intersection(set(expected)) # gotta remember this trick

        if len(results) == len(expected):
            score += 4
            message += str(i) + ".pcap  "  + "FALSE_POSITIVE: " + str(0) + " FALSE_NEGATIVE: " + str(0) + "\n"

        #false positive
        elif len(results) > len(expected):
            d = len(results) - len(expected) 
            score += max(0,4-d)
            message += str(i) + ".pcap  "  + "FALSE_POSITIVE: " + str(d) + " FALSE_NEGATIVE: " + str(0) + "\n"

        #false negative
        else:
            d = len(expected) - len(temp_set)
            if len(temp_set) != 0:
                score += max(0,4-d)
            message += str(i) + ".pcap  "  + "FALSE_POSITIVE: " + str(0) + " FALSE_NEGATIVE: " + str(d) + "\n"
        
    print str(score)+"\t"+message;