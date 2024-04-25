from faker import Faker
from presidio_anonymizer.entities import OperatorConfig

fake = Faker(locale="en_US")


def fake_phone_number(_=None):
    return fake.phone_number()


phone_number_operator = {
    "PHONE_NUMBER": OperatorConfig("custom", {"lambda": fake_phone_number})
}
