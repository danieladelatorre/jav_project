from flask import Blueprint, jsonify, request
from . import db
from .models import Information
import csv

main = Blueprint('main', __name__)

@main.route('/')
def always_do():
    with open('api/datasets_596958_1073629_Placement_Data_Full_Class (1).csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if(line['status']=="Not Placed"):
                line.update({'salary': 0})
            new_entry = Information(
                sl_no = line['sl_no'],
                gender = line['gender'],
                ssc_p = line['ssc_p'],
                ssc_b = line['ssc_b'],
                hsc_p = line['hsc_p'],
                hsc_b = line['hsc_b'],
                hsc_s = line['hsc_s'],
                degree_p = line['degree_p'],
                degree_t = line['degree_t'],
                workex = line['workex'],
                etest_p = line['etest_p'],
                specialisation = line['specialisation'],
                mba_p = line['mba_p'],
                status = line['status'],
                salary = line['salary']
            )
            db.session.add(new_entry)
            db.session.commit()
        return 'Done', 201
    

@main.route('/add_entry', methods=['POST'])
def add_entry():
    line_entry = request.get_json()
    new_entry = Information(
        sl_no = line_entry['sl_no'],
        gender = line_entry['gender'],
        ssc_p = line_entry['ssc_p'],
        ssc_b = line_entry['ssc_b'],
        hsc_p = line_entry['hsc_p'],
        hsc_b = line_entry['hsc_b'],
        hsc_s = line_entry['hsc_s'],
        degree_p = line_entry['degree_p'],
        degree_t = line_entry['degree_t'],
        workex = line_entry['workex'],
        etest_p = line_entry['etest_p'],
        specialisation = line_entry['specialisation'],
        mba_p = line_entry['mba_p'],
        status = line_entry['status'],
        salary = line_entry['salary']
    )
    db.session.add(new_entry)
    db.session.commit()
    return 'Done', 201

@main.route('/reveal')
def reveal():
    information_list = Information.query.all()
    info_list = []
    for item in information_list:
        info_list.append({
                        'sl_no': item.sl_no,
                        'gender': item.gender,
                        'ssc_p': item.ssc_p,
                        'ssc_b': item.ssc_b,
                        'hsc_p': item.hsc_p,
                        'hsc_b': item.hsc_b,
                        'hsc_s': item.hsc_s,
                        'degree_p': item.degree_p,
                        'degree_t': item.degree_t,
                        'workex': item.workex,
                        'etest_p': item.etest_p,
                        'specialisation': item.specialisation,
                        'mba_p': item.mba_p,
                        'status': item.status,
                        'salary': item.salary,
                        })
    return jsonify({'Information' : info_list})

@main.route('/reveal/<int:id>')
def reveal_person(id):
    person_list = Information.query.all()
    person_information = {'sl_no': person_list[id].sl_no,
                        'gender': person_list[id].gender,
                        'ssc_p': person_list[id].ssc_p,
                        'ssc_b': person_list[id].ssc_b,
                        'hsc_p': person_list[id].hsc_p,
                        'hsc_b': person_list[id].hsc_b,
                        'hsc_s': person_list[id].hsc_s,
                        'degree_p': person_list[id].degree_p,
                        'degree_t': person_list[id].degree_t,
                        'workex': person_list[id].workex,
                        'etest_p': person_list[id].etest_p,
                        'specialisation': person_list[id].specialisation,
                        'mba_p': person_list[id].mba_p,
                        'status': person_list[id].status,
                        'salary': person_list[id].salary}
    return jsonify({'Person_Information': person_information})