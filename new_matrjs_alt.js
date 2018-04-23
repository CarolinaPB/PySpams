section_names=["file", "timechange", "demesizes"];

var count = 0;
var div_ids = [];


function Checkbox(e){

  for (var id in div_ids){
    classname_div = document.getElementById(div_ids[id]).className;
    classname_chk = e.className;

    if (classname_div == classname_chk){
      if (e.checked == false){
        //alert("unchecked "+"div " + classname_div);
        $("#"+div_ids[id]).hide();
      } else {
        //alert("checked "+"chk " +classname_chk);
        $("#"+div_ids[id]).show();
      };
    };
  };
};


$(document).ready(function(){

  $("#btn_repeat").on("click", function(){
    count++;
    div_ids.push("repeated_fields"+count);

    var content =
    '<div class="myclass' + count + '"  id="repeated_fields' + count + '">'+

    '<label>' + 'Initial migration matrix' + '</label>' + "<br>"+
    '<input type="file" name= '+ section_names[0] +'' + count + ' id='+ section_names[0] +'' + count + ' >' + '<br>'+"<br>"+'<br>'+

    '<label>' + 'Time of change' + '</label>' + "<br>"+
    '<input type="text" name= '+ section_names[1] +'' + count + ' id='+ section_names[1] +'' + count + ' >' + '<br>'+"<br>"+

    '<label>' + 'Deme sizes' + '</label>' + "<br>"+
    '<input type="text" name= '+ section_names[2] +'' + count + ' id='+ section_names[2] +'' + count + ' >' + '<br>'+"<br>" +
    '</div>'+

    '<input type="checkbox" id="chk_remove' + count + '" name="chk_remove' + count + '" value="Remove" checked onclick="Checkbox(this)"class="myclass' + count + '">'+
    '<label for"chk_remove' + count + '">   Use</label>'+
    '<input type="hidden" name="chk_remove' + count + '" value="unchecked">'+
    '<br>'+'<br>' +'<br>' ;

    $("#fields_to_repeat").append(content);

  });

});
