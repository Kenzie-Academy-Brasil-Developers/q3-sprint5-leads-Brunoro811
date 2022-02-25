# Leads



## Enpoints
### POST /leads 
  A rota deve é capaz de registrar um novo Lead no banco de dados.
  #### Modelo de requisição:
  ```bash
  {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
}  
  ```
   #### Modelo de resposta:
   os campos creation_date, last_visit e visits são preenchidos automaticamente.
  ```bash
 {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
    "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
    "visits": 1
}  
  ```
### GET /leads 
  A rota busca todos os LEADS por ordem de visitas, do maior para o menor.
  #### Modelo de requisição:
  ```GET - localhost:5000/leads``` sem body.


### PATH /leads 
  A cada requisição o campo visits acresceta 1 automaticamente.
  A cada requisição o campo last_visit é atualizado automaticamente.
  
  O email do Lead é utilizado para encontrar o registro a ser atualizado.
  #### Modelo de requisição:
  ```bash
 {
    "email": "john@email.com"
}  
  ```
  #### Modelo de resposta é vazio.


### DELETE /leads 
  A rota deleta um Lead específico. O email do Lead deve ser utilizado para encontrar o registro a ser deletado.
  
  O email do Lead é utilizado para encontrar o registro a ser atualizado.
  #### Modelo de requisição:
  ```bash
 {
    "email": "john@email.com"
}  
  ```
   #### Modelo de resposta é vazio.
