from MFEA.mfea import mfea
from BENCHMARK.task import Task
from BENCHMARK.benchmark import CI_HS, CI_MS, CI_LS, PI_HS, PI_MS, PI_LS, NI_HS, NI_MS, NI_LS
from SAMPLE.toyfnc import ackley, sphere, rastrigin
from PyCEC2022.Python.CEC2022 import cec2022_func

if __name__ == "__main__":
    # print('test')
    # tasks = [Task(50, ackley, 50, -50),
    #          Task(20, sphere, 50, -50)]
    #
    # TotalEvaluations, bestobj, bestind = mfea(tasks)
    # tasks = CI_HS()

    CEC1 = cec2022_func(func_num=1)
    CEC2 = cec2022_func(func_num=2)

    tasks = [Task(10, CEC1.calcValues, -100, 100),
             Task(10, CEC1.calcValues, -50, 50)]
    print('starting task')
    TotalEvaluations, bestobj, bestind = mfea(tasks, reps=1)
    print('ending task')
