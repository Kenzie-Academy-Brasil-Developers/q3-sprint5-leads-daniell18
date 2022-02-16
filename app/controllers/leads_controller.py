from flask import jsonify,request
from datetime import datetime
from app.config.database import db
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
import re

from app.models.leads_models import Leads
def get_all():
    base_querry=db.session.query(Leads)
    result=base_querry.order_by(Leads.visits).all()
    return jsonify(result),HTTPStatus.OK
def create():
    default_keys=['name','email','phone']
    data=request.get_json()
    if(set(data)!=set(default_keys)):
        return jsonify({'error':f'Wrong keys the correct keys are {default_keys}'}),HTTPStatus.BAD_GATEWAY
    if not all(isinstance(n,str)for n in data.values()):
        return jsonify({'error':'all values must be strigs'}),HTTPStatus.BAD_REQUEST
    if not (re.fullmatch(r'\([0-9]{2}\)[0-9]{4,5}-[0-9]{4}',data['phone'])):
        return jsonify({'error':f'incorrect phone the correct format is (xx)xxxxx-xxx'}),HTTPStatus.BAD_REQUEST
    data['creation_date']=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    data['last_visit']=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    leads=Leads(**data)
    try:
        db.session.add(leads)
        db.session.commit()
    except IntegrityError as e:
        return jsonify({'error':e.args}),HTTPStatus.CONFLICT
    return jsonify(leads),HTTPStatus.CREATED
def update():
    default=set()
    default.add('email')
    data=request.get_json()
    if(set(data)!=default):
        return jsonify({'error':'The request must only contain the email key'}),HTTPStatus.BAD_REQUEST
    base_querry=db.session.query(Leads)
    user=base_querry.filter_by(email=data['email']).first_or_404(description="email not found")
    setattr(user,'visits',user.visits+1)
    setattr(user,'last_visit',datetime.today())
    db.session.add(user)
    db.session.commit()
    return '',HTTPStatus.NO_CONTENT
def delete():
    default=set()
    default.add('email')
    data=request.get_json()
    if(set(data)!=default):
        return jsonify({'error':'The request must only contain the email key'}),HTTPStatus.BAD_REQUEST
    base_querry=db.session.query(Leads)
    user=base_querry.filter_by(email=data['email']).first_or_404(description="email not found")
    db.session.delete(user)
    db.session.commit()
    return '',HTTPStatus.NO_CONTENT