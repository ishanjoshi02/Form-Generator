$(document).ready(function() {
  var max_fields = 10;
  var wrapper = $(".input_fields.wrap");
  var add_button = $(".add_field_button");

  var x = 1;
  $(add_button).click(function(e){
    e.preventDefault();
    if (x < max_fields){
      x++;
      $(wrapper).append(
        '<div><input type="text" name="mytext[]"/>'
      )
    }
  });

  $(wrapper).on("click", ".remove_field", function(e){
    e.preventDefault();
    if (x > 0) {
      $(this).parent('div').remove();
      x--;
    }
  });

});
