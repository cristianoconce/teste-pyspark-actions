import pytest
from app import iniciar_spark, dobrar_valores

@pytest.fixture(scope="session")
def spark():
    sessao = iniciar_spark()
    yield sessao
    sessao.stop()

def test_dobrar_valores(spark):
    # 1. Cria dados falsos
    dados = [(10,), (20,)]
    df = spark.createDataFrame(dados, ["valor"])

    # 2. Roda sua função
    resultado = dobrar_valores(df)

    # 3. Verifica se 10 virou 20
    primeira_linha = resultado.first()
    assert primeira_linha["valor_dobrado"] == 20
