from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required
from app import db

main = Blueprint('main', __name__)

@main.route('/agendamentos')
@login_required
def agendamentos():
    return render_template('main/agendamentos.html', title = "Agendamentos")


