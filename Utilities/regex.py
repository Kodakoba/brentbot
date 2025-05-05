import re

class Regex:
    def __init__(self):
        pass

    def escape_regex(self, text):
        return re.escape(text)

    def text_to_regex(self, text, exact_match:bool, case_insensitive:bool):
       #    args:
      # #   text: The input text string.
     #   #  exact_match: If True, the regex will match the whole string. If False, it can match a substring.
    #     # case_insensitive: If True, the regex will ignore case.
        escaped_text = self.escape_regex(text)
        if exact_match:
            regex = r"^" + escaped_text + r"$"
        else:
            regex = escaped_text

        if case_insensitive:
            regex = r"(?i)" + regex

        return regex
