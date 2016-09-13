#!/usr/bin/python
import os
import filecmp
import subprocess


def read_lines(filepath):
    content = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if (len(line) == 0) or (line[0] == '#'):
                continue
            content.append(line.lower())
    return content


def grade_mp4cp2part2(svndir, solutiondir):
    message = ""
    score = 0
    total = 40

    filepath = "{}/4.2.2.py".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(0)
    else:
        pcap_num = 10
        solution_path_format = solutiondir + "/{0}.txt"
        pcap_path_format = solutiondir + "/{0}.pcap"
        default_filepath = solutiondir + "/default_submission.py"

        if filecmp.cmp(filepath, default_filepath):
            message += "\t+{} sample file found".format(0)
        else:
            for i in range(0, pcap_num, 1):
                solution_path = solution_path_format.format(i)
                pcap_path = pcap_path_format.format(i)
                solution = read_lines(solution_path)
                solution.sort()
                try:
                    result = subprocess.check_output(['python', filepath, pcap_path])

                # print results
                except KeyboardInterrupt:
                    message += "\t+{} {}.pcap: manually stopped. took too long\n".format(0, i)
                    continue
                except:
                    message += "\t+{} {}.pcap: exception encountered\n".format(0, i)
                    continue

                # add results to report
                results = result.split("\n")
                # remove empty strings from list if present
                results = filter(None, results)
                skip1 = "input filename: {}".format(pcap_path)
                skip2 = "fixme"
                if skip1 in results:
                    results.remove(skip1)
                if skip2 in results:
                    results.remove(skip2)
                results.sort()
                # temp_set = set(results).intersection(set(solution)) # gotta remember this trick

                false_negative = 0
                for ip in solution:
                    if ip in results:
                        while ip in results:
                            results.remove(ip)
                    else:
                        false_negative += 1
                false_positive = len(results)
                pcap_score = 4 - false_positive - false_negative

                score += pcap_score if pcap_score > 0 else 0
                message += "\t+{} {}.pcap: false_positive={}; false_negative={}\n".format(
                    pcap_score, i, false_positive, false_negative)

    header = "4.2.2\t {} / {}\n".format(score, total)
    return header + message, score, total
