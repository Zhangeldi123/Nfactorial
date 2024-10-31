def test_compose(self):
        def plus_one(x):
            return x + 1
        def double(x):
            return x * 2
        new_func = hw.compose(plus_one, double)
        self.assertEqual(new_func(3), 8)
        self.assertEqual(new_func(0), 2)