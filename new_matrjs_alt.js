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
    '</div>'+
    '<input type="checkbox" id="chk_remove" name="chk_remove" value="Remove" checked>'+'Use this input'+
    '<label>'+ '**name of the chosen file**' +'<br>'  ;

    $("#fields_to_repeat").append(content);


    $("#chk_remove").change(function(){
      if (this.checked){
        $("#repeated_fields"+count).show();
      } else {
        $("#repeated_fields"+count).hide();
      }
    });

  });


});
