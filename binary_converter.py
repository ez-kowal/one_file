from sys import argv

def to_binary(num:int) -> int:
    '''
    Converts an Int type base-10 number to base-2(8-bits)
    '''
    bits = [128,64,32,16,8,4,2,1];
    result = '';
    if (num > sum(bits) or num < 0):
        return "only acceptes values between 0-255"
    else:
        for bit in bits:
            if (num >= bit):
                result += '1';
                num -= bit;
            else: 
                result += '0';
        return int(result);

def to_decimal(num:int) -> int:
    '''
    Converts an Int type base-2 number to base-10
    '''

    bits = [128,64,32,16,8,4,2,1];
    bits_count = 0;
    result = 0;
    for x in str(num):
        if int(x) == 1:
            result += bits[bits_count];
            bits_count += 1;
        else:
            result += 0;
            bits_count += 1;
    return int(result);

def to_octal(num:int) -> int:
    '''
    Converts an Int type base-10 number to base-8
    '''
    result = '';
    while num != 0:
        result += str(num%8);
        num = int(num/8);
    return int(result[::-1]);