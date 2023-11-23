document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    var cpf = document.getElementById("cpf").value;
    var ativo = document.getElementById("ativo").value;
    var valor = parseFloat(document.getElementById("valor").value.replace(",", "."));
    var preco;
    switch (ativo) {
      case "PETR4":
        preco = 25.80;
        break;
      case "VALE3":
        preco = 95.25;
        break;
      case "BBAS3":
        preco = 39.45;
        break;
    }
    var resultado = document.getElementById("resultado");
    var ganhoPerda = (preco - valor) * 100 / valor;
    resultado.innerHTML = "CPF: " + cpf + "<br>" + "Ativo: " + ativo + "<br>" + "Preço: R$ " + preco.toFixed(2) + "<br>" + "Investido: R$ " + valor.toFixed(2) + "<br>" + "Ganho/Perda: " + ganhoPerda.toFixed(2) + "%";
  });
  