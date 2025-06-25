class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        original_text = str.lower(original_text)
        for letter in original_text:
            if self.alphabet.find(letter) != -1:
                index = (self.alphabet.find(letter)+shift) % 33
                result.append(self.alphabet[index])
            else:
                result.append(letter)
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        cipher_text = str.lower(cipher_text)
        result = []
        for letter in cipher_text:
            if self.alphabet.find(letter) != -1:
                index = (self.alphabet.find(letter)-shift) % 33
                result.append(self.alphabet[index])
            else:
                result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
