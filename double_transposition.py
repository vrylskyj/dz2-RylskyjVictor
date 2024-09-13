def create_grid(text, key):
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    grid = ['' for _ in range(num_cols)]
    
    for i in range(len(text)):
        grid[i % num_cols] += text[i]
        
    return grid, num_rows

def encrypt(text, key):
    grid, num_rows = create_grid(text, key)
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    encrypted_text = ''.join(''.join(grid[i] for i in key_order))
    return encrypted_text

def decrypt(text, key):
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    grid = ['' for _ in range(num_cols)]
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    
    index = 0
    for i in key_order:
        grid[i] = text[index:index + num_rows]
        index += num_rows

    decrypted_text = ''.join(''.join(grid[i][j] if j < len(grid[i]) else '' for i in range(num_cols)) for j in range(num_rows))
    return decrypted_text

def double_transposition_encrypt(text, key1, key2):
    text = ''.join(text.split())
    encrypted_once = encrypt(text, key1)
    return encrypt(encrypted_once, key2)

def double_transposition_decrypt(text, key1, key2):
    decrypted_once = decrypt(text, key2)
    return decrypt(decrypted_once, key1)

# Тестування
text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
key1 = "SECRET"
key2 = "CRYPTO"

ciphertext = double_transposition_encrypt(text, key1, key2)
print("Шифротекст:", ciphertext)

decrypted_text = double_transposition_decrypt(ciphertext, key1, key2)
print("Розшифрований текст:", decrypted_text)
