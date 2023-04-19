def tempconvert(celcius=None, farenheit=None):
    if celcius is not None:
        result = celcius * 1.8 + 32
        return result
    elif farenheit is not None:
        result = (farenheit -32) / 1.8
        return result
    else:
        oppleg = "one of the temperature needs to have a value"
        return oppleg




