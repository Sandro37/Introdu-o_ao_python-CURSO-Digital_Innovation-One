# Aprenda a utilizar informações de data, horário e relacionar
# datas diferentes
from datetime import date,time, datetime, timedelta


def trabalhando_com_date():
    data_atual = date.today()
    data_formatada = data_atual.strftime('%d/%m/%y')  # y Minusculo trás 2 digitos no ano

    print(data_atual.strftime('%d/%m/%Y'))  # Y maiusculo trás 4 digitos no ano
    print('Formatada: {}'.format(data_formatada))

    data_atual = data_atual.strftime('%A %B %Y')
    print(data_atual)


def trabalhando_com_time():
    horario = time(hour=15,minute=18,second=30)
    print(horario)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_com_dateTime():
    data_actual = datetime.now()
    print(data_actual)
    print(data_actual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_actual.strftime('%c'))
    print(data_actual.day)
    print(data_actual.month)
    print(data_actual.year)

    print(data_actual.minute)
    print(data_actual.second)
    print(data_actual.date())

    #dia da semana
    print(data_actual.weekday())
    print(data_actual.isoweekday())

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_actual.weekday()])

    data_criada = datetime(2018, 6, 20, 15,30,20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    data_string = '01/01/2019 12:20:22'

    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=40)
    print(nova_data)

def verificar_dia_semana():
    data_actual = datetime.now()

    if data_actual.isoweekday() == 1:
        return 'Segunda-Feira'
    elif data_actual.isoweekday() == 2:
        return 'Terça-Feira'
    elif data_actual.isoweekday() == 3:
        return 'Quarta-feira'
    elif data_actual.isoweekday() == 4:
        return 'Quinta-Feira'
    elif data_actual.isoweekday() == 5:
        return 'Sexta-Feira'
    elif data_actual.isoweekday() == 6:
        return 'Sábado'
    elif data_actual.isoweekday() == 7:
        return 'Domingo'

if __name__ == '__main__':
    trabalhando_com_dateTime()
    # hoje_dia_semana = verificar_dia_semana()
    # print('hoje é {}'.format(hoje_dia_semana))

