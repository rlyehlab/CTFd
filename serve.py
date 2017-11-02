from CTFd import create_app

app = create_app()
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(debug=True, threaded=True, host="127.0.0.1", port=4000)

