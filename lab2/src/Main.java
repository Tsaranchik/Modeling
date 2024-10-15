import java.io.*;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.util.Arrays;

public class Main {

    private static void runPyFile() throws InterruptedException {
        try {
            ProcessBuilder pb = new ProcessBuilder("python3", "chart.py");
            pb.inheritIO();

            Process process = pb.start();
            process.waitFor();


            File[] plots = {new File("uniformity_check.png"), new File("F(x).png"),
            new File("f(x).png"), new File("p(x).png")};

            for (File plot : plots) {
                if (plot.exists()) {
                    java.awt.Desktop.getDesktop().open(plot);
                }
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();

        } 
    }

    private static void printData() {
        int[] series = NumberGenerator.generateSeries();
        System.out.println(Arrays.toString(series));

        double mean = Statistics.mean(series);
        System.out.println(mean);
        double var = Statistics.var(series);
        System.out.println(var);
        double std = Statistics.std(series);
        System.out.println(std);
    }

    private static void writeDataToTxt(int[] series) {
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

    public static void main(String[] args) throws InterruptedException {
        printData();
        writeDataToTxt(NumberGenerator.generateSeries());
        runPyFile();
    }
}
