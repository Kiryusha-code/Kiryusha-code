import json

class UserProfile:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "interests": self.interests
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["interests"])

def save_profile(user, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(user.to_dict(), f)
    except (IOError, TypeError) as e:
        print(f"Ошибка сохранения: {e}")

def load_profile(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return UserProfile.from_dict(data)
    except FileNotFoundError:
        print("Файл не найден")
    except json.JSONDecodeError:
        print("Ошибка: файл поврежден или не является JSON")
    except KeyError as e:
        print(f"Ошибка: отсутствует обязательное поле {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    return None

# Пример использования
user = UserProfile("Alice", 25, ["Python", "AI"])
save_profile(user, "profile.json")
new_user = load_profile("profile.json")

if new_user:
    print(f"Загружен профиль: {new_user.name}, {new_user.age} лет")
    print(f"Интересы: {', '.join(new_user.interests)}")
