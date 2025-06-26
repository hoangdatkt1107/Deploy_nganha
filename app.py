from flask import Flask, render_template, request, redirect, url_for
import os
from models import db, Task, init_db

app = Flask(__name__)

# Configure and initialize the database
init_db(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    """Display tasks and handle new task submissions."""
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            new_task = Task(content=content)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('tasks'))

    all_tasks = Task.query.all()
    return render_template('tasks.html', tasks=all_tasks)


@app.route('/tasks/<int:id>/done')
def mark_done(id):
    """Mark a task as done."""
    task = Task.query.get_or_404(id)
    task.done = True
    db.session.commit()
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)