$(document).ready(function(){
  var $busca = $('#busca');
  var $chatTxt = $('#chat-txt');
  var $chatUl = $('#chat-ul');
  $('#jq').click(function(){
    $busca.slideToggle();
  });

  $('#jq2').click(function(){
    $busca.empty();
  });

  $('#chat-btn').click(function(){
    var msg = $chatTxt.val();
    $chatTxt.val('');

    var li='<li>'+msg+'</li>'
    $chatUl.fadeOut({duration: 400, 'complete':function(){
      $chatUl.fadeIn(500);
    }});
    $chatUl.prepend(li);
  });
});