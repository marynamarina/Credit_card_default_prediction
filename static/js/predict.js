$.ajaxSetup({
  url: '/predict',
  type: 'POST',
  dataType: 'json',
  error: function(req, text, error){
    console.error('Error: ' + text + ' | ' + error);
  },
});

$(function(){
  $('#predict-form').on('submit', function(e){
    e.preventDefault();
	$('#prediction-text').removeClass('alert-success');
	$('#prediction-text').removeClass('alert-danger');
	$('#prediction-text').addClass('d-none');
	
    var $that = $(this),
    formData = new FormData($that.get(0));
    $.ajax({
      contentType: false,
      processData: false,
      data: formData,
      success: function(data){
        if(data){
          $('#prediction-text').html(data.prediction_text);
		  $('#prediction-text').removeClass('d-none');
		  var resultClass = 'alert-danger';
		  if (data.result == 'No') {
			resultClass = 'alert-success';
		  }
		  $('#prediction-text').addClass(resultClass);
        }
      }
    });
  });
});
