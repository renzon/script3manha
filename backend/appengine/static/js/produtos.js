var olaMundo = function olaMundo(){
  console.log('Olá Mundo');

}

olaMundo();

var outro= olaMundo;

outro();

olaMundo= 'blah';

outro();

console.log(olaMundo);

function executadorDeFuncao(fcn){
  fcn('Executador de funcao');
}

function blah1(str){
  console.log(str+' blah1');
}

function blah2(str){
  console.log(str+' blah2');
}

executadorDeFuncao(blah1);
executadorDeFuncao(blah2);

function derivar(fcn){
  var deltax=0.0000000001;
  function derivada(x){
    return (fcn(x+deltax)-fcn(x))/deltax;
  }

  return derivada;
}

function reta(x){
  return x;
}

function parabola(x){
  return x*x;
}

var parabolaDerivada=derivar(parabola);

console.log(parabolaDerivada(1));
console.log(parabolaDerivada(2));

//var retaTransladada=derivar(reta);
//
//console.log(retaTransladada(1));
//console.log(retaTransladada(2));