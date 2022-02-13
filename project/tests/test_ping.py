# project/tests/test_ping.py

# principle Given-When-Then
def test_ping(test_app):
    # given: test_app

    # when
    response = test_app.get("/ping")

    # then
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}
