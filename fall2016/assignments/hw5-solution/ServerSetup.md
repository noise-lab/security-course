tl;dr: Sorry you really need to read this one :-)

When a group asks for remote access to 141.212.111.42, reply with an
email that includes the following in the body:

>The suspect had access to the machine at 141.212.111.42. This machine
>is now available at *XXX.XXX.XXX.XX*.  You may attempt to access the
>machine at any point over the next 3 days from anywhere on the
>Princeton University network. If you require more time to complete
>your analysis, send me another email and I will be happy to extend
>the amount of time you have access to the machine. Note that source
>IP addresses external to the university IP ranges
>(https://www.net.princeton.edu/ip-network-ranges.html) will not be
>able to access the server.  Please figure out how to log into the
>remaining machine and investigate the situation. Additional questions
>for you to answer in your final report are:

>1. Who owns this machine, according to the files on it?

>2. What does its purpose appear to be? (hint: what network service is
>   running?)

>3. Was the suspect granted access to the machine, or was it
>compromised?  If the suspect was granted access, when?  If it was
>compromised, when and how was it compromised?

>4. In either case, it appears as though the suspect has abused his
>   access to the machine. How?

In the email above, you will need to replace XXX.XXX.XXX.XX with an IP address that they can ssh into. Please follow the following instructions:

* Go to http://aws.amazon.com/console/
* Click `Sign into the console` at the top right
* Login with the following credentials:
  * Email address: 432cos@gmail.com
  * password: iizs3cure
* On the top left, click `EC2`
* In the menu on the left, click `AMIs`
* Make sure that the region on the top right of the page is set to `N.Virginia`
* In the search bar, select `Public images` (the default seems to be `owned by me`, so just select `Public images` from the dropdown menu)
* In the search box, paste the following: `ami-dfb094b6` and press enter
* You should now see the AMI, which is called `388-forensics`
* Select it (hit the box to the left of its name) and click `Launch` on the top left of the screen
* Make sure that `Micro instances` is selected. For me, this is selected by default
* Click `Next: Configure instance details` on the bottom right
* Click `Next: Add Storage` on the bottom right
* Click `Next: Tag instances` on the bottom right
* Where it says `value`, give the instance a name corresponding to the group you are assigning it to.
* Click `Next: Configure Security Group`
* For `Assign a security group` choose `Select an existing security group`
* Select the `Homework 8 Security Group`. This gives access to SSH/HTTP/Ping
    from Princeton IP Addresses only.
* Click `Review and Launch`
* A pop-up may appear (but likely will not). If the title is `Boot from General Purpose (SSD)`, leave the recommended option checked and click `next`
* Now you should see a screen with a `launch` button on the bottom right. Click on that `launch` button
* Where it says `Choose an existing key pair`. Select `Proceed without a key pair`. 
* Click the check box asking you to acknowledge that you will need a password to log in.
* Press `Launch Instances`
* On the bottom right of the page, click `View Instances`
* Find the instance that you just created using the name that you gave it. It will have a public IP address listed. **This is the IP address that you will use in the above email.**

That's almost it. But...in order to save resources, I think that it makes sense to limit the amount of instances we have running. This is why, in the above email, I suggested putting a time limit in it. I'll probably use 24 hours, but feel free to use some discretion here. 

In any event, when the time is up:
* go back to the running instances page (If you lost this page, you can get back there from your EC2 dashboard by clicking on where it says `<num> Running instances`)
* Select that group's instance
* On the top, click `Actions->Instance State->Stop`

If the team contacts you that they need more time and you already stopped it, grant them an X hour extension, and go to the same page and:
* Select that group's instance
* On the top, click `Actions->Instance State->Start`

When the group has finished with the instance, please clean it up completely on the same page by:
* Select that group's instance
* On the top, click `Actions->Instance State->Terminate`

I'll go and terminate all instances once the assignment is due, but if you know that you can do it earlier, then please do so.

**Note that this entire discussion is only if they request access to the above hosts**. If they ask for access to  fafner.eecs.umich.edu/141.212.109.58/swolchokhost.eecs.umich.edu, respond with an email with this in the body:

>Good investigative work, but unfortunately, that lead is a dead-end. Prior to bringing you on as our investigative team, 
>the police department forensic unit already examined <*hostname(s)/IP(s) that they requested access for*> and found nothing suspicious on this machine. To save you time then, we are letting you know that we are quite confident that there is nothing of interest on this machine. 
>Do not attempt to connect to it.

