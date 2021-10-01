def to_base2(num:int) -> int:
    '''
    Converts an Int type base-10 
    number to base-2(8-bits)
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

def to_base10(num,base:int = 2) -> int:
    '''
    Converts an Int type of user specified 
    base(deafult base-2) number to base-10
    '''
    if base == 2:
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
    
    if base == 16 or base == 8:
        base16 = ['0','1','2','3','4','5','6','7','8','9',"A","B","C","D","E","F"];
        num = str(num)[::-1].upper();
        result = 0;
        for x, y in enumerate(num):
            result += int(base16.index(y))*(base**int(x));
        return int(result);

def to_base8(num:int) -> int:
    '''
    Converts an Int type base-10 
    number to base-8
    '''
    result = '';
    while num != 0:
        result += str(num%8);
        num = int(num/8);
    return int(result[::-1]);

def to_base16(num:int) -> str:
    '''
    Converts an Int type base-10 
    number to base-16
    '''
    base16 = ['0','1','2','3','4','5','6','7','8','9',"A","B","C","D","E","F"];
    result = '';
    while num != 0:
        result += base16[int(num%16)];
        num = int(num/16);
    return result[::-1];
