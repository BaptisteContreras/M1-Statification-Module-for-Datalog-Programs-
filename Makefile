PACKAGE = StratifiedProgram
MAINFILE = Main
#change with your own name:
MYNAME = p1
DIR = $(shell basename $(PWD))
PYTEST_OPTS = 

TESTFILE?=test/test.txt

ifndef ANTLR4
abort:
	$(error variable ANTLR4 is not set)
endif

all: run

StratifiedProgramLexer.py StratifiedProgramParser.py: $(PACKAGE).g4
	$(ANTLR4) $< -Dlanguage=Python3 -visitor -no-listener

deps: StratifiedProgramLexer.py StratifiedProgramParser.py StratifiedProgramVisitor.py

run: $(MAINFILE).py deps
	python3  $< $(TESTFILE)

# tests all files in ex/test*.c
tests: test_interpreter.py deps
	python3 -m pytest $(PYTEST_OPTS) -v --failed-first $< \
	        --cov=$(PWD) --cov-report=term --cov-report=html 

tar: clean
	cd ..; tar cvfz $(DIR)-$(MYNAME).tgz $(DIR) --transform 's/$(DIR)/$(DIR)-$(MYNAME)/'
	@echo "Created ../$(DIR)-$(MYNAME).tgz"

clean:
	rm -rf *~ $(PACKAGE)Parser.py $(PACKAGE)Lexer.py $(PACKAGE)Visitor.py *.pyc *.tokens  __pycache* ex/*~ .cache* ex-types/*~ *.interp *.diff log*.txt .coverage htmlcov/ .pytest_cache/
