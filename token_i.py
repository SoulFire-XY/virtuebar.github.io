###########################################
# TOKENS
###########################################

TT_INT          = 'INT'
TT_FLOAT        = 'FLOAT'
TT_STRING       = 'STRING'
TT_IDENTIFIER   = 'IDENTIFIER'
TT_KEYWORD      = 'KEYWORD'
'''
Keywords
- VAL - variable
- WITH - and operator
- OR - or operator
- INVER - not operator
- CONST - Constant
- IF - If statement
- ACT - Do if statement
- ELIF - Else If statement
- OTHER - Else statement
- FOR - For Loop statement
- WHILE - While Loop statement
- TO - In FOR Loop statement
- STEP - Amount of Value to skip while iterating
- FUNC - Function Declaration Statement
- END - End a loop, condition or function statement
- RETURN - return value/values
- BREAK - break out a loop
- SKIP - Skip a iteration
- GOTO - goto a specific line
'''

TT_EE           = 'EE'   #Dounle Equals to
TT_NE           = 'NE'   #Not Equals to
TT_LT           = 'LT'   #Less Than
TT_GT           = 'GT'   #Greater Than
TT_LTE          = 'LTE'  #Less than equals to
TT_GTE          = 'GTE'  #Greater then equals to
TT_EQ           = 'EQ'   #Equals

TT_PLUS         = 'PLUS'
TT_MINUS        = 'MINUS'
TT_MUL          = 'MUL'
TT_DIV          = 'DIV'
TT_POWER        = 'POWER'

TT_LPAREN       = 'LPAREM'
TT_RPAREN       = 'RPAREM'
TT_LSQUARE      = 'LSQUARE'
TT_RSQUARE      = 'RSQUARE'
TT_LCRBRAC      = 'LCRBRAC'
TT_RCRBRAC      = 'RCRBRAC'
TT_COMMA        = 'COMMA'
TT_NEWLINE      = 'NEWLINE'
TT_ARROW        = 'ARROW'
TT_COLON        = 'COLON'

TT_EOF          = 'EOF'                 #End of file

#No. of tokens currently = 19

KEYWORDS = [
    'VAL',
    'WITH',  #AND
    'OR',
    'INVER', #Not
    'CONST',  #Constant
    'IF',
    'ACT', # Do
    'ELIF',  #Else If
    'OTHER',  #Else
    'FOR',
    'TO',
    'STEP',
    'WHILE',
    'END', #End a statement
    'FUNC', #Function
    'RETURN', #Returns value/values
    'SKIP',
    'BREAK',
    'GOTO' # go to a specific line
]

class Token:
    def __init__(self, type_, value = None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start: 
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end: self.pos_end = pos_end

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
