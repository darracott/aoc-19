"""Contains useful common classes for Advent of Code problems."""


KNOWN_OPCODES = [1, 2, 3, 4, 5, 6, 7, 8, 99]
KNOWN_MODES = [0, 1]


class IntCodeComputer(object):
    """
    Computes IntCode programs.
    """
    def __init__(self, intcode):
        self.memory = list(intcode)
        self.instruction_pointer = 0
        self.running = False
        self.waiting_for_input = False
        self.user_mode = False
        self.known_opcodes = KNOWN_OPCODES
        self.known_modes = KNOWN_MODES
        self.inputs = []
        self.outputs = []

    def queue_input(self, _input):
        """
        Adds an input to the back of the queue.
        """
        assert isinstance(_input, int)
        self.inputs.append(_input)

    def retrieve_value(self, parameter, mode):
        """
        Get the value from
        """
        if mode == 0:
            # Position mode.
            return self.memory[parameter]
        elif mode == 1:
            # Immediate mode.
            return parameter
        else:
            print(f"Unknown parameter mode: {mode}")

    def step_forward(self):
        # Get the instruction value.
        instruction = self.memory[self.instruction_pointer]

        # Parse instruction to extract opcode and parameter modes.
        digits = [digit for digit in str(instruction)]
        opcode = int("".join(digits[-2:]))
        parameter_modes = [ int(mode) for mode in digits[-3::-1] ]

        # Check we've got a good Opcode.
        if opcode not in self.known_opcodes:
            print(f"Unknown opcode: {opcode}")
            self.running = False

        # Opcode3 requires input.
        # If we don't have it and don't expext user input, then wait.
        if opcode == 3 and not self.inputs and not self.user_mode:
            self.waiting_for_input = True
            return

        # Run the instruction.
        if parameter_modes:
            self.__getattribute__(f"opcode{opcode}")(*parameter_modes)
        else:
            self.__getattribute__(f"opcode{opcode}")()

    def run(self):
        self.running = True
        self.waiting_for_input = False
        while self.running and not self.waiting_for_input:
            # print(self.memory)
            self.step_forward()

    def opcode1(self, mode_a=0, mode_b=0, mode_c=0):
        """
        Adds the values from addresses a and b.
        Writes this sum to address c.
        """
        # print(f"running 1 with {[mode_a, mode_b,mode_c]}")
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        self.memory[c] = self.retrieve_value(a, mode_a) + self.retrieve_value(b, mode_b)
        self.instruction_pointer += 4

    def opcode2(self, mode_a=0, mode_b=0, mode_c=0):
        """
        Multiplies the values from addresses a and b.
        Writes this sum to address c.
        """
        # print(f"running 2 with {[mode_a, mode_b,mode_c]}")
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        self.memory[c] = self.retrieve_value(a, mode_a) * self.retrieve_value(b, mode_b)
        self.instruction_pointer += 4

    def opcode3(self, mode_a=0):
        """
        Takes a single integer as input and
        saves it to the address x.

        :param input: An integer
        """
        # Obtain input.
        if self.inputs and not self.user_mode:
            _input = self.inputs.pop(0)
        elif not self.inputs and not self.user_mode:
            print("ERROR: No input found and not expecting user to provide it.")
        else:
            _input = input("Input required: ")

        try:
            _input = int(_input)
        except ValueError as e:
            print("ERROR: Opcode 3 only takes an integer as input.")
            raise(e)

        a = self.memory[self.instruction_pointer + 1]
        self.memory[a] = _input
        self.instruction_pointer += 2

    def opcode4(self, mode_a=0):
        """
        Outputs the value from address a.
        """
        # print(f"running 4 with {[mode_a]}")
        a = self.memory[self.instruction_pointer + 1]
        output = self.retrieve_value(a, mode_a)
        self.outputs.append(output)
        # print(f"Opcode4 output: {output}")
        self.instruction_pointer += 2
        return output

    def opcode5(self, mode_a=0, mode_b=0):
        """
        If the first parameter is non-zero, set the instruction pointer
        to the value from the second parameter.
        Otherwise, do nothing.
        """
        # print(f"running 5 with {[mode_a, mode_b]}")
        a = self.memory[self.instruction_pointer + 1]
        if self.retrieve_value(a, mode_a):
            b = self.memory[self.instruction_pointer + 2]
            self.instruction_pointer = self.retrieve_value(b, mode_b)
        else:
            self.instruction_pointer += 3

    def opcode6(self, mode_a=0, mode_b=0):
        """
        If the first parameter is zero, set the instruction pointer
        to the value from the second parameter.
        Otherwise, do nothing.
        """
        # print(f"running 6 with {[mode_a, mode_b]}")
        a = self.memory[self.instruction_pointer + 1]
        if self.retrieve_value(a, mode_a) == 0:
            b = self.memory[self.instruction_pointer + 2]
            self.instruction_pointer = self.retrieve_value(b, mode_b)
        else:
            self.instruction_pointer += 3

    def opcode7(self, mode_a=0, mode_b=0, mode_c=0):
        """
        If the first parameter is less than the second parameter,
        store 1 in the position given by the third parameter.
        Otherwise, store 0.
        """
        # print(f"running 7 with {[mode_a, mode_b, mode_c]}")
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        if self.retrieve_value(a, mode_a) < self.retrieve_value(b, mode_b):
            self.memory[c] = 1
        else:
            self.memory[c] = 0
        self.instruction_pointer += 4

    def opcode8(self, mode_a=0, mode_b=0, mode_c=0):
        """
        If the first parameter is equal to the second parameter,
        store 1 in the position given by the third parameter.
        Otherwise, store 0.
        """
        # print(f"running 8 with {[mode_a, mode_b, mode_c]}")
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        if self.retrieve_value(a, mode_a) == self.retrieve_value(b, mode_b):
            self.memory[c] = 1
        else:
            self.memory[c] = 0
        self.instruction_pointer += 4

    def opcode99(self):
        """
        Stop running.
        """
        self.running = False