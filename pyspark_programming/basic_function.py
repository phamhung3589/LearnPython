from pyspark import SparkContext, SparkConf
import os

os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\\Users\hungph8\AppData\Local\Continuum\\anaconda3\python.exe"
os.environ["PYSPARK_PYTHON"] = "C:\\Users\hungph8\AppData\Local\Continuum\\anaconda3\python.exe"

def read_file():
    lines = sc.textFile("data/ambari_tutorial.txt")
    line_filter = lines.filter(lambda line: "sudo" in line)
    print(line_filter.collect())

def key_value():
    arr = sc.parallelize([("panda", 0), ("pink", 3), ("pirate", 3), ("panda", 1), ("pink", 4)])
    arr = arr.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
    print(arr.collect())

if __name__ == "__main__":
    conf = SparkConf().setAppName("testing function").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")

    # read_file()

    key_value()