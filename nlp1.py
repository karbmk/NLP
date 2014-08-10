import ply.lex as lex
import sys
import re
f=open("Dataset15.txt","r")

tokens = {
'NUMBER','SNAME','RT','HASHTAG','URL','SLANG','WORD','SINGLEQUOTE','DOUBLEQOUTE','EXCLAMATION','QUESTION','EMOTICON','PUNCTUATION','PERIOD'
}
cHASH,cNUM,cNAM,cSING,cDOUB,cWORD,cPUNC,cEXCL,cSLAN,cEMOT,cPER,cRT,cURL,cQUES=0,0,0,0,0,0,0,0,0,0,0,0,0,0
def t_SINGLEQUOTE(t):
	r'\''
	cSING+=1
def t_DOUBLEQUOTE(t):
	r'\"'
	cDOUB+=1
def t_WORD(t):
	r'\w+'
	cWORD+=1
def t_EXCLAMATION(t):
	r'[!]'
	cEXCL+=1
def t_QUESTION(t):
	r'[?]'
	cQUES+=1
def t_PUNCTUATION(t):
	r'[",",";",":",".","\'"]'
	cPUNC+=1
def t_PERIOD(t):
	r'\.'
	cPER+=1
def t_HASHTAG(t):
	r'\#w+'
	cHASH+=1 
def t_NUMBER(t):
    r'\d+'
    cNUM+=1
def t_SNAME(t):
	r'\@.+'
	cNAM+=1
def t_URL(t):
	r'^http://(w+\.)+'
	cURL+=1
def t_RT(t):
	r'\#.'
	cRT+=1
def t_SLANG(t):
	r'["LOL","ROFL","LMAO"]'
	cSLAN+=1
def t_EMOTICON(t):
	r'[":)",":(",":p",":D",":O",";)","B)",":*","3:)","O:)"]'
	cEMOT+=1

print "Hashtags=%d \n number=%d \n Sname=%d \n singlequote=%d \n doublequote=%d \n word=%d \n punctuation=%d \n exclamation=%d \n slang=%d \n emoticon=%d \n \
period=%d \n RT=%d \n URL=%d \n Question=%d "%(cHASH,cNUM,cNAM,cSING,cDOUB,cWORD,cPUNC,cEXCL,cSLAN,cEMOT,cPER,cRT,cURL,cQUES)	
	
lexer=lex.lex()
lexer.input(f)
for t in lexer:
    pass
