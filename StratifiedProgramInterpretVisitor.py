from StratifiedProgramVisitor import StratifiedProgramVisitor
from classes.Memory import Memory
from classes.Predicate import Predicate
from classes.Rule import Rule


# Visitor to *interpret* StratifiedProgram files


class StratifiedProgramRuntimeError(Exception):
    pass


class StratifiedProgramInternalError(Exception):
    pass


class StratifiedProgramInterpretVisitor(StratifiedProgramVisitor):

    def __init__(self):
        self._memory = Memory()  # store all variable ids and values.
        self._rules = []
        self.has_edb = False
        self.has_idb = False

    # visitors for args declarations

    def visitArgVar(self, ctx):
        return ctx.VARIABLE().getText()  # temporaire

    def visitArgInt(self, ctx):
        return ctx.INT().getText()

    def visitArgString(self, ctx):
        return ctx.STRING().getText()

    def visitArgUnderLine(self, ctx):
        return ctx.UNDERLINE().getText()

    def visitArgAlone(self, ctx):

        return [self.visit(ctx.args())]

    def visitArgList(self, ctx):
        return [self.visit(ctx.args())] + self.visit(ctx.args_l())

    def visitNoArg(self, ctx):
        return []

    def visitPredEdbLine(self, ctx):
        ret = self.visit(ctx.predicat())
        if self._memory.isValidPredicate(ret):
            return ret
        else:
            raise StratifiedProgramRuntimeError("Several predicate declaration")

    def visitEdbRuleLine(self, ctx):
        if self.has_edb & (not self.has_idb):
            ret = self.visit(ctx.edbrule())
        else:
            raise StratifiedProgramRuntimeError("Not correct edb declaration")

    def visitPredBuilder(self, ctx):

        name = ctx.NAME().getText()
        args = self.visit(ctx.args_l())
        predicate = Predicate(name)
        predicate.args = args
        return predicate

    def visitNotPredicatWithList(self, ctx):
        tmp = self.visit(ctx.predicat())
        tmp.negated = True
        return [tmp] + self.visit(ctx.body())

    def visitPredicatWithList(self, ctx):
        return [self.visit(ctx.predicat())] + self.visit(ctx.body())

    def visitNotPredicatWithoutList(self, ctx):
        tmp = self.visit(ctx.predicat())
        tmp.negated = True
        return [tmp]

    def visitPredicatWithoutList(self, ctx):
        return [self.visit(ctx.predicat())]

    def visitPredIdbLine(self, ctx):

        head = self.visit(ctx.predicat())
        self._memory.addPredicate(head)
        subGoal = self.visit(ctx.body())

        return Rule(head, subGoal)

    def visitIdbruleLine(self, ctx):
        if self.has_idb:
            self._rules.append(self.visit(ctx.idbrule()))
        else:
            raise StratifiedProgramRuntimeError("Not correct idb declaration")

    def visitEdbLine(self, ctx):
        self.has_edb = True

    def visitIdbLine(self, ctx):
        self.has_idb = True

    def visitProgRule(self, ctx):
        for line in ctx.line():
            self.visit(line)

        if not (self.has_edb | self.has_idb):
            # A program without a main function is compilable (hence
            # it's not a typing error per se), but not executable,
            # hence we consider it a runtime error.
            raise StratifiedProgramRuntimeError("No idb or cdb in file")
        return
