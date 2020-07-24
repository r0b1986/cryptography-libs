def rot_char(input, shift: int):
    """Apply Caesar shift to a character."""
    input = ord(input)
    if input >= ord('a') and input <= ord('z'):
        return chr(ord('a') + (input - ord('a') + shift) % 26)
    elif input >= ord('A') and input <= ord('Z'):
        return chr(ord('A') + (input - ord('A') + shift) % 26)
    return chr(input)

def rot_string(input, shift:int):
    if shift < 0:
        shift = 26 - (abs(shift) % 26)
    result = ""
    for char in input:
        result += rot_char(char, shift)
    return result

def crack_caesar(input: str):
    english_freq = []
