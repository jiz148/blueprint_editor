"""
Operation: Minus
"""


def generate_code(json_dict, lang='python'):
    result = ''
    minus_1, minus_2, output = parse_json(json_dict)
    if lang == 'python':
        result = "{} = {} - {}".format(output, minus_1, minus_2)
    return result


def parse_json(json_dict):
    """
    @param json_dict: should have keys: minus_1, minus_2, output
    @return: strings of minus_1, minus_2, output
    """
    try:
        return str(json_dict['minus_1']), str(json_dict['minus_2']), str(json_dict['output'])
    except Exception:
        raise KeyError('Error while paring: Minus')


if __name__ == '__main__':
    print(generate_code({'minus_1': 'a', 'minus_2': 'b', 'output': 'asd'}))
