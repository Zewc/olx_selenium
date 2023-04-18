import json


def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        clear_data('data.json', 'clear_data.json')


def clear_data(data, clear_data):
    with open(data) as file1:
        data = json.load(file1)
        output_data = [v for v in {inp['link']: inp for inp in data}.values()]
        with open(clear_data, 'w', encoding='utf-8') as file2:
            json.dump(output_data, file2, indent=4, ensure_ascii=False)
