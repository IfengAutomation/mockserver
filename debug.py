import mockserver

if __name__ == '__main__':
    app = mockserver.get_app()
    app.run(host='0.0.0.0', port=8080, use_reloader=False, threaded=True)
