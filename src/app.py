#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
import time
from algorithm import calculate_patterns

app = Flask(__name__)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger"
}

swagger_template = {
    "info": {
        "title": "Ogathon Challenges API",
        "description": "API para resolver reto 1",
        "version": "1.0.0",
    },
    "schemes": ["http"],
    "tags": [
        {
            "name": "Reto",
            "description": "Endpoints para resolver Reto 1"
        }
    ]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

@app.route('/challenges/solution-1', methods=['GET'])
@swag_from({
    "tags": ["Desafíos"],
    "summary": "Solución al reto de patrones de propagación viral",
    "description": "Calcula el número de patrones diferentes de propagación viral para una distancia dada",
    "parameters": [
        {
            "name": "n",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Distancia para la cual calcular los patrones"
        }
    ],
    "responses": {
        "200": {
            "description": "Resultado del cálculo",
            "schema": {
                "type": "object",
                "properties": {
                    "result": {
                        "type": "string",
                        "description": "Número de patrones diferentes"
                    },
                    "executionTimeMs": {
                        "type": "number",
                        "format": "float",
                        "description": "Tiempo de ejecución en milisegundos"
                    }
                }
            }
        },
        "400": {
            "description": "Parámetros inválidos",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Descripción del error"
                    }
                }
            }
        },
        "500": {
            "description": "Error interno del servidor",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Descripción del error"
                    }
                }
            }
        }
    }
})
def viral_propagation_patterns():
    try:
        n = request.args.get('n', type=int)
        if n is None:
            return jsonify({"error": "El parámetro 'n' es requerido y debe ser un entero"}), 400
        
        start_time = time.time()
        result = calculate_patterns(n)
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        
        return jsonify({
            "result": str(result),
            "executionTimeMs": execution_time_ms
        })
    except Exception as e:
        return "An internal error has occurred!", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
