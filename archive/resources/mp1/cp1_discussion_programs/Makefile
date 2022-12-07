CC := gcc
CFLAGS := -m32 -static

programs:= demo

.PHONY: default clean install uninstall

demo: CFLAGS +=

demo: demo.c demo.S

clean:
	rm -f $(programs)
