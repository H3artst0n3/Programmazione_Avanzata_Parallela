CC = gcc
PROG = main

all: main

main: main.o lib/libbst.a
	${CC} -o $@ $< -L./lib -lbst

main.o: main.c node.h tree.h
	${CC} -c $<
	
node.o: node.c node.h
	${CC} -c $<

tree.o: tree.c tree.h
	${CC} -c $<

lib:
	mkdir lib

lib/libbst.a: tree.o node.o lib
	ar rs $@ $< node.o

clean: 
	rm -f *.o
	rm -f ${PROG}
