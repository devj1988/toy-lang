from lexer import Lexer
from parser import Parser
from codegen import CodeGen

code = """
print(4 + 4-2);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(code)

codegen = CodeGen()

pg = Parser(codegen.module, codegen.builder, codegen.printf)
pg.parse()

parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")