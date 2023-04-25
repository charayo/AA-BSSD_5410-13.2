import math


# Homework Q1 Card Deck


def card_type(n):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
    suits = ['C', 'D', 'H', 'S']
    rank = cards[n]
    suit = suits[math.floor(n / 13)]
    # print(4 % 13)
    return rank + suit


# Homework Q2
# Given an unsigned integer, swap all odd bits with even bits. For example, if the given number is 23 (
# 00010111), it should be converted to 43 (00101011). Every even position bit is swapped with adjacent bit on right
# side (even position bits are highlighted in binary representation of 23), and every odd position bit is swapped
# with adjacent on left side.
def swap_odd_bits(n):
    # Even bits of n
    even_bits = n & 0b10101010

    # Odd bits of n
    odd_bits = n & 0b01010101

    # Right shift even bits
    even_bits >>= 1

    # Left shift odd bits
    odd_bits <<= 1

    # Combining both bits
    # print(even_bits, odd_bits)
    result = even_bits + odd_bits

    return result


if __name__ == "__main__":
    # Q1. For n = 0, the output should be "2C"
    card = card_type(0)
    print(card)

    #  Q2. For example, if the given number is 23 (00010111), it should be converted to 43 (00101011)
    ans = swap_odd_bits(23)
    print(ans)
