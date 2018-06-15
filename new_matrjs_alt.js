var count = 0;
var div_ids = [];
var list_ids =[]

$(function(){
    $('a').each(function(){
        if ($(this).prop('href') == window.location.href) {
            $(this).addClass('active'); $(this).parents('li').addClass('active');
        }
    });
});

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

function Makelist (count){
  chk_list = []
  var numdemes = document.getElementById("numdemes0").value;

  for (i=0; i<=count; i++){
    var matr_names =[]
    chk_list.push("chk_remove"+i);
    var chk_state = document.getElementById(chk_list[i]).checked;
    if ( chk_state== true){

      list_ids.push("timechange"+i)
      for (n=0; n< numdemes; n++){
        list_ids.push("demesizes_cell"+i+"_"+n)
        for (k=0;k<numdemes;k++){
          matr_names.push("matr_cell"+i+"_"+n+"_"+k)
        }
      }
      for (b=0;b<matr_names.length;b++){
        list_ids.push(matr_names[b])
      }
    }
  }
}

function Add_checkbox(count){

  div_ids.push("div_chk"+count); //list with ids of all the new div

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

function Add_matr(count){
  var numdemes = Number(document.getElementById("numdemes0").value)

  var matr_div = '<div id="matr_div'+count+'"></div>'

  var matr = '<label id="matr_label'+count+'">Migration matrix</label><br><table id="matr_table'+count+'" class="table-striped table-hover"><tr>'

  $("#repeated_fields"+count).append(matr_div);
  $("#matr_div"+count).append(matr)

  table = document.getElementById("matr_table"+count)
  for (var i=0; i<numdemes;i++){
    row=table.insertRow();
    for (var j = 0; j<numdemes; j++){
      var cell=row.insertCell();
      cell.innerHTML = "<input type='text' value='0' id='matr_cell"+count+""+'_'+""+ i +""+'_'+""+ j +"' name='matr_cell"+count+""+'_'+""+ i +""+'_'+""+ j +"'>";
    }
  }
}

function Add_fields(count){
  var numdemes = Number(document.getElementById("numdemes0").value)

  //created a div inside the checkbox to append the other fields
  var repeated_fields_div = '<div class="myclass' + count + '" id="repeated_fields' + count + '">'

  //creates table with num of cells = num of demes
  var deme = '<label id="demesizes_label1">Deme sizes</label><table id="demesizes_table'+count+'" class="table-striped table-hover"><tr>';

  deme1=""
  for (var i=0;i<numdemes;i++){
    var deme1 = deme1+"<td id='deme_cell"+count+"" + i + "'></td>";
  }
  var deme_content = deme + deme1 + "</tr></table><br>";

  var options ='<select id ="dd_menu'+count+'" onchange="Add_island(this)"><option value="Custom" id="opt_custom'+count+'">Custom</option><option value="N-island" id="opt_island'+count+'">N-island</option></select><br><br>'



  $("#div_chk"+count).append(repeated_fields_div);
  $("#repeated_fields"+count).append(deme_content);
  $("#repeated_fields"+count).append(options);


  //adds the input fields to the demesizes_table
  for (var i=0;i<numdemes;i++){
    $("#deme_cell"+count+i).append("<input type='text' value='1' id='demesizes_cell"+ count +""+'_'+"" + i + "' name='demesizes_cell"+ count +""+'_'+"" + i + "' >")
  }

  Add_matr(count)


}

function Populate_isl(e){
  var numdemes = Number(document.getElementById("numdemes0").value)


  mig_rate=$(e).attr("id")
  this_count = Number(mig_rate.replace("mig_rate",''));

  mig_rate_id= "mig_rate"+this_count

  mig_rate_val = document.getElementById(mig_rate_id).value

  var cell_val = mig_rate_val/(numdemes-1)

  for (i=0; i<=this_count; i++){
    cell_names=[]
    diagcell_names=[]
    for (n=0; n< numdemes; n++){
      for (k=0;k<numdemes;k++){
        cell_names.push("matr_cell"+i+"_"+n+"_"+k)
        if (n==k){
          diagcell_names.push("matr_cell"+i+"_"+n+"_"+k)
        }
      }
    }
  }


  for (i=0; i<cell_names.length;i++){
    document.getElementById(cell_names[i]).value = cell_val
  }
  for (i=0; i<diagcell_names.length;i++){
    document.getElementById(diagcell_names[i]).value = 0
  }


}


function Add_island(e){
  dd_menu=$(e).attr("id")

  this_count = Number(dd_menu.replace("dd_menu",''));


  var ddm = document.getElementById(dd_menu);
  var ddm_value = ddm.options[ddm.selectedIndex].value;
    if(ddm_value == "N-island"){

      $("#matr_div"+this_count).remove()

      var numdemes = Number(document.getElementById("numdemes0").value)

      var isl_div = '<div id="isl_div'+this_count+'"></div>'

      var mig_rate = '<label id= "mig_rate_label'+this_count+'">Migration rate</label><input type="text" name="mig_rate'+this_count+'" id="mig_rate'+this_count+'" onchange=Populate_isl(this) ><br><br>'

      var matr_isl = '<label id="matr_label'+this_count+'">Migration matrix</label><br><table id="matr_isl_table'+count+'" class="table-striped table-hover"><tr>'

      $("#repeated_fields"+this_count).append(isl_div)
      $("#isl_div"+this_count).append(mig_rate)

      $("#isl_div"+this_count).append(matr_isl);

      table = document.getElementById("matr_isl_table"+count)
      for (var i=0; i<numdemes;i++){
        row=table.insertRow();
        for (var j = 0; j<numdemes; j++){
          var cell=row.insertCell();
          cell.innerHTML = "<input type='text' value=0 id='matr_cell"+count+""+'_'+""+ i +""+'_'+""+ j +"' name='matr_cell"+count+""+'_'+""+ i +""+'_'+""+ j +"'>";
        }
      }


    }else {
      $("#isl_div"+this_count).remove();

      Add_matr(this_count);
    }

}




function Remove_fields(){

  $("#sampvector_table").remove();
  $("#sampvector_label").remove();

  for (var i=0; i<count+1; i++){
    $("#repeated_fields"+i).remove();
  }
}



function Ndemes(){
  $("#chk_hidden").remove()
  var numdemes0 = document.getElementById("numdemes0").value
  var numloci0 = document.getElementById("numloci0").value
  if ((numdemes0 === "") || (numloci0 === "")){
    alert("Fields missing")
  } else {
    var chk0_name = document.getElementById("chk_remove0")
    if (chk0_name==null){ //if this will be the first input group added
      Add_checkbox(count);
      Add_fields(count);
    } else {
      Remove_fields();
      for (var n=0; n<count+1;n++){
        Add_fields(n);
      }
    }
    var numdemes = Number(document.getElementById("numdemes0").value)

    var samp= '<label id="sampvector_label">Sampling vector</label><table id="sampvector_table"class="table-striped  table-hover"><tr>';
    samp1=""
    for (var i=0;i<numdemes;i++){
      var samp1 = samp1+"<td id='samp_cell" + i + "'></td>";
      }
      var samp_content = samp + samp1 + "</tr></table>";

      $("#sampvector_div").append(samp_content);

      for (var i=0;i<numdemes;i++){
        $("#samp_cell"+i).append("<input type='text' value='0' id='samp_cell"+i+"' name='samp_cell"+i+"' >")
      }
      document.getElementById("btn_ndemes").click();
    }
}



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
    Ndemes()

  });


  $("#btn_save").on("click", function(){
    Makelist(count);
    if (document.getElementById(list_ids[0]).value != "0"){
      alert("The first time change must be zero")
    }
    for (i=0; i<list_ids.length; i++){
      if (document.getElementById(list_ids[i]).value < 0){
        var negative = 0
      }

    }
    if (negative != null){
      alert("Make sure all values are ≥ 0")
    }
    for (i=0; i<list_ids.length; i++){
      if (document.getElementById(list_ids[i]).value ==""){
        empty = "empty"
      }
    }
    if (empty != null){
      alert ("Make sure all fields are filled")
    }

    //document.getElementById("form").reset()

  });
});
