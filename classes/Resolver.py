class Resolver:

    def __init__(self):
        self.stratum = dict()

    def resolve(self, memory, rules):
        self.stratum = dict()

        predicates = memory.getPredicates()

        # Init
        for (i, predicates) in predicates.items():
            for predicate in predicates:
                self.stratum[predicate.getName()] = 1

        change = True

        while self.canContinue(change,len(self.stratum)):
            change = False
            for rule in rules:
                change |= self.goThroughtNegatedSubgoal(rule.getNegatedSubgoals(), rule.getHead())
                change |= self.goThroughtSubgoal(rule.getNoNegatedSubgoals(), rule.getHead())

        result = self.getRulesLevel(rules)

        return result


    def canContinue(self, change, nbPredicate):
        if not change:
            return False
        for s in self.stratum:
            if self.stratum[s] > nbPredicate:
                return False
        return True

    def goThroughtNegatedSubgoal(self, subgoals, head):
        changed = False
        for subgoal in subgoals:
            last = self.stratum[head.getName()]
            if subgoal.getName() in self.stratum:
                self.stratum[head.getName()] = max(self.stratum[head.getName()], 1+self.stratum[subgoal.getName()])
            changed |= last != self.stratum[head.getName()]

        return changed

    def goThroughtSubgoal(self, subgoals,head):
        changed = False
        for subgoal in subgoals:
            last = self.stratum[head.getName()]
            if subgoal.getName() in self.stratum:
                self.stratum[head.getName()] = max(self.stratum[head.getName()], self.stratum[subgoal.getName()])

            changed |= last != self.stratum[head.getName()]

        return changed

    def getRulesLevel(self,rules):
        levels = dict()
        for (predicate, level) in self.stratum.items():
            currentRules = self.getRuleWithHead(predicate, rules)
            if currentRules:
                if level in levels:
                    for currentRule in currentRules:
                        levels[level].append(currentRule)
                else:
                    levels[level] = currentRules
        return levels



    def getRuleWithHead(self, head, rules):
        tmp = []
        for rule in rules:
            if rule.isHeadStr(head):
                tmp.append(rule)
        if len(tmp) == 0:
            return False
        return tmp