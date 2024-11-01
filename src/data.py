from faker import Faker


class User:

    @staticmethod
    def generate_user_data():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return reg_data


    valid_data = {
    "email": "nuhjnj44@gmail.com",
    "password": "password",
    "name": "Anna"
}

    invalid_data = {
        "email": 'ghjafghjyd876',
        "password": "jhjh8776544"
    }

    duplicate_user_data = {
        "email": 'nuhjnj44@gmail.com',
        "password": "password",
        "name": "Anna"
    }

    data_missing_email = {
        "email": '',
        "password": "password",
        "name": "Anna"
    }

    data_missing_password = {
        "email": 'nuhjnj44@gmail.com',
        "password": "",
        "name": "Anna"
    }

    data_missing_name = {
        "email": 'nuhjnj44@gmail.com',
        "password": "password",
        "name": ""
    }

    updated_user_data = {
        "email": 'nuhjnj44@gmail.com',
        "password": "password",
        "name": "Andrey"
    }
