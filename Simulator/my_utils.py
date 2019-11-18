def extract_binary(num, start, end, unsiged=True):
    count_bit = (end - start) + 1
    i = (1 << count_bit) - 1  # 2^n-1
    i <<= start
    extracted_bit = (num & i) >> start
    if unsiged:
        return extracted_bit
    # check sign bit
    if (1 << (count_bit - 1)) & extracted_bit:
        return extracted_bit - (1 << count_bit)  # กลับบิท + 1

    return extracted_bit


def get_sign_bit(num, count_bit):
    signed_bit = ((1 << (count_bit - 1)) & num) >> (count_bit - 1)
    return signed_bit


def clamp_value(value):
    # clamp value to 32 bit
    maxint32_bit = (1 << 32) - 1
    value = maxint32_bit & value  # (2^32)-1 & value get only 32 bit
    # convert sign bit
    if value & (1 << 31):
        value = value - (1 << 32)
    return value
