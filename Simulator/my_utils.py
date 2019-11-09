def extract_binary(num, start, end, unsiged=True):
    count_bit = (end - start) + 1
    i = (1 << count_bit) - 1  # 2^n-1
    i <<= start
    extracted_bit = (num & i) >> start
    if unsiged:
        return extracted_bit

    signed_bit = ((1 << (count_bit - 1)) & extracted_bit) >> (count_bit - 1)
    if not signed_bit:
        return extracted_bit

    return extracted_bit - (1 << count_bit)  # กลับบิท + 1
