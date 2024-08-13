import datetime
import time


def enterEmpl():
    # Accessing the default configuration file and loading the values into variables:
    f = open('DataFiles/Defaults.dat', 'r')
    NEXT_TRAN_NUM = f.readline().strip()
    NEXT_DRIVER_ID = int(f.readline())
    M0NTH_STAND_FEE = float(f.readline())
    DAILY_RENT_FEE = float(f.readline())
    WEEK_RENT_FEE = float(f.readline())
    HTS = float(f.readline())
    f.close()

    # User Inputs:
    emplFullName = input('Enter employee\'s full name: ').title()
    streetAdd = input('Enter a street address: ').title()
    city = input('Enter a city: ').title()
    province = input('Enter the province (LL): ').upper()
    zip = input('Enter a postal code (XXXXXX): ').upper()
    phoneNum = input('Enter a phone number (###-###-####): ')
    licNum = input('Enter a licence number (#########): ')

    licExpDate = input('Enter a licence expiry date: (DD-MM-YYYY): ')
    licExpDate = datetime.datetime.strptime(licExpDate, "%d-%m-%Y")

    insurPolComp = input('Enter an insurance policy company: ').title()
    insurPolNum = input('Enter the insurance policy number (###########): ')

    rentCar = input('Will the employee rent a car? Enter Y for Yes or N for No: ').upper()
    if rentCar == 'Y':
        carOwnRent = 'Rent'
        payment = input('Is rental for a day or a week? Enter Day or Week: ').title()
        if payment == 'Day':
            balDue = DAILY_RENT_FEE
        else:
            balDue = WEEK_RENT_FEE
    else:
        balDue = M0NTH_STAND_FEE
        carOwnRent = 'Own'

    emplPosition = input('Enter the employee\'s position: ').title()
    carId = input('Enter a car ID if required, or press the Enter key to continue: ').upper()

    print()
    print()
    print('Information is processing...')
    print()

    # Write the values to a file for future reference:
    f = open('DataFiles/Employees.dat', 'a')
    f.write(f'{NEXT_DRIVER_ID}, ')
    f.write(f'{emplFullName}, ')
    f.write(f'{streetAdd} {city} {province} {zip}, ')
    f.write(f'{phoneNum}, ')
    f.write(f'{licNum}, ')
    f.write(f'{licExpDate.date()}, ')
    f.write(f'{insurPolComp}, ')
    f.write(f'{insurPolNum}, ')
    f.write(f'{carOwnRent}, ')
    f.write(f'{str(balDue)}, ')
    if carOwnRent == 'Own':
        f.write(f'{emplPosition}\n')
    else:
        f.write(f'{emplPosition}, ')
        f.write(f'{carId}\n')
    f.close()

    time.sleep(2)
    print('Information is processed and saved.')

    NEXT_DRIVER_ID += 1

    # Housekeeping:
    # Updating the default files with the current values:
    f = open('DataFiles/Defaults.dat', 'w')
    f.write(f'{NEXT_TRAN_NUM}\n')
    f.write(f'{NEXT_DRIVER_ID}\n')
    f.write(f'{M0NTH_STAND_FEE}\n')
    f.write(f'{DAILY_RENT_FEE}\n')
    f.write(f'{WEEK_RENT_FEE}\n')
    f.write(f'{HTS}\n')
    f.close()

    print()
    input("Press the Enter key to continue...")



