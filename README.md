# Unitrack-Backend-Flask
## Proyecto para materia sistemas distribuidos - Universidad de los llanos

Este proyecto consiste en una aplicación de Flask que utiliza microservicios para brindar información sobre los horarios de los paraderos de autobuses. La aplicación cuenta con tres endpoints diferentes que brindan información sobre los paraderos de autobuses de forma separada.

## Tabla de Contenido

- [Timetable Service: Ver horarios de paraderos](#timetable-service-ver-horarios-de-paraderos)
- [Stop-Timetable Service: Ver ID de paraderos a cierta hora](#stop-timetable-service-ver-id-de-paraderos-a-cierta-hora)
- [Stop Service: Ver información completa de paraderos](#stop-service-ver-información-completa-de-paraderos)
- [Iniciando los proyectos](#iniciando-los-proyectos)
    - [Ejecución individual](#ejecución-individual)
    - [Ejecución con docker compose](#ejecución-con-docker-compose)


## Timetable Service: Ver horarios de paraderos
Este servcio permite obtener los horarios de los paraderos de autobuses. Para utilizarlo se debe enviar una solicitud GET a la URL correspondiente y la aplicación responderá con una lista de todos los horarios disponibles para los paraderos.

## Stop-Timetable Service: Ver ID de paraderos a cierta hora
Este servicio permite a los usuarios ver los ID de los paraderos que están programados para llegar a una hora específica. Para utilizarlo se debe enviar una solicitud GET a la URL correspondiente, incluyendo el ID de la hora para la cual desean ver los ID de los paraderos. La aplicación responderá con una lista de los ID de los paraderos que están programados para llegar a esa hora. `<URL>/<ID_HORA>`

## Stop Service: Ver información completa de paraderos
Este servicio permite a los usuarios ver la información completa de una lista de paraderos, incluyendo su ID, nombre, descripción, imagen y ubicación. Para utilizarlo se debe enviar una solicitud POST a la URL correspondiente, incluyendo una lista de los ID de los paraderos que desean ver. La aplicación responderá con la información completa de los paraderos correspondientes.

```
{
  "stops": [1, 2, 3, ...]
}
```

## Iniciando los Proyectos

Para iniciar los proyectos en este repositorio, deberá tener Python instalado en su máquina si desea ejecutarlos manualmente o puede usar el archivo `docker-compose.yml` incluido.

### Ejecución individual

Primero deberá instalar las dependencias para cada proyecto ejecutando `pip install -r requirements.txt` en el directorio raíz de cada proyecto. 

Además debe crear un archivo `.env` con las variables que estan en `.env.example` para cada uno y tambien crear la base de datos (se incluyen los scripts en el repositorio).

Para iniciar cualquier proyecto, navegue hasta el directorio del mismo y ejecute el siguiente comando:

```markdown
> cd <DIRECTORIO_PROYECTO>
> python run.py
```

### Ejecución con docker compose

Debe tener instalado docker y docker compose en su máquina. Además, debe crear un archivo `.env` con las variables que estan en `.env.example` para cada proyecto y asignar como host de la base de datos la `IP` de su máquina, como puerto `9091` y como usuario y contraseña `admin` (estos valores están establecidos en el archivo `docker-compose.yml` y puede cambiarlos si desea). 

Una vez realizado lo anterio, navegue hasta el directorio del repositorio y ejecute este comando:

```markdown
> cd <DIRECTORIO_REPOSITORIO>
> docker-compose up --build
```
