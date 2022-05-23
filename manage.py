
import click

from app.main import create_app
from app import blueprint

app = create_app()

app.register_blueprint(blueprint)

@click.command()
def run():
    print("run called")
    app.run(host="0.0.0.0", port=8080)


if __name__ == '__main__':
    run()