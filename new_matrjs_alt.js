section_names=["file", "timechange", "demesizes"];

var count = 0;
var div_ids = [];

function Checkbox(e){
  for (var id in div_ids){
    classname_div = document.getElementById(div_ids[id]).className;
    classname_chk = e.className;

    if (classname_div == classname_chk){
      if (e.checked == false){
        $("#"+div_ids[id]).hide();
      } else {
        $("#"+div_ids[id]).show();
      };
    };
  };
};

var file_id =[]
var label_id=[]

function show_filename(){
  for (var id in div_ids){
    classname_file = document.getElementById(file_id[id]).className;
    classname_label = document.getElementById(label_id[id]).className;

    if (classname_file == classname_label){
      //filepath = document.getElementById(file_id[id]).value
      filepath = document.getElementById(file_id[id]).files[0].name;
      $("."+classname_label).html("<h4>" + filepath + "</h4>");
    } else {
      alert("not working");
    };
  };
};



$(document).ready(function(){
  $("#btn_repeat").on("click", function(){
    count++;
    div_ids.push("repeated_fields"+count); //creates list with the ids of all the new div (new group of input)
    file_id.push("file"+count);
    label_id.push("label"+count);
    var content =
    //content related to the checkboxes
    '<input type="checkbox" id="chk_remove' + count + '" name="chk_remove' + count + '" value="Remove" checked onclick="Checkbox(this)" class="myclass' + count + '">'+
    '   '+
    '<label id="label' + count + '" class="label' + count + '" for"chk_remove' + count + '"></label>'+
    '<input type="hidden" name="chk_remove' + count + '" value="unchecked">'+'<br>' +'<br>'+

    //content related to the new input fields
    '<div class="myclass' + count + '" id="repeated_fields' + count + '">'+

      '<label>' + 'Time of change' + '</label>' + "<br>"+
      '<input type="text" name= '+ section_names[1] +'' + count + ' id='+ section_names[1] +'' + count + ' >' + '<br>'+"<br>"+

      '<label>' + 'Deme sizes' + '</label>' + "<br>"+
      '<input type="text" name= '+ section_names[2] +'' + count + ' id='+ section_names[2] +'' + count + ' >' + '<br>'+"<br>" +

      '<label>' + 'Initial migration matrix' + '</label>' + "<br>"+
      '<input type="file" name= '+ section_names[0] +'' + count + ' id='+ section_names[0] +'' + count + ' onchange="show_filename()" class="label' + count + '">' + '<br>'+"<br>"+'<br>'+


    '</div>'+ '<br>' ;
    $("#div_to_append").append(content);

  });
  //Creates matrix with number of rows and columns = number of demes
  var tnum =0
  $("#btn_ndemes").on("click", function(){

    var myEle = document.getElementsByClassName("table");
    if(myEle){
        $("#table"+(tnum-1)).remove();
        $("#sampvector_table"+(tnum-1)).remove();
        $("#demesizes_table"+(tnum-1)).remove();
        $("#sampvector_label").remove();
        $("#demesizes_label").remove();
    }

    var numdemes = document.getElementById("numdemes0").value;
    var num = []
    for (i=1;i<=(numdemes); i++){
      num.push(i);
    };
    var table = document.createElement("TABLE");
    table.setAttribute("id", "table"+tnum);
    table.setAttribute("class", "table-striped table-bordered table-hover");
    //table.border="1";

    var columnCount = num.length;

    for (var i=0; i<columnCount;i++){
      row=table.insertRow();
      for (var j = 0; j<columnCount; j++){
        var cell=row.insertCell();
        cell.innerHTML = "0.";
      }
    }

    var str_t1 = '<table id="sampvector_table' + tnum + '"class="table-striped table-bordered table-hover"><tr>';
    str_t2=""
    for (var i=0;i<columnCount;i++){
      var str_t2 = str_t2+"<td>0</td>";
    }
    var str_t3 = str_t1 + str_t2 + "</tr></table>";

    var str_t4 = '<table id="demesizes_table' + tnum + '" class="table-striped table-bordered table-hover"><tr>';
    str_t5=""
    for (var i=0;i<columnCount;i++){
      var str_t5 = str_t5+"<td>1</td>";
    }
    var str_t6 = str_t4 + str_t5 + "</tr></table>";

    $("#sampvector_div").append("<label id='sampvector_label'>Sampling vector</label>");
    $("#sampvector_div").append(str_t3);

    $("#demesizes_div").append("<label id='demesizes_label'>Deme sizes</label>");
    $("#demesizes_div").append(str_t6);

    $("#new_matr").append(table);

    tnum++

  });

});
