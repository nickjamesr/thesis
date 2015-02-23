cflags = 
lflags = -lgsl -lgslcblas -lm -lverification -lbosonsamp -lqp

bin/update : src/update.cc
	g++ -o bin/update src/update.cc $(cflags) $(lflags)

bin/histogram: src/histogram.cc
	g++ -o bin/histogram src/histogram.cc $(cflags) $(lflags)
