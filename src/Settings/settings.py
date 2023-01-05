import string

TOOL_TITLE = "Password Generator"
FONT_SETTINGS = ("ARIAL", 20, "bold")

CHARACTER_LIST = [string.digits, string.ascii_lowercase, string.punctuation, string.ascii_uppercase]
MIN_LENGTH = 8
MAX_LENGTH =  sum(len(length) for length in CHARACTER_LIST)