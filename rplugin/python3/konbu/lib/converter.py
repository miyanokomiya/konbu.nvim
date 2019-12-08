import re
from typing import List


def convert_p(lines: List[str]) -> List[str]:
    ret = []

    text = re.sub('\n{3,}', '\n\n', '\n'.join(lines))
    blocks = text.split('\n\n')

    for block in blocks:
        ret = ret + convert_block(block)

    return ret


def convert_block(block: str) -> List[str]:
    ret = []

    lines = block.split('\n')
    ret.append('<p>')

    for index, line in enumerate(lines):
        if index > 0:
            ret.append('<br/>' + line)
        else:
            ret.append(line)

    ret.append('</p>')
    return ret
