from sys import getsizeof

def _compress(data):
    bit_string =1
    for d in data.upper():
        bit_string <<= 2
        # print(bin(bit_string))
        if d == "A":
            bit_string |= 0b00 # 0b100 | 0b00 = 0b100
        elif d == "C":
            bit_string |= 0b01 # 0b100 | 0b01 = 0b101
        elif d == "G":
            bit_string |= 0b10 # 0b100 | 0b11 = 0b110
        elif d == "T":
            bit_string |= 0b11 # 0b100 | 0b11 = 0b111

        # print(bin(bit_string))
        # break
        # print(d,bin(d))
    return bit_string

def decompress(compress_data):
    gene = ""
    # print(bin(compress_data))
    # print(compress_data.bit_length())
    for i in range(0,compress_data.bit_length()-1,2):
        # print`(i)
        bits = compress_data >> i & 0b11
        # print(bin(bits))
        if bits == 0b00:
            gene += 'A'
        elif bits == 0b01:
            gene += "C"
        elif bits == 0b10:
            gene += "G"
        elif bits == 0b11:
            gene += "T"
    # print(gene[::-1])
    return gene[::-1]

a = "ACGT" # ACGT
compress_data = _compress(data=a)
d = decompress(compress_data)

print("original data ",getsizeof(a),"bytes")
print("compress data",getsizeof(compress_data),"bytes")
print("decompress data",getsizeof(d),"bytes")