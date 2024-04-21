from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Server running on http://127.0.0.1:8080")
    app.run(debug=True, host='0.0.0.0', port=8080)
