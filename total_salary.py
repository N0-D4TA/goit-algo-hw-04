from pathlib import Path


def total_salary(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Initializing sum and quantity of salaries
            total = 0
            count = 0
            # Parsing and counting salaries from string
            for line in file:
                try:
                    worker, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                # Skips non-digit salaries and 
                except ValueError:
                    print("Файл містить неправильно форматовані записи!")
                    continue
            # No data to operate with
            if  count == 0:
                print("Файл порожній або не містить даних про зарплату!")
                return (0, 0)
            average = total / count
            return total, int(average)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        return (0, 0)



total, average = total_salary('C:/Users/User/Desktop/goit-algo-hw-04/salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")