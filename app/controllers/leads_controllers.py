from datetime import datetime
from http import HTTPStatus
from xml.dom import NotFoundErr
from flask import current_app, jsonify, request

from app.models.leads_model import LeadsModel
from app.controllers.decorators_lead import verify_all_types_string, verify_keys, validate_values

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import Query

@verify_keys(['email','name','phone'])
@verify_all_types_string
@validate_values
def create_lead():
    try:
        data = request.get_json()
        new_lead = LeadsModel(**data)
        current_app.db.session.add(new_lead)
        current_app.db.session.commit()
        return jsonify(new_lead),HTTPStatus.CREATED
    except IntegrityError:
        return {"error": "email or phone already exists!"},HTTPStatus.CONFLICT
    except Exception as e:
        raise e

def get_all_leads():
    try:
        leads = Query(LeadsModel,current_app.db.session).order_by(LeadsModel.visits.desc()).all()
        if not leads:
            raise NotFoundErr
        serializer = LeadsModel.serializer(leads)
        return jsonify(serializer), HTTPStatus.OK
    except NotFoundErr:
        return {'error': 'Not Found'},HTTPStatus.NOT_FOUND
    except Exception as e:
        raise e

@verify_all_types_string
@validate_values
def update_lead():
    try:
        data:dict = request.get_json()
        email = data['email']
        print(data)
        if(len(list(data.keys())) > 1 ):
            return{'error': 'must have only the email'},HTTPStatus.UNPROCESSABLE_ENTITY

        lead = LeadsModel.query.filter(LeadsModel.email==email).first()
        
        setattr(lead,'visits',f"{lead.visits+1}")
        setattr(lead,'last_visit',datetime.utcnow())

        current_app.db.session.add(lead)
        current_app.db.session.commit()
        return "", HTTPStatus.NO_CONTENT
    except AttributeError:
        return {'error': "Not Found"}, HTTPStatus.NOT_FOUND
    except Exception as e:
        raise e

@verify_all_types_string
@validate_values
def delete_lead():
    try:
        data = request.get_json()
        email = data['email']
        if(len(list(data.keys())) > 1 ):
            return{'error': 'must have only the email'},HTTPStatus.UNPROCESSABLE_ENTITY
            
        lead = LeadsModel.query.filter(LeadsModel.email==email).first()
        print('EMAIL',email)
        print('LEAD',lead)
        current_app.db.session.delete(lead)
        current_app.db.session.commit()

        return "", HTTPStatus.NO_CONTENT
    except UnmappedInstanceError:
        return {'error': "Not Found"}, HTTPStatus.NOT_FOUND    
    except Exception as e:
        raise e
