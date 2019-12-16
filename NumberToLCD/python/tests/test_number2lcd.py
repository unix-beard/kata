import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lcd.display import Display


class TestDisplay(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Display.unic[Display.space]
        self.lv = Display.unic[Display.left_vertical]
        self.rv = Display.unic[Display.right_vertical]
        self.th = Display.unic[Display.top_horizontal]
        self.mh = Display.unic[Display.middle_horizontal]
        self.bh = Display.unic[Display.bottom_horizontal]
        self.s_th_s = f"{self.s}{self.th}{self.s}"
        self.lv_bh_rv = f"{self.lv}{self.bh}{self.rv}"
        self.lv_mh_rv = f"{self.lv}{self.mh}{self.rv}"

    def test_with_scale_one_number_one(self):
        d = Display(scale_factor=1, number=1)
        self.assertEqual(f"{self.s*3}\n{self.s*2}{self.rv}\n{self.s*2}{self.rv}\n", d.show())

    def test_with_scale_one_number_two(self):
        d = Display(scale_factor=1, number=2)
        self.assertEqual(f"{self.s_th_s}\n{self.s}{self.mh}{self.rv}\n{self.lv}{self.bh}{self.s}\n", d.show())

    def test_with_scale_one_number_three(self):
        d = Display(scale_factor=1, number=3)
        self.assertEqual(f"{self.s_th_s}\n{self.s}{self.mh}{self.rv}\n{self.s}{self.bh}{self.rv}\n", d.show())

    def test_with_scale_one_number_four(self):
        d = Display(scale_factor=1, number=4)
        self.assertEqual(f"{self.s*3}\n{self.lv_mh_rv}\n{self.s*2}{self.rv}\n", d.show())

    def test_with_scale_one_number_five(self):
        d = Display(scale_factor=1, number=5)
        self.assertEqual(f"{self.s_th_s}\n{self.lv}{self.mh}{self.s}\n{self.s}{self.bh}{self.rv}\n", d.show())

    def test_with_scale_one_number_six(self):
        d = Display(scale_factor=1, number=6)
        self.assertEqual(f"{self.s_th_s}\n{self.lv}{self.mh}{self.s}\n{self.lv_bh_rv}\n", d.show())

    def test_with_scale_one_number_seven(self):
        d = Display(scale_factor=1, number=7)
        self.assertEqual(f"{self.s_th_s}\n{self.s*2}{self.rv}\n{self.s*2}{self.rv}\n", d.show())

    def test_with_scale_one_number_eight(self):
        d = Display(scale_factor=1, number=8)
        self.assertEqual(f"{self.s_th_s}\n{self.lv_mh_rv}\n{self.lv_bh_rv}\n", d.show())

    def test_with_scale_one_number_nine(self):
        d = Display(scale_factor=1, number=9)
        self.assertEqual(f"{self.s_th_s}\n{self.lv_mh_rv}\n{self.s*2}{self.rv}\n", d.show())

    def test_with_scale_one_number_zero(self):
        d = Display(scale_factor=1, number=0)
        self.assertEqual(f"{self.s_th_s}\n{self.lv}{self.s}{self.rv}\n{self.lv_bh_rv}\n", d.show())

    def test_with_scale_two_number_one(self):
        d = Display(scale_factor=2, number=1)
        s_3_rv = f"{self.s*3}{self.rv}"
        self.assertEqual(f"{self.s*4}\n{s_3_rv}\n{s_3_rv}\n{s_3_rv}\n{s_3_rv}\n", d.show())


if __name__ == '__main__':
    unittest.main()
