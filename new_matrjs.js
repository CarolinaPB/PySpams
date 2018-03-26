$(document).ready(function(){
  $(".hidden_fields1").hide();
  $(".btn_repeat").click(function(){
    $(".hidden_fields1").show();
  });


});



// Goal:
//nmatr=0
//#if clicked:

//nmatr=nmatr+1
//for i in range(0,nmatr+1):
 //   file="file"+str(i)
   // timechange="timechange"+str(i)
    //demesizes="demesizes"+str(i)

//section_names=[file, timechange, demesizes]
//print section_names

  //    <div class="hidden_fields">
    //    <br><br>
      //  <label>
        //    <span >Initial migration matrix</span><br>
          //  <input name=section_names[0] type="file"/> <br>
        //</label><br>
        //<label>
          //  <span >Time of change</span><br>
           // <input name=section_names[1] type="text"/> <br>
       // </label><br>
        //<label>
         //   <span >Deme sizes</span><br>
          //  <input name=section_names[2] type="text"/> <br>
        //</label><br>
        //<button type="button"class="btn_repeat">Add matrix</button>
      //</div>
