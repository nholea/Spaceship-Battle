from flask import Flask, jsonify, request

from Models import Spaceship, spaceships

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>SpaceShip Battle</h1>"

@app.route("/spaceships")
def get_spaceships():
    return jsonify({"Spaceships": [spaceship.serialize() for spaceship in spaceships], "Message": "Spaceships's List"})

@app.route("/spaceships", methods=["POST"])
def create_spaceship():
    new_spaceship = Spaceship(request.json["name"],
        request.json["health"])
    spaceships.append(new_spaceship)
    return jsonify({"Message": "Spaceship Successfully Created and Added", "New Spaceship": new_spaceship.serialize()})

@app.route("/spaceships/<spaceship_name>")
def get_spaceship(spaceship_name):
    spaceship_found = [
        spaceship for spaceship in spaceships if spaceship.name == spaceship_name]
    if (len(spaceship_found) > 0):
        return jsonify({"Name": spaceship_found[0].name, "State": spaceship_found[0].state(),"Spaceship": spaceship_found[0].serialize()})
    return jsonify({"Message": "Spaceship Not Found!"})


@app.route("/spaceships/<spaceship_name>", methods=["PATCH"])
def battle(spaceship_name):
    spaceship_found = [
        spaceship for spaceship in spaceships if spaceship.name == spaceship_name]
    if (len(spaceship_found) > 0):
        attacking_spaceship = [spaceship for spaceship in spaceships if spaceship != spaceship_found[0]]
        if spaceship_found[0].protection():
            attacking_spaceship[0].battle(spaceship_found[0])
            return jsonify({"Message":  attacking_spaceship[0].name + " shot " + spaceship_found[0].name, "Protection": "Activated" if spaceship_found[0].protection() else "Deleted"})
        else:
            spaceship_found[0].name =  spaceship_found[0].name
            spaceship_found[0].health = spaceship_found[0].health - 1

            spaceship_found[0].active_protection()
            return jsonify({"Message":  attacking_spaceship[0].name + " shot " + spaceship_found[0].name + " again", "Health": spaceship_found[0].health})

        
    return jsonify({"message": "Customer Not Found!"})


if __name__ == "__main__":
    app.run(debug=True)