def transform_date_format(dates):
    transformed_dates = []
    for date in dates:
        year, month, day = None, None, None
        if '/' in date:
            parts = date.split('/')
            transformed_dates.append(identifier(parts))
        elif '-' in date:
            parts = date.split('-')
            transformed_dates.append(identifier(parts))
    return transformed_dates

def identifier(parts):
    for part in parts:
        if len(part) == 4:
            year = part
        elif int(part) <= 12:
            month = part
        else:
            day = part

    new_date = f"{year}{month}{day}"
    return new_date
# Ejemplo de uso
dates = ["2010/02/20", "19/12/2016", "11-18-2012", "20130720"]
transformed = transform_date_format(dates)
print(transformed)  # Debería imprimir ['20100220', '20161219', '20121118']
