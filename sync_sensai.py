import shutil
import os


def sync():
    SRC_DIRECTORY = os.path.join("..", "sensAI", "src", "sensai")
    LIB_DIRECTORY = os.path.join("src", "sensai")

    shutil.move(os.path.join(LIB_DIRECTORY, "util", "__init__.py"), "__init__.py.util.bak")
    shutil.move(os.path.join(LIB_DIRECTORY, "__init__.py"), "__init__.py.sensai.bak")

    if os.path.exists(LIB_DIRECTORY):
        shutil.rmtree(LIB_DIRECTORY)

    shutil.copytree(os.path.join(SRC_DIRECTORY, "util"), os.path.join(LIB_DIRECTORY, "util"))
    os.unlink(os.path.join(LIB_DIRECTORY, "util", "__init__.py"))

    shutil.move("__init__.py.util.bak", os.path.join(LIB_DIRECTORY, "util", "__init__.py"))
    shutil.move("__init__.py.sensai.bak", os.path.join(LIB_DIRECTORY, "__init__.py"))


if __name__ == "__main__":
    sync()
