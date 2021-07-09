
from parsing_data import parse_instance
from instance import Bid, InstanceWDP
from genetic_algorithm import GeneticAlgorithm

def main():
    instance = parse_instance("instance/in601")
    instance.build_concurent_items()
    ga = GeneticAlgorithm(50, 50, instance)
    ga.process()
    import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()
