window.onload=function(){
  $('body').append('<h1></h1>');


  $(".one").on("mouseenter", function(){
    $(".s_one").show();

    $(".one").on("mouseleave", function(){
        $(".slide").hide();
      });
  });


  $(".two").on("mouseenter", function(){
    $(".s_two").show();

    $(".two").on("mouseleave", function(){
        $(".slide").hide();
      });
  });


  $(".three").on("mouseenter", function(){
    $(".s_three").show();

    $(".three").on("mouseleave", function(){
        $(".slide").hide();
      });
  });

}
