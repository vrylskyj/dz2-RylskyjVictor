def vigenere_encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    text = text.upper().replace(' ', '')
    encrypted_text = ''
    key_len = len(key)
    
    for i, char in enumerate(text):
        if char in alphabet:
            key_char = key[i % key_len]
            encrypted_char = alphabet[(alphabet.index(char) + alphabet.index(key_char)) % 26]
            encrypted_text += encrypted_char
    
    return encrypted_text

def create_table(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []
    used_chars = set()
    
    for char in key.upper():
        if char not in used_chars:
            used_chars.add(char)
            table.append(char)
    
    for char in alphabet:
        if char not in used_chars:
            table.append(char)
    
    return table

def table_cipher_encrypt(text, key):
    table = create_table(key)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper().replace(' ', '')
    encrypted_text = ''
    
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += table[index]
    
    return encrypted_text

def double_encrypt(text, key1, key2):
    vigenere_encrypted = vigenere_encrypt(text, key1)
    table_encrypted = table_cipher_encrypt(vigenere_encrypted, key2)
    return table_encrypted

# Тестування
text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
key1 = "MATRIX"
key2 = "CRYPTO"

# Спочатку шифрування Віженера
vigenere_encrypted_text = vigenere_encrypt(text, key1)
print("Шифротекст після Віженера:", vigenere_encrypted_text)

# Потім табличний шифр
final_encrypted_text = table_cipher_encrypt(vigenere_encrypted_text, key2)
print("Остаточний шифротекст:", final_encrypted_text)
