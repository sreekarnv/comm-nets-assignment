# Double Square Cipher

During the encryption process, all white space, punctuation, special characters, and numerals will be erased from the plaintext.

Non-letter characters will be disregarded and deleted from the message. The whitespace numbers and punctuation will not be restored when the ciphertext is subsequently decoded.

Another thing to remember is that this cypher replaces all 'J' letter characters with a 'I' character. This is done to fit the complete 26-letter alphabet into a 5-by-5 Playfair table with just twenty-five cells.

While this design option fixes the extra letter problem, when the process is reversed and the ciphertext is decrypted back to plaintext, some information is lost. In practise, it makes little difference because the encoded message is usually simple to read and comprehend.

### Rules For Keys Used

    1. Upto 25 characters in length
    2. Each letter may only be used once
    3. No white space punctuation numeric or special characters are allowed.
