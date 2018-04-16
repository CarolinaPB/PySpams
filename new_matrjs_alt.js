section_names=["file", "timechange", "demesizes"];

var count = 0;

$("#btn_repeat").on("click", function(){

  count++;

  var content =
  '<label>' + 'Initial migration matrix' + '</label>' + "<br>"+
  '<input type="file" name= '+ section_names[0] +'' + count + ' id='+ section_names[0] +'' + count + ' class="repeated_fields">' + '<br>'+"<br>"+'<br>'+
  '<label>' + 'Time of change' + '</label>' + "<br>"+
  '<input type="text" name= '+ section_names[1] +'' + count + ' id='+ section_names[1] +'' + count + ' >' + '<br>'+"<br>"+
  '<label>' + 'Deme sizes' + '</label>' + "<br>"+
  '<input type="text" name= '+ section_names[2] +'' + count + ' id='+ section_names[2] +'' + count + ' >' + '<br>'+"<br>" +
  '<input type=submit name="button" data-id="remove_btn ' + count + '" value="Remove">' +"<br><br>"


  $("#fields_to_repeat").append(content)

  $("#remove_btn").off("click").on("click", removeFields);
});

//not working
function removeFields() {
    var id = $(this).data("id");
    $("#repeated_fields").remove();
};
