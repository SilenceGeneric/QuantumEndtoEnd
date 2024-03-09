from qiskit import QuantumCircuit, Aer, execute
import numpy as np

# Function to simulate the generation of entangled photons using a quantum circuit
def generate_entangled_photons():
    # Create a quantum circuit with two qubits
    qc = QuantumCircuit(2)
    
    # Apply a Hadamard gate to the first qubit
    qc.h(0)
    
    # Apply a CNOT gate to entangle the two qubits
    qc.cx(0, 1)
    
    return qc

# Function to perform a quantum measurement on entangled photons
def perform_measurement(qc):
    # Perform a measurement on both qubits
    qc.measure_all()
    
    # Simulate the quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    
    # Get the measurement outcome
    counts = result.get_counts()
    return list(counts.keys())[0]

# Function to encrypt a message using the shared secret key
def encrypt_message(message, key):
    # Convert the message and key to binary strings
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_key = format(key, '08b')
    
    # XOR the message with the key to encrypt it
    encrypted_message = ''.join(str(int(binary_message[i]) ^ int(binary_key[i])) for i in range(len(binary_message)))
    
    return encrypted_message

# Function to decrypt a message using the shared secret key
def decrypt_message(encrypted_message, key):
    # Convert the encrypted message and key to binary strings
    binary_encrypted_message = encrypted_message
    binary_key = format(key, '08b')
    
    # XOR the encrypted message with the key to decrypt it
    decrypted_message = ''.join(str(int(binary_encrypted_message[i]) ^ int(binary_key[i])) for i in range(len(binary_encrypted_message)))
    
    # Convert the decrypted binary string back to characters
    decrypted_message_chars = [chr(int(decrypted_message[i:i+8], 2)) for i in range(0, len(decrypted_message), 8)]
    decrypted_message_text = ''.join(decrypted_message_chars)
    
    return decrypted_message_text

# Main function
def main():
    # Alice generates entangled photons
    entangled_photons_circuit = generate_entangled_photons()
    
    # Alice performs a measurement to establish the shared secret key
    key_measurement = perform_measurement(entangled_photons_circuit)
    
    # Bob performs the same measurement to obtain the same key
    shared_secret_key = int(key_measurement, 2)
    
    # Alice encrypts her message using the shared secret key
    message = "Hello, Bob!"
    encrypted_message = encrypt_message(message, shared_secret_key)
    
    # Bob decrypts the message using the shared secret key
    decrypted_message = decrypt_message(encrypted_message, shared_secret_key)
    
    print("Original message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

# Run the main function
if __name__ == "__main__":
    main()
