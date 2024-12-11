import os

def open_file():
    filename = input("Введите имя файла: ")
    try:
        with open(filename, 'r') as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print("Файл не найден.")
        return ""

def save_file(text):
    filename = input("Введите имя файла для сохранения: ")
    try:
        with open(filename, 'w') as f:
            f.write(text)
        print("Файл сохранен.")
    except Exception as e:
        print(f"Ошибка сохранения файла: {e}")

def edit_text():
    text = open_file()
    print("Текст файла:")
    print(text)
    new_text = input("Введите измененный текст (или оставьте пустым для выхода): ")
    if new_text:
      save_file(new_text)


if __name__ == "__main__":
    edit_text()