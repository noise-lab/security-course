import os
import sys
import tools

__author__ = 'simonsk'


def find_partners(svn_basedir, netid):
    partners_filepath = svn_basedir + "/" + netid + "/mp5/partners.txt"
    partners = []
    if os.path.exists(partners_filepath):
        partners.extend(tools.read_partners(partners_filepath))
        for netid in partners:
            if netid == "":
                partners.remove(netid)
    return partners


def main(argv):
    svn_basedir = argv[0]
    roster = argv[1]
    file_dir = svn_basedir + "/{0}/mp5/5.2.8_location.txt"
    blacklist = dict()

    with open(roster, 'r') as f:
        for netid in f:
            netid = netid.strip()
            secret_submission = tools.read_solution_asis(file_dir.format(netid))
            num_line = len(secret_submission)
            if num_line > 0:
                if num_line > 1:
                    secret_submission = ''.join(secret_submission)
                secret_submission = secret_submission[0]
                if secret_submission != "":
                    partners = find_partners(svn_basedir, netid)
                    if secret_submission in blacklist:
                        if netid not in blacklist[secret_submission]:
                            blacklist[secret_submission].extend(partners)
                    else:
                        blacklist[secret_submission] = partners
    with open('blacklist.txt', 'w') as f:
        for secret, netids in blacklist.iteritems():
            line = ""
            if len(netids) <= 2:
                blacklist[secret] = None
            else:
                for netid in netids:
                    line += netid + " "
                line += secret+"\n"
            if line != "":
                f.write(line)


if __name__ == '__main__':
    main(sys.argv[1:])
