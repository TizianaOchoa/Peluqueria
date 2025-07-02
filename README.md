# 💈 Sistema de Turnos para Peluquería

Actividad: 11/06-25/06

Alumna:Ochoa Tiziana

Este proyecto es una aplicación web desarrollada en Python con Flask que permite gestionar turnos en una peluquería de forma sencilla. El sistema permite registrar clientes, agendar turnos, consultar el cronograma y ver los turnos futuros por cliente.

---

## 🚀 Características

- Registro de clientes
- Reserva de turnos (fecha y hora)
- Visualización de turnos agendados (administrador)
- Consulta de turnos futuros por cliente

---

## ✅ Historias de Usuario y Criterios de Aceptación

### 🧍 1. Registrar Cliente

- **Como** cliente  
- **Quiero** registrar mi nombre y contacto  
- **Para** poder reservar un turno en la peluquería  

#### 🎯 Criterios de Aceptación

- **Dado** que soy un nuevo cliente  
- **Cuando** ingreso mi nombre y contacto  
- **Entonces** el sistema debe guardar mi información correctamente  

---

### 📅 2. Reservar Turno

- **Como** cliente  
- **Quiero** reservar un turno especificando fecha y hora  
- **Para** poder atenderme en la peluquería en un horario conveniente  

#### 🎯 Criterios de Aceptación

- **Dado** que soy un cliente registrado  
- **Cuando** ingreso una fecha y hora válida  
- **Entonces** el sistema debe crear el turno y asociarlo a mi cuenta  

---

### 📋 3. Listar Turnos Agendados

- **Como** administrador  
- **Quiero** listar todos los turnos agendados  
- **Para** poder visualizar el cronograma de la peluquería y organizar el personal  

#### 🎯 Criterios de Aceptación

- **Dado** que soy administrador  
- **Cuando** solicito la lista de turnos  
- **Entonces** el sistema debe mostrarme todos los turnos ordenados por fecha y hora  

---

### 🔍 4. Ver Mis Turnos Futuros

- **Como** cliente  
- **Quiero** ver mis turnos futuros  
- **Para** poder organizarme mejor y no perder ninguna cita  

#### 🎯 Criterios de Aceptación

- **Dado** que soy cliente  
- **Cuando** solicito mis turnos con mi ID  
- **Entonces** el sistema debe mostrarme solo los turnos futuros asociados  

---

## 🧪 Requisitos

- Python 3.7 o superior
- Flask

---

## ⚙️ Instalación

```bash
pip install flask

## Imagen

![Captura de pantalla (57)](https://github.com/user-attachments/assets/024f85f5-d352-4969-901b-160dfa802dee)
![Captura de pantalla (58)](https://github.com/user-attachments/assets/119930bc-e418-49d7-8973-34897aa08ce3)


