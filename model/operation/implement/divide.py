"""
Operation: divide
"""


def generate_code(json_dict, lang='python'):
    result = ''
    divide_1, divide_2, output = parse_json(json_dict)
    if lang == 'python':
        result = "{} = {} / {}".format(output, divide_1, divide_2)
    return result


def parse_json(json_dict):
    """
    @param json_dict: should have keys: divide_1, divide_2, output
    @return: strings of divide_1, divide_2, output
    """
    try:
        return str(json_dict['divide_1']), str(json_dict['divide_2']), str(json_dict['output'])
    except Exception:
        raise KeyError('Error while paring: Divid')


if __name__ == '__main__':
    print(generate_code({'divide_1': 'a', 'divide_2': 'b', 'output': 'asd'}))
