def clamp_value(value):
    # clamp value to 32 bit
    maxint32_bit = (1 << 32) - 1
    value = maxint32_bit & value  # (2^32)-1 & value get only 32 bit
    # convert sign bit
    if value & (1 << 31):
        value = value - (1 << 32)
    return value


class RegisterValue:
    def __init__(self):
        self.register = [0, 0, 0, 0, 0, 0, 0, 0]

    def __setitem__(self, index, value):
        if index != 0:
            self.register[index] = clamp_value(value)
        # r0 เป็น 0 เสมอไม่เปลี่ยนค่า

    def __getitem__(self, index):
        return self.register[index]

    def __repr__(self):
        return str(self.register)