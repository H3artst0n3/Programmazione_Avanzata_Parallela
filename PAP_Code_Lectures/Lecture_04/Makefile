CC = gcc
libmode = dinamic
LIB = lib
HEADERS = ${wildcard *.h}

all: main

ifeq "static" "${libmode}"
main: main.o ${LIB}/libbst.a
	${CC} -o $@ $< -L./${LIB} -lbst	
else
main: main.o ${LIB}/libbstd.so 
	${CC} -o $@ $< -L./${LIB} -lbstd
endif

main.o: main.c node.h tree.h
	${CC} -c $<
	
%.o: %.c ${HEADERS}
ifeq "static" "${libmode}"
	${CC} -c $<	
else
	${CC} -c -fPIC $<
endif

${LIB}:
	mkdir $@

${LIB}/libbst.a: tree.o node.o ${LIB}
	ar rs $@ $< node.o

${LIB}/libbstd.so: node.o tree.o ${LIB}
	${CC} -shared -o $@ $< tree.o 	

.PHONY: clean clean-all
clean: 
	rm -f *.o
	
clean-all: clean
	rm -rf ${LIB}/*.a ${LIB}/*.so
	rmdir ${LIB}
	rm main
