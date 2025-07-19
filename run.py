from flask import Flask, render_template, request, make_response, redirect, url_for
import json
from battleships import init_board, place_ships

app = Flask(__name__)

# Nombre total de tours autorisés
TOTAL_TURNS = 5

@app.route("/", methods=["GET", "POST"])
def index():
    # Récupère l’état depuis le cookie, ou initialise s’il n’existe pas
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
        # Place les navires
        place_ships(state["player_board"], "@")
        place_ships(state["computer_board"], "'")

    # Traite un tir du joueur
    if request.method == "POST" and state["turns"] < TOTAL_TURNS:
        r = int(request.form["row"])
        c = int(request.form["col"])
        if (r, c) not in state["player_guessed"]:
            state["player_guessed"].append((r, c))
            state["turns"] += 1
            if state["computer_board"][r][c] == "'":
                state["display_board"][r][c] = "$"
                state["player_score"] += 1
                state["feedback"] = "Hit! You sank an enemy ship!"
            else:
                state["display_board"][r][c] = "X"
                state["feedback"] = "Miss!"

            # (Optionnel) Tour de l’ordinateur après le joueur
            import random
            if state["turns"] < TOTAL_TURNS:
                while True:
                    cr = random.randint(0, 4)
                    cc = random.randint(0, 4)
                    if (cr, cc) not in state["computer_guessed"]:
                        state["computer_guessed"].append((cr, cc))
                        break
                if state["player_board"][cr][cc] == "@":
                    state["player_board"][cr][cc] = "£"
                    state["computer_score"] += 1
                # pas de feedback pour la miss de l’ordi

    # Détermine si la partie est finie
    done = state["turns"] >= TOTAL_TURNS or \
           state["player_score"] == 4 or \
           state["computer_score"] == 4

    # Prépare la réponse avec le rendu du template
    resp = make_response(render_template(
        "index.html",
        board=state["display_board"],
        player_board=state["player_board"],
        computer_board=state["computer_board"],
        turns=state["turns"],
        player_score=state["player_score"],
        computer_score=state["computer_score"],
        feedback=state["feedback"],
        done=done,
        TOTAL_TURNS=TOTAL_TURNS
    ))

    # Sauvegarde l’état dans un cookie (1 jour)
    resp.set_cookie("battleships_state", json.dumps(state), max_age=60*60*24)
    return resp

@app.route("/reset", methods=["POST"])
def reset():
    # Supprime le cookie et redirige à la racine
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie("battleships_state", "", expires=0)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
