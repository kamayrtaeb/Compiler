
from Scanner.scanner import Scanner

if __name__ =="__main__":
    scanner =Scanner('input.txt')
    scanner.state()

    scanner.lexicalErrors('lexical_errors.txt')

    scanner.close_file()





