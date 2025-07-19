from flask import Flask, render_template, request, make_response
import json
from battleships import init_board, place_ships

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # On first visit: initialize game state
    state_cookie = request.cookies.get("battleships_state")
    if state_cookie:
        state = json.loads(state_cookie)
    else:
        state = {
            "player_board": init_board(),
            "computer_board": init_board(),
            "display_board": init_board(),
            "player_guessed": [],
            "computer_guessed": [],
            "turns": 0,
            "player_score": 0,
            "computer_score": 0,
            "feedback": ""
        }
        place_ships(state["player_board"], "@")
        place_ships(state["computer_board"], "'")

    # Handle a shot if POST
    if request.method == "POST":
        r = int(request.form["row"])
        c = int(request.form["col"])
        if (r, c) not in state["player_guessed"] and state["turns"] < 5:
            state["player_guessed"].append((r, c))
            state["turns"] += 1
            if state["computer_board"][r][c] == "'":
                state["display_board"][r][c] = "$"
                state["player_score"] += 1
                state["feedback"] = "Hit! You sank an enemy ship!"
            else:
                state["display_board"][r][c] = "X"
                state["feedback"] = "Miss!"

    # Render template with current state
    resp = make_response(render_template(
        "index.html",
        board=state["display_board"],
        turns=state["turns"],
        player_score=state["player_score"],
        computer_score=state["computer_score"],
        feedback=state["feedback"]
    ))

    # Store updated state in cookie
    resp.set_cookie("battleships_state", json.dumps(state), max_age=60*60*24)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
