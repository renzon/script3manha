$(document).ready(function () {
  var $ajaxSaveGif = $('#ajax-save-gif');
  $ajaxSaveGif.hide();
  var $precoInput = $('#preco-input');
  var $nomeInput = $('#nome-input');
  var $categoriaInput = $('#categoria-input');
  var $produtosUl = $('#produtos-ul');

  function adicionarProduto(produto) {
    var li = '<li id="li-' + produto.id + '"';
    li = li + '><button id="btn-deletar-' + produto.id + '"';
    li = li + ' class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button>';
    li = li + produto.nome + ' - ' + produto.preco + '</li>';
    $produtosUl.append(li);
    $('#btn-deletar-' + produto.id).click(function () {
      $.post('/produtos/rest/deletar', {produto_id: produto.id}, function () {
        $("#li-"+produto.id).remove();
      });
    });
  }

  $.get('/produtos/rest/listar', function (produtos) {
    $.each(produtos, function (index, p) {
      adicionarProduto(p);
    });
  });


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
    $salvarBotao.attr('disabled', 'disabled')
    $.post('/produtos/rest/salvar',
        obterInputsDeProduto(),
        function (produto) {
          $('input[type="text"]').val('');
          adicionarProduto(produto);
        }).error(function (erro) {
          for (propriedade in erro.responseJSON) {
            $('#' + propriedade + '-div').addClass('has-error');
            $('#' + propriedade + '-span').text(erro.responseJSON[propriedade]);
          }
        }).always(function () {
          $ajaxSaveGif.hide();
          $salvarBotao.removeAttr('disabled')
        });
  });

});