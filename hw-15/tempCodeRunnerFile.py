elevator = hw.Elevator()
        elevator.go_up()
        self.assertEqual(elevator.get_current_floor(), 1)
        elevator.go_down()
        self.assertEqual(elevator.get_current_floor(), 0)
        elevator.go_down()
        self.assertEqual(elevator.get_current_floor(), 0)