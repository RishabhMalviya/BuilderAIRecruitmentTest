from flask import Flask
from pathfinder.solve import solve
from pathfinder.errors import ShortestPathNotFoundError
from os import linesep
app = Flask(__name__)


@app.route('/')
def basic():
    return "Up and running!"


@app.route('/map/<string:input_file>')
def map_shortest_path(input_file):
    base_folder = './sample_input_data/'

    try:
        marked_map = solve(base_folder + input_file + '.txt')
    except FileNotFoundError:
        return "ERROR: Input file not found..."
    except ShortestPathNotFoundError as e:
        return "error: " + str(e)
    else:
        return "<br/>".join(marked_map.split(linesep))
