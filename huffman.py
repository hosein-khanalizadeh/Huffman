#!/usr/bin/python
'''Created by hosein-khanalizadeh'''

import sys


bin_data = '11110001100110110'
str_data = ''

def BinaryToDecimal(binary):
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)

for i in range(0, len(bin_data), 7):
    temp_data = int(bin_data[i:i + 7])
    decimal_data = BinaryToDecimal(temp_data)
    str_data = str_data + chr(decimal_data)

class Tree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffman_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (left, right) = node.children()
    d = {}
    d.update(huffman_tree(left, True, binString + '0'))
    d.update(huffman_tree(right, False, binString + '1'))
    return d

def main():
    freq = {}
    for c in str_data:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    nodes = freq

    while len(nodes) > 1:
        (key1, value1) = nodes[-1]
        (key2, value2) = nodes[-2]
        nodes = nodes[:-2]
        node = Tree(key1, key2)
        nodes.append((node, value1 + value2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmancode = huffman_tree(nodes[0][0])

    print(f'Binary Input : {bin_data}')
    print('================================')
    print(f'Decode Binary Input : {str_data}')
    print('================================')
    print('Char    | Code ')
    print('--------------------------------')
    for (char, frequency) in freq:
        print(f'{ascii(char)}    | {huffmancode[char]}')

    print('================================')

    out = ''
    for s in str_data:
        out += str(huffmancode[s])
    print(f'huffman code : {out}')

if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
