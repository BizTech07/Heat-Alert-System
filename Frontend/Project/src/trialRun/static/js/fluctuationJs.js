$(document).ready(function () {
    $.datepicker.setDefaults({
      dateFormat: 'yy-mm-dd'
    });
    $(function () {
      $("#From").datepicker();
      $("#to").datepicker();
    });
    $('#range').click(function () {
      var From = $('#From').val();
      var to = $('#to').val();
      if (From != '' && to != '') {
        $.ajax({
          url: "/range",
          method: "POST",
          data: { From: From, to: to },
          success: function (data) {
            $('#panel_generation_table').html(data);
            $('#panel_generation_table').append(data.htmlresponse);
          }
        });
      }
      else {
        alert("Please Select the Date");
      }
    });
  });
  // Code goes here