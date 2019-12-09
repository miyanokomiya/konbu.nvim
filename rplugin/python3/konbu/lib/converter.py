import re
from typing import List


def convert_p(lines: List[str]) -> List[str]:
    ret = []

    text = re.sub('\n{3,}', '\n\n', '\n'.join(lines))
    blocks = text.split('\n\n')

    for block in blocks:
        if block != '':
            ret.append(convert_block(block))

    return ret


def convert_block(block: str) -> str:
    ret = []

    lines = block.split('\n')
    ret.append('<p>')

    for index, line in enumerate(lines):
        if line == '':
            continue
        elif index > 0:
            ret.append('<br/>' + line.strip())
        else:
            ret.append(line.strip())

    ret.append('</p>')
    return ''.join(ret)
