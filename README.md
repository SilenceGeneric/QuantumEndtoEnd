        # QuantumEndtoEnd
A simplified secure communication system using quantum entanglement for key distribution.

This code will simulate the generation of entangled photons, perform a quantum measurement to establish a shared secret key, and encrypt and decrypt a message using that key.

!!!***IMPORTANT***!!!

CRz Gate Angle: The angle used in the controlled-RZ gate (qc.crz()) might need adjustment depending on the desired entanglement strength. The current value of 2 * np.pi / 4 corresponds to π/2 radians, which results in a 50-50 beam splitter. You may need to adjust this angle for different levels of entanglement.

Key Conversion: In the encrypt_message and decrypt_message functions, make sure to convert the key to an integer before performing XOR operations. The current implementation assumes the key is already an integer.

Decryption: When decrypting the message, ensure that the length of the decrypted binary string is a multiple of 8 to avoid losing characters during conversion back to text. The current implementation might miss the last few characters if the length is not a multiple of 8.
