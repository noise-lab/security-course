#!/usr/bin/python
import sys,os,subprocess,re;
from string import whitespace

def read_solution(filepath):
    data = []
    with open(filepath,'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            data.append(line)

    return data

def read_solution_string(filepath):
    data = ""
    with open(filepath,'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            data += line.lower()

    return data

def get_suspect_selection(filepath):
    with open(filepath, 'r') as f:
        line = f.read().strip()
        suspect = line[len(line)-1]
    return suspect

# solution
link_l_sol = ['https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+perform+hydra+attack+on+remote+ssh+machine&ie=utf-8&oe=utf-8',
              'https://hackertarget.com/brute-forcing-passwords-with-ncrack-hydra-and-medusa/',
              'http://itswapshop.com/content/how-crack-ssh-ftp-or-telnet-server-using-hydra-ubuntu',
              'http://www.how-tofind.com/tube/4vm2M_oZt34/bruteforce-attack-with-hydra-ssh-hacking',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+use+nmap+to+get+ip+address&ie=utf-8&oe=utf-8',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=hydra+tutorial&ie=utf-8&oe=utf-8',
              'http://xeushack.com/thc-hydra/',
              'http://security.stackexchange.com/questions/36198/how-to-find-live-hosts-on-my-network',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=dictionary+attack+word+list&ie=utf-8&oe=utf-8',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=dictionary+attack+word+list&ie=utf-8&oe=utf-8#channel=fs&q=dictionary+word+list',
              'http://breakthesecurity.cysecurity.org/2011/12/large-password-list-free-download-dictionary-file-for-password-cracking.html',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=dictionary+attack+word+list&ie=utf-8&oe=utf-8#channel=fs&q=dictionary+attack+word+list+security',
              'https://wiki.skullsecurity.org/Passwords',
              'http://pastebin.com/EBniehm3',
              'http://pastebin.com/download.php?i=EBniehm3',
              'https://www.google.com/search?q=effective+weapons+for+a+murder&ie=UTF-8&sa=Search&channel=fe&client=browser-ubuntu&hl=en&gws_rd=ssl',
              'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0CCsQFjACahUKEwi3tLW5v_bIAhUENz4KHVYaCGA&url=http%3A%2F%2Fcriminalcasegame.wikia.com%2Fwiki%2FMurder_Weapons&usg=AFQjCNHFL9X3yuV1GTyof7ICznoY6XV4aQ',
              'http://listverse.com/2013/07/21/10-bizarre-murder-weapons/',
              'http://criminalcasegame.wikia.com/wiki/Murder_Weapons',
              'http://www.therichest.com/rich-list/most-shocking/the-10-most-common-murder-weapons-in-the-united-states/',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=commonly+used+suicidal+weapon&ie=utf-8&oe=utf-8',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=commonly+used+suicidal+weapon&ie=utf-8&oe=utf-8#channel=fs&q=commonly+used+suicide+weapon',
              'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0CCwQFjACahUKEwi7_YSGwPbIAhUKOyYKHUfRCjk&url=http%3A%2F%2Fwww.hsph.harvard.edu%2Fmagazine-features%2Fguns-and-suicide-the-hidden-toll%2F&usg=AFQjCNE0DK1Zt3G-h4-zbzVHt5ktth0CbA&bvm=bv.106379543,d.eWE',
              'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&cad=rja&uact=8&ved=0CD8QFjAFahUKEwi7_YSGwPbIAhUKOyYKHUfRCjk&url=http%3A%2F%2Fwww.usatoday.com%2Fstory%2Fnews%2Fnation%2F2013%2F07%2F21%2Fguns-most-deadly-choice-in-suicide-attempts%2F2572097%2F&usg=AFQjCNHICAoM1h5aY7d-_96uRhkK68dE2A&bvm=bv.106379543,d.eWE',
              'http://www.hsph.harvard.edu/magazine-features/guns-and-suicide-the-hidden-toll/',
              'http://www.usatoday.com/story/news/nation/2013/07/21/guns-most-deadly-choice-in-suicide-attempts/2572097/',
              'http://lostallhope.com/suicide-methods/firearms',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=nerf+gun&ie=utf-8&oe=utf-8',
              'http://nerf.hasbro.com/en-us/',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=amazon+nerf+gun+shipping+time&ie=utf-8&oe=utf-8',
              'http://www.amazon.com/Nerf-N-Strike-Elite-Rough-Blaster/dp/B009T45XN2',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=nerf+gun+store+pick+up&ie=utf-8&oe=utf-8',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=nerf+gun+store+pick+up&ie=utf-8&oe=utf-8#channel=fs&q=nerf+gun+store+pick+up+today',
              'http://www.walmart.com/c/kp/nerf-guns',
              'http://www.walmart.com/ip/Nerf-N-Strike-Modulus-ECS-10-Blaster/45057744',
              'https://www.walmart.com/checkout/',
              'https://www.walmart.com/checkout/#checkout/sign-in',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=gloves+to+hide+the+fingerprint&ie=utf-8&oe=utf-8',
              'https://www.quora.com/What-gloves-dont-leave-any-fingerprints',
              'https://answers.yahoo.com/question/index?qid=20090531222708AA32Rs7']

link_w_sol = ['https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+install+aircrack&ie=utf-8&oe=utf-8',
              'http://askubuntu.com/questions/496585/how-to-install-aircrack',
              'https://www.google.com/?gws_rd=ssl',
              'https://www.google.com/?gws_rd=ssl#q=how+to+add+apt+repository',
              'http://askubuntu.com/questions/493460/how-to-install-add-apt-repository-using-the-terminal',
              'https://www.google.com/?gws_rd=ssl#q=aircrack+ppa+ubuntu+12.04',
              'https://launchpad.net/ubuntu/precise/+package/aircrack-ng',
              'http://askubuntu.com/questions/296269/problems-with-installing-aircrack-ng-on-ubuntu-12-04',
              'http://pastebin.com/EBniehm3',
              'http://pastebin.com/download.php?i=EBniehm3',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=remove+old+ubuntu+versions&ie=utf-8&oe=utf-8',
              'http://askubuntu.com/questions/2793/how-do-i-remove-or-hide-old-kernel-versions-to-clean-up-the-boot-menu',
              'http://ubuntu-tweak.com/',
              'https://www.google.com/search?q=poison+candy&ie=UTF-8&sa=Search&channel=fe&client=browser-ubuntu&hl=en&gws_rd=ssl',
              'https://www.google.com/search?q=poison+candy&ie=UTF-8&sa=Search&channel=fe&client=browser-ubuntu&hl=en&gws_rd=ssl#channel=fe&hl=en&q=toxic+waste+candy',
              'http://www.toxicwastecandy.com/',
              'http://www.amazon.com/TOXIC-WASTE-Hazardously-1-7-Ounce-Plastic/dp/B001AC8JL4',
              'https://www.google.com/search?q=toxic+waste+candy&client=browser-ubuntu&hs=dAi&channel=fe&hl=en&biw=638&bih=355&source=lnms&tbm=isch&sa=X&sqi=2&ved=0CAgQ_AUoA2oVChMIqtKl95T3yAIVCFoeCh3z8A0D',
              'https://www.google.com/search?q=toxic+waste+candy&client=browser-ubuntu&hs=dAi&channel=fe&hl=en&biw=638&bih=355&source=lnms&tbm=isch&sa=X&sqi=2&ved=0CAgQ_AUoA2oVChMIqtKl95T3yAIVCFoeCh3z8A0D#imgrc=Vx3VVkw9YAmvfM%3A',
              'http://www.marthasbackyard.co.nz/images/toxic%20waste%201.7%20oz.jpg',
              'https://www.google.com/?gws_rd=ssl',
              'https://www.google.com/?gws_rd=ssl#q=toxic+waste+candy+local+store',
              'http://www.toxicwastecandy.com/storeLocator.aspx',
              'http://www.toxicwastecandy.com/storeLocator.aspx?cid=13',
              'https://www.google.com/?gws_rd=ssl',
              'https://www.google.com/?gws_rd=ssl#q=poison+candies',
              'https://www.google.com/?gws_rd=ssl#q=poisoned+candies',
              'https://www.google.com/?gws_rd=ssl#q=painless+poisons+for+death',
              'http://listverse.com/2012/12/02/10-poisons-used-to-kill-people/',
              'https://www.google.com/?gws_rd=ssl',
              'https://www.google.com/?gws_rd=ssl#q=cyanide',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=arsenic&ie=utf-8&oe=utf-8',
              'https://www.google.com/search?client=ubuntu&channel=fs&q=mercury&ie=utf-8&oe=utf-8']

link_sol = {'1' : link_l_sol,
            '3' : link_w_sol}

domain_l = {'www.google.com' : 0, 'hackertarget.com' : 0, 'itswapshop.com' : 0, 'www.how-tofind.com' : 0, 'xeushack.com' : 0, 'security.stackexchange.com' : 0, 'breakthesecurity.cysecurity.org' : 0, 'wiki.skullsecurity.org' : 0, 'pastebin.com' : 0, 'listverse.com' : 0, 'criminalcasegame.wikia.com' : 0, 'www.therichest.com' : 0, 'www.hsph.harvard.edu' : 0, 'www.usatoday.com' : 0, 'lostallhope.com' : 0, 'nerf.hasbro.com' : 0, 'www.amazon.com' : 0, 'www.walmart.com' : 0, 'www.quora.com' : 0, 'answers.yahoo.com' : 0}

domain_w = {'www.google.com' : 0, 'askubuntu.com' : 0, 'launchpad.net' : 0, 'pastebin.com' : 0, 'ubuntu-tweak.com' : 0, 'www.toxicwastecandy.com' : 0, 'www.amazon.com' : 0, 'www.marthasbackyard.co.nz' : 0, 'listverse.com' : 0}

domain_list = {'1' : domain_l,
               '3' : domain_w}

weapon_l_sol = ['nerf gun', 'gun', 'nerf n-strike modulus ecs-10 blaster']
weapon_w_sol = ['toxic', 'toxic waste', 'poison', 'poison candy', 'toxic candy', 'poison']

weapon_sol = {'1' : weapon_l_sol,
              '3' : weapon_w_sol}

# look for solution file
link_filepath = "./5.2.2.3_link.txt"
weapon_filepath = "./5.2.2.3_weapon.txt"

if not (os.path.exists(link_filepath) and os.path.exists(weapon_filepath)): 
    print "0\tUnable to find your solution file(s).  Aborting."
else:

    # init return values
    score = 0;
    message = "\n";

    # suspect selection
    suspect_path = "./suspect_vm.txt"
    suspect = get_suspect_selection(suspect_path)

    # start grading
    link_submission = read_solution(link_filepath)
    weapon_submission = read_solution_string(weapon_filepath).lower()

    # grade search links
    find_i = 0  # index to track the order
    for i in range (0, len(link_submission)):
        if link_submission[i] == '':
            continue
        elif link_submission[i] in link_sol[suspect][find_i:]:
            find_i = link_sol[suspect].index(link_submission[i])
            score += 1
            message += "link " + str(i) + " passed\n"
            
            ds = link_submission[i].find('//')
            de = link_submission[i].find('/', ds+2)
            domain = link_submission[i][ds+2:de]
            domain_list[suspect][domain] += 1
            if (domain_list[suspect][domain] >= 2):
                score -= 1
                message += "duplicate domain\n"
        elif link_submission[i] in link_sol[suspect]:
            score += 0.5
            message += "link " + str(i) + " not in order, partially passed\n"
            
            ds = link_submission[i].find('//')
            de = link_submission[i].find('/', ds+2)
            domain = link_submission[i][ds+2:de]
            domain_list[suspect][domain] += 1
            if (domain_list[suspect][domain] >= 2):
                score -= 0.5
                message += "duplicate domain\n"
        else:
            message += "link " + str(i) + " failed\n"

    # if submitted more than 5 correct links
    if score >= 5:
        score = 5
    elif score <= 0:
        score = 0

    # grade weapon
    w_find = False
    for ws in weapon_sol[suspect]:
        if ws in weapon_submission:
            score += 5
            message += "weapon passed\n"
            w_find = True
            break
    if not w_find:
        message += "weapon failed\n"

    # for client in client_list:
    #     try:
    #         if client_submission.index(client) >= 0:
    #             count +=1
    #         else:
    #             message += "\nCannot find {0}".format(client)
    #     except ValueError:
    #         message += "\nCannot find {0}".format(client)
    
    # print result
    print str(score)+"\t"+message;
    
