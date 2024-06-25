import json

def employees_rewrite(sort_type):
    with open("employees.json", "r") as json_file:
        data = json.load(json_file)
    if sort_type not in data['employees'][0]:
        raise ValueError('Bad key for sorting')
    data['employees'].sort(key=lambda x: x[sort_type],
                           reverse=isinstance(data['employees'][0][sort_type], int))

    with open(f'employees_{sort_type}_sorted.json',
              'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Сотрудники успешно отсортированы по ключу '{sort_type}' "
          f"и записаны в файл 'employees_{sort_type}_sorted.json'")





employees_rewrite('lastName')
