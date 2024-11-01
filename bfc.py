def bf_to_c(bf_code, out='output.c'):
    c_code = """
int main() {
    char memory[30000] = {0};
    char *ptr = memory;

    """
    c_code += """
    return 0;
}
"""
    with open(out, 'w') as f:
        f.write(c_code)
bf_to_c('++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.')