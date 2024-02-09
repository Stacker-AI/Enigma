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
enigma_guard.add_pattern("name", r"(Name:|Name is|My name is) ([a-zA-Z]+ [a-zA-Z]+)")
enigma_guard.add_pattern("cnic", r"(CNIC:|CNIC is|My CNIC is) (\d{5}-\d{7}-\d)")
enigma_guard.add_pattern("address", r"(Address:|Address is|My address is) (House \d+, Street \d+, Area \d+, City \d+)")
enigma_guard.add_pattern("passport", r"(Passport:|Passport is|My passport is) ([A-Z]{2}\d{7})")
enigma_guard.add_pattern("credit_card", r"(Credit Card:|Credit Card is|My credit card is) (\d{4}-\d{4}-\d{4}-\d{4})")

# Testing:

text = "My name is John Doe. My phone number is 923001234567. My email is faisal@gmail.com. My CNIC is 12345-1234567-1. My address is House 123, Street 123, Area 123, City 123. My passport is AB1234567. My credit card is 1234-5678-1234-5678."
filtered_text = enigma_guard.filter(text)
print(filtered_text)
defiltered_text = enigma_guard.defilter(filtered_text)
print(defiltered_text)
