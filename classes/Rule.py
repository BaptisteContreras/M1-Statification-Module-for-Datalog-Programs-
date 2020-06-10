class Rule:

    def __init__(self, head, body):
        self.head = head # predicate
        self.subGoals = body # list of predicate

    def getHead(self):
        return  self.head

    def getSubgoals(self):
        return self.subGoals

    def isInSubgoals(self, predicate):
        for p in self.subGoals:
            if p.getName() == predicate.getName():
                return True
        return False

    def isNameInSubgoals(self, predicateName):
        for p in self.subGoals:
            if p.getName() == predicateName:
                return p
        return False

    def getNegatedSubgoals(self):
        return filter(lambda e: e.isNegated(), self.subGoals)

    def getNoNegatedSubgoals(self):
        return filter(lambda e: not e.isNegated(), self.subGoals)

    def isHead(self, predicate):
        return predicate.getName() == self.head.getName()

    def isHeadStr(self, predicateName):
        return predicateName == self.head.getName()

    def _displayPredicate(self,preds):
        if len(preds) == 0:
            return preds[0].__str__()
        else:
            result = ""
            for i in range (len(preds)):
                result += preds[i].__str__()
                if i + 1 != len(preds):
                    result += ", "
            return result


    def __str__(self) -> str:
        return self.getHead().__str__() + " :- " + self._displayPredicate(self.subGoals)



