import java.io.*;
import java.lang.reflect.Array;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] series = NumberGenerator.generateSeries();
        System.out.println(Arrays.toString(series));

        double mean = Statistics.mean(series);
        System.out.println(mean);
        double var = Statistics.var(series);
        System.out.println(var);
        double std = Statistics.std(series);
        System.out.println(std);

        double[] means = Statistics.meanForEachSeries(series);

        int[] frequency = new int[100];

        for (int success : series) {
            ++frequency[success];
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("data.txt"))) {
            writer.write("N: " + NumberGenerator.TESTS);
            writer.newLine();
            writer.write("Probability: " + NumberGenerator.P);
            writer.newLine();

            writer.write("Theoretical mean: " + Statistics.THEORETICAL_MEAN);
            writer.newLine();

            writer.write("Means: " + Arrays.toString(means));
            writer.newLine();

            writer.write("Frequency: " + Arrays.toString(frequency));
            writer.newLine();
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
