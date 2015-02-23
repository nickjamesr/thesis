cflags = 
lflags = -lgsl -lgslcblas -lm -lverification -lbosonsamp -lqp

bin/update : src/update.cc src/heads/update.h
	g++ -o bin/update src/update.cc $(cflags) $(lflags)
