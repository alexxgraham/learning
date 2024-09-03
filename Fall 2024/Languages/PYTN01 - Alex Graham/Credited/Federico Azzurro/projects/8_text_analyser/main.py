# ----------------------------------------------------------------------
# |  main.py
# |
# |  by Federico Azzurro
# ----------------------------------------------------------------------
def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text

def analyse(text: str) -> dict[str, int]:
    result: dict[str, int] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_excl_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split())
    }

    return result

def main() -> None:
    text: str = open_file(path='note.txt')
    analysis: dict[str, int] = analyse(text)

    for key, value in analysis.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    main()

"""
1. Create a much more user friendly message regarding the analysis (eg. "This text file contains...").
2. Add the top 5 most common words to the analysis message.

"""