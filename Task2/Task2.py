def get_cats_info(path):
    try:
        # безпечно читаємо файл
        with open(path, "r", encoding="utf-8") as fl:
            lines = fl.readlines()
            
            cats_list = []
            
        #перебираємо кожен рядок, розділяємо його і формуємо словники для кожного запису
        for line in lines:
            try:
                clear_line = line.strip()
                id, name, age = clear_line.split(",")
                
                # Якщо id пустий, ігноруємо рядок
                if not id.strip():
                    print(f"Skipped line due to empty ID: {line.strip()}")
                    continue
                
                cats_list.append({'id': id, 'name': name, 'age': age})
                
            except ValueError:
                print(f"Invalid line: {line.strip()}")
        return cats_list
    
    except FileNotFoundError:
        print("File not found")
        return None
    
    except Exception as e:
        print("Some error happend: {e}")
        return None
        
# вивід функції        
cats_info = get_cats_info("D:/Python Cources GoIT/goit-algo-hw-04/Task2/cats_file.txt")
print(cats_info)