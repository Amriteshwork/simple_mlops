import os


dirs = [
    os.path.join('data','raw'),
    os.path.join('data','processes'),
    'notebooks',
    'saved_models',
    'src'

]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

file_= [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py"),

]

for file in file_:
    with open(file, "w") as f:
        pass