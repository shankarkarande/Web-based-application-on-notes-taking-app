from logging import error
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from werkzeug.utils import redirect
from .models import Note
from . import db

import json

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        note = request.form.get('note')

        if not note:
            error_statement = "Fields are required "
            return render_template('home.html', error_statement=error_statement,note=note, title = title, user=current_user)

        new_note = Note(title = title , note=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added!', category='success')

    allnote = Note.query.all()
    db.create_all()
    return render_template("home.html", user=current_user, allnote=allnote)


@views.route('/show')
def show():
    return render_template('show.html', user=current_user)


@views.route('/about')
def about():
    return render_template('about.html', user=current_user)


@views.route('/deleteAccout')
def deleteAccout():
    return render_template('deleteAccout.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        title = request.form.get('title')
        note = request.form.get('note')

        notify = Note.query.filter_by(id=id).first()
        notify.title = title
        notify.note = note
        db.session.add(notify)
        db.session.commit()
        return redirect('/show')

    note = Note.query.filter_by(id = id).first()
    return render_template('update.html',  note=note, user=current_user)
