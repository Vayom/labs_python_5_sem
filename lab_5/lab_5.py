import boreholes

choice = 1
oil_field = boreholes.OilField()
while choice != 0:
    print(f'1) Добавить нефтяную скважину\n'
          f'2) Добавить газовую скважину\n'
          f'3) Добавить нагнетающую скважину\n'
          f'4) Закачать воду\n'
          f'5) Закачать топливо\n'
          f'6) Показать все скважины в месторождении\n'
          f'0) Выйти\n')
    while True:
        try:
            choice = int(input())
            if 0 <= choice <= 6:
                break
            else:
                print('Недопустимое значение')
        except ValueError:
            print('Недопустимое значение')

    if choice == 1:
        level = 0
        print('Выберите уровень скважины\n'
              '1) 1 уровень\n'
              '2) 2 уровень\n'
              '3) 3 уровень\n')
        while True:
            try:
                level = int(input())
                if 1 <= level <= 3:
                    break
                else:
                    print('Недопустимое значение')
            except ValueError:
                print('Недопустимое значение')
        oil_field.add_borehole(boreholes.OilBorehole(level=level))

    if choice == 2:
        level = 0
        print('Выберите уровень скважины\n'
              '1) 1 уровень\n'
              '2) 2 уровень\n'
              '3) 3 уровень\n')
        while True:
            try:
                level = int(input())
                if 1 <= level <= 3:
                    break
                else:
                    print('Недопустимое значение')
            except ValueError:
                print('Недопустимое значение')
        oil_field.add_borehole(boreholes.GasBorehole(level=level))

    if choice == 3:
        level = 0
        print('Выберите уровень скважины\n'
              '1) 1 уровень\n'
              '2) 2 уровень\n'
              '3) 3 уровень\n')
        while True:
            try:
                level = int(input())
                if 1 <= level <= 3:
                    break
                else:
                    print('Недопустимое значение')
            except ValueError:
                print('Недопустимое значение')
        oil_field.add_borehole(boreholes.InjectionBorehole(level=level))

    if choice == 4:
        if oil_field.injection_boreholes:
            cur_water_volume = oil_field.water_volume
            oil_field.pump_water()
            if oil_field.water_volume - cur_water_volume > 0:
                print(f'Добавлено - {oil_field.water_volume - cur_water_volume} единиц воды')
        else:
            print('Нет нагнетающих скважин')
    if choice == 5:
        if oil_field.fuel_boreholes:
            cur_gas_volume = oil_field.gas_volume
            cur_oil_volume = oil_field.oil_volume
            oil_field.pump_fuel()
            if oil_field.oil_volume - cur_oil_volume > 0:
                print(f'Добавлено - {oil_field.oil_volume - cur_oil_volume} единиц нефти')
            if oil_field.gas_volume - cur_gas_volume > 0:
                print(f'Добавлено - {oil_field.gas_volume - cur_gas_volume} единиц газа')
        else:
            print('Нет добывающих топливо скважин')
    if choice == 6:
        oil_field.show_boreholes()

