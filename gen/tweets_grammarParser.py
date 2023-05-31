# Generated from C:/Users/nonda/PycharmProjects/pythonProject1\tweets_grammar.g4 by ANTLR 4.12.0
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
        4,1,7,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,1,4,1,23,8,1,11,1,12,1,24,1,2,4,2,
        28,8,2,11,2,12,2,29,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,
        4,7,43,8,7,11,7,12,7,44,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,0,3,5,
        1,0,3,4,44,0,16,1,0,0,0,2,22,1,0,0,0,4,27,1,0,0,0,6,31,1,0,0,0,8,
        34,1,0,0,0,10,36,1,0,0,0,12,39,1,0,0,0,14,42,1,0,0,0,16,17,3,2,1,
        0,17,1,1,0,0,0,18,23,3,4,2,0,19,23,3,6,3,0,20,23,3,10,5,0,21,23,
        3,14,7,0,22,18,1,0,0,0,22,19,1,0,0,0,22,20,1,0,0,0,22,21,1,0,0,0,
        23,24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,0,26,28,7,0,
        0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,5,
        1,0,0,0,31,32,5,1,0,0,32,33,3,8,4,0,33,7,1,0,0,0,34,35,7,1,0,0,35,
        9,1,0,0,0,36,37,5,2,0,0,37,38,3,12,6,0,38,11,1,0,0,0,39,40,7,1,0,
        0,40,13,1,0,0,0,41,43,5,6,0,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,
        1,0,0,0,44,45,1,0,0,0,45,15,1,0,0,0,4,22,24,29,44
    ]

class tweets_grammarParser ( Parser ):

    grammarFileName = "tweets_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PAL", "NUM", 
                      "CHARESP", "EMOJI", "Space" ]

    RULE_ini = 0
    RULE_tweet = 1
    RULE_palavra = 2
    RULE_usuario = 3
    RULE_username = 4
    RULE_hash = 5
    RULE_hashtag = 6
    RULE_emoji = 7

    ruleNames =  [ "ini", "tweet", "palavra", "usuario", "username", "hash", 
                   "hashtag", "emoji" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    PAL=3
    NUM=4
    CHARESP=5
    EMOJI=6
    Space=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class IniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tweet(self):
            return self.getTypedRuleContext(tweets_grammarParser.TweetContext,0)


        def getRuleIndex(self):
            return tweets_grammarParser.RULE_ini

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIni" ):
                listener.enterIni(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIni" ):
                listener.exitIni(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIni" ):
                return visitor.visitIni(self)
            else:
                return visitor.visitChildren(self)




    def ini(self):

        localctx = tweets_grammarParser.IniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.tweet()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TweetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def palavra(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tweets_grammarParser.PalavraContext)
            else:
                return self.getTypedRuleContext(tweets_grammarParser.PalavraContext,i)


        def usuario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tweets_grammarParser.UsuarioContext)
            else:
                return self.getTypedRuleContext(tweets_grammarParser.UsuarioContext,i)


        def hash_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tweets_grammarParser.HashContext)
            else:
                return self.getTypedRuleContext(tweets_grammarParser.HashContext,i)


        def emoji(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tweets_grammarParser.EmojiContext)
            else:
                return self.getTypedRuleContext(tweets_grammarParser.EmojiContext,i)


        def getRuleIndex(self):
            return tweets_grammarParser.RULE_tweet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTweet" ):
                listener.enterTweet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTweet" ):
                listener.exitTweet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTweet" ):
                return visitor.visitTweet(self)
            else:
                return visitor.visitChildren(self)




    def tweet(self):

        localctx = tweets_grammarParser.TweetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tweet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5]:
                    self.state = 18
                    self.palavra()
                    pass
                elif token in [1]:
                    self.state = 19
                    self.usuario()
                    pass
                elif token in [2]:
                    self.state = 20
                    self.hash_()
                    pass
                elif token in [6]:
                    self.state = 21
                    self.emoji()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PalavraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAL(self, i:int=None):
            if i is None:
                return self.getTokens(tweets_grammarParser.PAL)
            else:
                return self.getToken(tweets_grammarParser.PAL, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(tweets_grammarParser.NUM)
            else:
                return self.getToken(tweets_grammarParser.NUM, i)

        def CHARESP(self, i:int=None):
            if i is None:
                return self.getTokens(tweets_grammarParser.CHARESP)
            else:
                return self.getToken(tweets_grammarParser.CHARESP, i)

        def getRuleIndex(self):
            return tweets_grammarParser.RULE_palavra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPalavra" ):
                listener.enterPalavra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPalavra" ):
                listener.exitPalavra(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPalavra" ):
                return visitor.visitPalavra(self)
            else:
                return visitor.visitChildren(self)




    def palavra(self):

        localctx = tweets_grammarParser.PalavraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_palavra)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 26
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 29 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsuarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def username(self):
            return self.getTypedRuleContext(tweets_grammarParser.UsernameContext,0)


        def getRuleIndex(self):
            return tweets_grammarParser.RULE_usuario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsuario" ):
                listener.enterUsuario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsuario" ):
                listener.exitUsuario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsuario" ):
                return visitor.visitUsuario(self)
            else:
                return visitor.visitChildren(self)




    def usuario(self):

        localctx = tweets_grammarParser.UsuarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_usuario)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(tweets_grammarParser.T__0)
            self.state = 32
            self.username()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsernameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAL(self):
            return self.getToken(tweets_grammarParser.PAL, 0)

        def NUM(self):
            return self.getToken(tweets_grammarParser.NUM, 0)

        def getRuleIndex(self):
            return tweets_grammarParser.RULE_username

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsername" ):
                listener.enterUsername(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsername" ):
                listener.exitUsername(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsername" ):
                return visitor.visitUsername(self)
            else:
                return visitor.visitChildren(self)




    def username(self):

        localctx = tweets_grammarParser.UsernameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_username)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
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


    class HashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hashtag(self):
            return self.getTypedRuleContext(tweets_grammarParser.HashtagContext,0)


        def getRuleIndex(self):
            return tweets_grammarParser.RULE_hash

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHash" ):
                listener.enterHash(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHash" ):
                listener.exitHash(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHash" ):
                return visitor.visitHash(self)
            else:
                return visitor.visitChildren(self)




    def hash_(self):

        localctx = tweets_grammarParser.HashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(tweets_grammarParser.T__1)
            self.state = 37
            self.hashtag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HashtagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAL(self):
            return self.getToken(tweets_grammarParser.PAL, 0)

        def NUM(self):
            return self.getToken(tweets_grammarParser.NUM, 0)

        def getRuleIndex(self):
            return tweets_grammarParser.RULE_hashtag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHashtag" ):
                listener.enterHashtag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHashtag" ):
                listener.exitHashtag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHashtag" ):
                return visitor.visitHashtag(self)
            else:
                return visitor.visitChildren(self)




    def hashtag(self):

        localctx = tweets_grammarParser.HashtagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_hashtag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
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


    class EmojiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMOJI(self, i:int=None):
            if i is None:
                return self.getTokens(tweets_grammarParser.EMOJI)
            else:
                return self.getToken(tweets_grammarParser.EMOJI, i)

        def getRuleIndex(self):
            return tweets_grammarParser.RULE_emoji

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmoji" ):
                listener.enterEmoji(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmoji" ):
                listener.exitEmoji(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmoji" ):
                return visitor.visitEmoji(self)
            else:
                return visitor.visitChildren(self)




    def emoji(self):

        localctx = tweets_grammarParser.EmojiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_emoji)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 41
                    self.match(tweets_grammarParser.EMOJI)

                else:
                    raise NoViableAltException(self)
                self.state = 44 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





