CC = gcc
CFLAGS = -O3 -fPIC -std=c17 -pedantic

all: libtree.dll

libtree.dll: tree.o
	${CC} ${CFLAGS} -shared $< -o $@

%.o: %.c %.h
	${CC} ${CFLAGS} -c $<

.PHONY: clean all

clean:
	rm -rf *.o
