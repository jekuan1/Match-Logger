from website import create_app

app = create_app()

# gunicorn -b 0.0.0.0:8000 -w 4 app:app
# $ nginx

# TODO add font awesome offline
# TODO add admin controls
# TODO add player info
# TODO add dark mode

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=8000)
