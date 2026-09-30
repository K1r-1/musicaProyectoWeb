# musicaProyectoWeb
Repositorio Proyecto Web

INVESTIGACIÓN

E1 

1. Estrategias

¿Qué formas existen de combinar React con Django? 

(a) React como aplicación independiente que consume la API
Tanto React como Django funcionan independientemente una de la otra. React gestiona todo lo que es interfaz y enrutamiento como una SPA (Single-page app) de forma dinámica. Django actúa como una API que envía datos en formato JSON ante peticiones HTTP, permitiendo una comunicación más efectiva.

https://react.dev/learn/build-a-react-app-from-scratch#data-fetching
https://docs.djangoproject.com/en/6.1/ref/request-response/

(b) Django sirviendo el build de React
React se compila mediante npm run build lo que genera un conjunto de archivos optimizados para un servicio de hosting estático. En este contexto, Django se configura para servir los archivos estáticos, actuando como un servidor web que entrega los recursos estáticos como un paquete preconstruido al navegador.

https://vite.dev/guide/build
https://docs.djangoproject.com/en/6.1/howto/static-files/deployment/

(c) Plantillas de Django con React embebido
En este contexto React no actúa como una SPA sino que sus componentes son inyectados en las vistas de servidor de Django. Django-Vite es una integración que permite generar esta conexión en la que React está embebido en las plantillas de Django mediante template tags que se introducen en el HTML. 


https://vite.dev/guide/backend-integration
https://pypi.org/project/django-vite/

2. Desarrollo

El origen de una página es la combinación de protocolo, dominio y el puerto. 
Sitios que coinciden en esta combinación son del mismo origen. Si alguno de estos es diferente se le considera de origen distinto.

La política de mismo origen es un mecanismo de seguridad que restringe como un documento o script cargado desde un origen interactúa con recursos de otro origen evitando posibles manipulación o lectura no deseadas.

Dado que Django y React utilizan puertos distintos (8000 y 5173). Al momento de realizar una petición HTTP hacia la API, el navegador se encarga de revisar el origen y dado que los puertos difieren, se bloquea la lectura de la respuesta. 


https://developer.mozilla.org/en-US/docs/Glossary/Origin
https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy


