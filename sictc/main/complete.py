from main import scanner
from main import parser


filename = input("Input file name: ")

tokens = scanner.scanner(filename)
#parsed = parser.parse(tokens)
#print("is this correct:",parsed)
