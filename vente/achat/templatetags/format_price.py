from django import template

register=template.Library()
@register.filter(name="formatprice")
def formatprice(value):
    value=str(value)
    indexDot=value.find(",")
    if indexDot==-1:
        indexDot=len(value)
    enterPart=value[:indexDot][::-1]
    decimalPart=value[indexDot+1:]
    valuePart=[]
    i=0
    while(1):
        part=enterPart[i:i+3]
        if part=="":
            break
        valuePart.append(part)
        i+=3
    valuePart=" ".join(valuePart)[::-1]
    if len(decimalPart)>0:
        valuePart+=("."+decimalPart)

    return valuePart
