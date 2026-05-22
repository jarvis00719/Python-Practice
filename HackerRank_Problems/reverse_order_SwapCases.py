def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(" ")
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence.swapcase()


s = input()
print(reverse_words_order_and_swap_cases(s))
bjdvM4UkP:_7MqE