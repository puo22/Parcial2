# Generated from DataLang.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,3,0,38,8,0,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,5,3,59,8,3,10,3,12,3,62,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,3,6,75,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,9,3,9,89,8,9,1,10,1,10,1,10,5,10,94,8,10,10,10,12,10,97,9,10,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,108,8,12,1,13,
        1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,3,1,0,12,
        14,1,0,15,20,2,0,10,11,28,29,107,0,28,1,0,0,0,2,45,1,0,0,0,4,47,
        1,0,0,0,6,55,1,0,0,0,8,63,1,0,0,0,10,67,1,0,0,0,12,69,1,0,0,0,14,
        76,1,0,0,0,16,80,1,0,0,0,18,82,1,0,0,0,20,90,1,0,0,0,22,98,1,0,0,
        0,24,102,1,0,0,0,26,109,1,0,0,0,28,33,3,2,1,0,29,30,5,26,0,0,30,
        32,3,2,1,0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,
        0,34,37,1,0,0,0,35,33,1,0,0,0,36,38,5,26,0,0,37,36,1,0,0,0,37,38,
        1,0,0,0,38,39,1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,46,3,4,2,0,42,
        46,3,12,6,0,43,46,3,18,9,0,44,46,3,24,12,0,45,41,1,0,0,0,45,42,1,
        0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,3,1,0,0,0,47,48,5,1,0,0,48,
        49,5,2,0,0,49,50,5,27,0,0,50,51,5,3,0,0,51,52,5,24,0,0,52,53,3,6,
        3,0,53,54,5,25,0,0,54,5,1,0,0,0,55,60,3,8,4,0,56,57,5,23,0,0,57,
        59,3,8,4,0,58,56,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,
        0,61,7,1,0,0,0,62,60,1,0,0,0,63,64,5,27,0,0,64,65,5,22,0,0,65,66,
        3,10,5,0,66,9,1,0,0,0,67,68,7,0,0,0,68,11,1,0,0,0,69,70,5,4,0,0,
        70,71,5,5,0,0,71,74,5,27,0,0,72,73,5,6,0,0,73,75,3,14,7,0,74,72,
        1,0,0,0,74,75,1,0,0,0,75,13,1,0,0,0,76,77,5,27,0,0,77,78,3,16,8,
        0,78,79,3,26,13,0,79,15,1,0,0,0,80,81,7,1,0,0,81,17,1,0,0,0,82,83,
        5,7,0,0,83,84,5,27,0,0,84,85,5,8,0,0,85,88,3,20,10,0,86,87,5,6,0,
        0,87,89,3,14,7,0,88,86,1,0,0,0,88,89,1,0,0,0,89,19,1,0,0,0,90,95,
        3,22,11,0,91,92,5,23,0,0,92,94,3,22,11,0,93,91,1,0,0,0,94,97,1,0,
        0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,21,1,0,0,0,97,95,1,0,0,0,98,99,
        5,27,0,0,99,100,5,21,0,0,100,101,3,26,13,0,101,23,1,0,0,0,102,103,
        5,9,0,0,103,104,5,5,0,0,104,107,5,27,0,0,105,106,5,6,0,0,106,108,
        3,14,7,0,107,105,1,0,0,0,107,108,1,0,0,0,108,25,1,0,0,0,109,110,
        7,2,0,0,110,27,1,0,0,0,8,33,37,45,60,74,88,95,107
    ]

class DataLangParser ( Parser ):

    grammarFileName = "DataLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'build'", "'table'", "'with'", "'get'", 
                     "'from'", "'where'", "'update'", "'set'", "'erase'", 
                     "'true'", "'false'", "'number'", "'text'", "'bool'", 
                     "<INVALID>", "'<'", "'>'", "'<='", "'>='", "'!='", 
                     "<INVALID>", "':'", "','", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "BUILD", "TABLE", "WITH", "GET", "FROM", 
                      "WHERE", "UPDATE", "SET", "ERASE", "TRUE", "FALSE", 
                      "NUMBER_T", "TEXT_T", "BOOL_T", "EQ", "LT", "GT", 
                      "LE", "GE", "NEQ", "ASSIGN", "COLON", "COMMA", "LPAREN", 
                      "RPAREN", "SEMI", "ID", "NUMBER", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_createStmt = 2
    RULE_colList = 3
    RULE_column = 4
    RULE_type = 5
    RULE_readStmt = 6
    RULE_condition = 7
    RULE_opRel = 8
    RULE_updateStmt = 9
    RULE_assignList = 10
    RULE_assignment = 11
    RULE_deleteStmt = 12
    RULE_value = 13

    ruleNames =  [ "program", "statement", "createStmt", "colList", "column", 
                   "type", "readStmt", "condition", "opRel", "updateStmt", 
                   "assignList", "assignment", "deleteStmt", "value" ]

    EOF = Token.EOF
    BUILD=1
    TABLE=2
    WITH=3
    GET=4
    FROM=5
    WHERE=6
    UPDATE=7
    SET=8
    ERASE=9
    TRUE=10
    FALSE=11
    NUMBER_T=12
    TEXT_T=13
    BOOL_T=14
    EQ=15
    LT=16
    GT=17
    LE=18
    GE=19
    NEQ=20
    ASSIGN=21
    COLON=22
    COMMA=23
    LPAREN=24
    RPAREN=25
    SEMI=26
    ID=27
    NUMBER=28
    STRING=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(DataLangParser.StatementContext,i)


        def EOF(self):
            return self.getToken(DataLangParser.EOF, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(DataLangParser.SEMI)
            else:
                return self.getToken(DataLangParser.SEMI, i)

        def getRuleIndex(self):
            return DataLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = DataLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.statement()
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 29
                    self.match(DataLangParser.SEMI)
                    self.state = 30
                    self.statement() 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 36
                self.match(DataLangParser.SEMI)


            self.state = 39
            self.match(DataLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def createStmt(self):
            return self.getTypedRuleContext(DataLangParser.CreateStmtContext,0)


        def readStmt(self):
            return self.getTypedRuleContext(DataLangParser.ReadStmtContext,0)


        def updateStmt(self):
            return self.getTypedRuleContext(DataLangParser.UpdateStmtContext,0)


        def deleteStmt(self):
            return self.getTypedRuleContext(DataLangParser.DeleteStmtContext,0)


        def getRuleIndex(self):
            return DataLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = DataLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.createStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.readStmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.updateStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.deleteStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BUILD(self):
            return self.getToken(DataLangParser.BUILD, 0)

        def TABLE(self):
            return self.getToken(DataLangParser.TABLE, 0)

        def ID(self):
            return self.getToken(DataLangParser.ID, 0)

        def WITH(self):
            return self.getToken(DataLangParser.WITH, 0)

        def LPAREN(self):
            return self.getToken(DataLangParser.LPAREN, 0)

        def colList(self):
            return self.getTypedRuleContext(DataLangParser.ColListContext,0)


        def RPAREN(self):
            return self.getToken(DataLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return DataLangParser.RULE_createStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateStmt" ):
                listener.enterCreateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateStmt" ):
                listener.exitCreateStmt(self)




    def createStmt(self):

        localctx = DataLangParser.CreateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_createStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(DataLangParser.BUILD)
            self.state = 48
            self.match(DataLangParser.TABLE)
            self.state = 49
            self.match(DataLangParser.ID)
            self.state = 50
            self.match(DataLangParser.WITH)
            self.state = 51
            self.match(DataLangParser.LPAREN)
            self.state = 52
            self.colList()
            self.state = 53
            self.match(DataLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataLangParser.ColumnContext)
            else:
                return self.getTypedRuleContext(DataLangParser.ColumnContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DataLangParser.COMMA)
            else:
                return self.getToken(DataLangParser.COMMA, i)

        def getRuleIndex(self):
            return DataLangParser.RULE_colList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColList" ):
                listener.enterColList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColList" ):
                listener.exitColList(self)




    def colList(self):

        localctx = DataLangParser.ColListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_colList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.column()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 56
                self.match(DataLangParser.COMMA)
                self.state = 57
                self.column()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DataLangParser.ID, 0)

        def COLON(self):
            return self.getToken(DataLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(DataLangParser.TypeContext,0)


        def getRuleIndex(self):
            return DataLangParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = DataLangParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(DataLangParser.ID)
            self.state = 64
            self.match(DataLangParser.COLON)
            self.state = 65
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_T(self):
            return self.getToken(DataLangParser.NUMBER_T, 0)

        def TEXT_T(self):
            return self.getToken(DataLangParser.TEXT_T, 0)

        def BOOL_T(self):
            return self.getToken(DataLangParser.BOOL_T, 0)

        def getRuleIndex(self):
            return DataLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = DataLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(DataLangParser.GET, 0)

        def FROM(self):
            return self.getToken(DataLangParser.FROM, 0)

        def ID(self):
            return self.getToken(DataLangParser.ID, 0)

        def WHERE(self):
            return self.getToken(DataLangParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(DataLangParser.ConditionContext,0)


        def getRuleIndex(self):
            return DataLangParser.RULE_readStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)




    def readStmt(self):

        localctx = DataLangParser.ReadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_readStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(DataLangParser.GET)
            self.state = 70
            self.match(DataLangParser.FROM)
            self.state = 71
            self.match(DataLangParser.ID)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 72
                self.match(DataLangParser.WHERE)
                self.state = 73
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DataLangParser.ID, 0)

        def opRel(self):
            return self.getTypedRuleContext(DataLangParser.OpRelContext,0)


        def value(self):
            return self.getTypedRuleContext(DataLangParser.ValueContext,0)


        def getRuleIndex(self):
            return DataLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = DataLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(DataLangParser.ID)
            self.state = 77
            self.opRel()
            self.state = 78
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpRelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(DataLangParser.EQ, 0)

        def LT(self):
            return self.getToken(DataLangParser.LT, 0)

        def GT(self):
            return self.getToken(DataLangParser.GT, 0)

        def LE(self):
            return self.getToken(DataLangParser.LE, 0)

        def GE(self):
            return self.getToken(DataLangParser.GE, 0)

        def NEQ(self):
            return self.getToken(DataLangParser.NEQ, 0)

        def getRuleIndex(self):
            return DataLangParser.RULE_opRel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpRel" ):
                listener.enterOpRel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpRel" ):
                listener.exitOpRel(self)




    def opRel(self):

        localctx = DataLangParser.OpRelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_opRel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(DataLangParser.UPDATE, 0)

        def ID(self):
            return self.getToken(DataLangParser.ID, 0)

        def SET(self):
            return self.getToken(DataLangParser.SET, 0)

        def assignList(self):
            return self.getTypedRuleContext(DataLangParser.AssignListContext,0)


        def WHERE(self):
            return self.getToken(DataLangParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(DataLangParser.ConditionContext,0)


        def getRuleIndex(self):
            return DataLangParser.RULE_updateStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStmt" ):
                listener.enterUpdateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStmt" ):
                listener.exitUpdateStmt(self)




    def updateStmt(self):

        localctx = DataLangParser.UpdateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_updateStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(DataLangParser.UPDATE)
            self.state = 83
            self.match(DataLangParser.ID)
            self.state = 84
            self.match(DataLangParser.SET)
            self.state = 85
            self.assignList()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 86
                self.match(DataLangParser.WHERE)
                self.state = 87
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataLangParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(DataLangParser.AssignmentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DataLangParser.COMMA)
            else:
                return self.getToken(DataLangParser.COMMA, i)

        def getRuleIndex(self):
            return DataLangParser.RULE_assignList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignList" ):
                listener.enterAssignList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignList" ):
                listener.exitAssignList(self)




    def assignList(self):

        localctx = DataLangParser.AssignListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.assignment()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 91
                self.match(DataLangParser.COMMA)
                self.state = 92
                self.assignment()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DataLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(DataLangParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(DataLangParser.ValueContext,0)


        def getRuleIndex(self):
            return DataLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = DataLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DataLangParser.ID)
            self.state = 99
            self.match(DataLangParser.ASSIGN)
            self.state = 100
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ERASE(self):
            return self.getToken(DataLangParser.ERASE, 0)

        def FROM(self):
            return self.getToken(DataLangParser.FROM, 0)

        def ID(self):
            return self.getToken(DataLangParser.ID, 0)

        def WHERE(self):
            return self.getToken(DataLangParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(DataLangParser.ConditionContext,0)


        def getRuleIndex(self):
            return DataLangParser.RULE_deleteStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStmt" ):
                listener.enterDeleteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStmt" ):
                listener.exitDeleteStmt(self)




    def deleteStmt(self):

        localctx = DataLangParser.DeleteStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_deleteStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(DataLangParser.ERASE)
            self.state = 103
            self.match(DataLangParser.FROM)
            self.state = 104
            self.match(DataLangParser.ID)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 105
                self.match(DataLangParser.WHERE)
                self.state = 106
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(DataLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(DataLangParser.STRING, 0)

        def TRUE(self):
            return self.getToken(DataLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(DataLangParser.FALSE, 0)

        def getRuleIndex(self):
            return DataLangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = DataLangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 805309440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





