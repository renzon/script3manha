$(document).ready(function () {
  var $ajaxSaveGif = $('#ajax-save-gif');
  $ajaxSaveGif.hide();
  var $precoInput = $('#preco-input');
  var $nomeInput = $('#nome-input');
  var $categoriaInput = $('#categoria-input');

  function obterInputsDeProduto() {
    return {
      'preco': $precoInput.val(),
      'nome': $nomeInput.val(),
      'categoria': $categoriaInput.val()
    };
  }

  var $salvarBotao = $('#salvar-btn');
  $salvarBotao.click(function () {
    $('.has-error').removeClass('has-error');
    $('.help-block').empty();
    $ajaxSaveGif.fadeIn();
    $salvarBotao.attr('disabled','disabled')
    $.post('/produtos/rest/salvar',
        obterInputsDeProduto(),
        function (produto) {
          $('input[type="text"]').val('');
        }).error(function(erro){
          for (propriedade in erro.responseJSON){
            $('#'+propriedade+'-div').addClass('has-error');
            $('#'+propriedade+'-span').text(erro.responseJSON[propriedade]);
          }
        }).always(function(){
          $ajaxSaveGif.hide();
          $salvarBotao.removeAttr('disabled')
        });
  });

});