from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Chave secreta para funcionamento das sessões
app.secret_key = "chave-secreta-flask-tarefas"


# Rota principal
@app.route("/")
def index():
    # Se a lista de tarefas ainda não existir, cria uma lista vazia
    if "tasks" not in session:
        session["tasks"] = []

    tasks = session["tasks"]

    return render_template("index.html", tasks=tasks)


# Rota para adicionar uma tarefa
@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")

    if task and task.strip():
        # Recupera a lista da sessão
        tasks = session.get("tasks", [])

        # Adiciona a nova tarefa
        tasks.append(task.strip())

        # Atualiza a sessão
        session["tasks"] = tasks
        session.modified = True

    return redirect(url_for("index"))


# Rota para remover uma tarefa
@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = session.get("tasks", [])

    # Verifica se o ID corresponde a uma tarefa existente
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)

        # Salva a alteração na sessão
        session["tasks"] = tasks
        session.modified = True

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
