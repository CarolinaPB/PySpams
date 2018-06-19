var count = 0
var div_ids = [];
var list_ids =[]

$(function(){
// show which tab is open in the navbar //
    $('a').each(function(){
        if ($(this).prop('href') == window.location.href) {
            $(this).addClass('active'); $(this).parents('li').addClass('active');
        }
    });
});

function Back() {
    window.history.back();
}

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

function Checkbox(e){
  id=$(e).attr("id")
  c = Number(id.replace("chk_remove", ''));

  if (e.checked == false){
    $("#hide_div"+c).hide();
  } else {
    $("#hide_div"+c).show();
  }
};

function Add_checkbox(c){
  div_ids.push("div_chk"+c);

  var chk_div = "<div class='myclass"+ c +"' id='div_chk"+ c +"'></div>"
  var chk = '<br><input type="checkbox" id="chk_remove' + c + '" name="chk_remove' + c + '" value="Remove" checked onclick="Checkbox(this)" class="myclass' + c + '">'
  var chk_hidden = '<input type="hidden" name="chk_remove' + c + '" value="unchecked">'+'<br>' +'<br>'
  var div_to_hide = '<div id="hide_div'+c+'"></div>'
  var chk_timechange ='<label>' + 'Time of change' + '</label>' + "<br>"+
  '<input type="text" name="timechange'+c+'" id="timechange'+c+'" ><br><br>'

  $("#div_to_append").append(chk_div)
  $("#div_chk"+c).append(chk)
  $("#div_chk"+c).append(chk_hidden)
  $("#div_chk"+c).append(div_to_hide)
  $("#hide_div"+c).append(chk_timechange)
};

function Add_demes (c, numdemes){
  var deme_div = '<div id="deme_div'+c+'"></div>'
  var deme = '<label>Deme sizes</label><table id="demesizes_table'+c+'" class="table-striped table-hover"><tr>';

  deme1=""
  for (var i=0;i<numdemes;i++){
    var deme1 = deme1+"<td id='deme_cell"+c+"" + i + "'></td>";
  }
  var deme_content = deme + deme1 + "</tr></table><br>";

  $("#hide_div"+c).append(deme_div)
  $("#deme_div"+c).append(deme_content)

  for (var i=0;i<numdemes;i++){
    $("#deme_cell"+c+i).append("<input type='text' value='1' id='demesizes_cell"+ c +""+'_'+"" + i + "' name='demesizes_cell"+ c +""+'_'+"" + i + "' >")
  }
}

function Add_modelOptions(c){
    var options ='<select id ="menu'+c+'" onchange="Matr_mode(this)"><option value="Custom" id="opt_custom'+c+'">Custom</option><option value="N-island" id="opt_island'+c+'">N-island</option></select><br><br>'

    $("#deme_div"+c).append(options)
}

function Add_matrix(c, numdemes){
  var matr_div = '<div id="matr_div'+c+'"></div>'

  var matr = '<label>Migration matrix</label><br><table id="matr_table'+c+'" class="table-striped table-hover"><tr>'

  $("#deme_div"+c).append(matr_div);
  $("#matr_div"+c).append(matr)

  table = document.getElementById("matr_table"+c)
  for (var i=0; i<numdemes;i++){
    row=table.insertRow();
    for (var j = 0; j<numdemes; j++){
      var cell=row.insertCell();
      cell.innerHTML = "<input type='text' value='0' id='matr_cell"+c+""+'_'+""+ i +""+'_'+""+ j +"' name='matr_cell"+c+""+'_'+""+ i +""+'_'+""+ j +"'>";
    }
  }
}

function Add_island(e, numdemes){
  id = $(e).attr("id")
  c = Number(id.replace("menu", ''));

  var isl_div = '<div id="isl_div'+c+'"></div>'

  var mig_rate = '<label>Migration rate</label><input type="text" name="mig_rate'+c+'" id="mig_rate'+c+'" onchange=Populate_isl(this) ><br><br>'

  var matr_isl = '<label id="matr_label'+c+'">Migration matrix</label><br><table id="matr_isl_table'+c+'" class="table-striped table-hover"><tr>'

  $("#deme_div"+c).append(isl_div)
  $("#isl_div"+c).append(mig_rate)

  $("#isl_div"+c).append(matr_isl);

  table = document.getElementById("matr_isl_table"+c)
  for (var i=0; i<numdemes;i++){
    row=table.insertRow();
    for (var j = 0; j<numdemes; j++){
      var cell=row.insertCell();
      cell.innerHTML = "<input type='text' value=0 id='matr_cell"+c+""+'_'+""+ i +""+'_'+""+ j +"' name='matr_cell"+c+""+'_'+""+ i +""+'_'+""+ j +"'>";
    }
  }

}

function Matr_mode(e){
  mode= e.value
  id = $(e).attr("id")
  var numdemes = Number(document.getElementById("numdemes0").value);
  c = Number(id.replace("menu", ''))
  if (mode == "N-island"){
    $("#matr_div"+c).remove()
    Add_island(e,numdemes)
  } else {
    $("#isl_div"+c).remove()
    Add_matrix(count, numdemes)
  }
}

function Add_fields(c, numdemes){
  Add_demes(c,numdemes)
  Add_modelOptions(c)
  Add_matrix(c, numdemes)

};

function Ndemes(){
  var numdemes = Number(document.getElementById("numdemes0").value);
  $("#chk_hidden").remove()
  var numdemes0 = document.getElementById("numdemes0").value
  var numloci0 = document.getElementById("numloci0").value

  if ((numdemes0 === "") || (numloci0 === "")){
    alert("Fields missing")
  } else {
    var chk0_name = document.getElementById("chk_remove0")

    if (chk0_name==null){
      Add_checkbox(count)
      Add_fields(count, numdemes);
    } else {
      for (var n=0; n<count+1;n++){
        $("#deme_div"+n).remove()
        Add_fields(n, numdemes)
      }

    }
  }
  document.getElementById("btn_ndemes").click();
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




$(document).ready(function(){

  $("#btn_repeat").on("click", function(){
    var numdemes = Number(document.getElementById("numdemes0").value);
    var chk0_name = document.getElementById("chk_remove0")

    if (chk0_name!=null){
      count++;
      Add_checkbox(count);
      Add_fields(count, numdemes);
    }

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
      empty ="no"
      if (document.getElementById(list_ids[i]).value ==""){
        empty = "empty"
      }
    }
    if (empty == "empty"){
      alert ("Make sure all fields are filled")
      empty="no"
    }


  });


})
