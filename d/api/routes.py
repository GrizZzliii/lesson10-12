from flask import Blueprint, jsonify, request
from .models import robots, Robot

api_blueprint = Blueprint('api', __name__)

# Получение списка роботов
@api_blueprint.route('/robots', methods=['GET'])
def get_robots():
    return jsonify([vars(robot) for robot in robots]), 200

# Добавление нового робота
@api_blueprint.route('/robots', methods=['POST'])
def add_robot():
    data = request.json
    new_robot = Robot(robot_id=len(robots) + 1, name=data['name'], status=data['status'])
    robots.append(new_robot)
    return jsonify(vars(new_robot)), 201

# Обновление информации о роботе
@api_blueprint.route('/robots/<int:robot_id>', methods=['PUT'])
def update_robot(robot_id):
    data = request.json
    for robot in robots:
        if robot.robot_id == robot_id:
            robot.name = data.get('name', robot.name)
            robot.status = data.get('status', robot.status)
            return jsonify(vars(robot)), 200
    return jsonify({"message": "Robot not found"}), 404

# Удаление робота
@api_blueprint.route('/robots/<int:robot_id>', methods=['DELETE'])
def delete_robot(robot_id):
    global robots
    robots = [robot for robot in robots if robot.robot_id != robot_id]
    return jsonify({"message": "Robot deleted"}), 204