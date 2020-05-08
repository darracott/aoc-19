#! /usr/bin/python3


from common.classes import IntCodeComputer
from itertools import permutations


AMPLIFIER_INTCODE = [3,8,1001,8,10,8,105,1,0,0,21,38,63,72,81,106,187,268,349,430,99999,3,9,101,5,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,102,3,9,9,101,4,9,9,1002,9,2,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]


def day7_part1(intcode=None):
    """
    Queue inputs and pass along outputs.
    """
    if not intcode:
        intcode = AMPLIFIER_INTCODE

    # Make a generator for phase setting seqs
    phase_setting_sequences = permutations(range(0,5))

    thruster_signals = []

    for phase_setting_sequence in phase_setting_sequences:
        amplifiers = [IntCodeComputer(intcode) for x in range(5)]
        input_signal = 0
        for amplifier, phase_setting in zip(amplifiers, phase_setting_sequence):
            amplifier.queue_input(phase_setting)
            amplifier.queue_input(input_signal)
            amplifier.run()
            assert len(amplifier.outputs) == 1
            input_signal = amplifier.outputs[0]
        thruster_signals.append(input_signal)

    return max(thruster_signals)

def day7_part2(intcode=None):
    """
    Amplifier feedback loop.
    All Amplifers first input is their phase setting.
    The first Amplifer then gets a one off input of 0.
    Outputs from each Amplifer are the inputs to the next Amplifer.
    Amplifers will need to pause running to wait for input until
    the previous Amplifer can supply that input.
    Eventually all Amplifers stop running.

    Start with a fixed intcode. Try all phase settings.
    Find the biggest thruster signal possible.
    """
    if not intcode:
        intcode = AMPLIFIER_INTCODE

    # Make a generator for all possible phase setting sequences.
    phase_setting_sequences = permutations(range(5,10))

    thruster_signals = []
    for phase_setting_sequence in phase_setting_sequences:
        # Set up fresh Amplifiers.
        amplifiers = [IntCodeComputer(intcode) for _ in range(5)]

        # Queue phase setting inputs for each Amplifier.
        for amp, phase in zip(amplifiers, phase_setting_sequence):
            amp.queue_input(phase)
            amp.running = True

        # Queue one off 0 input to the first Amplifier.
        amplifiers[0].queue_input(0)

        # Now start the Amplifiers running.
        amp_id = 0
        while any([amp.running for amp in amplifiers]):
            # Use mod to cycle through running the Amplifiers.
            amp = amplifiers[amp_id % 5]
            amp.run()

            # Check if we got any outputs from this run.
            # If so, queue them as inputs to the next amplifier.
            next_amp = amplifiers[(amp_id + 1) % 5]
            while amp.outputs:
                _input = amp.outputs.pop(0)
                next_amp.queue_input(_input)

            # Move to the next Amplifier.
            amp_id += 1

        # Exited while loop, save the last output, called _input.
        thruster_signals.append(_input)

    return max(thruster_signals)

if __name__ == "__main__":
    print(f"Day 7, Part 1: Max thruster signal is: {day7_part1()}")
    print(f"Day 7, Part 2: Max thruster signal is: {day7_part2()}")