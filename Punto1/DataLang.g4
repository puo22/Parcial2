grammar DataLang;

// ---------- Reglas del parser ----------
program
  : statement (SEMI statement)* SEMI? EOF
  ;

statement
  : createStmt
  | readStmt
  | updateStmt
  | deleteStmt
  ;

// -------- CREATE --------
createStmt
  : BUILD TABLE ID WITH LPAREN colList RPAREN
  ;

colList
  : column (COMMA column)*
  ;

column
  : ID COLON type
  ;

type
  : NUMBER_T
  | TEXT_T
  | BOOL_T
  ;

// -------- READ --------
readStmt
  : GET FROM ID (WHERE condition)?
  ;

condition
  : ID opRel value
  ;

opRel
  : EQ
  | LT
  | GT
  | LE
  | GE
  | NEQ
  ;

// -------- UPDATE --------
updateStmt
  : UPDATE ID SET assignList (WHERE condition)?
  ;

assignList
  : assignment (COMMA assignment)*
  ;

assignment
  : ID ASSIGN value
  ;

// -------- DELETE --------
deleteStmt
  : ERASE FROM ID (WHERE condition)?
  ;

// -------- Valores y tokens --------
value
  : NUMBER
  | STRING
  | TRUE
  | FALSE
  ;


// ---------- TOKENS ----------

BUILD    : 'build';
TABLE    : 'table';
WITH     : 'with';
GET      : 'get';
FROM     : 'from';
WHERE    : 'where';
UPDATE   : 'update';
SET      : 'set';
ERASE    : 'erase';
TRUE     : 'true';
FALSE    : 'false';
NUMBER_T : 'number';
TEXT_T   : 'text';
BOOL_T   : 'bool';

EQ   : '=';
LT   : '<';
GT   : '>';
LE   : '<=';
GE   : '>=';
NEQ  : '!=';
ASSIGN : '=';
COLON  : ':';
COMMA  : ',';
LPAREN : '(';
RPAREN : ')';
SEMI   : ';';

ID      : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER  : [0-9]+;
STRING  : '"' (~["\r\n])* '"';
WS      : [ \t\r\n]+ -> skip;
