var count = 0
var div_ids=[]

$(function(){
// show which tab is open in the navbar //
    $('a').each(function(){
        if ($(this).prop('href') == window.location.href) {
            $(this).addClass('active'); $(this).parents('li').addClass('active');
        }
    });
});


function Reload(){
 hidden = document.getElementById("hidden_reload")
 hidden.value="Reload"
}

// checks if there are empty fields or fields with negative numbers.
// It will download the file and reload the page if all fields are filled correctly
function Validate_form(){
  var form=document.getElementById("myform");
  inputs=form.getElementsByTagName("input");
  var empty="no"
  var negative ="no"

  for (index=0; index<inputs.length; index++){
    if (inputs[index].value==null || inputs[index].value==""){
      empty="empty"
    } else if (Number(inputs[index].value)<0 ){
      negative ="negative"
    }
  }

  if (empty=="no"&& negative=="no"){

    Download()
    Reload()

  } else if (empty=="empty" || negative=="negative"){
    if (empty=="empty"){
      alert("There are empty fields")
    }
    if (negative=="negative"){
      alert("Make sure all values are ≥ 0")
    }
  }

}

function Download(){
  filename = document.getElementById("filename").value

  numdemes = Number(document.getElementById("numdemes0").value)
  var final_array= []

  if (count == 0){
    for ( i=0; i< (Math.pow(numdemes,2)+numdemes+1); i++){
      final_array.push(0)
    }
    final_array[0]="timechange0"
    for (i=0; i<numdemes; i++){
      final_array[i+1] = ("demesizes_cell0_"+i)
    }
    matr_names=[]
    for (i=0; i<numdemes; i++){
      for (n=0; n<numdemes; n++){
        matr_names.push("matr_cell0_"+i+"_"+n)
      }
    }
    a=0
    while (a< Math.pow(numdemes,2)){
      for (f=numdemes+1; f< final_array.length; f++){
        final_array[f] = matr_names[a]
        a++
      }
    }
    var num_check=1

  } else if (count > 0){

    final_array =[]
    var num_check =0
    for (i =0; i<count+1; i++){

      a=0
      if (document.getElementById("chk_remove"+i).checked){
        num_check++

        inter_array=[]
        final_array.push("timechange"+i)
        for (c=0; c<numdemes; c++){
          final_array.push("demesizes_cell"+i+"_"+c)
        }

        matr_names = []
        for (n=0; n<numdemes; n++){
          for (f=0; f<numdemes; f++){
            final_array.push("matr_cell"+i+"_"+n+"_"+f)
          }
        }

        a++

      }
    }
  }


  if (document.getElementById(final_array[0,0]).value !=0){
    alert("The first time change must be zero")

  } else {
    data_to_save=[]
    len = Math.pow(numdemes,2)+numdemes+1
    group=0
    while (group < num_check){
      if (group>0){
        data_to_save.push("\n")
      }
      data_to_save.push("# Time")
      data_to_save.push("\n")
      if (group==0){
        data_to_save.push(document.getElementById(final_array[group,0]).value)
        data_to_save.push("\n\n")
        data_to_save.push("# Deme sizes")
        data_to_save.push("\n")
        for (col = 1; col < numdemes+1; col++){
          data_to_save.push(document.getElementById(final_array[group,col]).value)
          if (col<numdemes){
            data_to_save.push(" ")
          }
        }
        data_to_save.push("\n\n")
        data_to_save.push("# Migration matrix")
        data_to_save.push("\n")
        iter = 0
        while (iter<(Math.pow(numdemes, 2))) {
          for (i=1; i<numdemes+1; i++){
            data_to_save.push(document.getElementById(final_array[group,iter+numdemes+i]).value)
            if (i<numdemes){
              data_to_save.push(" ")
            }
          }
        data_to_save.push("\n")
        iter=iter+numdemes
        }

      } else {

        data_to_save.push(document.getElementById(final_array[group,group*len]).value)
        data_to_save.push("\n\n")
        data_to_save.push("# Deme sizes")
        data_to_save.push("\n")
        for (col = group*len+1; col < group*len+numdemes+1; col++){
          data_to_save.push(document.getElementById(final_array[group,col]).value)
          if (col<group*len+numdemes){
            data_to_save.push(" ")
          }
        }
        data_to_save.push("\n\n")
        data_to_save.push("# Migration matrix")
        data_to_save.push("\n")

        iter=0
        for (n=0; n<numdemes;n++){
          for (i=Number(group*len+numdemes+1); i<Number((group+1)*len-Math.pow(numdemes, 2)+numdemes); i++){
            data_to_save.push(document.getElementById(final_array[group+1,i+iter]).value)
            if (i<Number((group+1)*len-Math.pow(numdemes, 2)+numdemes-1)){
              data_to_save.push(" ")
            }
          }
          data_to_save.push("\n")
          iter=Number(iter+numdemes)
        }

      }

      group++

    }

    data_to_save = data_to_save.join('')


    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(data_to_save));
    element.setAttribute('download', filename+".txt");

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);

  }
}

function Back() {
    window.history.back();
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
  '<input type="number" step="any" min="0" name="timechange'+c+'" id="timechange'+c+'" ><br><br>'

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
    $("#deme_cell"+c+i).append("<input type='number' step='any' min='0' value='1' id='demesizes_cell"+ c +""+'_'+"" + i + "' name='demesizes_cell"+ c +""+'_'+"" + i + "' >")
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
      cell.innerHTML = "<input type='number' step='any' min='0' value='0' id='matr_cell"+c+""+'_'+""+ i +""+'_'+""+ j +"' name='matr_cell"+c+""+'_'+""+ i +""+'_'+""+ j +"'>";
    }
  }
}

function Add_island(e, numdemes){
  id = $(e).attr("id")
  c = Number(id.replace("menu", ''));

  var isl_div = '<div id="isl_div'+c+'"></div>'

  var mig_rate = '<label>Migration rate</label><input type="number" step="any" min="0" name="mig_rate'+c+'" id="mig_rate'+c+'" onchange=Populate_isl(this) ><br><br>'

  var matr_isl = '<label id="matr_label'+c+'">Migration matrix</label><br><table id="matr_isl_table'+c+'" class="table-striped table-hover"><tr>'

  $("#deme_div"+c).append(isl_div)
  $("#isl_div"+c).append(mig_rate)

  $("#isl_div"+c).append(matr_isl);

  table = document.getElementById("matr_isl_table"+c)
  for (var i=0; i<numdemes;i++){
    row=table.insertRow();
    for (var j = 0; j<numdemes; j++){
      var cell=row.insertCell();
      cell.innerHTML = "<input type='number' step='any' min='0' value=0 id='matr_cell"+c+""+'_'+""+ i +""+'_'+""+ j +"' name='matr_cell"+c+""+'_'+""+ i +""+'_'+""+ j +"'>";
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
    Validate_form()
  });


})
