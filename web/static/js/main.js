
function popitup(link) {
  var w = window.open(link.href,
    link.target || "_blank",
 'menubar=no,toolbar=no,location=no,directories=no,status=no,scrollbars=no,resizable=no,dependent,width=1200,height=620,left=0,top=0');
  return w ? false : true; // allow the link to work if popup is blocked
}

var myText = 'Hello world!',
    myHTML = '<b>'+myText+'</b>';

function openFile (textToEncode, contentType, newWindow) {
    var encodedText = window.btoa(textToEncode);
    var dataURL = 'data:' + contentType + ';base64,' + encodedText;
    if (newWindow) { // Not useful for application/octet-stream type
        window.open(dataURL); // To open in a new tab/window
    }
    else {
        window.location = dataURL; // To change the current page
    }
}

