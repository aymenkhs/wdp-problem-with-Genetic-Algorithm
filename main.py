import time
import csv

from parsing_data import parse_instance, parse_multiple
from instance import Bid, InstanceWDP
from genetic_algorithm import GeneticAlgorithm

def solve(instance, pop_size, nb_gen):
    ga = GeneticAlgorithm(pop_size, nb_gen, instance)
    x = time.time()
    ga.process()
    y = time.time()
    final_time = y - x
    return ga.genetic.best_individual, final_time,

def test_multiples():
    directory_name = "instance"
    data = parse_multiple(directory_name)
    results = []
    for wdp_instance in data:
        print("instance: ", wdp_instance)
        print("Pretraitement: ")
        data[wdp_instance].build_concurent_items()
        print("Genetic Algorithm: ")
        best_individual, execution_time = solve(data[wdp_instance], 50, 50)
        results.append({
            "instance" : wdp_instance,
            "best_ind" : best_individual,
            "time_exec" : execution_time
        })
        write_csv(results)

def write_csv(results):
    with open("result.csv", "w") as results_file:
        writer = csv.writer(results_file)
        first_line = ["instance", "solution", "solution score", "time"]
        writer.writerow(first_line)

        for line in results:
            solution = [index for index, g in enumerate(line["best_ind"].genome) if g]
            to_write = [line["instance"], solution, line["best_ind"].score, line["time_exec"]]
            writer.writerow(to_write)


def main():
    test_multiples()

if __name__ == '__main__':
    main()
