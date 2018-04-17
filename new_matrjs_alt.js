section_names=["file", "timechange", "demesizes"];

var count = 0;
$(document).ready(function(){

  $("#btn_repeat").on("click", function(){

    count++;

    var content =
    '<div id="repeated_fields' + count + '">'+
    '<label>' + 'Initial migration matrix' + '</label>' + "<br>"+
    '<input type="file" name= '+ section_names[0] +'' + count + ' id='+ section_names[0] +'' + count + ' >' + '<br>'+"<br>"+'<br>'+

    '<label>' + 'Time of change' + '</label>' + "<br>"+
    '<input type="text" name= '+ section_names[1] +'' + count + ' id='+ section_names[1] +'' + count + ' >' + '<br>'+"<br>"+

    '<label>' + 'Deme sizes' + '</label>' + "<br>"+
    '<input type="text" name= '+ section_names[2] +'' + count + ' id='+ section_names[2] +'' + count + ' >' + '<br>'+"<br>" +

    '<input type="submit" class="btn_remove" name="button" id="btn_remove" value="Remove">' +"<br><br>" +
    '</div>'


    $("#fields_to_repeat").append(content);

    element = $(".btn_remove");
    for (var i in element) {
      element.on('click', function() {
        $(this).parent().remove();
      });
    };
  });
});
