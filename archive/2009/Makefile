HOST=kendall.gtnoise.net
#DIR=www/classes/CS7260-SP07
DIR=/usr/local/www/apache22/data/classes/cs6262/spring_2009/

LDIR=$(DIR)/lectures/

SRCS = $(wildcard *.*)
LECTURES = lectures/*.pdf lectures/*.ppt

all: web

web: local
	scp -C $(SRCS) Makefile $(HOST):$(DIR)
	rsync -avz -e ssh -r $(LECTURES) $(HOST):$(LDIR)/

local: $(SRCS)
	./datereplace.rb index.html
	./mklectures.rb > syllabus.html
