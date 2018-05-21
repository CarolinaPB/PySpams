section_names=["file", "timechange", "demesizes"];

var count = 0;
var div_ids = [];
numdemes_value=[]

//controls the checkboxes. if checked the content is showed.
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
//shows the name of the chosen matrix file next to the checkbox
function show_filename(){
  for (var id in div_ids){
    classname_file = document.getElementById(file_id[id]).className;
    classname_label = document.getElementById(label_id[id]).className;

    if (classname_file == classname_label){
      //filepath = document.getElementById(file_id[id]).value
      filepath = document.getElementById(file_id[id]).files[0].name;
      $("."+classname_label).html("<h4>" + filepath + "</h4>");
    } else {
      alert("show_filename not working");
    };
  };
};

//$(document).on('click', 'td', function () {
  //    this.contentEditable = 'true';
//});

//adds the checkbox and the "time of change" field
function Add_checkbox(count){
  // this function will work when the add_matrix button is clicked
  div_ids.push("repeated_fields"+count); //list with ids of all the new div
  //needed for the show_filename function
  file_id.push("file"+count);
  label_id.push("label"+count);
  //
  //creates a checkbox
  var chk_content =
  '<input type="checkbox" id="chk_remove' + count + '" name="chk_remove' + count + '" value="Remove" checked onclick="Checkbox(this)" class="myclass' + count + '">'+
  '   '+
  '<label id="label' + count + '" class="label' + count + '" for"chk_remove' + count + '"></label>'+
  '<input type="hidden" name="chk_remove' + count + '" value="unchecked">'+'<br>' +'<br>'

  //created a div inside the checkbox to append the other fields
  var repeated_fields_div = '<div class="myclass' + count + '" id="repeated_fields' + count + '">'

  //creates time of change field
  var timechange_content =
  '<label>' + 'Time of change' + '</label>' + "<br>"+
  '<input type="text" name="timechange'+count+'" id="timechange'+count+'" >' + '<br>'+"<br>"

  var numdemes = document.getElementById("numdemes0").value;
  var num = []
  for (i=1;i<=numdemes; i++){
    num.push(i);
  };

  var columnCount = num.length;

  //creates table with num of cells = num of demes
  var deme = '<label id="demesizes_label1">Deme sizes</label><table id="demesizes_table'+count+'" class="table-striped table-hover"><tr>';

  deme1=""
  for (var i=0;i<columnCount;i++){
    var deme1 = deme1+"<td id='deme_cell"+count+"" + i + "'></td>";
  }
  var deme_content = deme + deme1 + "</tr></table>";

  var matr = '<table id="matr_table'+count+'" class="table-striped table-hover"><tr>'
  var matr_upload='<label>Initial migration matrix</label><br><input id="file'+count+'" name="file'+count+'" type="file">'


  $("#div_to_append").append(chk_content);
  $("#div_to_append").append(repeated_fields_div);
  $("#repeated_fields"+count).append(timechange_content);
  $("#repeated_fields"+count).append(deme_content);
  $("#repeated_fields"+count).append("<br>");
  $("#repeated_fields"+count).append(matr_upload);
  $("#repeated_fields"+count).append("<br><br><br>")
  $("#repeated_fields"+count).append(matr);



  //adds the input fields to the demesizes_table
  for (var i=0;i<columnCount;i++){
    $("#deme_cell"+count+i).append("<input type='text' value='1' id='demesizes_cell"+ count +"" + i + "' name='demesizes_cell"+ count +"" + i + "' >")
  }
  table = document.getElementById("matr_table"+count)
  for (var i=0; i<columnCount;i++){
    row=table.insertRow();
    for (var j = 0; j<columnCount; j++){
      var cell=row.insertCell();
      cell.innerHTML = "<input type='text' value='0' id='matr_cell"+ i +""+ j +"' name='matr_cell"+ i +""+ j +"'>";
    }
  }

}


// creates and adds "deme size" field

$(document).ready(function(){
  $("#btn_repeat").on("click", function(){
    count++;

    Add_checkbox(count)

  });


  $("#btn_ndemes").on("click", function(){
    if (count == 0){
      Add_checkbox(count);
    }
    var numdemes = document.getElementById("numdemes0").value;
    var num = []
    for (i=1;i<=numdemes; i++){
      num.push(i);
    };

    var columnCount = num.length;

    numdemes_value.push(numdemes)


      //$("#table").remove();
      //  $("#matr_table").remove();

      //$("#sampvector_table").remove();
      //$("#demesizes_table"+count).remove();
        //$("#sampvector_label").remove();
        //$("#demesizes_label1").remove();

        //giving wrong results each time "OK" is clicked, the counter "i" starts from zero.
        //for (var i=0; i<columnCount; i++){
          //$("#demesizes_table"+i).remove();
          //$("#matr_table"+i).remove();
        //}

    //}

//Sampling vector
    var samp= '<label id="sampvector_label">Sampling vector</label><table id="sampvector_table"class="table-striped  table-hover"><tr>';
    samp1=""
    for (var i=0;i<columnCount;i++){
      var samp1 = samp1+"<td id='samp_cell" + i + "'></td>";
    }
    var samp_content = samp + samp1 + "</tr></table>";


    //$("#sampvector_div").append("<label id='sampvector_label'>Sampling vector</label>");
    $("#sampvector_div").append(samp_content);

    for (var i=0;i<columnCount;i++){
      $("#samp_cell"+i).append("<input type='text' value='0' id='samp_cell"+i+"' name='samp_cell"+i+"' >")
    }
  });

});
