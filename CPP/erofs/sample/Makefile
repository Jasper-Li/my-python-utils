CXX = clang++
CPPFLAGS = -Wall 
CPPFLAGS += -std=c++14
LDLIBS = -lstdc++ -lm

CPPHEADERS = $(wildcard *.h)
CPPFILES = $(wildcard *.cpp)
OBJFILES = $(CPPFILES:.cpp=.o)
OUT      = main.exe


$(OUT): $(OBJFILES) 
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)
	./$(OUT)

$(OBJFILES): $(CPPHEADERS)

.PHONY: clean
clean:
	rm -f $(OBJFILES) $(OUT) 
