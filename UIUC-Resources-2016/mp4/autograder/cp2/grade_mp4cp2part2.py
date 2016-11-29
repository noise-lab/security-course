#!/usr/bin/python
import os
import filecmp
import subprocess
import shlex


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
    timeout = 30
    message = ""
    zero = float(0)
    score = zero
    total = float(30)

    filepath = "{}/4.2.2.py".format(svndir)
    if not os.path.exists(filepath):
        message += "\t+{} unable to find your solution file...\n".format(zero)
    else:
        pcap_num = 10
        solution_path_format = solutiondir + "/{0}.txt"
        pcap_path_format = solutiondir + "/{0}.pcap"
        default_filepath = solutiondir + "/default_submission.py"

        if filecmp.cmp(filepath, default_filepath):
            message += "\t+{} sample file found".format(zero)
        else:
            for i in range(0, pcap_num, 1):
                solution_path = solution_path_format.format(i)
                pcap_path = pcap_path_format.format(i)
                solution = read_lines(solution_path)
                solution.sort()
                command = "timeout {} python {} {}".format(timeout, filepath, pcap_path)
                command = shlex.split(command)
                try:
                    result = subprocess.check_output(command)

                # print results
                except subprocess.CalledProcessError as exc:
                    if exc.returncode == 124:
                        message += "\t+{} {}.pcap: {}s timeout\n".format(zero, i, timeout)
                    else:
                        message += "\t+{} {}.pcap: unknown error encountered\n".format(zero, i)
                    continue
                except KeyboardInterrupt:
                    message += "\t+{} {}.pcap: manually stopped. took too long\n".format(zero, i)
                    continue
                except:
                    message += "\t+{} {}.pcap: exception encountered\n".format(zero, i)
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
                pcap_score = float(3) - false_positive - false_negative
                pcap_score = zero if pcap_score < 0 else pcap_score

                score += pcap_score
                message += "\t+{} {}.pcap: false_positive={}; false_negative={}\n".format(
                    pcap_score, i, false_positive, false_negative)

    header = "4.2.2\t {} / {}\n".format(score, total)
    return header + message, score, total
