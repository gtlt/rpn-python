from calculator.rpn import Calculator

client_instances = {}


def get_calculator(client: str) -> Calculator:
    if client not in client_instances.keys():
        create_calculator(client)
    return client_instances[client]


def create_calculator(client: str):
    if client not in client_instances.keys():
        client_instances[client] = Calculator()
