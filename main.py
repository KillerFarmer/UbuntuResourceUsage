
import matplotlib.pyplot as plt
import numpy as np

def ComputerUsage(navigator, file):

    overral_cpu_usage = 0
    overral_memory_usage = 0
    chrome_cpu_usage = 0
    chrome_memory_usage = 0
    firefox_cpu_usage = 0
    firefox_memory_usage = 0

    if navigator == 'chrome':

        with open(file, 'r') as f:
            for i in range(7):
                f.readline()

            for line in f:
                line = line.split()

                if line[-1] == 'chrome':
                    chrome_cpu_usage += float(line[8])
                    chrome_memory_usage += float(line[9])
                else:
                    overral_cpu_usage += float(line[8])
                    overral_memory_usage += float(line[9])

            #print("Overral CPU usage:", overral_cpu_usage, "Overral Memory usage:", overral_memory_usage)
            #print("Chrome CPU usage:", chrome_cpu_usage, "Chrome Memory usage:", chrome_memory_usage)

            return overral_cpu_usage, overral_memory_usage, chrome_cpu_usage, chrome_memory_usage

    elif navigator == 'firefox':

        with open(file, 'r') as f:
            for i in range(7):
                f.readline()

            for line in f:
                line = line.split()

                if line[-1] == 'firefox':
                    firefox_cpu_usage += float(line[8])
                    firefox_memory_usage += float(line[9])
                else:
                    overral_cpu_usage += float(line[8])
                    overral_memory_usage += float(line[9])

            #print("Overral CPU usage:", overral_cpu_usage, "Overral Memory usage:", overral_memory_usage)
            #print("Firefox CPU usage:", firefox_cpu_usage, "Firefox Memory usage:", firefox_memory_usage)

            return overral_cpu_usage, overral_memory_usage, firefox_cpu_usage, firefox_memory_usage

    else:

        with open(file, 'r') as f:
            for i in range(7):
                f.readline()

            for line in f:

                line = line.split()

                overral_cpu_usage += float(line[8])
                overral_memory_usage += float(line[9])

            #print("Overral CPU usage:", overral_cpu_usage, "Overral Memory usage:", overral_memory_usage)

            return overral_cpu_usage, overral_memory_usage

def ComputerLoadAvarage(file):

    LoadAvarage = 0

    with open(file, 'r') as f:
        line = f.readline().split()
        weight = line[8]
        weight = weight[0:-1]
        LoadAvarage = float(weight)

    return LoadAvarage

def ComputerUsedMemory(file):

    UsedMemory = 0

    with open(file, 'r') as f:

        f.readline()

        line = f.readline().split()
        UsedMemory = float(line[2])

    return UsedMemory

def ComputerActiveInactiveMemory(file):

    ActiveMemory = 0
    InactiveMemory = 0

    with open(file, 'r') as f:

        f.readline()
        f.readline()

        line = f.readline().split()
        ActiveMemory = float(line[5])
        InactiveMemory = float(line[4])

    return ActiveMemory, InactiveMemory

def printSamples(samples):

    i = 1
    for s in samples:
        print('\n#')
        print('#Sample %s' % (i))
        print('#\n')
        print(s.overral_cpu_usage)
        print(s.overral_memory_usage)
        print(s.overral_load_avarage)
        print(s.overral_used_memory)
        print(s.overral_active_memory)
        print(s.overral_inactive_memory)
        print('-'*20)
        print(s.chrome_system_cpu_usage)
        print(s.chrome_cpu_usage)
        print(s.chrome_system_memory_usage)
        print(s.chrome_memory_usage)
        print(s.chrome_load_avarage)
        print(s.chrome_used_memory)
        print(s.chrome_active_memory)
        print(s.chrome_inactive_memory)
        print('-'*20)
        print(s.firefox_system_cpu_usage)
        print(s.firefox_cpu_usage)
        print(s.firefox_system_memory_usage)
        print(s.firefox_memory_usage)
        print(s.firefox_load_avarage)
        print(s.firefox_used_memory)
        print(s.firefox_active_memory)
        print(s.firefox_inactive_memory)

        i += 1




def plot1(samples):


    overral_values = np.array([])

    # chrome_system_means = np.array([])
    # chrome_means = np.array([])
    # firefox_system_means = np.array([])
    # firefox_means = np.array([])

    chrome_system_values = []
    chrome_values = []
    firefox_system_values = []
    firefox_values = []

    for i in range(11):
        chrome_system_values.append(np.array([]))
        chrome_values.append(np.array([]))
        firefox_system_values.append(np.array([]))
        firefox_values.append(np.array([]))

    # print(chrome_system_values)
    # print(chrome_values)
    # print(firefox_system_values)
    # print(firefox_values)


    for s in samples:

        overral_values = np.append(overral_values, s.overral_cpu_usage)

        for test in range(11):
            chrome_system_values[test] = np.append(chrome_system_values[test], s.chrome_system_cpu_usage[test])
            chrome_values[test] = np.append(chrome_values[test], s.chrome_cpu_usage[test])
            firefox_system_values[test] = np.append(firefox_system_values[test], s.firefox_system_cpu_usage[test])
            firefox_values[test] = np.append(firefox_values[test], s.firefox_cpu_usage[test])

    # n = 0
    # print(len(chrome_system_values[n]))
    # print(chrome_system_values[n])
    # print(len(chrome_values[n]))
    # print(chrome_values[n])
    # print(len(firefox_system_values[n]))
    # print(firefox_system_values[n])
    # print(len(firefox_values[n]))
    # print(firefox_values[n])


    # for test in range(11):
    #
    #     chrome_system_values = np.array([])
    #     chrome_values = np.array([])
    #     firefox_system_values = np.array([])
    #     firefox_values = np.array([])
    #
    #     i = 1
    #     for s in samples:
    #         print('\nSample',str(i),'\n')
    #         print(s.chrome_system_cpu_usage)
    #         np.append(chrome_system_values, [s.chrome_system_cpu_usage[test]])
    #         np.append(chrome_values, [s.chrome_cpu_usage[test]])
    #         np.append(firefox_system_values, [s.firefox_system_cpu_usage[test]])
    #         np.append(firefox_values, [s.firefox_cpu_usage[test]])
    #         i += 1
    #     #print(chrome_system_values.mean(), chrome_values.mean(), firefox_system_values.mean(), firefox_values.mean())


    overral_mean = overral_values.mean()


    chrome_system_means = []
    chrome_means = []
    firefox_system_means = []
    firefox_means = []



    for test in range(11):
        chrome_system_means.append(chrome_system_values[test].mean() + chrome_values[test].mean())
        chrome_means.append(chrome_values[test].mean())
        firefox_system_means.append(firefox_system_values[test].mean() + firefox_values[test].mean())
        firefox_means.append(firefox_values[test].mean())


    TESTS = [i+1 for i in range(11)]

    plt.xticks(TESTS)

    plt.plot([1, 11], [overral_mean, overral_mean], 'r--',color='black')

    plt.plot(TESTS, chrome_system_means, "ro-", color='#4C88F5')
    plt.plot(TESTS, chrome_means, "ro-", color='#DD5144')

    plt.plot(TESTS, firefox_system_means, "r^-", color='#FF6611')
    plt.plot(TESTS, firefox_means, "r^-", color='#BE0575')

    plt.xlabel('Tests')
    plt.ylabel('CPU mean usage')
    plt.title('CPU mean vs Tests')
    plt.legend(["CPU usage without navigators",
                "Overral CPU usage w/chrome",
                "Chrome CPU usage",
                "Overral CPU usage w/firefox",
                "Firefox CPU usage"])

    plt.show()

def plot2(samples):

    overral_values = np.array([])

    chrome_system_values = []
    chrome_values = []
    firefox_system_values = []
    firefox_values = []

    for i in range(11):
        chrome_system_values.append(np.array([]))
        chrome_values.append(np.array([]))
        firefox_system_values.append(np.array([]))
        firefox_values.append(np.array([]))


    for s in samples:

        overral_values = np.append(overral_values, s.overral_memory_usage)

        for test in range(11):
            chrome_system_values[test] = np.append(chrome_system_values[test], s.chrome_system_memory_usage[test])
            chrome_values[test] = np.append(chrome_values[test], s.chrome_memory_usage[test])
            firefox_system_values[test] = np.append(firefox_system_values[test], s.firefox_system_memory_usage[test])
            firefox_values[test] = np.append(firefox_values[test], s.firefox_memory_usage[test])


    overral_mean = overral_values.mean()

    chrome_system_means = []
    chrome_means = []
    firefox_system_means = []
    firefox_means = []

    for test in range(11):
        chrome_system_means.append(chrome_system_values[test].mean() + chrome_values[test].mean())
        chrome_means.append(chrome_values[test].mean())
        firefox_system_means.append(firefox_system_values[test].mean() + firefox_values[test].mean())
        firefox_means.append(firefox_values[test].mean())

    TESTS = [i + 1 for i in range(11)]

    plt.xticks(TESTS)

    plt.plot([1, 11], [overral_mean, overral_mean], 'r--', color='black')

    plt.plot(TESTS, chrome_system_means, "ro-", color='#4C88F5')
    plt.plot(TESTS, chrome_means, "ro-", color='#DD5144')

    plt.plot(TESTS, firefox_system_means, "r^-", color='#FF6611')
    plt.plot(TESTS, firefox_means, "r^-", color='#BE0575')

    plt.xlabel('Tests')
    plt.ylabel('Memory mean usage')
    plt.title('Memory mean vs Tests')
    plt.legend(["MEM usage without navigators",
                "Overral MEM usage w/chrome",
                "Chrome MEM usage",
                "Overral MEM usage w/firefox",
                "Firefox MEM usage"])

    plt.show()

def plot3(samples):

    overral_values = np.array([])

    chrome_values = []
    firefox_values = []

    for i in range(11):

        chrome_values.append(np.array([]))
        firefox_values.append(np.array([]))

    for s in samples:

        overral_values = np.append(overral_values, s.overral_load_avarage)

        for test in range(11):

            chrome_values[test] = np.append(chrome_values[test], s.chrome_load_avarage[test])
            firefox_values[test] = np.append(firefox_values[test], s.firefox_load_avarage[test])

    overral_mean = overral_values.mean()

    chrome_means = []
    firefox_means = []

    for test in range(11):
        chrome_means.append(chrome_values[test].mean())
        firefox_means.append(firefox_values[test].mean())

    TESTS = [i + 1 for i in range(11)]

    plt.xticks(TESTS)

    plt.plot([1, 11], [overral_mean, overral_mean], 'r--', color='black')

    plt.plot(TESTS, chrome_means, "ro-", color='#DD5144')
    plt.plot(TESTS, firefox_means, "r^-", color='#BE0575')

    plt.xlabel('Tests')
    plt.ylabel('Load Avarage mean')
    plt.title('Load Avarage mean vs Tests')
    plt.legend(["Load Avarage without navigators",
                "Chrome L.A. usage",
                "Firefox L.A. usage"])

    plt.show()

def plot4(samples):
    overral_values = np.array([])

    chrome_values = []
    firefox_values = []

    for i in range(11):
        chrome_values.append(np.array([]))
        firefox_values.append(np.array([]))

    for s in samples:

        overral_values = np.append(overral_values, s.overral_used_memory)

        for test in range(11):
            chrome_values[test] = np.append(chrome_values[test], s.chrome_used_memory[test])
            firefox_values[test] = np.append(firefox_values[test], s.firefox_used_memory[test])

    overral_mean = overral_values.mean()

    chrome_means = []
    firefox_means = []

    for test in range(11):

        chrome_means.append(chrome_values[test].mean())
        firefox_means.append(firefox_values[test].mean())

    TESTS = [i + 1 for i in range(11)]

    plt.xticks(TESTS)

    plt.plot([1, 11], [overral_mean, overral_mean], 'r--', color='black')

    plt.plot(TESTS, chrome_means, "ro-", color='#DD5144')
    plt.plot(TESTS, firefox_means, "r^-", color='#BE0575')

    plt.xlabel('Tests')
    plt.ylabel('Used Memory mean')
    plt.title('Used Memory mean vs Tests')
    plt.legend(["Used Memory without navigators",
                "Chrome U.M usage",
                "Firefox U.M usage"])

    plt.show()

def plot5(samples):
    overral_values = np.array([])

    chrome_values = []
    firefox_values = []

    for i in range(11):
        chrome_values.append(np.array([]))
        firefox_values.append(np.array([]))

    for s in samples:

        overral_values = np.append(overral_values, s.overral_active_memory)

        for test in range(11):
            chrome_values[test] = np.append(chrome_values[test], s.chrome_active_memory[test])
            firefox_values[test] = np.append(firefox_values[test], s.firefox_active_memory[test])

    overral_mean = overral_values.mean()

    chrome_means = []
    firefox_means = []

    for test in range(11):
        chrome_means.append(chrome_values[test].mean())
        firefox_means.append(firefox_values[test].mean())

    TESTS = [i + 1 for i in range(11)]

    plt.xticks(TESTS)

    plt.plot([1, 11], [overral_mean, overral_mean], 'r--', color='black')

    plt.plot(TESTS, chrome_means, "ro-", color='#DD5144')
    plt.plot(TESTS, firefox_means, "r^-", color='#BE0575')

    plt.xlabel('Tests')
    plt.ylabel('Active Memory mean')
    plt.title('Active Memory mean vs Tests')
    plt.legend(["Active Memory without navigators",
                "Chrome A.M. usage",
                "Firefox A.M usage"])

    plt.show()

def plot6(samples):
    overral_values = np.array([])

    chrome_values = []
    firefox_values = []

    for i in range(11):
        chrome_values.append(np.array([]))
        firefox_values.append(np.array([]))

    for s in samples:

        overral_values = np.append(overral_values, s.overral_inactive_memory)

        for test in range(11):
            chrome_values[test] = np.append(chrome_values[test], s.chrome_inactive_memory[test])
            firefox_values[test] = np.append(firefox_values[test], s.firefox_inactive_memory[test])

    overral_mean = overral_values.mean()

    chrome_means = []
    firefox_means = []

    for test in range(11):
        chrome_means.append(chrome_values[test].mean())
        firefox_means.append(firefox_values[test].mean())

    TESTS = [i + 1 for i in range(11)]

    plt.xticks(TESTS)

    plt.plot([1, 11], [overral_mean, overral_mean], 'r--', color='black')

    plt.plot(TESTS, chrome_means, "ro-", color='#DD5144')
    plt.plot(TESTS, firefox_means, "r^-", color='#BE0575')

    plt.xlabel('Tests')
    plt.ylabel('Inactive Memory mean')
    plt.title('Inactive Memory mean vs Tests')
    plt.legend(["Inactive Memory without navigators",
                "Chrome I.M. usage",
                "Firefox I.M usage"])

    plt.show()

class Sample:
    def __init__(self):
        self.overral_cpu_usage = 0
        self.overral_memory_usage = 0
        self.overral_load_avarage = 0
        self.overral_used_memory = 0
        self.overral_active_memory = 0
        self.overral_inactive_memory = 0

        self.chrome_cpu_usage = []
        self.chrome_system_cpu_usage = []
        self.chrome_memory_usage = []
        self.chrome_system_memory_usage = []
        self.chrome_load_avarage = []
        self.chrome_used_memory = []
        self.chrome_active_memory = []
        self.chrome_inactive_memory = []


        self.firefox_cpu_usage = []
        self.firefox_system_cpu_usage = []
        self.firefox_memory_usage = []
        self.firefox_system_memory_usage = []
        self.firefox_load_avarage = []
        self.firefox_used_memory = []
        self.firefox_active_memory = []
        self.firefox_inactive_memory = []


def main():

    #ComputerUsage('firefox', r'./Results/sample2/firefox/test1/FirefoxUtilization')
    #ComputerLoadAvarage(r'./Results/sample2/loadAvarage')
    #ComputerUsedMemory(r'./Results/sample2/memoryStatus')
    #ComputerActiveInactiveMemory(r'./Results/sample2/activeInactiveMemory')


    samples = []

    for i in range(1,6):

        sample = Sample()

        sample.overral_cpu_usage, sample.overral_memory_usage = ComputerUsage('', 'Results/sample%s/utilization' % (i))
        sample.overral_load_avarage = ComputerLoadAvarage('Results/sample%s/loadAvarage' % (i))
        sample.overral_used_memory = ComputerUsedMemory('Results/sample%s/memoryStatus' % (i))
        sample.overral_active_memory, sample.overral_inactive_memory = ComputerActiveInactiveMemory('Results/sample%s/activeInactiveMemory' % (i))


        for test in range(1,12):

            C_S_cpu, C_S_memory, C_cpu, C_memory = ComputerUsage('chrome', 'Results/sample%s/chrome/test%s/ChromeUtilization' % (i, test))

            # sample.chrome_system_cpu_usage = C_S_cpu
            # sample.chrome_system_memory_usage = C_S_memory
            # sample.chrome_cpu_usage = C_cpu
            # sample.chrome_memory_usage = C_memory

            sample.chrome_system_cpu_usage.append(C_S_cpu)
            sample.chrome_system_memory_usage.append(C_S_memory)
            sample.chrome_cpu_usage.append(C_cpu)
            sample.chrome_memory_usage.append(C_memory)

            # sample.chrome_load_avarage = ComputerLoadAvarage('Results/sample%s/chrome/test%s/ChromeLoadAvarage' % (i, test))
            # sample.chrome_used_memory = ComputerUsedMemory('Results/sample%s/chrome/test%s/ChromeMemoryStatus' % (i, test))

            sample.chrome_load_avarage.append(ComputerLoadAvarage(
                'Results/sample%s/chrome/test%s/ChromeLoadAvarage' % (i, test)))
            sample.chrome_used_memory.append(ComputerUsedMemory(
                'Results/sample%s/chrome/test%s/ChromeMemoryStatus' % (i, test)))

            active_mem, inactive_mem = ComputerActiveInactiveMemory('Results/sample%s/chrome/test%s/ChromActiveInactiveMemory' % (i, test))

            # sample.chrome_active_memory = active_mem
            # sample.chrome_inactive_memory = inactive_mem

            sample.chrome_active_memory.append(active_mem)
            sample.chrome_inactive_memory.append(inactive_mem)


        for test in range(1, 12):

            F_S_cpu, F_S_memory, F_cpu, F_memory = ComputerUsage('firefox', 'Results/sample%s/firefox/test%s/FirefoxUtilization' % (i, test))

            # sample.firefox_system_cpu_usage = F_S_cpu
            # sample.firefox_system_memory_usage = F_S_memory
            # sample.firefox_cpu_usage = F_cpu
            # sample.firefox_memory_usage = F_memory

            sample.firefox_system_cpu_usage.append(F_S_cpu)
            sample.firefox_system_memory_usage.append(F_S_memory)
            sample.firefox_cpu_usage.append(F_cpu)
            sample.firefox_memory_usage.append(F_memory)

            # sample.firefox_load_avarage = ComputerLoadAvarage('Results/sample%s/firefox/test%s/FirefoxLoadAvarage' % (i, test))
            # sample.firefox_used_memory = ComputerUsedMemory('Results/sample%s/firefox/test%s/FirefoxMemoryStatus' % (i, test))

            sample.firefox_load_avarage.append(ComputerLoadAvarage(
                'Results/sample%s/firefox/test%s/FirefoxLoadAvarage' % (i, test)))
            sample.firefox_used_memory.append(ComputerUsedMemory(
                'Results/sample%s/firefox/test%s/FirefoxMemoryStatus' % (i, test)))

            active_mem, inactive_mem = ComputerActiveInactiveMemory('Results/sample%s/firefox/test%s/FirefoxActiveInactiveMemory' % (i, test))

            # sample.firefox_active_memory = active_mem
            # sample.firefox_inactive_memory = inactive_mem

            sample.firefox_active_memory.append(active_mem)
            sample.firefox_inactive_memory.append(inactive_mem)

        samples.append(sample)

    # printSamples(samples)
    # print(samples[0].chrome_system_cpu_usage)
    # print(len(samples[0].chrome_system_cpu_usage))


    plot1(samples)
    plot2(samples)
    plot3(samples)
    plot4(samples)
    plot5(samples)
    plot6(samples)

if __name__ == '__main__':
    main()

