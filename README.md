Método Fábrica

![image](https://github.com/LuizGulhermeGeron/engSoft2/assets/77393049/e8c8f709-a533-41cd-9cb8-e9d10e4d92af)


    Quando temos entidades que apresentam comportamentos semelhantes, podemos reutilizar o código de uma com a outra, em vez de refazê-lo. Para isso, uma abordagem é utilizar fábricas, classes com métodos que instanciam diferentes objetos, para que o código possa trabalhar com diferentes entidades na mesma execução.
    No exemplo dado, temos uma classe Cliente que pode dirigir um carro, mas temos várias classes de carro, então foi implementada uma classe FabricaCarros, que instancia o carro desejado, permitindo que o Cliente dirija vários carros na mesma excução.

Mediador

![image](https://github.com/LuizGulhermeGeron/engSoft2/assets/77393049/d930b8cd-520b-45c6-8bbe-d0e26d4d891c)

    Quando possuímos vários objetos que interagem diretamente um com o outro, podemos designar um novo objeto, Mediador, para centralizar todas as interações, tirando a dependência direta entre os outros objetos.
    No exemplo de código, temos alguns campos de dados que devem ser exibidos para o usuário seguindo uma lógica. Toda essa lógica foi implementada na classe MediadorViagem, chamando os campos de dados que, por sua vez, chamam métodos da classe mediadora quando os dados são inseridos, permitindo o prosseguimento da aplicação.

Proxy

![image](https://github.com/LuizGulhermeGeron/engSoft2/assets/77393049/5d1a64c2-79e1-4d5f-b83b-a05c0fae18f9)

    Quando estamos trabalhando com bibliotecas ou com programas já em funcionamento, podemos nos deparar com limitações de alguns métodos, sendo necessário adicionar comportamentos antes e depois. Para isso existem algumas opções: alterar o código da classe usada, o que nem sempre é possível, adicionar um novo método, chamando-o antes ou depois do método limitado, e criar uma classe proxy, que implementará todos os métodos da classe alvo, chamando todos os métodos originais, mas, adicionando códigos antes ou depois. Tendo em vista que alterar código é algo a ser evitado, a alternativa de substituir a classe limitada por um proxy é a melhor opção.
    No exemplo do repositório, temos uma classe BancoDeDados capaz de listar entidades, porém ela possuí um buffer que faz ela retornar dados desatualizados. Felizmente, ela também traz um método chamado limparBuffer, obrigando o retorno de dados atualizados. Para evitar a necessidade de sempre chamar limparBuffer, foi criada uma classe ProxyBancoDeDados, que implementa no método listar a chamada do método limparBuffer.


