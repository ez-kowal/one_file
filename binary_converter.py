from sys import argv

def to_binary(num: int) -> str:
    '''
    This function converts an int in range of 0-255 to an 8bit binary integer
    '''
    bits = [128,64,32,16,8,4,2,1];
    result = '';
    if (num > sum(bits) or num < 0):
        return "number to high or low"
    else:
        for bit in bits:
            if (num >= bit):
                result += '1';
                num -= bit;
            else: 
                result += '0';
        return result;

def to_decimal(num:str) -> int:
    '''
    This function converts an binary Integer in range of 0-255 to a decimal number
    '''
    bits = [128,64,32,16,8,4,2,1];
    bits_count = 0;
    result = 0;
    for x in num:
        if int(x) == 1:
            result += bits[bits_count];
            bits_count += 1;
        else:
            result += 0;
            bits_count += 1;
    return result;

try:
    if (argv[1] == '-I' or argv[1] == "--Info" or argv[1] == "--help" or argv[1] == "" or argv[1] == None):
        print("INFO\n\nThis is a simple CLI tool to convert Base-10 numer to 8-bit binary and reversed\n\nCommands:\n -D/--Decimal <8-bit binary number>\n -B/--Binary <base-10 number> \n -I/--Info for info page");
    elif (argv[1] == '-B' or argv[1] == "--Binary"):
        print(to_binary(int(argv[2])));
    elif (argv[1] == '-D' or argv[1] == "--Decimal"):
        print(to_decimal(str(argv[2])));
except:
    print("INFO\n\nThis is a simple CLI tool to convert Base-10 numer to 8-bit binary and reversed\n\nCommands:\n -D/--Decimal <8-bit binary number>\n -B/--Binary <base-10 number> \n -I/--Info for info page");