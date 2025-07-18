import requests

def test_enjambre():
    resp = requests.get('http://localhost:5000/enjambre')
    assert resp.status_code == 200
    assert resp.headers['Content-Type'].startswith('application/json')
    print('✔️ /enjambre OK')

def test_estaciones_marica():
    resp = requests.get('http://localhost:5000/api/ana/estaciones_marica')
    assert resp.status_code == 200
    assert resp.headers['Content-Type'].startswith('application/json')
    print('✔️ /api/ana/estaciones_marica OK')

if __name__ == '__main__':
    test_enjambre()
    test_estaciones_marica() 