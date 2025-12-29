def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Файл {filename} не найден"
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"
