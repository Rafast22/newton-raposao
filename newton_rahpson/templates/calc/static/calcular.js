var mathFieldSpan = document.getElementById('math-field');
var MQ = MathQuill.getInterface(2); 
var mathField = MQ.MathField(mathFieldSpan, {
  spaceBehavesLikeTab: true,   
// Permite usar a tecla espaço como Tab
  leftRightIntoCmdGoes: 'up', // Move o cursor para cima/baixo ao usar as teclas de seta
  restrictMismatchedBrackets: true, // Impede a inserção de parênteses/colchetes incompatíveis
  supSubsRequireOperand: true, // Requer um operando antes de inserir sobrescritos/subscritos
  autoCommands: 'pi theta sqrt sum prod alpha beta gamma delta epsilon zeta eta', // Comandos que podem ser inseridos digitando seus nomes
  autoOperatorNames: 'sin cos tan arcsin arccos arctan ln log', // Operadores que podem ser inseridos digitando seus nomes
  handlers: {
    edit: function() { 
      // Aqui você pode adicionar código para lidar com as edições no campo, se necessário
    }
  }
});
var keyboardButtons = document.querySelectorAll('#math-keyboard button');
var keyboard = document.querySelectorAll('#symbols button');
var numpad = document.querySelectorAll("#math-numpad button")
keyboardButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    var latex = this.getAttribute('data-latex');
    mathField.write(latex);
    mathField.focus(); 
  });
});
keyboard.forEach(function(button) {
  button.addEventListener('click', function() {
    var latex = this.getAttribute('data-latex');
    mathField.write(latex);
    mathField.focus(); 
  });
});

