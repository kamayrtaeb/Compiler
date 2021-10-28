
from Scanner.scanner import Scanners

if __name__ =="__main__":
    scanner =Scanner('input.txt')
    scanner.state()

    scanner.lexicalErrors('lexical_errors.txt')
    scanner.symbolList('symbol_table.txt')
    scanner.tokens('tokens.txt')

    scanner.close_file()





