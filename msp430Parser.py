binary_map = {
    'load':'00',
    'store':'01',
    'add':'10',
    'neg':'110000',
    'shr':'110001',
    'in':'110011',
    'out':'1110',
    'jr30':'1111',
    'r0':'00',
    'r1':'01',
    'r2':'10',
    'r3':'11',
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    '10':'1010',
    '11':'1011',
    '12':'1100',
    '13':'1101',
    '14':'1110',
    '15':'1111',
    'led':'01',
    'lcd':'10',
}

hex_map={
    '0000':'0',
    '0001':'1',
    '0010':'2',
    '0011':'3',
    '0100':'4',
    '0101':'5',
    '0110':'6',
    '0111':'7',
    '1000':'8',
    '1001':'9',
    '1010':'A',
    '1011':'B',
    '1100':'C',
    '1101':'D',
    '1110':'E',
    '1111':'F',
}
binary_instructions = []
with open('inst.txt', 'r') as file:
    for line in file:
        binary_string = ''
        for x in line.lower().split():
            binary_string+=binary_map[x]
        if binary_string:
            if 'add' in line: binary_instructions.append(binary_string+'00')
            else: binary_instructions.append(binary_string)


hex_instructions = [hex_map[x[:4]] + hex_map[x[4:]] for x in binary_instructions]

p1 = 'RAM db ' + 'b, '.join(binary_instructions)+'b'
p2 = 'RAM db 0x' + ', 0x'.join(hex_instructions)

print(p1)
print(p2)

with open('output.txt', 'w') as file:
    file.write(p1)
    file.write('\n')
    file.write(p2)