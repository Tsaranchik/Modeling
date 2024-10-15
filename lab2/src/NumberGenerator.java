import java.util.Random;

public class NumberGenerator {
    public static final double P = 0.9;
    public static final int MAX = 114;
    public static final int TESTS = 100;

    public NumberGenerator() {}

    public static int[] generateSeries() {
        int[] series = new int[MAX];
        for (int i = 0; i < MAX; ++i) {
            int counter = 0;

            for (int j = 0; j < TESTS; ++j) {
                double num = Math.random();
                if (num < P) {
                    ++counter;
                }
            }

            series[i] = counter;
        }
        return series;
    }
}
