# When store informations in dictionary, use function_name['valuation']=values

def car_info(company, model, **details):
    info = {}
    
    info['company_name'] = company
    info['model_type'] = model
    
    for key, value in details.items():
        info[key] = value
    return info
        
new_car = car_info('jaguar', 'business', color='white', seat='leather')
print(new_car)