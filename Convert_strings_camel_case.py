def to_camel_case(text):
    result = ""
    nextupper = False
    for i in  text:
        if i == "-" or i == "_":
            nextupper = True
        elif nextupper == True:
            result += i.upper()
            nextupper = False
        else:
            result += i
    return result
to_camel_case("T_hh")