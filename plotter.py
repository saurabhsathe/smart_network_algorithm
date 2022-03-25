import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def plot_bar_chunksize():
    import matplotlib.pyplot as plt
    df=pd.read_csv("chunk_throughput_update.csv")
    print(df.head())
    chunkbar1=df["Chunksize"]
    chunkbar2=df["chunksize_zip"]
    throughputbar1=df["Throughput"]
    throughputbar2=df["Throughput_zip"]
    X = np.arange(4)
    fig = plt.subplots(figsize =(12, 8))


    plt.bar(X + 0.00, chunkbar1, color = 'b', width = 0.25,label="Unzipped")
    plt.bar(X + 0.25, chunkbar2, color = 'g', width = 0.25,label="Zipped ")

    """
    data = [[30, 25, 50, 20],
            [40, 23, 51, 17],
            [35, 22, 45, 19]]
    X = np.arange(4)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
    
    """

    plt.xlabel("Threads")
    plt.ylabel("chunksize")
    plt.legend()
    plt.savefig('unzipped_vs_zipped_data_comparison.png')
    plt.show()

def plot_bar_throughput():
    import matplotlib.pyplot as plt
    df=pd.read_csv("chunk_throughput_update.csv")
    print(df.head())
    #chunkbar1=df["Chunksize"]
    #chunkbar2=df["chunksize_zip"]
    throughputbar1=df["Throughput"]
    throughputbar2=df["Throughput_zip"]
    X = np.arange(4)
    fig = plt.subplots(figsize =(12, 8))


    plt.bar(X + 0.00, throughputbar1, color = 'r', width = 0.25,label="Unzipped")
    plt.bar(X + 0.25, throughputbar2, color = 'b', width = 0.25,label="Zipped ")

    """
    data = [[30, 25, 50, 20],
            [40, 23, 51, 17],
            [35, 22, 45, 19]]
    X = np.arange(4)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
    
    """

    plt.xlabel("Threads")
    plt.ylabel("throughput")
    plt.legend()
    plt.savefig('unzipped_vs_zipped_throughput_comparison.png')
    plt.show()

def plot_thread_comparison():
    df=pd.read_csv("thread1.csv")
    print(df.iloc[:,[1]])
    for i in range(1,5):
        df=pd.read_csv("thread{}.csv".format(i))
        x=df.iloc[:,[1]]
        y=df.iloc[:,[2]]
        plt.plot(x,y,label="with {} thread".format(i))
    plt.xlabel("chunksize")
    plt.ylabel("throughput observed")
    plt.legend()
    plt.savefig('threadpool_comparison2.png')
    plt.show()


def plot_time_chunksize():
    df=pd.read_csv("time_series_packetsize.csv")
    plt.plot(df.iloc[:,[0]],df.iloc[:,[1]])
    plt.xlabel("time")
    plt.ylabel("chunksize")
    plt.legend()
    plt.savefig('time_series_chunksize.png')
    plt.show()

if __name__=='__main__':
    plot_time_chunksize()



