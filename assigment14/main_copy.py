import sys

art_styles = {
    "standard": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii_art_project_1_doctorrin_main\standard.txt",
    "shadow": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii_art_project_1_doctorrin_main\shadow.txt",
    "thinkertoy": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii_art_project_1_doctorrin_main\thikertoy.txt"
}

import os

def load_art_style(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()

        ascii_art = {}
        current_symbol_code = 32  # ASCII space starts at 32
        symbol_art = []

        for line in lines:
            if len(symbol_art) == 8:  # Each character occupies 8 lines of art
                ascii_art[chr(current_symbol_code)] = [row.ljust(8) for row in symbol_art]
                current_symbol_code += 1
                symbol_art = []
            else:
                symbol_art.append(line.ljust(8))

        if len(symbol_art) == 8:  # Ensure the last symbol is added
            ascii_art[chr(current_symbol_code)] = [row.ljust(8) for row in symbol_art]

        return ascii_art
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}  # Return an empty dictionary instead of None


def generate_ascii_art(text, ascii_art):
    lines = text.split("\\n")  # Handle literal newlines
    result_rows = []

    for line in lines:
        rows = ['' for _ in range(8)]  # Each character takes up 8 rows
        for char in line:
            art = ascii_art.get(char, [' ' * 8] * 8)  # Default to 8 spaces if char not found
            for i in range(8):
                rows[i] += art[i]

        result_rows.extend(rows)  # Append the rows for each line

    return "\n".join(result_rows)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 main.py [--output=<fileName.txt>] [STRING] [BANNER]")
        sys.exit(1)

    output_file = None
    if '--output=' in sys.argv[1]:
        output_file = sys.argv[1].split('=')[1]
        args = sys.argv[2:]
    else:
        args = sys.argv[1:]

    if len(args) != 2:
        print("Usage: python3 main.py [--output=<fileName.txt>] [STRING] [BANNER]")
        sys.exit(1)

    text, art_style = args
    file_path = art_styles.get(art_style.lower())

    if not file_path:
        print(f"Art style '{art_style}' not found. Available styles: {', '.join(art_styles.keys())}.")
        sys.exit(1)

    # Load the art style and generate ASCII art
    ascii_art = load_art_style(file_path)
    result = generate_ascii_art(text, ascii_art)

    # Output the result
    if output_file:
        try:
            with open(output_file, 'w') as f:
                f.write(result)
            print(f"ASCII art written to {output_file}")
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print(result)
