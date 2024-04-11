# Compiladores

## Introdução:
Nesse repositório você encontrará algumas atividades desenvolvida pelos discentes para as avaliações da disciplina de Compiladores. 

As atividades estão organizadas dentro dos diretórios nomeados em suas respectivas ordens (Trabalho 1 e Trabalho 2).

## Discentes:
Myrna Gabrielle Bastos de Castro <br />
Euler Pablo Bentes Sarmento

## Portfolio 2
### Atividade 4: Analisador Sintático: parser_1.py e script 3 <br />
Este é um código simplificado para simular o funcionamento das primeiras etapas de um compilador, sendo desenvolvido o analisador léxico e sintático (Lexer e Parser) o qual serve com o propósito básico de interpretador de expressões matemáticas simples.

#### 1. Funcionalidades

- Suporte para adição (+), subtração (-), multiplicação (*) e divisão (/).
- Avaliação de expressões com parênteses para prioridade de operações.

#### 2. Arquivo de script

Para a execução do código é utilizada o arquivo Script.txt que serve como a entrada inserida pelo usuário que será avaliado pelo código.

Exemplo de script aceito pela gramática:
```python
5 + 5 * 6 + (4 / 2)
```

Exemplo de script não aceito pela gramática:
```python
(5 + 5 *)
```

#### 3. Estrutura do Código

- **parser_1.py:** Contém o código principal que lê o arquivo, realiza a análise léxica e sintática, e imprime o resultado.
- **Lexer:** Classe responsável por converter uma sequência de caracteres em tokens.
- **Parser:** Classe responsável por analisar a sequência de tokens e avaliar a expressão matemática.

---

### Atividade 5: Lista de exercícios do capitulo 3<br />
