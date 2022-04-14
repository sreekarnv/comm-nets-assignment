from string import ascii_uppercase

alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

KEY_1 = "KEYABLO"
KEY_2 = "KEYCDPE"


def decrypt(ciphertext: str) -> str:
    digraphs = []

    if len(ciphertext) % 2 != 0:
        raise ValueError("Ciphertext must be an even number of characters")

    for n in range(0, ciphertext.__len__(), 2):
        digraphs.append(ciphertext[n : n + 2])

    table_one = create_playfair_table(KEY_1)
    table_two = create_playfair_table(KEY_2)

    decrypted_message = ""

    for d in digraphs:
        l1, l2 = d

        row_one, col_one = find_row_col(l1, table_one)
        row_two, col_two = find_row_col(l2, table_two)

        # If the letters are in the same row
        if row_one == row_two:
            decrypted_message += table_one[row_one][(col_one - 1) % 5]
            decrypted_message += table_two[row_two][(col_two - 1) % 5]
        else:
            # If the letters are in the same column
            if col_one == col_two:
                decrypted_message += table_one[(row_one - 1) % 5][col_one]
                decrypted_message += table_two[(row_two - 1) % 5][col_two]
            else:
                decrypted_message += table_one[row_one][col_two]
                decrypted_message += table_two[row_two][col_one]

        if decrypted_message[-1] == "Z":
            decrypted_message = decrypted_message[:-1]

    return decrypted_message


def display_disclaimer():
    print("\nTWO SQUARE CHECKERBOARD ENCODING\n")
    print("Please note that white space, numbers and will be ignored ")
    print("and removed during the encryption process and data")
    print("related to these will not be restored")
    print("\n\n")


def create_playfair_table(key: str):
    """
    Create a 5x5 Playfair table from the given key
    but with the letters and replace letter J with I
    """
    # 5 by 5 table
    table = [[None for _ in range(5)] for _ in range(5)]

    alphas = alphabet

    # remove letters from keys in alphas
    for c in key:
        alphas = alphas.replace(c, "")

    # Remove the J from the alphabet
    alphas = alphas.replace("J", "")

    # concat key and alphas
    key_alphas = key + alphas

    # Fill the rest of the table with the alphabet
    for i in range(0, 25):
        table[i // 5][i % 5] = key_alphas[i]

    return table


def find_row_col(letter: str, table):
    """
    Find the row and column of the given letter in the given table.
    """
    for row in range(len(table)):
        for col in range(len(table[row])):
            if table[row][col] == letter:
                return row, col


def encrypt(plaintext: str) -> str:
    filtered_text = ""
    digraphs = []

    # Capitalize all letters in the message
    capitalized_plaintext = plaintext.upper()

    # Remove all non-alphabetic characters
    for c in capitalized_plaintext:
        if c in ascii_uppercase:
            filtered_text += "I" if c == "J" else c

    # If Length of the message is odd, add an "Z" to the end of the message
    if len(filtered_text) % 2 != 0:
        filtered_text += "Z"

    # Split the message into digraphs
    for i in range(0, len(filtered_text), 2):
        digraphs.append(filtered_text[i : i + 2])

    # Create a 5x5 Playfair table from the given key
    table_one = create_playfair_table(KEY_1)
    table_two = create_playfair_table(KEY_2)

    encrypted_message = ""

    # Encrypt the digraphs
    for d in digraphs:
        l1, l2 = d

        # Find the row and column of the first letter
        row_one, col_one = find_row_col(l1, table_one)
        row_two, col_two = find_row_col(l2, table_two)

        # If the letters are in the same row
        if row_one == row_two:
            encrypted_message += table_one[row_one][(col_one + 1) % 5]
            encrypted_message += table_two[row_two][(col_two + 1) % 5]

        # If the letters are in the same column
        if col_one == col_two:
            encrypted_message += table_one[(row_one + 1) % 5][col_one]
            encrypted_message += table_two[(row_two + 1) % 5][col_two]

        # If the letters are in different rows and columns
        if row_one != row_two and col_one != col_two:
            encrypted_message += table_one[row_one][col_two]
            encrypted_message += table_two[row_two][col_one]

    return encrypted_message


def main():

    # display disclaimer
    display_disclaimer()

    # Get user input for the message to be encrypted
    print("Please enter the message without any duplicate characters: ")
    message = input("Enter the message to be encrypted: ")

    # Remove repeated characters
    message = "".join(dict.fromkeys(message))

    # Remove all numeric characters
    message = "".join(filter(lambda x: x.isalpha(), message))

    # Remove all symbols
    message = "".join(filter(lambda x: x.isalnum(), message))

    # Remove whitespaces
    message = "".join(filter(lambda x: x.isspace() is False, message))

    print("Your Original Message: ", message)

    encrypted_message = encrypt(message)

    print("Your Encrypted Message", encrypted_message)

    decrypted_message = decrypt(encrypted_message)

    print("Your Decrypted Message: ", decrypted_message)


if __name__ == "__main__":
    main()
