from app import app


def test_saude_nao_aceita_post():
    resposta = app.test_client().post("/saude")
    assert resposta.status_code == 405