import re

class EnigmaGuard:
    def __init__(self):
        self.patterns = {}
        self.anonymization_mapping = {}

    def add_pattern(self, name, regex):
        self.patterns[name] = re.compile(regex)

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

# Example Usage:
enigma_guard = EnigmaGuard()
enigma_guard.add_pattern("phone_number", r"(92\d{10}|03\d{9}|3\d{9})")
enigma_guard.add_pattern("email", r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})")
enigma_guard.add_pattern("name", r"([A-Z][a-z]+ [A-Z][a-z]+)")
enigma_guard.add_pattern("address", r"(\d+ [A-Z][a-z]+ [A-Z][a-z]+)")
enigma_guard.addd_pattern("cnic", r"(\d{5}-\d{7}-\d{1})")


text_with_pii = "John Doe's phone number is 03211234567."
filtered_text = enigma_guard.filter(text_with_pii)
original_text = enigma_guard.defilter(filtered_text)

print(f"Original Text: {text_with_pii}")
print(f"Filtered Text: {filtered_text}")
print(f"Original Text: {original_text}")

print("done by healthlink-360")