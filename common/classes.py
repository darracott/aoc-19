"""Contains useful common classes for Advent of Code problems."""


KNOWN_OPCODES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
KNOWN_MODES = [0, 1, 2]


class IntCodeComputer(object):
    """
    Computes IntCode programs.
    """
    def __init__(self, intcode, additional_memory=0):
        self.memory = list(intcode) + [0]*additional_memory
        self.instruction_pointer = 0
        self.relative_base = 0
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

    def read(self, parameter, mode):
        """
        Get the usable value from parameter with mode.
        """
        if mode == 0:
            # Position mode.
            return self.memory[parameter]
        elif mode == 1:
            # Immediate mode.
            return parameter
        elif mode == 2:
            # Relative mode.
            return self.memory[self.relative_base + parameter]
        else:
            print(f"Unknown parameter mode: {mode}")

    def write(self, value, param, mode):
        """
        Write value to address given my param and mode.
        """
        assert mode != 1
        if mode == 0:
            # Positiion mode.
            self.memory[param] = value
        elif mode == 2:
            # Relative mode.
            self.memory[self.relative_base + param] = value

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
        # Get params.
        param_a = self.memory[self.instruction_pointer + 1]
        param_b = self.memory[self.instruction_pointer + 2]
        param_c = self.memory[self.instruction_pointer + 3]
        # Read vales from params intended to be read.
        value_a = self.read(param_a, mode_a)
        value_b = self.read(param_b, mode_b)
        # Compute content to be written.
        content = value_a + value_b
        # Write content to wherever param c & mode c indicate.
        self.write(content, param_c, mode_c)
        # Bump instruction pointer by 4 as we've used up 1 opcode and 3 params.
        self.instruction_pointer += 4

    def opcode2(self, mode_a=0, mode_b=0, mode_c=0):
        """
        Multiplies the values from addresses a and b.
        Writes this sum to address c.
        """
        # print(f"running 2 with {[mode_a, mode_b,mode_c]}")
        # Get params
        param_a = self.memory[self.instruction_pointer + 1]
        param_b = self.memory[self.instruction_pointer + 2]
        param_c = self.memory[self.instruction_pointer + 3]
        # Read vales from params intended to be read.
        value_a = self.read(param_a, mode_a)
        value_b = self.read(param_b, mode_b)
        # Compute content to be written.
        content = value_a * value_b
        # Write content to wherever param c & mode c indicate.
        self.write(content, param_c, mode_c)
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

        param_a = self.memory[self.instruction_pointer + 1]
        self.write(_input, param_a, mode_a)
        self.instruction_pointer += 2

    def opcode4(self, mode_a=0):
        """
        Outputs the value from address a.
        """
        # print(f"running 4 with {[mode_a]}")
        param_a = self.memory[self.instruction_pointer + 1]
        value_a = self.read(param_a, mode_a)
        self.outputs.append(value_a)
        # print(f"Opcode4 output: {value_a}")
        self.instruction_pointer += 2
        return value_a

    def opcode5(self, mode_a=0, mode_b=0):
        """
        If the first parameter is non-zero, set the instruction pointer
        to the value from the second parameter.
        Otherwise, do nothing.
        """
        # print(f"running 5 with {[mode_a, mode_b]}")
        param_a = self.memory[self.instruction_pointer + 1]
        value_a = self.read(param_a, mode_a)
        if value_a:
            param_b = self.memory[self.instruction_pointer + 2]
            value_b = self.read(param_b, mode_b)
            self.instruction_pointer = value_b
        else:
            self.instruction_pointer += 3

    def opcode6(self, mode_a=0, mode_b=0):
        """
        If the first parameter, a, is zero, set the instruction pointer
        to the value from the second parameter, b.
        Otherwise, do nothing.
        """
        # print(f"running 6 with {[mode_a, mode_b]}")
        param_a = self.memory[self.instruction_pointer + 1]

        value_a = self.read(param_a, mode_a)
        if value_a == 0:
            param_b = self.memory[self.instruction_pointer + 2]

            value_b = self.read(param_b, mode_b)
            self.instruction_pointer = value_b
        else:
            self.instruction_pointer += 3

    def opcode7(self, mode_a=0, mode_b=0, mode_c=0):
        """
        If the first parameter, a, is less than the second parameter, b,
        store 1 in the position given by the third parameter, c.
        Otherwise, store 0.
        """
        # print(f"running 7 with {[mode_a, mode_b, mode_c]}")
        param_a = self.memory[self.instruction_pointer + 1]
        param_b = self.memory[self.instruction_pointer + 2]
        param_c = self.memory[self.instruction_pointer + 3]
        value_a = self.read(param_a, mode_a)
        value_b = self.read(param_b, mode_b)
        if value_a < value_b:
            content = 1
        else:
            content = 0
        self.write(content, param_c, mode_c)
        self.instruction_pointer += 4

    def opcode8(self, mode_a=0, mode_b=0, mode_c=0):
        """
        If the first parameter, a, is equal to the second parameter, b,
        store 1 in the position given by the third parameter, c.
        Otherwise, store 0.
        """
        # print(f"running 8 with {[mode_a, mode_b, mode_c]}")
        param_a = self.memory[self.instruction_pointer + 1]
        param_b = self.memory[self.instruction_pointer + 2]
        param_c = self.memory[self.instruction_pointer + 3]
        value_a = self.read(param_a, mode_a)
        value_b = self.read(param_b, mode_b)
        if value_a == value_b:
            content = 1
        else:
            content = 0
        self.write(content, param_c, mode_c)
        self.instruction_pointer += 4

    def opcode9(self, mode_a=0):
        """
        Update the relative base by adding a.
        """
        # print(f"running 9 with {[mode_a]}")
        param_a = self.memory[self.instruction_pointer + 1]
        value_a = self.read(param_a, mode_a)
        self.relative_base += value_a
        self.instruction_pointer += 2

    def opcode99(self):
        """
        Stop running.
        """
        self.running = False