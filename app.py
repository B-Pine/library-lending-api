from flask import Flask, jsonify, request

from library import books, loans

app = Flask(__name__)
APP_VERSION = "1.0.0"


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Library Lending API"})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "version": APP_VERSION}), 200


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


@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify(books.list_books()), 200


@app.route("/books/<int:book_id>", methods=["GET"])
def get_one_book(book_id):
    book = books.get_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200


@app.route("/loans", methods=["POST"])
def create_loan():
    data = request.get_json()

    error = loans.validate_loan_data(data)
    if error:
        return jsonify({"error": error}), 400

    book = books.get_book(data['book_id'])
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    if not book["available"]:
        return jsonify({"error": "Book is already on loan"}), 409

    loan = loans.borrow_book(book, data["borrower_name"])
    return jsonify(loan), 201


@app.route("/loans/<int:loan_id>/return", methods=["POST"])
def return_loan(loan_id):
    loan = loans.get_loan(loan_id)
    if loan is None:
        return jsonify({"error": "Loan not found"}), 404

    if loan["returned_on"] is not None:
        return jsonify({"error": "This loan has already been returned"}), 409

    loan = loans.return_book(loan)
    return jsonify(loan), 200


@app.route("/loans/overdue", methods=["GET"])
def get_overdue_loans():
    return jsonify(loans.find_overdue_loans()), 200


if __name__ == "__main__":
    app.run(debug=True)
