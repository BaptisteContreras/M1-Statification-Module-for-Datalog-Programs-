grammar StratifiedProgram;

prog: line+ EOF #progRule;


line
    : EDB       #edbLine
    | edbrule   #edbRuleLine
    | IDB       #idbLine
    | idbrule   #idbruleLine
    ;


args_l
    : args COM args_l #argList
    | args            #argAlone
    |                 #noArg
    ;

args
    : VARIABLE          #argVar
    | INT               #argInt
    | STRING            #argString
    | UNDERLINE         #argUnderLine
    ;

predicat:
    NAME OPAR args_l CPAR    #predBuilder;


body
    : predicat              #predicatWithoutList
    | NOT predicat          #notPredicatWithoutList
    | predicat COM body     #predicatWithList
    | NOT predicat COM body #notPredicatWithList
    ;

idbrule
    : predicat AFFECTATION body DOT #predIdbLine
    ;

edbrule
    : predicat DOT  #predEdbLine
    ;


EDB: '%edb';
IDB: '%idb';
OPAR : '(';
CPAR : ')';
COM : ',';
DOT: '.';
NOT: 'not';
QUOTE : '"';
AFFECTATION: ':-';
UNDERLINE: '_';

NAME
    : [A-Z][a-z]*
    ;

VARIABLE
    : [a-z]+[a-zA-Z]*
    ;

INT
 : [0-9]+
 ;

STRING
 : '"' (~["\r\n] | '""')* '"'
 ;


COMMENT
// # is a comment in Mini-C, and used for #include in real C so that we ignore #include statements
 : ('#' | '//') ~[\r\n]* -> skip
 ;

SPACE
 : [ \t\r\n] -> skip
 ;
