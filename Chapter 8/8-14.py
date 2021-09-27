# TRY IT YOURSELF
# 8-14, Cars.

def build_car(manufaktura, model_name, **car_info):
    car = {}
    car['manufakturer'] = manufaktura
    car['model'] = model_name

    for key,value in car_info.items():
        car['key'] = value
        return car


car1 = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)
