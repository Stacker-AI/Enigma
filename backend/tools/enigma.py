import re

class EnigmaGuard:
    def __init__(self):
        self.patterns = {}
        self.anonymization_mapping = {}

    def add_pattern(self, name, regex):
        self.patterns[name] = re.compile(regex, re.IGNORECASE)

    def add_anonymization_mapping(self, name, replacement):
        self.anonymization_mapping[name] = replacement

    def filter(self, text):
        filtered_text = text
        for name, pattern in self.patterns.items():
            filtered_text = pattern.sub(f"<{name}>", filtered_text)
            for match in pattern.finditer(text):
                self.add_anonymization_mapping(name, match.group())
        return filtered_text

    def defilter(self, text):
        defiltered_text = text
        for name, replacement in self.anonymization_mapping.items():
            defiltered_text = defiltered_text.replace(f"<{name}>",replacement)
        return defiltered_text

enigma_guard = EnigmaGuard()
enigma_guard.add_pattern("phone_number", r"(\d{11}|\d{9})")
enigma_guard.add_pattern("email", r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})")
enigma_guard.add_pattern("name", r"(?:\bMy\s+)?(?:Name(?:\sis)?(?:\s+is)?\s*:?\s*)([a-zA-Z]+ [a-zA-Z]+)")
enigma_guard.add_pattern("cnic", r"(?:\bMy\s+)?(?:CNIC(?:\sis)?(?:\s+is)?\s*:?\s*)(\d{5}-\d{7}-\d)")
enigma_guard.add_pattern("address", r"(?:\bMy\s+)?(?:Address(?:\sis)?(?:\s+is)?\s*:?\s*)([\w\d\s,]+)")
enigma_guard.add_pattern("passport", r"(?:\bMy\s+)?(?:Passport(?:\sis)?(?:\s+is)?\s*:?\s*)([A-Z]{2}\d{7})")
enigma_guard.add_pattern("credit_card", r"(?:\bMy\s+)?(?:Credit\s+Card(?:\sis)?(?:\s+is)?\s*:?\s*)(\d{4}-\d{4}-\d{4}-\d{4})")