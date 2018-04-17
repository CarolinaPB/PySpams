section_names=["file", "timechange", "demesizes"];
sections_label=["Initial migration matrix","Time of change","Deme sizes"];



$(document).ready(function(){
  var button = document.getElementById('btn_repeat');
    count=0;
  button.onclick = function(){
    count += 1;
  };

  $("#btn_repeat").click(function(){
    console.log("count is "+count)

    //create labels
    var makelabel = document.createElement("label");

    //create spans
    var sect_labels0 = document.createTextNode(sections_label[0]);
    var sect_labels1 = document.createTextNode(sections_label[1]);
    var sect_labels2 = document.createTextNode(sections_label[2]);

    //create input elements type="file"
    var makeinput_file = document.createElement("input");
    makeinput_file.className="fields_to_repeat";
    makeinput_file.setAttribute("class", "fields_to_repeat")
    makeinput_file.setAttribute("id", section_names[0]+count);
    makeinput_file.setAttribute("name", section_names[0]+count);
    makeinput_file.setAttribute("type", "file");

    //create input elements type="text"
    var makeinput1 = document.createElement("input");
    makeinput1.className="fields_to_repeat";
    makeinput1.setAttribute("class", "fields_to_repeat");
    makeinput1.setAttribute("id", section_names[1]+count);
    makeinput1.setAttribute("name", section_names[1]+count);
    makeinput1.setAttribute("type", "text");

    var makeinput2 = document.createElement("input");
    makeinput2.className="fields_to_repeat";
    makeinput2.setAttribute("class", "fields_to_repeat");
    makeinput2.setAttribute("id", section_names[2]+count);
    makeinput2.setAttribute("name", section_names[2]+count);
    makeinput2.setAttribute("type", "text");

    //create line break
    var br = document.createElement("br");
    var br2 = document.createElement("br");
    var br3 = document.createElement("br");
    var br4 = document.createElement("br");
    var br5 = document.createElement("br");
    var br6 = document.createElement("br");

    //append to parent div

    makelabel.appendChild(sect_labels0);
    makelabel.appendChild(br);
    makelabel.appendChild(makeinput_file);
    makelabel.appendChild(br2);
    makelabel.appendChild(br3);
    makelabel.appendChild(br4);
    makelabel.appendChild(sect_labels1);
    makelabel.appendChild(makeinput1);
    makelabel.appendChild(br5);
    makelabel.appendChild(br6);
    makelabel.appendChild(sect_labels2);
    makelabel.appendChild(makeinput2);

    $(".repeated_fields").append(makelabel);
  });

});
