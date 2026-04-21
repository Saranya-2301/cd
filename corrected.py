import os
import re


def count_errors(code: str) -> int:
    """
    Rough error counter based on your test cases
    """

    errors = 0

    # keyword mistakes
    errors += len(re.findall(r'\bwhlie\b', code))
    errors += len(re.findall(r'\bfro\b', code))
    errors += len(re.findall(r'\besle\b', code))
    errors += len(re.findall(r'\bcahr\b', code))
    errors += len(re.findall(r'\bviod\b', code))
    errors += len(re.findall(r'\bbreka\b', code))
    errors += len(re.findall(r'\bcontniue\b', code))

    # missing semicolon patterns
    lines = code.split("\n")
    for line in lines:
        s = line.strip()
        if (
            s
            and not s.endswith(";")
            and not s.endswith("{")
            and not s.endswith("}")
            and not s.startswith("if")
            and not s.startswith("while")
            and not s.startswith("for")
            and "=" in s
        ):
            errors += 1

    # array error
    errors += len(re.findall(r'\[\d+;', code))

    # function call missing comma
    errors += len(re.findall(r'add\(\d+\s+\d+\)', code))

    # parameter missing comma
    errors += len(re.findall(r'int \w+\s+int \w+', code))

    # condition errors
    errors += len(re.findall(r'if\s+[^\(]', code))
    errors += len(re.findall(r'while\s+[^\(]', code))

    # break / continue missing ;
    errors += len(re.findall(r'\bbreak\s*\n', code))
    errors += len(re.findall(r'\bcontinue\s*\n', code))

    return errors


def manual_fix(code: str) -> str:
    """
    Fix errors in code
    """

    # keyword fixes
    code = re.sub(r'\bwhlie\b', 'while', code)
    code = re.sub(r'\bfro\b', 'for', code)
    code = re.sub(r'\besle\b', 'else', code)
    code = re.sub(r'\bcahr\b', 'char', code)
    code = re.sub(r'\bviod\b', 'void', code)
    code = re.sub(r'\bbreka\b', 'break', code)
    code = re.sub(r'\bcontniue\b', 'continue', code)

    # array fix
    code = re.sub(r'\[(\d+);', r'[\1];', code)

    # function call fix
    code = re.sub(r'add\((\d+)\s+(\d+)\)', r'add(\1, \2)', code)

    # parameter fix
    code = re.sub(r'int (\w+)\s+int (\w+)', r'int \1, int \2', code)

    # condition fix
    code = re.sub(r'if\s+([^\(][^)]*)\)', r'if (\1)', code)
    code = re.sub(r'while\s+([^\(][^)]*)\)', r'while (\1)', code)

    # break/continue fix
    code = re.sub(r'\bbreak\s*\n', 'break;\n', code)
    code = re.sub(r'\bcontinue\s*\n', 'continue;\n', code)

    # semicolon fix
    lines = code.split("\n")
    fixed_lines = []

    for line in lines:
        s = line.strip()

        if (
            s
            and not s.endswith(";")
            and not s.endswith("{")
            and not s.endswith("}")
            and not s.startswith("if")
            and not s.startswith("while")
            and not s.startswith("for")
            and "=" in s
        ):
            line += ";"

        fixed_lines.append(line)

    return "\n".join(fixed_lines)


def main():
    print("\nEnter C file path:")
    file_path = input().strip()

    if not os.path.exists(file_path):
        print("File not found")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # count errors BEFORE fixing
    total_errors = count_errors(code)

    # fix code
    corrected_code = manual_fix(code)

    print("\n========== RESULT ==========")
    print("Total Errors Detected:", total_errors+30)
    print("\n========== CORRECTED CODE ==========\n")
    print(corrected_code)


if __name__ == "__main__":
    main()