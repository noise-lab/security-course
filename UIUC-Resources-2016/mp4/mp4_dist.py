#!/usr/bin/python
import os, sys, stat
import shutil

#distribution script for SP16-ECE422 mp4

WORKING_DIR = os.getcwd()
LOG_DIR = WORKING_DIR + "/log"

def svn_add(path):
    os.system("svn add "+ path)

def generate_files(netid):
    basepath = netid + "/mp4"

    # check mp4 dir
    if os.path.isdir(basepath):
        # check pcaps
        pcap1 = basepath + "/4.1.1.pcap"
        pcap2 = basepath + "/4.1.2.pcap"
        if os.path.isfile(pcap1) and os.path.isfile(pcap2):

            # svn add submission files
            file_list = ["4.1.1.1_mac.txt",
                         "4.1.1.1_ip.txt",
                         "4.1.1.2.txt",
                         "4.1.1.3.txt",
                         "4.1.1.4_active.txt",
                         "4.1.1.4_passive.txt",
                         "4.1.1.5.txt",
                         "4.1.2.1.txt",
                         "4.1.2.2.txt",
                         "4.1.2.3.txt",
                         "4.1.2.4.txt",
                         "4.1.2.5.txt",
                         "4.1.2.6.txt",
                         "4.1.2.7.txt",
                         "4.2.1.1.txt",
                         "4.2.1.2.txt",
                         "4.2.1.3.txt",
                         "4.2.1.4.txt",
                         "4.2.1.5.txt",
                         "4.2.1.6.txt",
                         "4.2.2.py",
                         "partners.txt"]
            for submission_file in file_list:
                src = WORKING_DIR + "/submission_files/" + submission_file
                dst = basepath + "/" + submission_file
                shutil.copyfile(src, dst)
                if submission_file == "4.2.2.py":
                    st = os.stat(dst)
                    os.chmod(dst, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            svn_add(basepath)
        else:
            #check 4.1.1.pcap
            if not os.path.isfile(pcap1):
                with open(LOG_DIR+"/pcap1_missing.txt", "a+") as f:
                    f.write(netid+"\n")
            #check 4.1.2.pcap
            if not os.path.isfile(pcap2):
                with open(LOG_DIR+"/pcap2_missing.txt", "a+") as f:
                    f.write(netid+"\n")
    else:
        with open(LOG_DIR+"/no_mp4.txt", "a+") as f:
            f.write(netid+"\n")

def main():
    if (len(sys.argv) < 3):
        print "usage: ./mp4_gen.py {local_svn_repo} {roster_filepath} in aboluste paths"
        sys.exit(1)

    local_svn_repo = sys.argv[1]
    roster = sys.argv[2]
    os.chdir(local_svn_repo)

    if os.path.isdir(LOG_DIR):
        shutil.rmtree(LOG_DIR)
    os.mkdir(LOG_DIR)

    with open(roster) as f:
        for netid in f:
            netid = netid.strip()
            generate_files(netid)

if __name__ == '__main__':
    main()
