def total_salary(path):
    try:
        # безпечно читаємо файл
        with open(path, "r", encoding="utf-8") as fl:
            lines = fl.readlines() 

        total = 0
        names = []
        
        #перебираємо кожен рядок, розділяємо його, знаходимо суму значень та записуємо всі імена
        for line in lines:
            try:
                name, salary = line.strip().split(",")
                total += int(salary)
                names.append(name)
            except ValueError:
                print(f"Invalid line: {line.strip()}")
        
        # знаходимо середню зп
        average = total / len(names)
        
        # повертаємо потрібні нам значення
        return (total, int(average))
    except FileNotFoundError:
        print("File not found")
        return (0,0)
    
    except Exception as e:
        print("Some error happend")
        return (0,0)
    
    



        
    
    
# вивід функції
total, average = total_salary("D:/Python Cources GoIT/goit-algo-hw-04/Task1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
