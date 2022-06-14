from aylien_model_serving.app_factory import FlaskAppWrapper


def run_app():
    """
    This is a mock app, showing how to make simple requests.
    """

    counter = 0

    def reverse_text(text):
        text = "".join(list(reversed(text)))
        return {"text": text}

    def increment_count():
        counter += 1
        return {"count": counter}

    def process_reverse_text():
        return FlaskAppWrapper.process_json(reverse_text)

    def process_increment_count():
        return FlaskAppWrapper.process_json(increment_count)


    routes = [
        {
            "endpoint": "/reverse",
            "callable": process_reverse_text,
            "methods": ["POST"]
        },
        {
            "endpoint": "/count",
            "callable": increment_count,
            "methods": ["POST"]
        },
    ]

    return FlaskAppWrapper.create_app(routes)
