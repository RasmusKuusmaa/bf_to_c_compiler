def bf_to_c(bf_code, out='output.c'):
    c_code = """#include <stdio.h>
int main() {
    char memory[30000] = {0};
    char *ptr = memory;\n
"""

    for cmd in bf_code:
        if cmd == '>':
            c_code += "\t++ptr;\n"
        elif cmd == '<':
            c_code += "\t--ptr;\n"
        elif cmd == '+':
            c_code += "\t++(*ptr);\n"
        elif cmd == '-':
            c_code += "\t--(*ptr);\n"
        elif cmd == '.':
            c_code += "\tputchar(*ptr);\n"
        elif cmd == ',':
            c_code += "*ptr = getchar();\n"

    c_code += """
    return 0;
}
"""
    with open(out, 'w') as f:
        f.write(c_code)

bf_to_c(',.,.')