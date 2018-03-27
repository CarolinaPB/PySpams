section_names=["file", "timechange", "demesizes"]
sections_label=["Initial migration matrix","Time of change","Deme sizes"]

$(document).ready(function(){
  $("#btn_repeat").click(function(){

    //function clickCounter() {
      //  if(typeof(Storage) !== "undefined") {
        //    if (localStorage.clickcount) {
          //      localStorage.clickcount = Number(localStorage.clickcount)+1;
           // } else {
             //   localStorage.clickcount = 1;
            //}
        //}
    //}
    //console.log(localStorage.clickcount);

    for (i=0;i<section_names.length; i++) {

      //create labels
      var makelabel = document.createElement("label");

      //create spans
      var spans = document.createElement("span");
      var sect_labels = document.createTextNode(sections_label[i]);
      spans.appendChild(sect_labels);

      //create input elements type="text"
      var makeinput = document.createElement("input");
      makeinput.className="fields_to_repeat";
      makeinput.setAttribute("class", "fields_to_repeat");
      makeinput.setAttribute("id", section_names[i]+i);
      makeinput.setAttribute("name", section_names[i]+i)
      makeinput.setAttribute("type", "text");

      //create input elements type="file"
      var makeinput_file = document.createElement("input");
      makeinput_file.className="fields_to_repeat";
      makeinput_file.setAttribute("class", "fields_to_repeat")
      makeinput_file.setAttribute("id", section_names[0]+1);
      makeinput_file.setAttribute("name", section_names[i]+i)
      makeinput_file.setAttribute("type", "file")

      //create line break
      var br = document.createElement("br")

      //append to parent div
      makelabel.appendChild(spans);
      makelabel.appendChild(makeinput);

      $("#fields_to_repeat").append(makelabel);
      $(makelabel).after(br);

    }
    $("#fields_to_repeat").append(makeinput_file);
  });
});
