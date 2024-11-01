import subprocess

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
        elif cmd == "[":
            c_code += "while (*ptr) {\n"
        elif cmd == "]":
            c_code += "}\n"

    c_code += """
    return 0;
}
"""
    return c_code


def compile_bf_file(bf_file):
    with open(bf_file, 'r') as file:
        bf_code = file.read()
    c_code = bf_to_c(bf_code)
    gcc_command = ["gcc", "-x", "c", "-o", "filename", "-"]
    process = subprocess.Popen(gcc_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=c_code.encode())
    if process.returncode != 0:
        print('Compilation failed:')
        print(stderr.decode())
        return
    


compile_bf_file('./helloworld.bf')