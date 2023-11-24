class FiniteAutomata:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.initial_state = None
        self.final_states = set()

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip().split()
                if line[0] == 'states':
                    self.states = set(line[1:])
                elif line[0] == 'alphabet':
                    self.alphabet = set(line[1:])
                elif line[0] == 'transitions':
                    for transition in line[1:]:
                        start, symbol, end = transition.split(',')
                        self.transitions[(start, symbol)] = end
                elif line[0] == 'initial':
                    self.initial_state = line[1]
                elif line[0] == 'final':
                    self.final_states = set(line[1:])

    def display_states(self):
        print("Set of states: ", self.states)

    def display_alphabet(self):
        print("Alphabet: ", self.alphabet)

    def display_transitions(self):
        print("Transitions: ")
        for (start, symbol), end in self.transitions.items():
            print(f"{start}--{symbol}-->{end}")

    def display_initial(self):
        print("Initial state: ", self.initial_state)

    def display_final_states(self):
        print("Final states are: ", self.final_states)

def main():
    fa = FiniteAutomata()
    filename = input("Enter the filename for the Finite Automata: ")
    fa.read_from_file(filename)

    while True:
        print("\n 1.Display states")
        print("\n 2.Display alphabet")
        print("\n 3.Display transitions")
        print("\n 4.Display initial state")
        print("\n 5.Display final states")
        print("\n 6.Exit the program")

        choice = input("Enter your choice(1/2/3/4/5/6): ")

        if choice == '1':
            fa.display_states()
        elif choice == '2':
            fa.display_alphabet()
        elif choice == '3':
            fa.display_transitions()
        elif choice == '4':
            fa.display_initial()
        elif choice == '5':
            fa.display_final_states()
        elif choice == '6':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please input a valid option! ")

if __name__ == '__main__':
    main()