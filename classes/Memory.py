class Memory:

    def __init__(self):
        self._list = dict()  # list of all encountered predicate

    def addPredicate(self, predicate):
        """ Add a given predicate in our list (if its not already exists, based on its name)"""
        if self.canAddPredicate(predicate):
            self._list[predicate.getName()].append(predicate)
            return True
        return False

    def canAddPredicate(self, predicate):
        """' Test if a given predicate already exists in our list (ONLY BASED ON ITS NAME) """

        if not any(predicate.getName() in s for s in self._list):
            self._list[predicate.getName()] = []
        return True

    def isValidPredicate(self, predicate):
        """ Test if a given predicate already exists in our list but with a different number of args """
        for p in self._list:
            if p.isNameEqual(predicate) and p.isValidDoublon(predicate):
                return False

        return True

    def getPredicate(self, name, nbArgs):
        if any(name in s for s in self._list):
            for i in self._list[name]:
                if i.getArgsNumber() == nbArgs:
                    return i
        return False

    def getPredicates(self):
        return self._list

    def __str__(self) -> str:
        return "\n".join(map(lambda e: e.__str__(), self._list))
