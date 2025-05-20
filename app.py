from pathlib import Path

from fonctions.main import run

file_quizz = Path().cwd() / "data/data_base_of_quizz_game.json"

file_users = Path().cwd() / "data/count_user.json"

run(file_quizz, file_users)