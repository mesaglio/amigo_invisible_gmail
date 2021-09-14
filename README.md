# Amigo invisible

## Requisitos

- Python > 3.9.5

- Cuenta de google con [acceso de apps menos seguras](https://support.google.com/accounts/answer/6010255?authuser=1&p=less-secure-apps&hl=es-419&authuser=1&visit_id=637671846266755528-80277445&rd=1)

- Datos de los jugadores

Ejemplo de datos:

data.json:

```json
[
  { "name": "Eve", "email": "eve@gmail.com" },
  { "name": "Nico", "email": "nico@gmail.com" },
  { "name": "Juan", "email": "juan@gmail.com" },
  { "name": "Mati", "email": "mati@gmail.com" }
]
```

## Para ejecutar

```bash
$ python3 main.py
> Email sender account:
> Email sender password:
```

## TODO:

- Eliminar los mails de la casilla de enviados.
