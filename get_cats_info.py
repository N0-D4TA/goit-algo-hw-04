from pathlib import Path


def get_cats_info(file_path: Path) -> list:
    cats = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    cat = {
                        'id': id, 
                        'name': name, 
                        'age': age
                        }
                    cats.append(cat)
                except ValueError:
                    print("Файл містить неправильно форматовані записи!")
                    continue
            if len(cats) == 0:
                print("Немає даних про котів або файл порожній!")
                return cats
            return cats
    except FileNotFoundError:
        print("Файл не знайдено!")
        return cats


cats_info = get_cats_info('C:/Users/User/Desktop/goit-algo-hw-03/cats_file.txt')
print(cats_info)