(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });

})(jQuery);


$('li').click(function(e) {
    $('li').removeClass('active');
    var $this = $(this);
    if (!$this.hasClass('active')) {
        $this.addClass('active');
    }
    //e.preventDefault();
});

function AjaxProcessing(btn_id){
    $('#' + btn_id).on('click', function(event) {
        $.ajax({
            data : $('#topic_list').serialize() + "&" + btn_id + "=",
            type : 'POST',
            url : '/topics',
        })
        .done(function(data) {
            if (data.error) {
            $.notifyBar({ cssClass: "error", html: "ERROR" });
            }
            else {
                refresh_topic();
            }
        });
        event.preventDefault();
    });
}
//send data to server
AjaxProcessing('homepage');
AjaxProcessing('subject_marker');
AjaxProcessing('object_marker');
AjaxProcessing('shiot_irregular');
AjaxProcessing('speech_levels');
AjaxProcessing('digeut_irregular');
AjaxProcessing('bieup_irregular');
AjaxProcessing('verb_ending_neyo');
AjaxProcessing('connecting_verbs');
AjaxProcessing('prepositions_of_place');

function refresh(){
    $.get( "/refresh", function(data) {
      $('#subject_marker').append("<a><span>" + data.all_topics[0][1] + "</span><br>" + data.all_topics[0][2] + "</a>")
      $('#object_marker').append("<a><span>" + data.all_topics[1][1] + "</span><br>" + data.all_topics[1][2] + "</a>")
      $('#shiot_irregular').append("<a><span>" + data.all_topics[2][1] + "</span><br>" + data.all_topics[2][2] + "</a>")
      $('#speech_levels').append("<a><span>" + data.all_topics[3][1] + "</span><br>" + data.all_topics[3][2] + "</a>")
      $('#digeut_irregular').append("<a><span>" + data.all_topics[4][1] + "</span><br>" + data.all_topics[4][2] + "</a>")
      $('#bieup_irregular').append("<a><span>" + data.all_topics[5][1] + "</span><br>" + data.all_topics[5][2] + "</a>")
      $('#verb_ending_neyo').append("<a><span>" + data.all_topics[6][1] + "</span><br>" + data.all_topics[6][2] + "</a>")
      $('#connecting_verbs').append("<a><span>" + data.all_topics[7][1] + "</span><br>" + data.all_topics[7][2] + "</a>")
      $('#prepositions_of_place').append("<a><span>" + data.all_topics[8][1] + "</span><br>" + data.all_topics[8][2] + "</a>")
    });
}
function refresh_topic(){
    $.get( "/topics", function(data) {
      $('#id').html(data.data[0]);
      $('#topic').html(data.data[1]);
      $('#title').html(data.data[2]);
      $('#description').html(data.data[3]);
      $('#rule1').html(data.data[4]);
      $('#rule2').html(data.data[5]);
      $('#rule3').html(data.data[6]);
      $('#rule4').html(data.data[7]);
      $('#rule5').html(data.data[8]);
      $('#rule6').html(data.data[9]);
      $('#rule7').html(data.data[10]);
      $('#rule8').html(data.data[11]);
      $('#example1').html(data.data[12]);
      $('#example2').html(data.data[13]);
      $('#example3').html(data.data[14]);
      $('#example4').html(data.data[15]);
      $('#example5').html(data.data[16]);
      $('#example6').html(data.data[17]);
      $('#example7').html(data.data[18]);
      $('#example8').html(data.data[19]);
    });
}


