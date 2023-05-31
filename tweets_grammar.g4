grammar tweets_grammar;

ini: tweet;

tweet: (palavra|usuario|hash|emoji)+;

palavra: (PAL|NUM|CHARESP)+;

usuario: '@' username;

username: (PAL|NUM);

hash: '#' hashtag;

hashtag: (PAL|NUM);

emoji: EMOJI+;


PAL: [a-zA-Záàãâäéèẽêëíìĩîïóòõôöúùũûüç]+;
NUM: [0-9];
CHARESP:('.' | ',' | ':' | ';' | '·' | '+' | '|' | '_' | '[' | ']' | '{' | '}' | '(' | ')' | '*' | '&' | '%' | '$' | '!' | '?' | '>' | '<' | '/' | '-' | '"' | '\'' | '-')+;
EMOJI : [\p{Emoji}];
Space: [ \t\r\n]->skip;