"""
Operation: Multiply
"""


def generate_code(json_dict, lang='python'):
    result = ''
    multiply_1, multiply_2, output = parse_json(json_dict)
    if lang == 'python':
        result = "{} = {} * {}".format(output, multiply_1, multiply_2)
    return result


def parse_json(json_dict):
    """
    @param json_dict: should have keys: multiply_1, multiply_2, output
    @return: strings of multiply_1, multiply_2, output
    """
    try:
        return str(json_dict['multiply_1']), str(json_dict['multiply_2']), str(json_dict['output'])
    except Exception:
        raise KeyError('Error while paring: Multiply')


if __name__ == '__main__':
    print(generate_code({'multiply_1': 'a', 'multiply_2': 'b', 'output': 'asd'}))
