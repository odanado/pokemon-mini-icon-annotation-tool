import json
import numpy as np
from pathlib import Path

import cv2


def main():
    Path('data/icons').mkdir(exist_ok=True)
    icons = cv2.imread('data/smicons-sheet.png')
    test_icons = np.array(icons)
    poke2num = dict(json.loads(Path('data/poke2num.json').read_text()))
    for poke, num in poke2num.items():
        top = num // 12 * 30
        left = (num % 12) * 40
        cv2.rectangle(test_icons, (left, top),
                      (left + 40, top + 30), (0, 0, 255), 1)

        icon = icons[top:top + 30, left:left + 40, :]
        fname = 'data/icons/{}.png'
        assert not Path(fname).exists()
        cv2.imwrite(fname.format(poke), icon)

    # test.png を目視してだいたい大丈夫か確認する
    cv2.imwrite('data/test.png', test_icons)


if __name__ == '__main__':
    main()
