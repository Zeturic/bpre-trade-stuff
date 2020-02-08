def decode(bytestring):
    chars = []

    for byte in bytestring:
        if byte in decode.dictionary:
            chars.append(decode.dictionary[byte])
        elif 0xBB <= byte <= 0xD4:
            chars.append(chr(byte - 0xBB + ord("A")))
        elif 0xD5 <= byte <= 0xEE:
            chars.append(chr(byte - 0xD5 + ord("a")))
        elif 0xA1 <= byte <= 0xAA:
            chars.append(chr(byte - 0xA1 + ord("0")))
        elif byte == 0xFF:
            break
        else:
            raise ValueError(f"0x{byte :02X}")

    return "".join(chars)

decode.dictionary = {
    0x00: " ",
    0xAD: ".",
    0xB4: "'"
}
