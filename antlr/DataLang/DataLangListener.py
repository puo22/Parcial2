# Generated from DataLang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .DataLangParser import DataLangParser
else:
    from DataLangParser import DataLangParser

# This class defines a complete listener for a parse tree produced by DataLangParser.
class DataLangListener(ParseTreeListener):

    # Enter a parse tree produced by DataLangParser#program.
    def enterProgram(self, ctx:DataLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by DataLangParser#program.
    def exitProgram(self, ctx:DataLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by DataLangParser#statement.
    def enterStatement(self, ctx:DataLangParser.StatementContext):
        pass

    # Exit a parse tree produced by DataLangParser#statement.
    def exitStatement(self, ctx:DataLangParser.StatementContext):
        pass


    # Enter a parse tree produced by DataLangParser#createStmt.
    def enterCreateStmt(self, ctx:DataLangParser.CreateStmtContext):
        pass

    # Exit a parse tree produced by DataLangParser#createStmt.
    def exitCreateStmt(self, ctx:DataLangParser.CreateStmtContext):
        pass


    # Enter a parse tree produced by DataLangParser#colList.
    def enterColList(self, ctx:DataLangParser.ColListContext):
        pass

    # Exit a parse tree produced by DataLangParser#colList.
    def exitColList(self, ctx:DataLangParser.ColListContext):
        pass


    # Enter a parse tree produced by DataLangParser#column.
    def enterColumn(self, ctx:DataLangParser.ColumnContext):
        pass

    # Exit a parse tree produced by DataLangParser#column.
    def exitColumn(self, ctx:DataLangParser.ColumnContext):
        pass


    # Enter a parse tree produced by DataLangParser#type.
    def enterType(self, ctx:DataLangParser.TypeContext):
        pass

    # Exit a parse tree produced by DataLangParser#type.
    def exitType(self, ctx:DataLangParser.TypeContext):
        pass


    # Enter a parse tree produced by DataLangParser#readStmt.
    def enterReadStmt(self, ctx:DataLangParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by DataLangParser#readStmt.
    def exitReadStmt(self, ctx:DataLangParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by DataLangParser#condition.
    def enterCondition(self, ctx:DataLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by DataLangParser#condition.
    def exitCondition(self, ctx:DataLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by DataLangParser#opRel.
    def enterOpRel(self, ctx:DataLangParser.OpRelContext):
        pass

    # Exit a parse tree produced by DataLangParser#opRel.
    def exitOpRel(self, ctx:DataLangParser.OpRelContext):
        pass


    # Enter a parse tree produced by DataLangParser#updateStmt.
    def enterUpdateStmt(self, ctx:DataLangParser.UpdateStmtContext):
        pass

    # Exit a parse tree produced by DataLangParser#updateStmt.
    def exitUpdateStmt(self, ctx:DataLangParser.UpdateStmtContext):
        pass


    # Enter a parse tree produced by DataLangParser#assignList.
    def enterAssignList(self, ctx:DataLangParser.AssignListContext):
        pass

    # Exit a parse tree produced by DataLangParser#assignList.
    def exitAssignList(self, ctx:DataLangParser.AssignListContext):
        pass


    # Enter a parse tree produced by DataLangParser#assignment.
    def enterAssignment(self, ctx:DataLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DataLangParser#assignment.
    def exitAssignment(self, ctx:DataLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DataLangParser#deleteStmt.
    def enterDeleteStmt(self, ctx:DataLangParser.DeleteStmtContext):
        pass

    # Exit a parse tree produced by DataLangParser#deleteStmt.
    def exitDeleteStmt(self, ctx:DataLangParser.DeleteStmtContext):
        pass


    # Enter a parse tree produced by DataLangParser#value.
    def enterValue(self, ctx:DataLangParser.ValueContext):
        pass

    # Exit a parse tree produced by DataLangParser#value.
    def exitValue(self, ctx:DataLangParser.ValueContext):
        pass



del DataLangParser