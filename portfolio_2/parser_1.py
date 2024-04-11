import re

#Formato desejado de token: <TIPO, VALOR>
with open('portfolio_2\script3.txt', 'r') as file:
    script = file.read()

types = [
    ('SOMA', re.compile(r'\+')),
    ('SUB', re.compile(r'-')),
    ('MUL', re.compile(r'\*')),
    ('DIV', re.compile(r'/')),
    ('LPAREN', re.compile(r'\(')),
    ('RPAREN', re.compile(r'\)')),
    ('NUM_INT', re.compile(r'[0-9]+')),
]

class Lexer:
    def __init__(self, script):
        self.script = script
        self.tokens = []
        self.pos = 0

    def generate_tokens(self):
        while self.pos < len(self.script):
            if self.script[self.pos].isspace():
                self.pos += 1
            elif self.script[self.pos] == '\n':
                self.tokens.append(('NEWLINE', '\n'))
                self.pos += 1
            else:
                found_token = False
                for token_type, regex in types:
                    match = regex.match(self.script, self.pos)
                    if match:
                        self.tokens.append((token_type, match.group(0)))
                        self.pos = match.end()
                        found_token = True
                        break
                if not found_token:
                    raise Exception(f"Caractere ilegal '{self.script[self.pos]}'")
        return self.tokens

#Classe Parser para análise sintática
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def eat(self, token_type):
        if self.current_token()[0] == token_type:
            self.token_index += 1
        else:
            raise Exception(f"Erro de sintaxe: esperava {token_type}")

    def current_token(self):
        if self.token_index < len(self.tokens):
            return self.tokens[self.token_index]
        else:
            return None

    def factor(self):
        token = self.current_token()
        if token is not None:
            token_type, token_value = token
            if token_type == 'NUM_INT':
                self.eat('NUM_INT')
                return int(token_value)
            elif token_type == 'LPAREN':
                self.eat('LPAREN')
                result = self.expr()
                self.eat('RPAREN')
                return result
            else:
                raise Exception(f"Erro de sintaxe: token inesperado {token_type}")
        else:
            raise Exception("Fim inesperado da entrada")

    def term(self):
        result = self.factor()
        while self.current_token() is not None and self.current_token()[0] in ('MUL', 'DIV'):
            token_type, _ = self.current_token()
            if token_type == 'MUL':
                self.eat('MUL')
                result *= self.factor()
            elif token_type == 'DIV':
                self.eat('DIV')
                result /= self.factor()
        return result

    def expr(self):
        result = self.term()
        while self.current_token() is not None and self.current_token()[0] in ('SOMA', 'SUB'):
            token_type, _ = self.current_token()
            if token_type == 'SOMA':
                self.eat('SOMA')
                result += self.term()
            elif token_type == 'SUB':
                self.eat('SUB')
                result -= self.term()
        return result

#Função principal para executar o lexer e o parser
def main():
    lexer = Lexer(script)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    result = parser.expr()
    print(result)

if __name__ == "__main__":
    main()
