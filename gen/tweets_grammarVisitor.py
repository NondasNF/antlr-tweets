# Generated from C:/Users/nonda/PycharmProjects/pythonProject1\tweets_grammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tweets_grammarParser import tweets_grammarParser
else:
    from tweets_grammarParser import tweets_grammarParser

# This class defines a complete generic visitor for a parse tree produced by tweets_grammarParser.

class tweets_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tweets_grammarParser#ini.
    def visitIni(self, ctx:tweets_grammarParser.IniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tweets_grammarParser#tweet.
    def visitTweet(self, ctx:tweets_grammarParser.TweetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tweets_grammarParser#palavra.
    def visitPalavra(self, ctx:tweets_grammarParser.PalavraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tweets_grammarParser#usuario.
    def visitUsuario(self, ctx:tweets_grammarParser.UsuarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tweets_grammarParser#username.
    def visitUsername(self, ctx:tweets_grammarParser.UsernameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tweets_grammarParser#hash.
    def visitHash(self, ctx:tweets_grammarParser.HashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tweets_grammarParser#hashtag.
    def visitHashtag(self, ctx:tweets_grammarParser.HashtagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tweets_grammarParser#emoji.
    def visitEmoji(self, ctx:tweets_grammarParser.EmojiContext):
        return self.visitChildren(ctx)



del tweets_grammarParser