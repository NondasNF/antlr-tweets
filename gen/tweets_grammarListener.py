# Generated from C:/Users/nonda/PycharmProjects/pythonProject1\tweets_grammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tweets_grammarParser import tweets_grammarParser
else:
    from tweets_grammarParser import tweets_grammarParser

# This class defines a complete listener for a parse tree produced by tweets_grammarParser.
class tweets_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by tweets_grammarParser#ini.
    def enterIni(self, ctx:tweets_grammarParser.IniContext):
        pass

    # Exit a parse tree produced by tweets_grammarParser#ini.
    def exitIni(self, ctx:tweets_grammarParser.IniContext):
        pass


    # Enter a parse tree produced by tweets_grammarParser#tweet.
    def enterTweet(self, ctx:tweets_grammarParser.TweetContext):
        pass

    # Exit a parse tree produced by tweets_grammarParser#tweet.
    def exitTweet(self, ctx:tweets_grammarParser.TweetContext):
        pass


    # Enter a parse tree produced by tweets_grammarParser#palavra.
    def enterPalavra(self, ctx:tweets_grammarParser.PalavraContext):
        pass

    # Exit a parse tree produced by tweets_grammarParser#palavra.
    def exitPalavra(self, ctx:tweets_grammarParser.PalavraContext):
        pass


    # Enter a parse tree produced by tweets_grammarParser#usuario.
    def enterUsuario(self, ctx:tweets_grammarParser.UsuarioContext):
        pass

    # Exit a parse tree produced by tweets_grammarParser#usuario.
    def exitUsuario(self, ctx:tweets_grammarParser.UsuarioContext):
        pass


    # Enter a parse tree produced by tweets_grammarParser#username.
    def enterUsername(self, ctx:tweets_grammarParser.UsernameContext):
        pass

    # Exit a parse tree produced by tweets_grammarParser#username.
    def exitUsername(self, ctx:tweets_grammarParser.UsernameContext):
        pass


    # Enter a parse tree produced by tweets_grammarParser#hash.
    def enterHash(self, ctx:tweets_grammarParser.HashContext):
        pass

    # Exit a parse tree produced by tweets_grammarParser#hash.
    def exitHash(self, ctx:tweets_grammarParser.HashContext):
        pass


    # Enter a parse tree produced by tweets_grammarParser#hashtag.
    def enterHashtag(self, ctx:tweets_grammarParser.HashtagContext):
        pass

    # Exit a parse tree produced by tweets_grammarParser#hashtag.
    def exitHashtag(self, ctx:tweets_grammarParser.HashtagContext):
        pass


    # Enter a parse tree produced by tweets_grammarParser#emoji.
    def enterEmoji(self, ctx:tweets_grammarParser.EmojiContext):
        pass

    # Exit a parse tree produced by tweets_grammarParser#emoji.
    def exitEmoji(self, ctx:tweets_grammarParser.EmojiContext):
        pass



del tweets_grammarParser