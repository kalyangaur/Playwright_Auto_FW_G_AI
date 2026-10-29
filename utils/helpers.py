import random
import string
import time


class DataGenerator:
    """Helper to generate random test data for automated forms and tables."""

    @staticmethod
    def random_string(length: int = 8) -> str:
        return "".join(random.choices(string.ascii_letters, k=length))

    @staticmethod
    def random_name() -> str:
        first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Sam", "Chris", "Casey", "Riley"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    @staticmethod
    def random_email() -> str:
        timestamp = int(time.time() * 1000)
        return f"testuser_{timestamp}@example.com"

    @staticmethod
    def random_phone() -> str:
        return "".join(random.choices(string.digits, k=10))

    @staticmethod
    def random_salary() -> str:
        return str(random.randint(40000, 150000))

    @staticmethod
    def random_age() -> str:
        return str(random.randint(22, 60))

