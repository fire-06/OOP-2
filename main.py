#Задание 1
cook_book = {}

with open('cook.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
cook_name = ''
for line in lines:
    line = line.strip()
    if line:
        if not cook_name:
            cook_name = line
            cook_book[cook_name] = []
        else:
            ingredient_data = line.split(' | ')
            if len(ingredient_data) == 3:
                ingredient_name = ingredient_data[0]
                quantity = int(ingredient_data[1])
                measure = ingredient_data[2]
                cook_book[cook_name].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
    else:
        cook_name = ''

print("cook_book = {")
for recipe, ingredients in cook_book.items():
    print(f"  '{recipe}': [")
    for ingredient in ingredients:
        print(f"    {{'ingredient_name': '{ingredient['ingredient_name']}', 'quantity': {ingredient['quantity']}, 'measure': '{ingredient['measure']}'}},")

    print("  ],")
print("}")
print()
print()
#Задание 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity

    return shop_list


dishes_to_cook = ['Запеченный картофель', 'Омлет']
persons = 2
result = get_shop_list_by_dishes(dishes_to_cook, persons)

print("{")
for ingredient, values in result.items():
    print(f"  '{ingredient}': {{'measure': '{values['measure']}', 'quantity': {values['quantity']}}},")
print("}")

#Задание 3

def merge_files(file_paths, result_file):
    file_contents = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_name = file_path.split('/')[-1]
            lines = file.readlines()
            file_contents.append((file_name, len(lines), lines))

    file_contents.sort(key=lambda x: x[1])

    with open(result_file, 'w', encoding='utf-8') as result:
        for file_name, line_count, lines in file_contents:
            result.write(f"{file_name}\n{line_count}\n")
            result.writelines(lines)
            result.write('\n')

file_paths = ['1.txt', '2.txt']
result_file = 'result.txt'
merge_files(file_paths, result_file)