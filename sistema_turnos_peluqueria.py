# sistema_turnos_peluqueria.py
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Datos en memoria
clientes = []
turnos = []

# ------------------------------
# Historia de Usuario 1: Registrar Cliente
# ------------------------------
# Como cliente,
# Quiero registrar mi nombre y contacto
# Para poder reservar un turno
#
# Criterios de Aceptación:
# Dado que soy un nuevo cliente
# Cuando ingreso mi nombre y contacto
# Entonces el sistema debe guardar mi información correctamente

@app.route('/registrar_cliente', methods=['POST'])
def registrar_cliente():
    data = request.json
    nombre = data.get('nombre')
    contacto = data.get('contacto')

    if not nombre or not contacto:
        return jsonify({'error': 'Faltan datos: nombre y contacto son requeridos.'}), 400

    cliente = {
        'id': len(clientes) + 1,
        'nombre': nombre.strip(),
        'contacto': contacto.strip()
    }

    clientes.append(cliente)

    return jsonify({
        'mensaje': 'Cliente registrado con éxito',
        'cliente': cliente
    }), 201


# ------------------------------
# Historia de Usuario 2: Reservar Turno
# ------------------------------
# Como cliente,
# Quiero reservar un turno especificando fecha y hora
# Para poder atenderme en la peluquería
#
# Criterios de Aceptación:
# Dado que soy un cliente registrado
# Cuando ingreso una fecha y hora válida
# Entonces el sistema debe crear el turno y asociarlo a mi cuenta

@app.route('/reservar_turno', methods=['POST'])
def reservar_turno():
    data = request.json
    cliente_id = data.get('cliente_id')
    fecha_str = data.get('fecha')  # formato esperado: "2025-07-10 14:00"

    if not cliente_id or not fecha_str:
        return jsonify({'error': 'cliente_id y fecha son obligatorios'}), 400

    cliente = next((c for c in clientes if c['id'] == cliente_id), None)
    if not cliente:
        return jsonify({'error': 'Cliente no encontrado'}), 404

    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return jsonify({'error': 'Formato de fecha inválido. Use YYYY-MM-DD HH:MM'}), 400

    turno = {
        'id': len(turnos) + 1,
        'cliente_id': cliente_id,
        'fecha': fecha.strftime("%Y-%m-%d %H:%M")
    }

    turnos.append(turno)

    return jsonify({
        'mensaje': 'Turno reservado con éxito',
        'turno': turno
    }), 201


# ------------------------------
# Historia de Usuario 3: Listar Todos los Turnos
# ------------------------------
# Como administrador,
# Quiero listar todos los turnos agendados
# Para poder ver el cronograma
#
# Criterios de Aceptación:
# Dado que soy administrador
# Cuando solicito la lista de turnos
# Entonces el sistema debe mostrarme todos los turnos ordenados por fecha y hora

@app.route('/listar_turnos', methods=['GET'])
def listar_turnos():
    turnos_ordenados = sorted(turnos, key=lambda x: x['fecha'])
    lista = []

    for turno in turnos_ordenados:
        cliente = next((c for c in clientes if c['id'] == turno['cliente_id']), None)
        if cliente:
            lista.append({
                'Turno ID': turno['id'],
                'Cliente': cliente['nombre'],
                'Contacto': cliente['contacto'],
                'Fecha': turno['fecha']
            })

    return jsonify(lista), 200


# ------------------------------
# Historia de Usuario 4: Ver Turnos Futuros del Cliente
# ------------------------------
# Como cliente,
# Quiero ver mis turnos futuros
# Para poder organizarme mejor
#
# Criterios de Aceptación:
# Dado que soy cliente
# Cuando solicito mis turnos con mi ID
# Entonces el sistema debe mostrarme solo los turnos futuros asociados

@app.route('/turnos_cliente/<int:cliente_id>', methods=['GET'])
def turnos_cliente(cliente_id):
    ahora = datetime.now()
    futuros = []

    for turno in turnos:
        if turno['cliente_id'] == cliente_id:
            fecha_turno = datetime.strptime(turno['fecha'], "%Y-%m-%d %H:%M")
            if fecha_turno > ahora:
                futuros.append(turno)

    futuros_ordenados = sorted(futuros, key=lambda x: x['fecha'])

    return jsonify(futuros_ordenados), 200


# ------------------------------
# Main
# ------------------------------
if __name__ == '__main__':
    print("Sistema de Turnos para Peluquería corriendo en http://127.0.0.1:5000")
    app.run(debug=True)
