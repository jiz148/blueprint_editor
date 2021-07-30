"""
Operation: Plus
"""


def generate_code(json_dict):
    plus_1, plus_2, output = parse_json(json_dict)
    return "{} = {} + {}".format(output, plus_1, plus_2)


def parse_json(json_dict):
    """
    @param json_dict: should have keys: plus_1, plus_2, output
    @return: strings of plus_1, plus_2, output
    """
    try:
        return str(json_dict['plus_1']), str(json_dict['plus_2']), str(json_dict['output'])
    except Exception:
        raise KeyError('Error while paring: plus')


if __name__ == '__main__':
    print(generate_code({'plus_1': 'a', 'plus_2': 'b', 'output': 'asd'}))
