from MFEA.mfea import mfea
from BENCHMARK.task import Task
from BENCHMARK.benchmark import CI_HS, CI_MS, CI_LS, PI_HS, PI_MS, PI_LS, NI_HS, NI_MS, NI_LS
from SAMPLE.toyfnc import ackley, sphere, rastrigin
from PyCEC2022.Python.CEC2022 import cec2022_func

import os
import csv
# run combinations of CEC functions which correspond to combinations grom the BENCHMARK


def run_optimization_on_cec_functions(combination_name, func1_num, func2_num, func1_dim, func2_dim, known_optimization_goal, func1_bounds, func2_bounds):
    CEC1 = cec2022_func(func_num=func1_num)
    CEC2 = cec2022_func(func_num=func2_num)
    tasks = [Task(func1_dim, CEC1.calcValues, func1_bounds[0], func1_bounds[1]),
             Task(func2_dim, CEC2.calcValues, func2_bounds[0], func2_bounds[1])]
    print('starting task : ', combination_name)
    TotalEvaluations, bestobj, bestind, bestObjAtGen0, bestindAtGen0, bestObjAtLastGen, bestindAtLastGen = mfea(
        tasks, reps=1, gen=1000)
    print('ending task: ', combination_name)

    # TODO: 1, figure out why bestobj and bestObjAtGen0 are more than a set of values xd [[[a,b][a,b][a,b][a,b][a,b]]]] instead of [a,b]
    # 2. save to file
    print('TotalEvaluations: ', TotalEvaluations,
          'bestobj: ', bestobj, 'bestobjAtGen0: ', bestObjAtGen0, 'bestObjAtLastGen: ', bestObjAtLastGen, 'bestind: ', bestind, 'bestindAtGen0: ', bestindAtGen0, 'bestindAtLastGen: ', bestindAtLastGen)

    results_file_path = 'results_summary.csv'

    data_names = ['combination_name', 'bestObjAtGen0',
                  'bestObjAtLastGen', 'known_optimization_result']
    data = [combination_name, bestObjAtGen0,
            bestObjAtLastGen, known_optimization_goal]

    if not os.path.exists(results_file_path):
        with open(results_file_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data_names)

    with open(results_file_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


if __name__ == "__main__":
    # print('test')
    # tasks = [Task(50, ackley, 50, -50),
    #          Task(20, sphere, 50, -50)]
    #
    # TotalEvaluations, bestobj, bestind = mfea(tasks)
    # tasks = CI_HS()

    # constant among all for now (if needed can be specified)
    func1_bounds = [-100, 100]
    func2_bounds = func1_bounds
    func1_dim_count = 20
    func2_dim_count = 10

    combination_name = "F1: Zakharov - different dimension count"
    func1_num = 1
    func2_num = func1_num
    known_optimization_goal = 300

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F2: Rosencbrock - different dimension count"
    func1_num = 2
    func2_num = func1_num
    known_optimization_goal = 400

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F3: Schaffer - different dimension count"
    func1_num = 3
    func2_num = func1_num
    known_optimization_goal = 600

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F4: Rastrigin - different dimension count"
    func1_num = 4
    func2_num = func1_num
    known_optimization_goal = 800

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F5: Levy - different dimension count"
    func1_num = 5
    func2_num = func1_num
    known_optimization_goal = 900

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F6: hf02 - different dimension count"
    func1_num = 6
    func2_num = func1_num
    known_optimization_goal = 1800

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F7: hf10 - different dimension count"
    func1_num = 7
    func2_num = func1_num
    known_optimization_goal = 2000

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F8: hf06 - different dimension count"
    func1_num = 8
    func2_num = func1_num
    known_optimization_goal = 2200

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F9: cf01 - different dimension count"
    func1_num = 9
    func2_num = func1_num
    known_optimization_goal = 2300

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F10: cf02 - different dimension count"
    func1_num = 10
    func2_num = func1_num
    known_optimization_goal = 2400

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F11: cf06 - different dimension count"
    func1_num = 11
    func2_num = func1_num
    known_optimization_goal = 2600

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

    combination_name = "F12: cf07 - different dimension count"
    func1_num = 12
    func2_num = func1_num
    known_optimization_goal = 2700

    run_optimization_on_cec_functions(
        combination_name, func1_num, func2_num, func1_dim_count, func2_dim_count, known_optimization_goal, func1_bounds, func2_bounds)

# TODO:
# Sprawdzenie czy MFEA optymalizuje trywialne parę funkcji podobnych, to jest func1_num = func2_num ale dim1 = 10, dim2 = 20
# pewnie tak, więc ewentualnie poczytać o funckjach czy uda mi się znaleźć jakieś pary różnych funkcji spełniających kryteria benchmarku (w sensie czy będzie 9 kombinacji względem tego jak te minima są rozłożone i podobieństwo funkcji do siebie liczbowe - to drugie musi być sprawdzone najpierw teoretycznie bo inaczej będzie bardzo dużo kombinacji funkcji, sprawdzenie ich będzie bardzo czasochłonne: 12*11 * ~milion wartości + pososrtowanie + porównanie posortowanych ciągów od długości 1 milion)


# TODO trzeba dodać bestObjAtGen0, bestIndAtGen0 żeby można było porównać na końcu czy jest różnica (jeśli jest znacząca to znaczy że MFEA sobie radzi z tą konkretną funkcją)
