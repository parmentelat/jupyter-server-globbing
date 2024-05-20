from setuptools import setup

from globbing import __version__

setup(
    name="globbing",
    version=__version__,
    # ...
    include_package_data=True,
    data_files=[
        (
            "etc/jupyter/jupyter_server_config.d",
            ["jupyter-config/jupyter_server_config.d/globbing.json"],
        ),
    ],
)
