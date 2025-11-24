profile_fields = [
    "name", "email", "password", "bio",
    "address", "pincode", "state",
    "country", "phone"
]

def is_filled(value):
    return value is not None and str(value).strip() != ""

def clct_profile_completion(user):
    filled = 0

    for f in profile_fields:
        if is_filled(user.get(f)):
            filled = filled + 1
    total = len(profile_fields)
    return round((filled / total) * 100)
