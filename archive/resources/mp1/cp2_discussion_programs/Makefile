CC := gcc
CFLAGS := -m32 -static

programs:= demo

.PHONY: default clean install uninstall

demo: CFLAGS += -fno-stack-protector

demo: demo.c

clean:
	rm -f $(programs)
