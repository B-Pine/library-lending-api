from flask import Flask, jsonify, request

from library import books

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Library Lending API"})


@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json(silent=True)

    error = books.validate_book_data(data)
    if error:
        return jsonify({"error": error}), 400

    if books.isbn_exists(data["isbn"]):
        return jsonify({"error": "A book with this ISBN already exists"}), 409

    book = books.add_book(data)
    return jsonify(book), 201


if __name__ == "__main__":
    app.run(debug=True)
