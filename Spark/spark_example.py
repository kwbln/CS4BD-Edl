from pyspark import SparkContext, SparkConf


if __name__ == '__main__':

    conf = SparkConf().setAppName("create").setMaster("spark://172.17.0.2:4040")
    sc = SparkContext(conf=conf)

    inputStrings = ["Stefan 52", "Patrick 41", "Felix 43"]
    regularRDDs = sc.parallelize(inputStrings)

    pairRDDs = regularRDDs.map(lambda s: (s.split(" ")[0], s.split(" ")[1]))
    pairRDDs.coalesce(1).saveAsTextFile("out/RegularRDD2pairRDD")
