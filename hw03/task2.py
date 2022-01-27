def userdata(**kwargs):
    for k, v in kwargs.items():
        print(f"{k.upper()}: {v}", end=", ")


data = {
    "name": "John",
    "lastname": "Smith",
    "year": "1900",
    "city": "New York",
    "email": "johnsmith@gmail.com",
    "phone": "+12125130514"
}

userdata(**data)
