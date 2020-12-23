from iqoptionapi.stable_api import IQ_Option

API = IQ_Option(input('email: '), input('password: '))
check, reason = API.connect()
if not check:
    print('Falha na Conexão.')
    exit(0)
print(API.get_alerts())
