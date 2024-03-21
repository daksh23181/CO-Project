# convert number into 2's complement
def twos_complement(num, bits):
    max = (1 << (bits - 1)) - 1 
    min = -(1 << (bits - 1))     
    if num < min or num > max:
        return " imm: out of range "
    if num < 0:
        num = (1 << bits) + num

    binary = bin(num & ((1 << bits) - 1))[2:].zfill(bits)
    return binary

# convert decimal number into binary
def Convert_Binary(num, bits):
    binary_num = ""
    while num > 0:
        binary_num = str(num % 2) + binary_num
        num //= 2
    
    res = binary_num.zfill(bits)
    return res[-bits:]

# returns address of a register
def register_encode(register):
    if (register =='zero'):
        return(Convert_Binary(0,5))
    if (register =='ra'):
        return(Convert_Binary(1,5))
    if (register =='sp'):
        return(Convert_Binary(2,5))
    if (register =='gp'):
        return(Convert_Binary(3,5))
    if (register =='tp'):
        return(Convert_Binary(4,5))
    if (register =='t0'):
        return(Convert_Binary(5,5))
    if (register =='t1'):
        return(Convert_Binary(6,5))
    if (register =='t2'):
        return(Convert_Binary(7,5))
    if (register =='s0' or register == 'fp'):
        return(Convert_Binary(8,5))
    if (register =='s1'):
        return(Convert_Binary(9,5))
    if (register =='a0'):
        return(Convert_Binary(10,5))
    if (register =='a1'):
        return(Convert_Binary(11,5))
    if (register =='a2'):
        return(Convert_Binary(12,5))
    if (register =='a3'):
        return(Convert_Binary(13,5))
    if (register =='a4'):
        return(Convert_Binary(14,5))
    if (register =='a5'):
        return(Convert_Binary(15,5))
    if (register =='a6'):
        return(Convert_Binary(16,5))
    if (register =='a7'):
        return(Convert_Binary(17,5))
    if (register =='s2'):
        return(Convert_Binary(18,5))
    if (register =='s3'):
        return(Convert_Binary(19,5))
    if (register =='s4'):
        return(Convert_Binary(20,5))
    if (register =='s5'):
        return(Convert_Binary(21,5))
    if (register =='s6'):
        return(Convert_Binary(22,5))
    if (register =='s7'):
        return(Convert_Binary(23,5))
    if (register =='s8'):
        return(Convert_Binary(24,5))
    if (register =='s9'):
        return(Convert_Binary(25,5))
    if (register =='s10'):
        return(Convert_Binary(26,5))
    if (register =='s11'):
        return(Convert_Binary(27,5))
    if (register =='t3'):
        return(Convert_Binary(28,5))
    if (register =='t4'):
        return(Convert_Binary(29,5))
    if (register =='t5'):
        return(Convert_Binary(30,5))
    if (register =='t6'):
        return(Convert_Binary(31,5))
    else:
        s=" Invalid register "
        return s


def r_instruction(data):
    opcode = '0110011'
    rd = register_encode(data[1])
    rs1 = register_encode(data[2])
    rs2 = register_encode(data[3])
    inst = data[0]

    if inst == 'add':
        f3 = '000'
        f7 = '0000000'
    elif inst == 'sub':
        f3 = '000'
        f7 = '0100000'
    elif inst == 'sll':
        f3 = '001'
        f7 = '0000000'
    elif inst == 'slt':
        f3 = '010'
        f7 = '0000000'
    elif inst == 'sltu':
        f3 = '011'
        f7 = '0000000'
    elif inst == 'xor':
        f3 = '100'
        f7 = '0000000'
    elif inst == 'srl':
        f3 = '101'
        f7 = '0000000'
    elif inst == 'or':
        f3 = '110'
        f7 = '0000000'
    elif inst == 'and':
        f3 = '111'
        f7 = '0000000'

    result = f7 + rs2 + rs1 + f3 + rd + opcode
    return result


def i_instruction(data):
    inst=data[0]
    rd=register_encode(data[1])

    if inst=='lw':
        opcode='0000011'
        imm=twos_complement(int(data[2]),12)
        rs1=register_encode(data[3])
        f3='010'
    else:
        rs1=register_encode(data[2])
        imm=twos_complement(int(data[3]),12)
        if inst=='addi':
            opcode='0010011'
            f3='000'
        elif inst=='sltiu':
            opcode='0010011'
            f3='011'
        elif inst=='jalr':
            opcode='1100111'
            f3='000'

    result = imm + rs1 + f3 + rd + opcode
    return result


def s_instruction(data):
    opcode='0100011'
    rs1=register_encode(data[3])
    rs2=register_encode(data[1])
    imm=twos_complement(int(data[2]),12)
    imm_1=imm[0:7]
    imm_2=imm[7:12]
    f3='010'

    result = imm_1 + rs2 + rs1 + f3 + imm_2 + opcode
    return result


def b_instruction(data):
    opcode='1100011'
    rs1=register_encode(data[1])
    rs2=register_encode(data[2])
    inst=data[0]
    imm=twos_complement(int(data[3]),32)
    imm1 = imm[-13] + imm[-11:-5]
    imm2= imm[-5:-1] + imm[-12]

    if inst=='beq':
        f3='000'
    elif inst=='bne':
        f3='001'
    elif inst=='blt':
        f3='100'
    elif inst=='bge':
        f3='101'
    elif inst=='bltu':
        f3='110'
    elif inst=='bgeu':
        f3='111'

    result = imm1 + rs2 + rs1 + f3 + imm2 + opcode
    return result


def u_instruction(data):
    rd=register_encode(data[1])
    inst=data[0]
    temp=twos_complement(int(data[2]),32)
    imm=temp[-31:-11]

    if inst=='lui':
        opcode='0110111'
    elif inst=='auipc':
        opcode='0010111'

    result = imm + rd + opcode
    return result


def j_instruction(data):
    opcode='1101111'
    rd=register_encode(data[1])
    imm=twos_complement(int(data[2]),32)
    imm1= imm[-21] + imm[-11:-1] + imm[-12] + imm[-20:-12]

    result = imm1 + rd + opcode
    return result


r_type = ['add','sub','sll','slt','sltu','xor','srl','or','and']
i_type = ['lw','addi','sltiu','jalr']
s_type = ['sw']
b_type = ['beq','bne','blt','bge','bltu','bgeu']
u_type = ['lui','auipc']
j_type = ['jal']


def parse_label(instruction, label_dict, current):
    if ':' in instruction:
        label, _ = instruction.split(':')
        label_dict[label.strip()] = current
        return label.strip()
    return None

def resolve_labels(instruction, label_dict):
    resolved = []
    for part in instruction:
        if part.isdigit() or part.startswith('-'):
            resolved.append(part)
        elif part in label_dict:
            resolved.append(str(label_dict[part]))
        else:
            resolved.append(part)
    return resolved

label_dict = {}
address = 0

# to parse labels and store their addresses
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            label = parse_label(line, label_dict, address)
            if label:
                line = line.replace(label + ':', '') 
            if not parse_label(line, label_dict, address):
                address += 1

output_code = []

# process instructions
import re
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            instruction = re.split(r'[\s,()]', line)
            instruction = [part.strip() for part in instruction if part.strip()]
            instruction = resolve_labels(instruction, label_dict)

            for i in instruction:
                if ':' in i:
                    instruction.pop(0)

            if instruction[0] in r_type:
                res = r_instruction(instruction)
                output_code.append(res)
            elif instruction[0] in i_type:
                res = i_instruction(instruction)
                output_code.append(res)
            elif instruction[0] in s_type:
                res = s_instruction(instruction)
                output_code.append(res)
            elif instruction[0] in b_type:
                res = b_instruction(instruction)
                output_code.append(res)
            elif instruction[0] in u_type:
                res = u_instruction(instruction)
                output_code.append(res)
            elif instruction[0] in j_type:
                res = j_instruction(instruction)
                output_code.append(res)
            else:
                s = "Invalid instruction"
                output_code.append(s)

with open("output.txt", 'w') as f:
    for k in output_code:
        f.write(k + '\n')
