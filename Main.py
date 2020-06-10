from StratifiedProgramLexer import StratifiedProgramLexer
from StratifiedProgramParser import StratifiedProgramParser
from StratifiedProgramInterpretVisitor import (
    StratifiedProgramInterpretVisitor, StratifiedProgramRuntimeError, StratifiedProgramInternalError
)

import argparse
import antlr4
from antlr4.error.ErrorListener import ErrorListener
from classes.OutPut import OutPut
from classes.Resolver import Resolver


class CountErrorListener(ErrorListener):
    """Count number of errors.

    Parser provides getNumberOfSyntaxErrors(), but the Lexer
    apparently doesn't provide an easy way to know if an error occured
    after the fact. Do the counting ourserves with a listener.
    """

    def __init__(self):
        super(CountErrorListener, self).__init__()
        self.count = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.count += 1


enable_typing = True


def main():
    # command line
    parser = argparse.ArgumentParser(description='Exec/Type mu files.')
    parser.add_argument('path', type=str,
                        help='file to exec and type')
    args = parser.parse_args()

    # lex and parse
    input_s = antlr4.FileStream(args.path, encoding='utf8')
    lexer = StratifiedProgramLexer(input_s)
    counter = CountErrorListener()
    lexer._listeners.append(counter)
    stream = antlr4.CommonTokenStream(lexer)
    parser = StratifiedProgramParser(stream)
    parser._listeners.append(counter)
    tree = parser.prog()
    if counter.count > 0:
        exit(3)  # Syntax or lexicography errors occured

    # interpret Visitor
    interpreter_visitor = StratifiedProgramInterpretVisitor()
    try:
        interpreter_visitor.visit(tree)
        memory = interpreter_visitor._memory
        rules = interpreter_visitor._rules

        resolver = Resolver()
        result = resolver.resolve(memory,rules)
        output = OutPut()
        output.setData(result)

        output.print()
    except StratifiedProgramRuntimeError as e:
        print(e.args[0])
        exit(1)
    except StratifiedProgramInternalError as e:
        print(e.args[0])
        exit(4)


if __name__ == '__main__':
    main()
