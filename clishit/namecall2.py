import click
from art import text2art

@click.command()
@click.option('--name', default='World', help='The person to greet.')
def hello(name):
   click.echo(text2art(f'Hello, {name}!'))
if __name__ == '__main__':
   hello()