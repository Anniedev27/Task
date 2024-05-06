from models import *
from flask import render_template, request, redirect, url_for


apk = app

@app.route("/note", methods=["GET", "POST"])
def note_list():
    if request.method == "POST":
       
            todo = Todo(
                task=request.form["task"],
                date=request.form["date"]
            )
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for("note_list"))  
    
    task = Todo.query.all()

    return render_template("index.html", tasks=task)

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete_task(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("note_list"))

@app.route("/delete_all", methods=["POST"])
def delete_all_tasks():
    Todo.query.delete()
    db.session.commit()
    return redirect(url_for("note_list"))

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
     task = Todo.query.get_or_404(id)
     if request.method == "POST":
        task.task=request.form['task']
        task.date=request.form['date']
        db.session.commit()
        return redirect(url_for("note_list"))
     return render_template('update.html', task=task)