from abc import ABC, abstractmethod

# === STRATEGY PATTERN ===
class MoveStrategy(ABC):
    @abstractmethod
    def move(self):
        pass

class WalkStrategy(MoveStrategy):
    def move(self):
        print("Робот іде пішки.")

class RollStrategy(MoveStrategy):
    def move(self):
        print("Робот їде на колесах.")

class FlyStrategy(MoveStrategy):
    def move(self):
        print("Робот летить.")

# === STATE PATTERN ===
class RobotState(ABC):
    @abstractmethod
    def handle(self, robot):
        pass

class IdleState(RobotState):
    def handle(self, robot):
        print("Робот у режимі очікування.")

class WorkingState(RobotState):
    def handle(self, robot):
        print("Робот виконує роботу.")
        robot.perform_move()

class ChargingState(RobotState):
    def handle(self, robot):
        print("Робот заряджається.")

# === CONTEXT ===
class Robot:
    def __init__(self, move_strategy: MoveStrategy, state: RobotState):
        self.move_strategy = move_strategy
        self.state = state

    def set_move_strategy(self, strategy: MoveStrategy):
        self.move_strategy = strategy
        print("Змінено спосіб руху.")

    def set_state(self, state: RobotState):
        self.state = state
        print("Змінено стан робота.")

    def perform_move(self):
        self.move_strategy.move()

    def do_action(self):
        self.state.handle(self)

# === MAIN MENU ===
def main():
    robot = Robot(WalkStrategy(), IdleState())

    while True:
        print("\n=== Робот Меню ===")
        print("1. Змінити спосіб руху")
        print("2. Змінити стан")
        print("3. Виконати дію")
        print("4. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            print("Виберіть спосіб руху:")
            print("a. Йти")
            print("b. Їхати")
            print("c. Летіти")
            move_choice = input("Ваш вибір: ")
            if move_choice == 'a':
                robot.set_move_strategy(WalkStrategy())
            elif move_choice == 'b':
                robot.set_move_strategy(RollStrategy())
            elif move_choice == 'c':
                robot.set_move_strategy(FlyStrategy())
            else:
                print("Хибний вибір.")
        elif choice == '2':
            print("Виберіть стан:")
            print("a. Очікування")
            print("b. Робота")
            print("c. Заряджання")
            state_choice = input("Ваш вибір: ")
            if state_choice == 'a':
                robot.set_state(IdleState())
            elif state_choice == 'b':
                robot.set_state(WorkingState())
            elif state_choice == 'c':
                robot.set_state(ChargingState())
            else:
                print("Хибний вибір.")
        elif choice == '3':
            robot.do_action()
        elif choice == '4':
            print("Завершення програми.")
            break
        else:
            print("Хибний вибір.")

if __name__ == "__main__":
    main()
