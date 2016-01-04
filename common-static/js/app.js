$('#mygallery').justifiedGallery({
  lastRow : 'justify', 
  rowHeight : 220, 
  rel : 'gallery2',
  margins : 3
}).on('jg.complete', function () {
    $('#mygallery a').swipebox();
});
