class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def go_to_floor(self, target_floor):
        if target_floor > self.top:
            print(f"Cannot go to floor {target_floor}. Maximum floor is {self.top}.")
            return
        elif target_floor < self.bottom:
            print(f"Cannot go to floor {target_floor}. Minimum floor is {self.bottom}.")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Going up. Now at floor {self.current_floor}.")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Going down. Now at floor {self.current_floor}.")

if __name__ == "__main__":
    elevator = Elevator(1, 10)
    elevator.go_to_floor(5)
    elevator.go_to_floor(1)
