elf.assertEqual(hw.missing_elements([1] + [2, 3] + [10**6]), list(range(4, 10**6)))
        self.assertEqual(hw.missing_elements(list(range(1, 10**6+2))), [])