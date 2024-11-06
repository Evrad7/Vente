
var floatformat=function(number){
  number=String(number)
  parts=number.split(".")
  decimalPart=parts[1]
  if (decimalPart){
    decimalPart=decimalPart.substring(0, 4)
    if(decimalPart.length<4){
    }
    else{
      decimalLastIndex=decimalPart.length-1
      decimalLastChar=decimalPart.charAt(decimalLastIndex)
      if(parseInt(decimalLastChar)>=5){
        decimalLastChar=decimalPart.charAt(decimalLastIndex-1)
        decimalLastDigit=parseInt(decimalLastChar)+1
        if (decimalLastDigit==10){
          decimalLastChar=""
        }
        else{
          decimalLastChar=String(decimalLastDigit)
        }
        decimalPart=decimalPart.substring(0, decimalLastIndex-1)+decimalLastChar
      }
      else{
        decimalPart=decimalPart.substring(0, decimalLastIndex)
      }
    }
  }
  else{
    decimalPart=""
  }

  enterPart=parts[0]
  length=enterPart.length
  enterPartParse=""
  i=length%3
  enterPartParse+=enterPart.substring(0, i)
  for(var _=0; _<parseInt(length/3); _++){
    enterPartParse+=" "
    _*=3
    enterPartParse+=enterPart.substring(i+_, i+_+3)
  }
  if(decimalPart)
    return enterPartParse+"."+decimalPart
  else {
    return enterPartParse
  }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
