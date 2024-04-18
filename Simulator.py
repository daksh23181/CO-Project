# RISC-V Simulator

PC = 0
m = "0b00000000000000000000000000000000"

register_decode = {
    "00000":"zero", "00001":"ra", "00010":"sp", "00011":"gp", "00100":"tp","00101":"t0", 
    "00110":"t1", "00111":"t2", "01000":"s0", "01000":"fp", "01001":"s1", "01010":"a0", 
    "01011":"a1", "01100":"a2", "01101":"a3", "01110":"a4", "01111":"a5", "10000":"a6", 
    "10001":"a7", "10010":"s2", "10011": "s3", "10100":"s4", "10101":"s5", "10110":"s6", 
    "10111":"s7", "11000":"s8", "11001":"s9", "11010":"s10", "11011":"s11", "11100":"t3", 
    "11101":"t4", "11110":"t5", "11111":"t6"
}

register_value = {
    "zero": "0b00000000000000000000000000000000", "ra": "0b00000000000000000000000000000000",
    "sp": "0b00000000000000000000000000000000", "gp": "0b00000000000000000000000000000000",
    "tp": "0b00000000000000000000000000000000", "t0": "0b00000000000000000000000000000000",
    "t1": "0b00000000000000000000000000000000", "t2": "0b00000000000000000000000000000000",
    "fp": "0b00000000000000000000000000000000", "s0": "0b00000000000000000000000000000000",
    "s1": "0b00000000000000000000000000000000", "a0": "0b00000000000000000000000000000000",
    "a1": "0b00000000000000000000000000000000", "a2": "0b00000000000000000000000000000000",
    "a3": "0b00000000000000000000000000000000", "a4": "0b00000000000000000000000000000000",
    "a5": "0b00000000000000000000000000000000", "a6": "0b00000000000000000000000000000000",
    "a7": "0b00000000000000000000000000000000", "s2": "0b00000000000000000000000000000000",
    "s3": "0b00000000000000000000000000000000", "s4": "0b00000000000000000000000000000000",
    "s5": "0b00000000000000000000000000000000", "s6": "0b00000000000000000000000000000000",
    "s7": "0b00000000000000000000000000000000", "s8": "0b00000000000000000000000000000000",
    "s9": "0b00000000000000000000000000000000", "s10": "0b00000000000000000000000000000000",
    "s11": "0b00000000000000000000000000000000", "t3": "0b00000000000000000000000000000000",
    "t4": "0b00000000000000000000000000000000", "t5": "0b00000000000000000000000000000000",
    "t6": "0b00000000000000000000000000000000"
}

memory = {
    "00000000000000010000000000000000":"00000000000000000000000000000000",
    "00000000000000010000000000000100":"00000000000000000000000000000000",
    "00000000000000010000000000001000":"00000000000000000000000000000000",
    "00000000000000010000000000001100":"00000000000000000000000000000000",
    "00000000000000010000000000010000":"00000000000000000000000000000000",
    "00000000000000010000000000010100":"00000000000000000000000000000000",
    "00000000000000010000000000011000":"00000000000000000000000000000000",
    "00000000000000010000000000011100":"00000000000000000000000000000000",
    "00000000000000010000000000100000":"00000000000000000000000000000000",
    "00000000000000010000000000100100":"00000000000000000000000000000000",
    "00000000000000010000000000101000":"00000000000000000000000000000000",
    "00000000000000010000000000101100":"00000000000000000000000000000000",
    "00000000000000010000000000110000":"00000000000000000000000000000000",
    "00000000000000010000000000110100":"00000000000000000000000000000000",
    "00000000000000010000000000111000":"00000000000000000000000000000000",
    "00000000000000010000000000111100":"00000000000000000000000000000000",
    "00000000000000010000000001000000":"00000000000000000000000000000000",
    "00000000000000010000000001000100":"00000000000000000000000000000000",
    "00000000000000010000000001001000":"00000000000000000000000000000000",
    "00000000000000010000000001001100":"00000000000000000000000000000000",
    "00000000000000010000000001010000":"00000000000000000000000000000000",
    "00000000000000010000000001010100":"00000000000000000000000000000000",
    "00000000000000010000000001011000":"00000000000000000000000000000000",
    "00000000000000010000000001011100":"00000000000000000000000000000000",
    "00000000000000010000000001100000":"00000000000000000000000000000000",
    "00000000000000010000000001100100":"00000000000000000000000000000000",
    "00000000000000010000000001101000":"00000000000000000000000000000000",
    "00000000000000010000000001101100":"00000000000000000000000000000000",
    "00000000000000010000000001110000":"00000000000000000000000000000000",
    "00000000000000010000000001110100":"00000000000000000000000000000000",
    "00000000000000010000000001111000":"00000000000000000000000000000000",
    "00000000000000010000000001111100":"00000000000000000000000000000000"
}

memory_list=[
    "00000000000000010000000000000000", "00000000000000010000000000000100", "00000000000000010000000000001000", 
    "00000000000000010000000000001100", "00000000000000010000000000010000", "00000000000000010000000000010100",
    "00000000000000010000000000011000", "00000000000000010000000000011100", "00000000000000010000000000100000", 
    "00000000000000010000000000100100", "00000000000000010000000000101000", "00000000000000010000000000101100",
    "00000000000000010000000000110000", "00000000000000010000000000110100", "00000000000000010000000000111000", 
    "00000000000000010000000000111100", "00000000000000010000000001000000", "00000000000000010000000001000100",
    "00000000000000010000000001001000", "00000000000000010000000001001100", "00000000000000010000000001010000", 
    "00000000000000010000000001010100", "00000000000000010000000001011000", "00000000000000010000000001011100",
    "00000000000000010000000001100000", "00000000000000010000000001100100", "00000000000000010000000001101000", 
    "00000000000000010000000001101100", "00000000000000010000000001110000", "00000000000000010000000001110100",
    "00000000000000010000000001111000", "00000000000000010000000001111100"
]

# update the program counter
def UpdatePC():
    global PC,m
    PC += 4

# convert binary number to hexadecimal
def Convert_hex(binary):
    decimal = int(binary, 2)
    hex_num = hex(decimal)
    return  hex_num

# convert decimal number to binary
def Convert_Binary32(num, bits=32):
    binary_num = ""
    while num > 0:
        binary_num = str(num % 2) + binary_num
        num //= 2
    
    res = binary_num.zfill(bits)
    return res[-bits:]

# convert unsigned binary to decimal
def Convert_Unsigned(binary):
    decimal = int(binary, 2)
    return decimal

# convert signed binary to decimal
def Convert_Signed(binary):
    msb = binary[0]
    magnitude = binary[1:]
    decimal = int(magnitude, 2)
    if (msb=='1'):
        return -decimal
    else:
        return decimal

# convert 2's complement to decimal
def Convert_2scomplement(binary):
    if binary[0] == '1':
        binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        binary = bin(int(binary, 2) + 1)[2:]

        decimal = -int(binary, 2)
    else:
        decimal = int(binary, 2)

    return decimal


# executing all the types of instructions

def execute_R_type(instruction):
    rd = instruction[-12:-7]
    rs1 = instruction[12:17]
    rs2 = instruction[7:12]
    f3 = instruction[17:20]
    f7 = instruction[0:7]
    value1 = register_value[register_decode[rs1]]
    value2 = register_value[register_decode[rs2]]

    if (f7 == '0000000') and (f3 == '000'):
        # add
        UpdatePC()
        res = Convert_Signed(value1[2:]) + Convert_Signed(value2[2:])
        register_value[register_decode[rd]] = '0b' + Convert_Binary32(res)
    
    elif (f7 == '0100000') and (f3 == '000'):
        # sub
        UpdatePC()
        res = Convert_Signed(value1[2:]) - Convert_Signed(value2[2:])
        register_value[register_decode[rd]] = '0b' + Convert_Binary32(res)
  
    elif (f7 == '0000000') and (f3 == '001'):
        # sll
        UpdatePC()
        imm = Convert_Unsigned(value2[-5:])
        res = value1[imm:] + imm*'0'
        register_value[register_decode[rd]] = res
                
    elif (f7 == '0000000') and (f3 == '010'):
        # slt
        UpdatePC()
        i = Convert_Signed(value1[2:])
        j = Convert_Signed(value2[2:])
        if j > i:
            register_value[register_decode[rd]] = '0b00000000000000000000000000000001'
        
    elif (f7 == '0000000') and (f3 == '011') :
        # sltu
        UpdatePC()
        i = Convert_Unsigned(value1[2:])
        j = Convert_Unsigned(value2[2:])
        if j > i:
            register_value[register_decode[rd]] = '0b00000000000000000000000000000001'
        
    elif (f7 == '0000000') and (f3 == '100'):
        # xor
        UpdatePC()
        i = Convert_Signed(value1[2:])
        j = Convert_Signed(value2[2:])
        res = i ^ j
        register_value[register_decode[rd]] = '0b' + Convert_Binary32(res)        
        
    elif (f7 == '0000000') and (f3 == '101') :
        # srl
        UpdatePC()
        a = Convert_Unsigned(value2[-5:])
        if value1[a] == '1':
            x = a*'1' + value1[a:-a +1]
            register_value[register_decode[rd]] = x
        elif value1[a] == '0':
            x = a*'0' + value1[a:-a+1]
            register_value[register_decode[rd]] = x

    elif (f7 == '0000000') and (f3 == '110'):
        # or
        UpdatePC()
        i = Convert_Signed(value1[2:])
        j = Convert_Signed(value2[2:])
        res = i | j
        register_value[register_decode[rd]] = '0b' + Convert_Binary32(res)  

    elif (f7 == '0000000') and (f3 == '111'):
        # and
        UpdatePC()
        i = Convert_Signed(value1[2:])
        j = Convert_Signed(value2[2:])
        res = i & j
        register_value[register_decode[rd]] = '0b' + Convert_Binary32(res)  
            

def execute_I_type(instruction, opcode):
    global PC
    imm = instruction[0:12]
    rs1 = instruction[12:17]
    rd = instruction[-12:-7]
    f3 = instruction[17:20]

    if (f3=='010') and (opcode=='0000011'):
        # lw
        UpdatePC()
        x = Convert_2scomplement(imm)
        y = Convert_2scomplement(register_value[register_decode[rs1]])
        res = Convert_Binary32(x + y)
        register_value[register_decode[rd]] = memory[res]

    elif (f3=='000') and (opcode=='0010011'):
        # addi
        UpdatePC()
        x = Convert_2scomplement(imm)
        y = Convert_2scomplement(register_value[register_decode[rs1]])
        res = Convert_Binary32(x + y)
        register_value[register_decode[rd]] = res

    elif (f3=='011') and (opcode=='0010011'):
        # sltiu
        UpdatePC()
        l = Convert_Unsigned(imm)
        m = Convert_Unsigned(register_value[register_decode[rs1]])
        if l > m:
            register_value[register_decode[rd]] = '0b00000000000000000000000000000001'

    elif (f3=='000') and (opcode=='1100111'):
        # jalr
        x = Convert_2scomplement(imm)
        y = Convert_2scomplement(register_value[register_decode[rs1]])
        register_value[register_decode[rd]] = Convert_Binary32(PC+4)
        PC = x + y
        r = Convert_Binary32(PC)
        PC = Convert_2scomplement(r[:-1]+'0')


def execute_S_type(instruction):
    # sw
    UpdatePC()
    imm1 = instruction[:7]
    rs2 = instruction[7:12]
    rs1 = instruction[12:17]
    imm2 = instruction[20:25]
    imm = imm1 + imm2
    i = Convert_2scomplement(register_value[register_decode[rs1]]) 
    j = Convert_2scomplement(imm)
    x = i+j
    b = Convert_Binary32(x)
    memory[b] = register_value[register_decode[rs2]]


def execute_B_type(instruction):
    global PC
    imm = instruction[0] + instruction[24] + instruction[1:7] + instruction[20:24] + '0'
    rs2 = instruction[7:12]
    rs1 = instruction[12:17]
    f3 = instruction[17:20]
    a = register_value[register_decode[rs1]]
    b = register_value[register_decode[rs2]]

    if f3=='000':
        # beq
        c = Convert_2scomplement(imm)
        x = Convert_2scomplement(a)
        y = Convert_2scomplement(b)
        if x == y:
            PC = PC + c

    elif f3=='001':
        # bne
        c = Convert_2scomplement(imm)
        x = Convert_2scomplement(a)
        y = Convert_2scomplement(b)
        if x != y:
            PC = PC + c

    elif f3=='100':
        # blt
        c = Convert_2scomplement(imm)
        x = Convert_2scomplement(a)
        y = Convert_2scomplement(b)
        if x < y:
            PC = PC + c
    
    elif f3=='101':
        # bge
        c = Convert_2scomplement(imm)
        x = Convert_2scomplement(a)
        y = Convert_2scomplement(b)
        if x >= y:
            PC = PC + c
    
    elif f3=='110':
        # bltu
        c = Convert_2scomplement(imm)
        x = Convert_Unsigned(a)
        y = Convert_Unsigned(b)
        if x < y:
            PC = PC + c

    elif f3=='111':
        # bgeu
        c = Convert_Signed(imm)
        x = Convert_Unsigned(a)
        y = Convert_Unsigned(b)
        if x == y:
            PC = PC + c


def execute_U_type(instruction, opcode):
    global PC
    imm = instruction[:20] + '000000000000'
    rd = instruction[20:25]

    if opcode=='0110111':
        # lui
        UpdatePC()
        res = Convert_2scomplement(imm)
        register_value[register_decode[rd]] = Convert_Binary32(res)

    elif opcode=='0010111':
        # auipc
        UpdatePC()
        res = PC + Convert_2scomplement(imm)
        register_value[register_decode[rd]] = Convert_Binary32(res)


def execute_J_type(instruction):
    # jal
    global PC

    i = instruction[:20]
    imm = i[0] + i[10:20] + i[9] + i[1:9] + '0'
    x = Convert_2scomplement(imm)
    rd = instruction[20:25]
    register_value[register_decode[rd]] = Convert_Binary32(PC + 4)
    PC = PC + x
    v = Convert_Binary32(PC)
    PC = Convert_2scomplement(v[:-1]+'0')


# list of opcode for different instructions
r_opcode=["0110011"]
i_opcode=["0000011","0010011","1100111"]
s_opcode=["0100011"]
b_opcode=["1100011"]
u_opcode=["0110111","0010111"]
j_opcode=["1101111"]


# automated testing for input and output
import sys

# list of register adddress
R = [
    "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111",
    "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
    "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111",
    "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"
]

instruction_list = []

def filework(name):
    f = open(name,'r')
    data = f.readlines()
    m = ''
    for i in range(len(data)):
        k = data[i]
        if i == len(data)-1:
            m = k
        else:
            m = k[:-1]
        
        instruction_list.append(m)

def generate_file(list,filedir=""):
    h=''
    t = ''
    if filedir == "" or filedir == sys.argv[-2]:
        t = sys.argv[-1]
    f = open(f"{t}",'a')
    for i in range(len(list)):
        a = list[i]
        b = ''
        for i in range(len(a)):
            b += a[i] + ' '

        print(b)
        f.write(b)
        f.write("\n")

    for i in range(len(memory_list)):
        h = Convert_hex(memory_list[i]) + ':' + memory[memory_list[i]]
        print(h)
        f.write(h)
        f.write("\n")
    f.close()

def execute_registers(R):
    global PC
    register_output = []
    s = '0b' + Convert_Binary32(PC)
    register_output.append(s)
    for i in range(len(R)):
        if i == len(R)-1:
            register_output.append(register_value[register_decode[R[i]]])
        else:
            register_output.append(register_value[register_decode[R[i]]])

    return register_output

output = []

def execution(list):
    for i in list:
        if i[-7:] in r_opcode:
            execute_R_type(i)
            output.append(execute_registers(R))
        
        elif i[-7:] in i_opcode:
            execute_I_type(i, i[-7:])
            output.append(execute_registers(R))
        
        elif i[-7:] in s_opcode:
            execute_S_type(i)
            output.append(execute_registers(R))
        
        elif i[-7:] in b_opcode:
            execute_B_type(i)
            output.append(execute_registers(R))
        
        elif i[-7:] in u_opcode:
            execute_U_type(i, i[-7:])
            output.append(execute_registers(R))
        
        elif i[-7:] in j_opcode:
            execute_J_type(i)
            output.append(execute_registers(R))

def write_file(filename = ""):
    if filename == "":
        filename = sys.argv[-2]
    
    filework(filename)
    execution(instruction_list)
    generate_file(output,filename)

write_file()
