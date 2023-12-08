CC = gcc
CFLAGS = -O3 -Wall -std=c17 -pedantic -fopenmp
HEADERS = ${wildcard *.h}
OBJECTS = complex.o mandelbrot.o pgm.o main.o

all: main

main: ${OBJECTS} ${HEADERS}
	${CC} ${CFLAGS} -o $@ ${OBJECTS} -lm

%.o: %.c ${HEADERS}
	${CC} ${CFLAGS} -c $<

.PHONY: clean

clean:
	rm -rf *.o
