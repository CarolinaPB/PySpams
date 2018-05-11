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

$(document).on('click', 'td', function () {
      this.contentEditable = 'true';
});

function Add_checkbox(count){

  div_ids.push("repeated_fields"+count); //creates list with the ids of all the new div (new group of input)
  file_id.push("file"+count);
  label_id.push("label"+count);

  var chk_content =
  '<input type="checkbox" id="chk_remove' + count + '" name="chk_remove' + count + '" value="Remove" checked onclick="Checkbox(this)" class="myclass' + count + '">'+
  '   '+
  '<label id="label' + count + '" class="label' + count + '" for"chk_remove' + count + '"></label>'+
  '<input type="hidden" name="chk_remove' + count + '" value="unchecked">'+'<br>' +'<br>'

  var timechange_content =
  '<div class="myclass' + count + '" id="repeated_fields' + count + '">'+

    '<label>' + 'Time of change' + '</label>' + "<br>"+
    '<input type="text" name= '+ section_names[1] +'' + count + ' id='+ section_names[1] +'' + count + ' >' + '<br>'+"<br>"

  $("#div_to_append").append(chk_content);
  $("#div_to_append").append(timechange_content);

}
function create_fields(count){

  var numdemes = document.getElementById("numdemes0").value;
  var num = []
  for (i=1;i<=numdemes; i++){
    num.push(i);
  };

  var columnCount = num.length;

  //content related to the new input fields

  var deme = '<table id="demesizes_table'+count+'" class="table-striped table-hover"><tr>';
  deme1=""
  for (var i=0;i<columnCount;i++){
    var deme1 = deme1+"<td id='deme_cell"+count+"" + i + "'></td>";
  }
  var deme_content = deme + deme1 + "</tr></table>";

    //'<label>' + 'Initial migration matrix' + '</label>' + "<br>"+
    //'<input type="file" name= '+ section_names[0] +'' + count + ' id='+ section_names[0] +'' + count + ' onchange="show_filename()" class="label' + count + '">' + '<br>'+"<br>"+'<br>'+


  //'</div>'+ '<br>' ;

  var deme_label = "<label id='demesizes_label1'>Deme sizes</label>"

  $("#repeated_fields"+count).append(deme_label);
  $("#repeated_fields"+count).append(deme_content);

  for (var i=0;i<columnCount;i++){
    $("#deme_cell"+count+i).append("<input type='text' value='1' id='demesizes_cell"+ count +"" + i + "' name='demesizes_cell"+ count +"" + i + "' >")
  }
}

$(document).ready(function(){
  $("#btn_repeat").on("click", function(){
    count++;

    Add_checkbox(count)
    create_fields(count)

  });


  $("#btn_ndemes").on("click", function(){

    var numdemes = document.getElementById("numdemes0").value;
    var num = []
    for (i=1;i<=numdemes; i++){
      num.push(i);
    };

    var columnCount = num.length;


    var myEle = document.getElementsByClassName("table");
    if(myEle){
        //$("#table").remove();
        $("#matr_table").remove();
        $("#sampvector_table").remove();
        $("#demesizes_table").remove();
        $("#sampvector_label").remove();
        $("#demesizes_label").remove();

        //giving wrong results each time "OK" is clicked, the counter "i" starts from zero.
        for (var i=0; i<columnCount; i++){
          $("#demesizes_table"+i).remove();
        }
        $("#demesize_label1").remove();
        //create_fields(count-1);
        create_fields(count);
    }


    var matr1 = '<table id="matr_table" class="table-striped table-hover">'

//Sampling vector
    var str_t1 = '<table id="sampvector_table"class="table-striped  table-hover"><tr>';
    str_t2=""
    for (var i=0;i<columnCount;i++){
      var str_t2 = str_t2+"<td id='samp_cell" + i + "'></td>";
    }
    var str_t3 = str_t1 + str_t2 + "</tr></table>";

//Deme sizes
    var str_t4 = '<table id="demesizes_table" class="table-striped table-hover"><tr>';
    str_t5=""
    for (var i=0;i<columnCount;i++){
      var str_t5 = str_t5+"<td id='deme_cell" + i + "'></td>";
    }
    var str_t6 = str_t4 + str_t5 + "</tr></table>";

//Add to the page
    $("#sampvector_div").append("<label id='sampvector_label'>Sampling vector</label>");
    $("#sampvector_div").append(str_t3);

    $("#demesizes_div").append("<label id='demesizes_label'>Deme sizes</label>");
    $("#demesizes_div").append(str_t6);

    $("#matr_div").append(matr1);

//set attributes
    for (var i=0;i<columnCount;i++){
      $("#samp_cell"+i).append("<input type='text' value='0' id='sampvector_cell0" + i + "' name='sampvector_cell0" + i + "' >")
      $("#deme_cell"+i).append("<input type='text' value='1' id='demesizes_cell0" + i + "' name='demesizes_cell0" + i + "' >")
    }
//first matrix - set input tag
    table = document.getElementById("matr_table")
    for (var i=0; i<columnCount;i++){
      row=table.insertRow();
      for (var j = 0; j<columnCount; j++){
        var cell=row.insertCell();
        cell.innerHTML = "<input type='text' value='0' id='matr_cell0"+ i +""+ j +"' name='matr0_cell"+ i +""+ j +"'>";
      }
    }


  });

});
