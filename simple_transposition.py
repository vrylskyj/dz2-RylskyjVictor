def generate_permutation_key(keyword):
    """Генерує унікальний ключ з ключового слова."""
    key = ''.join(sorted(set(keyword), key=keyword.index))
    return key

def encrypt_permutation(text, keyword):
    """Шифрує текст за допомогою шифру перестановки."""
    key = generate_permutation_key(keyword)
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    grid = [''] * num_cols

    # Заповнюємо сітку текстом
    for i in range(len(text)):
        grid[i % num_cols] += text[i]

    # Сортуємо ключ для визначення порядку стовпців
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    encrypted_text = ''.join(''.join(grid[i] for i, _ in sorted_key))
    
    return encrypted_text

def decrypt_permutation(text, keyword):
    """Дешифрує текст за допомогою шифру перестановки."""
    key = generate_permutation_key(keyword)
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    grid = [''] * num_cols
    index = 0

    # Заповнюємо стовпці сітки
    for i, _ in sorted_key:
        grid[i] = text[index:index + num_rows]
        index += num_rows

    # Збираємо рядки, щоб відновити текст
    decrypted_text = ''.join(''.join(grid[i][j] if j < len(grid[i]) else '' for i in range(num_cols)) for j in range(num_rows))
    
    return decrypted_text.strip()

# Приклад використання
text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
keyword = "SECRET"

ciphertext = encrypt_permutation(text, keyword)
print("Шифротекст:", ciphertext)

decrypted_text = decrypt_permutation(ciphertext, keyword)
print("Розшифрований текст:", decrypted_text)
