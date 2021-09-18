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


if (argv[1] == '-B' or argv[1] == "--Binary"):
    print(to_binary(int(argv[2])));
if (argv[1] == '-D' or argv[1] == "--Decimal"):
    print(to_decimal(str(argv[2])));
