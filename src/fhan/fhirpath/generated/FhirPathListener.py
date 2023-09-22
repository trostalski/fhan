# Generated from ./grammar/FhirPath.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FhirPathParser import FhirPathParser
else:
    from FhirPathParser import FhirPathParser

# This class defines a complete listener for a parse tree produced by FhirPathParser.
class FhirPathListener(ParseTreeListener):

    # Enter a parse tree produced by FhirPathParser#indexerExpression.
    def enterIndexerExpression(self, ctx:FhirPathParser.IndexerExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#indexerExpression.
    def exitIndexerExpression(self, ctx:FhirPathParser.IndexerExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#polarityExpression.
    def enterPolarityExpression(self, ctx:FhirPathParser.PolarityExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#polarityExpression.
    def exitPolarityExpression(self, ctx:FhirPathParser.PolarityExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:FhirPathParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:FhirPathParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:FhirPathParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:FhirPathParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#unionExpression.
    def enterUnionExpression(self, ctx:FhirPathParser.UnionExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#unionExpression.
    def exitUnionExpression(self, ctx:FhirPathParser.UnionExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#orExpression.
    def enterOrExpression(self, ctx:FhirPathParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#orExpression.
    def exitOrExpression(self, ctx:FhirPathParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#andExpression.
    def enterAndExpression(self, ctx:FhirPathParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#andExpression.
    def exitAndExpression(self, ctx:FhirPathParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#membershipExpression.
    def enterMembershipExpression(self, ctx:FhirPathParser.MembershipExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#membershipExpression.
    def exitMembershipExpression(self, ctx:FhirPathParser.MembershipExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#inequalityExpression.
    def enterInequalityExpression(self, ctx:FhirPathParser.InequalityExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#inequalityExpression.
    def exitInequalityExpression(self, ctx:FhirPathParser.InequalityExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#invocationExpression.
    def enterInvocationExpression(self, ctx:FhirPathParser.InvocationExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#invocationExpression.
    def exitInvocationExpression(self, ctx:FhirPathParser.InvocationExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#equalityExpression.
    def enterEqualityExpression(self, ctx:FhirPathParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#equalityExpression.
    def exitEqualityExpression(self, ctx:FhirPathParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#impliesExpression.
    def enterImpliesExpression(self, ctx:FhirPathParser.ImpliesExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#impliesExpression.
    def exitImpliesExpression(self, ctx:FhirPathParser.ImpliesExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#termExpression.
    def enterTermExpression(self, ctx:FhirPathParser.TermExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#termExpression.
    def exitTermExpression(self, ctx:FhirPathParser.TermExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#typeExpression.
    def enterTypeExpression(self, ctx:FhirPathParser.TypeExpressionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#typeExpression.
    def exitTypeExpression(self, ctx:FhirPathParser.TypeExpressionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#invocationTerm.
    def enterInvocationTerm(self, ctx:FhirPathParser.InvocationTermContext):
        pass

    # Exit a parse tree produced by FhirPathParser#invocationTerm.
    def exitInvocationTerm(self, ctx:FhirPathParser.InvocationTermContext):
        pass


    # Enter a parse tree produced by FhirPathParser#literalTerm.
    def enterLiteralTerm(self, ctx:FhirPathParser.LiteralTermContext):
        pass

    # Exit a parse tree produced by FhirPathParser#literalTerm.
    def exitLiteralTerm(self, ctx:FhirPathParser.LiteralTermContext):
        pass


    # Enter a parse tree produced by FhirPathParser#externalConstantTerm.
    def enterExternalConstantTerm(self, ctx:FhirPathParser.ExternalConstantTermContext):
        pass

    # Exit a parse tree produced by FhirPathParser#externalConstantTerm.
    def exitExternalConstantTerm(self, ctx:FhirPathParser.ExternalConstantTermContext):
        pass


    # Enter a parse tree produced by FhirPathParser#parenthesizedTerm.
    def enterParenthesizedTerm(self, ctx:FhirPathParser.ParenthesizedTermContext):
        pass

    # Exit a parse tree produced by FhirPathParser#parenthesizedTerm.
    def exitParenthesizedTerm(self, ctx:FhirPathParser.ParenthesizedTermContext):
        pass


    # Enter a parse tree produced by FhirPathParser#nullLiteral.
    def enterNullLiteral(self, ctx:FhirPathParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by FhirPathParser#nullLiteral.
    def exitNullLiteral(self, ctx:FhirPathParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by FhirPathParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:FhirPathParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by FhirPathParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:FhirPathParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by FhirPathParser#stringLiteral.
    def enterStringLiteral(self, ctx:FhirPathParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by FhirPathParser#stringLiteral.
    def exitStringLiteral(self, ctx:FhirPathParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by FhirPathParser#numberLiteral.
    def enterNumberLiteral(self, ctx:FhirPathParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by FhirPathParser#numberLiteral.
    def exitNumberLiteral(self, ctx:FhirPathParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by FhirPathParser#dateLiteral.
    def enterDateLiteral(self, ctx:FhirPathParser.DateLiteralContext):
        pass

    # Exit a parse tree produced by FhirPathParser#dateLiteral.
    def exitDateLiteral(self, ctx:FhirPathParser.DateLiteralContext):
        pass


    # Enter a parse tree produced by FhirPathParser#dateTimeLiteral.
    def enterDateTimeLiteral(self, ctx:FhirPathParser.DateTimeLiteralContext):
        pass

    # Exit a parse tree produced by FhirPathParser#dateTimeLiteral.
    def exitDateTimeLiteral(self, ctx:FhirPathParser.DateTimeLiteralContext):
        pass


    # Enter a parse tree produced by FhirPathParser#timeLiteral.
    def enterTimeLiteral(self, ctx:FhirPathParser.TimeLiteralContext):
        pass

    # Exit a parse tree produced by FhirPathParser#timeLiteral.
    def exitTimeLiteral(self, ctx:FhirPathParser.TimeLiteralContext):
        pass


    # Enter a parse tree produced by FhirPathParser#quantityLiteral.
    def enterQuantityLiteral(self, ctx:FhirPathParser.QuantityLiteralContext):
        pass

    # Exit a parse tree produced by FhirPathParser#quantityLiteral.
    def exitQuantityLiteral(self, ctx:FhirPathParser.QuantityLiteralContext):
        pass


    # Enter a parse tree produced by FhirPathParser#externalConstant.
    def enterExternalConstant(self, ctx:FhirPathParser.ExternalConstantContext):
        pass

    # Exit a parse tree produced by FhirPathParser#externalConstant.
    def exitExternalConstant(self, ctx:FhirPathParser.ExternalConstantContext):
        pass


    # Enter a parse tree produced by FhirPathParser#memberInvocation.
    def enterMemberInvocation(self, ctx:FhirPathParser.MemberInvocationContext):
        pass

    # Exit a parse tree produced by FhirPathParser#memberInvocation.
    def exitMemberInvocation(self, ctx:FhirPathParser.MemberInvocationContext):
        pass


    # Enter a parse tree produced by FhirPathParser#functionInvocation.
    def enterFunctionInvocation(self, ctx:FhirPathParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by FhirPathParser#functionInvocation.
    def exitFunctionInvocation(self, ctx:FhirPathParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by FhirPathParser#thisInvocation.
    def enterThisInvocation(self, ctx:FhirPathParser.ThisInvocationContext):
        pass

    # Exit a parse tree produced by FhirPathParser#thisInvocation.
    def exitThisInvocation(self, ctx:FhirPathParser.ThisInvocationContext):
        pass


    # Enter a parse tree produced by FhirPathParser#indexInvocation.
    def enterIndexInvocation(self, ctx:FhirPathParser.IndexInvocationContext):
        pass

    # Exit a parse tree produced by FhirPathParser#indexInvocation.
    def exitIndexInvocation(self, ctx:FhirPathParser.IndexInvocationContext):
        pass


    # Enter a parse tree produced by FhirPathParser#totalInvocation.
    def enterTotalInvocation(self, ctx:FhirPathParser.TotalInvocationContext):
        pass

    # Exit a parse tree produced by FhirPathParser#totalInvocation.
    def exitTotalInvocation(self, ctx:FhirPathParser.TotalInvocationContext):
        pass


    # Enter a parse tree produced by FhirPathParser#function.
    def enterFunction(self, ctx:FhirPathParser.FunctionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#function.
    def exitFunction(self, ctx:FhirPathParser.FunctionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#paramList.
    def enterParamList(self, ctx:FhirPathParser.ParamListContext):
        pass

    # Exit a parse tree produced by FhirPathParser#paramList.
    def exitParamList(self, ctx:FhirPathParser.ParamListContext):
        pass


    # Enter a parse tree produced by FhirPathParser#quantity.
    def enterQuantity(self, ctx:FhirPathParser.QuantityContext):
        pass

    # Exit a parse tree produced by FhirPathParser#quantity.
    def exitQuantity(self, ctx:FhirPathParser.QuantityContext):
        pass


    # Enter a parse tree produced by FhirPathParser#unit.
    def enterUnit(self, ctx:FhirPathParser.UnitContext):
        pass

    # Exit a parse tree produced by FhirPathParser#unit.
    def exitUnit(self, ctx:FhirPathParser.UnitContext):
        pass


    # Enter a parse tree produced by FhirPathParser#dateTimePrecision.
    def enterDateTimePrecision(self, ctx:FhirPathParser.DateTimePrecisionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#dateTimePrecision.
    def exitDateTimePrecision(self, ctx:FhirPathParser.DateTimePrecisionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#pluralDateTimePrecision.
    def enterPluralDateTimePrecision(self, ctx:FhirPathParser.PluralDateTimePrecisionContext):
        pass

    # Exit a parse tree produced by FhirPathParser#pluralDateTimePrecision.
    def exitPluralDateTimePrecision(self, ctx:FhirPathParser.PluralDateTimePrecisionContext):
        pass


    # Enter a parse tree produced by FhirPathParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:FhirPathParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by FhirPathParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:FhirPathParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by FhirPathParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:FhirPathParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by FhirPathParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:FhirPathParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by FhirPathParser#identifier.
    def enterIdentifier(self, ctx:FhirPathParser.IdentifierContext):
        pass

    # Exit a parse tree produced by FhirPathParser#identifier.
    def exitIdentifier(self, ctx:FhirPathParser.IdentifierContext):
        pass



del FhirPathParser