import java.util.HashMap;

public class Statistics {
    public static final double THEORETICAL_MEAN = 0.9;
    public static final double THEORETICAL_VAR = 9.0;
    public static final double THEORETICAL_STD = 3.0;

    public Statistics() {
    }

    public static double mean(int[] arr) {
        double mean = 0;
        for (int elem : arr) {
            mean += elem;
        }
        return mean / NumberGenerator.MAX;
    }

    public static double[] meanForEachSeries(int[] arr) {
        double[] means = new double[NumberGenerator.MAX];
        for (int i = 0; i < NumberGenerator.MAX; ++i) {
            means[i] = (double) arr[i] / 100;
        }
        return means;
    }

    public static double var(int[] arr) {
        double var = 0;
        double mean = Statistics.mean(arr);
        for (int elem: arr) {
            var += Math.pow(elem - mean, 2);
        }
        return var / (NumberGenerator.MAX - 1);
    }

    public static double std(int[] arr) {
        double var = var(arr);
        return Math.sqrt(var);
    }
}
