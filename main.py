from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Guilherme"}
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensagem": "API RESTful funcionando"
    })


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)


@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify(usuario)

    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()

    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": dados["nome"]
    }

    usuarios.append(novo_usuario)

    return jsonify(novo_usuario), 201


@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = dados["nome"]
            return jsonify(usuario)

    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return jsonify({
                "mensagem": "Usuário deletado com sucesso"
            })

    return jsonify({"erro": "Usuário não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)