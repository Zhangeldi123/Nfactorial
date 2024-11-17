import sys

# ASCII art styles mapped to file paths
art_styles = {
    "standard": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\standard.txt",
    "shadow": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\shadow.txt",
    "thinkertoy": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\thinkertoy.txt"
}

# Check if enough arguments are provided
if len(sys.argv) < 3:
    print("Usage: python3 main.py [--output=<fileName.txt>] [STRING] [BANNER]")
    sys.exit(1)

# Extract optional output file
output_file = None
if '--output=' in sys.argv[1]:
    output_file = sys.argv[1].split('=')[1]
    args = sys.argv[2:]
else:
    args = sys.argv[1:]

# Validate remaining arguments
if len(args) != 2:
    print("Usage: python3 main.py [--output=<fileName.txt>] [STRING] [BANNER]")
    sys.exit(1)

text, art_style = args

# Load the selected ASCII art style
file_path = art_styles.get(art_style.lower())
if not file_path:
    print(f"Art style '{art_style}' not found. Available styles: {', '.join(art_styles.keys())}.")
    sys.exit(1)

try:
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    ascii_art = {}
    current_symbol_code = 32  # ASCII starts from space
    symbol_art = []

    for line in lines:
        if len(symbol_art) == 8:  # 8 rows for each symbol
            ascii_art[chr(current_symbol_code)] = [row.ljust(8) for row in symbol_art]  # Ensure proper alignment
            current_symbol_code += 1
            symbol_art = []
        else:
            symbol_art.append(line.ljust(8))  # Left-justify all rows to maintain alignment

    if len(symbol_art) == 8:  # Add the last symbol if not added
        ascii_art[chr(current_symbol_code)] = [row.ljust(8) for row in symbol_art]

except FileNotFoundError:
    print(f"File for art style '{art_style}' not found.")
    sys.exit(1)

# Function to generate ASCII art
def generate_ascii_art(text):
    lines = text.split("\\n")  # Разделяем текст по символу \n
    result_rows = []  # Массив для хранения строк результата

    for line in lines:
        rows = ['' for _ in range(8)]  # Инициализируем 8 строк для символов
        for idx, char in enumerate(line):
            art = ascii_art.get(char, [' ' * 8] * 8)  # Получаем ASCII-арт для символа (если нет - пробелы)
            
            for i in range(8):
                rows[i] += art[i]  # Добавляем арт символа в соответствующие строки


        result_rows.extend(rows)  # Добавляем строки результата

    return "\n".join(result_rows)  # Возвращаем финальный результат
# Generate and output ASCII art
result = generate_ascii_art(text)
if output_file:
    try:
        with open(output_file, 'w') as f:
            f.write(result)
        print(f"ASCII art written to {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")
else:
    print(result)

