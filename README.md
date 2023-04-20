# MSP430 Instruction Parser
Ever wanted to write test programs for arqui2 quickly and not go through the pain of opening up Microsoft Calculator and writing the bits one by one to craft the instruction? Look no further! The MSP430 Instruction Parser is here to save you from the hassle.

This Python script parses a text file containing a list of MSP430 assembly instructions and generates the corresponding binary and hexadecimal representations.

## How to use
Write your MSP430 assembly instructions in a text file. For example, create a file named inst.txt with the following content:
```
load r1 15
load r2 14
load r3 13
neg r1
in r3
jr30 2
load r0 0
load r0 0
load r0 0
load r0 0
load r0 0
load r0 0
load r0 0
load r0 3
load r0 2
load r0 1
```
Run the Python script (msp430_parser.py) with the text file as input. The script reads the assembly instructions, generates the binary and hexadecimal representations, and saves them in a file named output.txt.

The generated output.txt file will contain the binary and hexadecimal representations of your assembly instructions:
```
inst db 00011111b, 00101110b, 00111101b, 11000001b, 11001111b, 11110010b, 00000000b, 00000000b, 00000000b, 00000000b, 00000000b, 00000000b, 00000000b, 00000011b, 00000010b, 00000001b
inst db 0x1F, 0x2E, 0x3D, 0xC1, 0xCF, 0xF2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x02, 0x01
```
That's it! You can now use the binary and hexadecimal representations in your test programs for arqui2. Just copy whichever form of instructions you want and use it in you program.
