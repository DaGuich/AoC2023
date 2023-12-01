# just used to read the input file
from pathlib import Path

# digits as chars
from string import digits


def convert_spelled_letters(line: str) -> str:
    spelled_digits = (
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9'),
    )

    # replace all spelled digits
    for (spelled, real) in spelled_digits:
        # we cannot just replace it with the real numbers,
        # but we have to make sure that other combinations still work
        # i.e. sevenine should result to 79
        # if we would just replace it "dumb" we'd just get 7ine
        replace_with = spelled + real + spelled
        line = line.replace(spelled, replace_with)
    return line


def process(lines: list[str]) -> int:
    # remove whitespace
    lines = map(lambda line: line.strip(), lines)
    # filter for empty lines
    lines = filter(lambda line: len(line) > 0, lines)
    # convert spelled out digits to actual digits
    lines = map(convert_spelled_letters, lines)
    # filter for digits in lines
    lines = map(lambda line: filter(lambda c: c in digits, line), lines)
    # join digits (char) to one string per line
    nums = map(lambda line: ''.join(line), lines)
    # create int out of first digit and last digit
    nums = list(map(lambda num: int(num[0] + num[-1]), nums))
    # return sum
    return sum(nums)


if __name__ == '__main__':
    input_file = Path(__file__).parent / 'input.txt'

    # first test with test input
    example = """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """
    assert process(example.split('\n')) == 281

    # process actual data
    with input_file.open() as f:
        result = process(f.readlines())
        print(result)


