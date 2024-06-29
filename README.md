# proyecto-sie

Repositorio para el proyecto del curso de Sistemas de Inteligencia Empresarial del ciclo 2024-1 en la carrera de Ingeniería de Sistemas.
<p align="center">
  <img src="https://www.ulima.edu.pe/sites/default/files/styles/600x300/public/news/img/escudo_600x300-01_1.jpg?itok=0_61sHmS"/>
</p>

Grupo 4 - Integrantes:
- Jesu Amoretti
- Cesar Lujan
- Fabrizio Romero
- Gerson Oviedo
- Erick Valderrama
<!-- - Frank Tapia Aquino o7 -->

---

## Schema
![](./images/schema.png)

## Schema SSIS
![](./images/ssis.png)

## Quickstart
1. Crear una base de datos SQL Server con los siguientes parámetros: 
- User: sa
- Password: ul1m4@2024$1

2. Cargar el [script inicial](./seeders/initital_script.sql) para crear las dimensiones en la instancia SQL Server

3. Abrir la solución del [proyecto](./proyecto-etl/proyecto-etl.sln) con Visual Studio 2022 (SSIS)

4. Configurar las siguientes conexiones:
- OLEDB para SQL Server:
  - Usar la base datos SQL Server previamente creada

- OLEDB para Excel
  - Clic derecho en bucle for each > Editar > Colección > Conexión > Nueva Conexión > Nueva...
  - Proveedores .NET de OLEDB > Microsoft Office 16.0 Access Database Engine...
    - Pegar la ruta del excel de [OLTP_VENTAS](./static/cleansing_laos_ventas_2024.xlsx) y aceptar
  - Verificar si la variable SheetName ha sido asignada con el valor "2"

- Conexiones con Excel
  - [Excel de OLTP_VENTAS](./static/cleansing_laos_ventas_2024.xlsx)
  - [Excel de DIM_FECHA](./seeders/dim_fecha.xlsx)
  - [Excel de DIM_HORA](./seeders/dim_hora.xlsx)

- Conexiones de texto plano
  - [ERROR_CATEGORIA](./logs/error_categoria.txt)
  - [ERROR_CLIENTE](./logs/error_cliente.txt)
  - [ERROR_PROMOTOR](./logs/error_promotor.txt)
  - [ERROR_TIPOPAGO](./logs/error_tipopago.txt)

5. Ejecutar el proyecto.