# FastAPI Project

API desenvolvida para exemplificar criação e configuração de uma API utilizando FastAPI.

## Documentação da API

#### Retorna todos os itens

```http
  POST /api/auth
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Obrigatório**. O nickname do usuário |
| `password` | `string` | **Obrigatório**. A senha do usuário |

#### Retorna um item

```http
  GET /api/clients
```

## Instalação/Inicialização

Instale projeto com pip3

```bash
  pip3 install -r requirements.txt
  make run ou python3 app/main.py
```
    
## Licença
[MIT](https://choosealicense.com/licenses/mit/)


## Autores
- [@guizaramellaf91](https://github.com/guizaramellaf91)
