def xor_encrypt_decrypt(data, key):
 
    Encrypts or decrypts the data using XOR operation with the given key.
    This function works for both encryption and decryption due to XOR properties.
   
    # Convert data and key to bytearray for XOR operation
    data_bytes = bytearray(data.encode('utf-8'))
    key_bytes = bytearray(key.encode('utf-8'))
    
    # Perform XOR operation
    result_bytes = bytearray(len(data_bytes))
    for i in range(len(data_bytes)):
        result_bytes[i] = data_bytes[i] ^ key_bytes[i % len(key_bytes)]
    
    # Return the result as a string
    return result_bytes.decode('utf-8', errors='replace')

def main():
    while True:
        print("\nXOR Encryption/Decryption Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue
        
        data = input("Enter the text to process: ")
        key = input("Enter the encryption/decryption key: ")
        
        result = xor_encrypt_decrypt(data, key)
        
        if choice == '1':
            print(f"Encrypted text: {result}")
        else:
            print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()
      
