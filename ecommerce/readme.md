# DJANGO API REST - GRUPO 5

## PASOS PARA LEVANTAR PROYECTO

* Instalar __*requirimientos*__

  `$ pip install -r requirements.txt`
* Hacer las migraciones de la base de datos

  `$ python manage.py makemigrations`

  `$ python manage.py migrate`

* Levantar servidor

    `$ python manage.py runserver`

## NUESTRO DIAGRAM DE CLASES

![Diagrama_de_clases _del_e-commerce](https://github.com/franciscolmos/API-REST-DJANGO/blob/dev/ecommerce/assets/Diagrama_de_clases_ecommerce.png)

## COMO PROBAR LOS ENDPOINTS

* Importar la siguiente coleccion de request
  * [DJANO-API-REST-POSTMAN-COLLECTION](https://github.com/franciscolmos/API-REST-DJANGO/blob/dev/ecommerce/assets/API-REST-DJANGO.postman_collection.json)
* Agregar el siguiente LOCAL environment
  ![LOCAL_ENVIRONMENTS](https://github.com/franciscolmos/API-REST-DJANGO/blob/dev/ecommerce/assets/LOCAL_ENVIRONMENT.png)

## USUARIOS
* __*ROOT*__
  * user_name: r00t@test.com
  * password: r00t
  
* __*TEST USERS:*__
  * __*TEST1*__
    * user_name: francisco@test.com
    * password: fr4nc1sc0
  * __*TEST2*__
    * user_name: benjamin@test.com
    * password: test123
  * __*TEST3*__
    * user_name: felipe@test.com
    * password: felipe

## COMO EJECUTAR LOS TEST

`$ python3 manage.py test carts_api.tests.ProductTest`

  
 