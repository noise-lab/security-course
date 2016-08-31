all: web 

web: www/index.html
	rsync -avz -e ssh www/ portal.cs.princeton.edu:/n/fs/csweb/courses/archive/fall16/cos432/

slides:
	rsync -avz lectures/ ~/Dropbox/Classes/COS432/Fall2016/slides/lectures/
	rsync -avz precepts/ ~/Dropbox/Classes/COS432/Fall2016/slides/precepts/

solutions:
	rsync -avz solutions/ ~/Dropbox/Classes/COS461/Spring2016/solutions/
