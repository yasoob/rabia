$('#mygallery').justifiedGallery({
  lastRow : 'justify', 
  rowHeight : 280, 
  rel : 'gallery2',
  margins : 10
}).on('jg.complete', function () {
    $('#mygallery a').swipebox();
});

$('#mygallery img').hover(function(){
	$('#mygallery img').css("opacity",".3");
	$(this).css("opacity","1");
}, function(){
	$('#mygallery img').css("opacity","1");
});