
from parsing_data import parse_instance
from instance import Bid, InstanceWDP

def main():
    instance = parse_instance("instance/in601")
    instance.build_concurent_items()
    import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()
