# Angold4 20200712
class CaesarCipher:
    """class for doing encryption and decryption using a Caesar cipher"""

    def __init__(self, shift):
        """
        construct caesar cipher using given integer shift for rotation
        ensure that every obj has it own decode list
        """
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            """
            chr() method decode a numer to a ASCII str
            ord() method is opposite to chr()
            """
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def _transform(self, original, code):
        """
        utinity to perform transformation based on given code string
        main func
        """
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

    def encrypt(self, message):
        """
        return string representing encrypted message
        message -> CaesarCipher
        """

        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """
        Return decrypted message given encrypted secret
        message <- CaesarCipher
        """
        return self._transform(secret, self._backward)


if __name__ == "__main__":
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print("Secret:", coded)  # Secret: WKH HDJOH LV LQ SODB; PHHW DW MRH'V.
    answer = cipher.decrypt(coded)
    print("Message:", answer)  # Secret: WKH HDJOH LV LQ SODB; PHHW DW MRH'V.
