def checkSqlInjection(input):
    if "'" in input:    return True
    elif "\\" in input:    return True
    elif "#" in input:    return True
    elif ";" in input:    return True
    elif "#" in input:    return True
    else:   return False