from setuptools import setup

setup(
    name="globbing",
    # ...
    include_package_data=True,
    data_files=[
        (
            "etc/jupyter/jupyter_server_config.d",
            ["jupyter-config/jupyter_server_config.d/globbing.json"],
        ),
    ],
)
