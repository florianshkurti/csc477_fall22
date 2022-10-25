from setuptools import setup

d = setup(
    name='path_planning_and_control_assignment',
    author=["Florian Shkurti"],
    author_email="florian@cs.toronto.edu",
    packages=["path_planning_and_control_assignment"],
    install_requires=[
        "numpy",
        "scipy",
        "opencv-python"
    ]
)
