class Predicate:

    def __init__(self, name, negated=False):
        self.name = name  # String
        self.args = dict()  # dict [argName1 : argValue1, argName2 : argValue2]
        self.negated = negated  # True if "not" was found before this predicate

    def isNegated(self):
        return self.negated

    def getName(self):
        return self.name + "-" + str(self.getArgsNumber())

    def getArgs(self):
        return self.args

    def getArgs(self, argName):
        return self.args[argName]

    def getArgsNumber(self):
        return len(self.args)

    def isNameEqual(self, predicate):
        return predicate.getName() == self.name

    def isNameEqualStr(self, name):
        return name == self.name

    def isSame(self, predicate):
        return self.isNameEqual(predicate) and predicate.getArgsNumber() == self.getArgsNumber()

    def isSemanticalyEquals(self, predicate):
        return self.isSame(predicate) and predicate.isNegated() == self.negated

    def isValidDoublon(self, doublon):
        return self.isNameEqual(doublon) and not self.isSame(doublon)

    def _displayArgs(self, args):
        if len(args) == 0:
            return ""
        if len(args) == 1:
            return args[0].__str__()
        else:
            result = ""
            for i in range(len(args)):
                result += args[i].__str__()
                if i + 1 != len(args):
                    result += ","
            return result

    def __str__(self) -> str:
        str = ""
        if self.negated:
            str += "not "
        return str + self.name + "(" + self._displayArgs(self.args) + ")"
