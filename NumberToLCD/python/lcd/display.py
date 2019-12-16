class Display:

    # Intermediate representation
    top_horizontal = 'TH'
    middle_horizontal = 'MH'
    bottom_horizontal = 'BH'
    left_vertical = 'LV'
    right_vertical = 'RV'
    space = 'S'

    # Mapping of intermediate representation to the UNICODE one
    unic = {
        top_horizontal: '\u268B',
        middle_horizontal: '\u268B',
        bottom_horizontal: '\u268B',
        left_vertical: '\u2575',
        right_vertical: '\u2575',
        space: ' ',
        '': ' '
    }

    digits = {
        '0': [['', top_horizontal, ''],
              [left_vertical, space, right_vertical],
              [left_vertical, bottom_horizontal, right_vertical]],

        '1': [['', space, ''],
              ['', space, right_vertical],
              ['', space, right_vertical]],

        '2': [['', top_horizontal, ''],
              ['', middle_horizontal, right_vertical],
              [left_vertical, bottom_horizontal, '']],

        '3': [['', top_horizontal, ''],
              ['', middle_horizontal, right_vertical],
              ['', bottom_horizontal, right_vertical]],

        '4': [['', space, ''],
              [left_vertical, middle_horizontal, right_vertical],
              ['', space, right_vertical]],

        '5': [['', top_horizontal, ''],
              [left_vertical, middle_horizontal, ''],
              ['', bottom_horizontal, right_vertical]],

        '6': [['', top_horizontal, ''],
              [left_vertical, middle_horizontal, ''],
              [left_vertical, bottom_horizontal, right_vertical]],

        '7': [['', top_horizontal, ''],
              ['', space, right_vertical],
              ['', space, right_vertical]],

        '8': [['', top_horizontal, ''],
              [left_vertical, middle_horizontal, right_vertical],
              [left_vertical, bottom_horizontal, right_vertical]],

        '9': [['',  top_horizontal, ''],
              [left_vertical, middle_horizontal, right_vertical],
              ['',  space, right_vertical]]
    }

    def __init__(self, scale_factor=1, number=0):
        self._scale_factor = scale_factor
        self._number = str(number)

    def _is_vertical(self, s: str) -> bool:
        return True if s == self.right_vertical or \
                       s == self.left_vertical else False

    def _is_horizontal(self, s: str) -> bool:
        return True if s == self.top_horizontal or \
                       s == self.middle_horizontal or \
                       s == self.bottom_horizontal else False

    def _is_space(self, s: str) -> bool:
        return True if s == self.space else False

    def _render(self, s: str) -> str:
        if self._is_vertical(s):
            return self.unic[s]
        if self._is_horizontal(s) or self._is_space(s):
            return self.unic[s] * self._scale_factor
        return self.unic[s]

    def _get_scaler_str(self, s: str) -> str:
        return s.replace(self.unic[self.middle_horizontal], self.unic[self.space])

    def _need_vertical_scaling(self, s: str) -> bool:
        return True if self.unic[self.left_vertical] in s or \
                       self.unic[self.right_vertical] in s else False

    def _scale(self, s: str) -> str:
        scale_str = ''
        for scale_iteration in range(0, self._scale_factor - 1):
            scale_str += self._get_scaler_str(s) + '\n'
        return scale_str

    def show(self) -> str:
        display_str = ''
        for y in range(0, len(self.digits['0'])):
            line = ''
            for d in self._number:
                s = ''
                for i in self.digits[d][y]:
                    s += self._render(i)

                line += s

            if self._need_vertical_scaling(line):
                display_str += self._scale(line)

            display_str += line + '\n'
        return display_str
