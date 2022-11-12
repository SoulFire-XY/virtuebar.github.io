###########################################
# TOKENS
###########################################

TT_INT          = 'TT_INT'
TT_FLOAT        = 'TT_FLOAT'
TT_IDENTIFIER   = 'TT_IDENTIFIER'
TT_KEYWORD      = 'TT_KEYWORD'

TT_EE           = 'EE'   #Dounle Equals to
TT_NE           = 'NE'   #Not Equals to
TT_LT           = 'LT'   #Less Than
TT_GT           = 'GT'   #Greater Than
TT_LTE          = 'LTE'  #Less than equals to
TT_GTE          = 'GTE'  #Greater then equals to

TT_PLUS         = 'PLUS'
TT_MINUS        = 'MINUS'
TT_MUL          = 'MUL'
TT_DIV          = 'DIV'
TT_POWER        = 'POWER'
TT_LPAREN       = 'LPAREM'
TT_RPAREN       = 'RPAREM'
TT_EQ           = 'EQ'                  #Equals

TT_EOF          = 'EOF'                 #End of file

#No. of tokens currently = 19

KEYWORDS = [
    'VAL',
    'WITH', #AND
    'OR',
    'INVER', #Not
    'CONST' # Constant
]
'''
Keywords
- VAL - variable
- WITH - and operator
- OR - or operator
- INVER - not operator
'''

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