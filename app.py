from flask import Flask, request, jsonify
import hashlib
from urllib.parse import parse_qs

app = Flask(__name__)

@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    # Your PayU Money credentials
    merchant_key = '62Boh5H7'
    merchant_salt = '3qdfCkKgi1'
    base_url="https://sandboxsecure.payu.in/_payment"

    # Payment parameters
    transaction_id = '001'
    amount = '100.00' 
    product_info = 'Product Information'
    customer_name = 'John'
    customer_email = 'john@example.com'
    customer_phone = '1234567890'
    success_url = 'https://payu.in/success'  

    # Calculate the hash
    hash_string = f"{merchant_key}|{transaction_id}|{amount}|{product_info}|{customer_name}|{base_url}|{customer_email}|{transaction_id}|||||||||||{merchant_salt}"
    hash_string = hash_string.encode('utf-8')
    hash = hashlib.sha512(hash_string).hexdigest()

    # Prepare the response
    response_data = {
        'base_url':base_url,
        'key': merchant_key,
        'txnid': transaction_id,
        'amount': amount,
        'productinfo': product_info,
        'firstname': customer_name,
        'email': customer_email,
        'phone': customer_phone,
        'surl': success_url,
        'service_provider': 'payu_paisa',
        'hash': hash,
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)




# Merchant Key   62Boh5H7
# Merchant Salt   3qdfCkKgi1

# PAYUMONEY_MERCHANT_ID 6726254
# Client ID  c306ac95d091f21cf44aba45ec676828084c8f9ff9463d435ff80f6219594071
# Client secret 1211877c2b153b29a9f37591fbd738f0a2b45ea46062ec9141d8ac47b383f361