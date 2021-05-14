"""
Koan to learn annotating the dictionary with fixed key/values.
"""

import datetime
import random
from uuid import UUID4


# Annotate the return type as TypedDict
# Documentation: https://docs.python.org/3/library/typing.html#typing.TypedDict
def get_random_user_data():
    return {
        "user_id": UUID4(),
        "company_id": random.randint(1, 1_000_000),
        "is_active": random.choice([True, False]),
        "last_seen": datetime.datetime.utcnow(),
    }


print(get_random_user_data())
