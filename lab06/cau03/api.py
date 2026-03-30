from flask import Flask, request, jsonify
from cipher.RailFence import RailFenceCipher
app = Flask(__name__)


rail_cipher = RailFenceCipher()
@app.route("/api/railfence/encrypt", methods=["POST"])
def rail_encrypt():
    data = request.json
    message = data['message']
    key = int(data['key'])  # số rail

    encrypted_message = rail_cipher.encrypt(message, key)

    return jsonify({'encrypted_message': encrypted_message})

@app.route("/api/railfence/decrypt", methods=["POST"])
def rail_decrypt():
    data = request.json
    cipher = data['ciphertext']
    key = int(data['key'])

    decrypted_message = rail_cipher.decrypt(cipher, key)

    return jsonify({'decrypted_message': decrypted_message})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)