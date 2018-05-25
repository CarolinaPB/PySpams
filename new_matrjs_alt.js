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

function Add_checkbox(count){

  div_ids.push("div_chk"+count); //list with ids of all the new div


  //creates a checkbox
  var chk_content =
  '<br><input type="checkbox" id="chk_remove' + count + '" name="chk_remove' + count + '" value="Remove" checked onclick="Checkbox(this)" class="myclass' + count + '">'+
  '   '+
  '<label id="label' + count + '" class="label' + count + '" for"chk_remove' + count + '"></label>'+
  '<input type="hidden" name="chk_remove' + count + '" value="unchecked">'+'<br>' +'<br>'


  var div_chk = "<div class='myclass"+count+"' id='div_chk"+count+"'></div>"
  var timechange_content =
  '<label>' + 'Time of change' + '</label>' + "<br>"+
  '<input type="text" name="timechange'+count+'" id="timechange'+count+'" ><br><br>'

  $("#div_to_append").append(chk_content);
  $("#div_to_append").append(div_chk);
  $("#div_chk"+count).append(timechange_content);
}

function Add_fields(count){
  var numdemes = document.getElementById("numdemes0").value;
  var num = []
  for (i=1;i<=numdemes; i++){
    num.push(i);
  };

  var columnCount = num.length;
  //created a div inside the checkbox to append the other fields
  var repeated_fields_div = '<div class="myclass' + count + '" id="repeated_fields' + count + '">'

  //creates table with num of cells = num of demes
  var deme = '<label id="demesizes_label1">Deme sizes</label><table id="demesizes_table'+count+'" class="table-striped table-hover"><tr>';

  deme1=""
  for (var i=0;i<columnCount;i++){
    var deme1 = deme1+"<td id='deme_cell"+count+"" + i + "'></td>";
  }
  var deme_content = deme + deme1 + "</tr></table><br>";

  var matr = '<label id="matr_label">Initial migration matrix</label><br><table id="matr_table'+count+'" class="table-striped table-hover"><tr>'

  $("#div_chk"+count).append(repeated_fields_div);
  $("#repeated_fields"+count).append(deme_content);
  //$("#repeated_fields"+count).append(matr_upload);
  $("#repeated_fields"+count).append(matr);



  //adds the input fields to the demesizes_table
  for (var i=0;i<columnCount;i++){
    $("#deme_cell"+count+i).append("<input type='text' value='1' id='demesizes_cell"+ count +""+'_'+"" + i + "' name='demesizes_cell"+ count +""+'_'+"" + i + "' >")
  }

  table = document.getElementById("matr_table"+count)
  for (var i=0; i<columnCount;i++){
    row=table.insertRow();
    for (var j = 0; j<columnCount; j++){
      var cell=row.insertCell();
      cell.innerHTML = "<input type='text' value='0' id='matr_cell"+count+""+'_'+""+ i +""+'_'+""+ j +"' name='matr_cell"+count+""+'_'+""+ i +""+'_'+""+ j +"'>";
    }
  }
}



function Remove_fields(){

  $("#sampvector_table").remove();
  $("#sampvector_label").remove();

  for (var i=0; i<count+1; i++){
    $("#repeated_fields"+i).remove();
  }
}


// creates and adds "deme size" field

$(document).ready(function(){
  $("#btn_repeat").on("click", function(){

    var chk0_name = document.getElementById("chk_remove0")

    if (chk0_name!=null){
      count++;
      Add_checkbox(count);
      Add_fields(count);
    }

  });


  $("#btn_ndemes").on("click", function(){
    $("#chk_hidden").remove()
    var numdemes0 = document.getElementById("numdemes0").value
    var numloci0 = document.getElementById("numloci0").value
    if ((numdemes0 === "") || (numloci0 === "")){
      alert("Fields missing")
    } else {
      var chk0_name = document.getElementById("chk_remove0")
      if (chk0_name==null){
        Add_checkbox(count);
        Add_fields(count);
      } else {
        Remove_fields();
        for (var n=0; n<count+1;n++){
          Add_fields(n);
        }
      }
      var numdemes = document.getElementById("numdemes0").value;
      var num = []
      for (i=1;i<=numdemes; i++){
        num.push(i);
      };

      var columnCount = num.length;

      //Sampling vector
      var samp= '<label id="sampvector_label">Sampling vector</label><table id="sampvector_table"class="table-striped  table-hover"><tr>';
      samp1=""
      for (var i=0;i<columnCount;i++){
        var samp1 = samp1+"<td id='samp_cell" + i + "'></td>";
        }
        var samp_content = samp + samp1 + "</tr></table>";

        $("#sampvector_div").append(samp_content);

        for (var i=0;i<columnCount;i++){
          $("#samp_cell"+i).append("<input type='text' value='0' id='samp_cell"+i+"' name='samp_cell"+i+"' >")
        }
      }


    });



});
