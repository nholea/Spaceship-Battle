from flask import Flask, jsonify, request

from Models import Spaceship, spaceships, Weapon, Generator

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h1>SpaceShip Battle</h1>"


@app.route("/spaceships")
def get_spaceships():
    return jsonify({"Spaceships": [spaceship.serialize() for spaceship in spaceships], "Message": "Spaceships's List"})


@app.route("/spaceships", methods=["POST"])
def create_spaceship():
    new_spaceship = Spaceship(request.json["name"], request.json["health"], Weapon(
        request.json["power needed"], request.json["power consumed"]), Generator(request.json["total power"]))
    spaceships.append(new_spaceship)
    return jsonify({"Message": "Spaceship Successfully Created and Added", "New Spaceship": new_spaceship.serialize()})


@app.route("/spaceships/<spaceship_name>")
def get_spaceship(spaceship_name):
    spaceship_found = [
        spaceship for spaceship in spaceships if spaceship.name == spaceship_name]
    if (len(spaceship_found) > 0):
        return jsonify({"Name": spaceship_found[0].name, "State": spaceship_found[0].state(), "Spaceship": spaceship_found[0].serialize()})
    return jsonify({"Message": "Spaceship Not Found!"})


@app.route("/spaceships/<attacker_name>/<target_name>", methods=["PATCH"])
def shoot_at(attacker_name, target_name):
    target_spaceship = [
        target for target in spaceships if target.name == target_name]
    attacking_spaceship = [
        attacker for attacker in spaceships if attacker.name == attacker_name]
    if (len(target_spaceship) > 0 and len(attacking_spaceship) > 0):
        attacking_spaceship[0].shoot_at(target_spaceship[0])
        return jsonify({"Message":  attacking_spaceship[0].name + " shot " + target_spaceship[0].name, "Health": target_spaceship[0].health, "Power": "Power not used by " + attacking_spaceship[0].name + " : " + str(attacking_spaceship[0].power_not_in_use)})
    return jsonify({"message": "Spaceship Not Found!"})


@app.route("/spaceships/weapon/<spaceship_name>", methods=["PATCH"])
def update_weapon_power_consumed(spaceship_name):
    spaceship_found = [
        spaceship for spaceship in spaceships if spaceship.name == spaceship_name]
    if (len(spaceship_found) > 0):
        if request.json["power consumed"] > 0 and request.json["power consumed"] <=spaceship_found[0].weapon.weapon_power_needed: 
            spaceship_found[0].weapon.power_consumed_by_weapon = request.json["power consumed"]
        else:
            raise ValueError("Power consumed must be > 0 and <= Power needed")
        return jsonify({"message": "Weapon power consumed Updated", "spaceship": spaceship_found[0].serialize()})
    return jsonify({"message": "Spaceship Not Found!"})


if __name__ == "__main__":
    app.run(debug=True)
