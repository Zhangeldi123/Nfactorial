import sys

# Define paths for the art styles
art_styles = {
    "standard": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\standard.txt",
    "shadow": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\shadow.txt",
    "thinkertoy": r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\thinkertoy.txt"
}

# Parse command-line arguments
args = sys.argv

# Check if output flag is provided
output_file = None
if len(args) > 2 and '--output=' in args[1]:
    output_file = args[1].split('=')[1]  # Extract the file name after '--output='
    text = args[2]  # The input text is the second argument
    art_style = args[3]  # The art style is the third argument
else:
    # Fallback to manual input if no args or invalid args
    output_file = None
    if len(args) >= 2:
        text = args[1]  # The input text
        art_style = args[2] if len(args) > 2 else 'standard'  # Default to 'standard' if no style is provided
    else:
        user_input = input("Enter text and art style (e.g., 'hello shadow'): ").strip()
        parts = user_input.rsplit(' ', 1)
        if len(parts) != 2:
            print("Invalid input. Please enter in the format '<text> <art_style>'.")
            exit()
        text, art_style = parts

print(f"Text: {text}, Art Style: {art_style}, Output File: {output_file}")  # Debugging message

# Get the file path for the selected art style
file_path = art_styles.get(art_style.lower())
if not file_path:
    print(f"Art style '{art_style}' not found. Available styles: {', '.join(art_styles.keys())}.")
    exit()

# Read the ASCII art file
try:
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    ascii_art = {}
    current_symbol_code = 32
    symbol_art = []

    
    for line in lines:
        if len(symbol_art) == 8:
            ascii_art[chr(current_symbol_code)] = symbol_art
            current_symbol_code += 1
            symbol_art = []
        else:
            symbol_art.append(line)

    if len(symbol_art) == 8:
        ascii_art[chr(current_symbol_code)] = symbol_art

except FileNotFoundError:
    print(f"File for art style '{art_style}' not found.")
    exit()


def display_ascii_art(text, output_file=None):
    rows = ['' for _ in range(8)]  
    for char in text:
        art = ascii_art.get(char, [' ' * 8] * 8)  
        for i in range(8):
            rows[i] += art[i] + ' '

    result = "\n".join(rows)

    if output_file:
        try:
            
            with open(output_file, 'w') as f:
                f.write(result)
            print(f"ASCII art written to {output_file}")  
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        
        print(result)


display_ascii_art(text, output_file)
