//import javax.swing.*;
//import java.awt.*;
//import java.util.Arrays;
//
//public class HistogramPanel extends JPanel {
//    private int[] series;
//
//    public HistogramPanel(int[] series) {
//        this.series = series;
//    }
//
//    @Override
//    protected void paintComponent(Graphics g) {
//        super.paintComponent(g);
//        if (series == null || series.length == 0) return;
//
//        int maxSuccesses = Arrays.stream(series).max().orElse(0);
//        int[] frequency = new int[maxSuccesses + 1];
//
//        for (int success : series) {
//            ++frequency[success];
//        }
//
//        int width = getWidth();
//        int height = getHeight();
//        int barWidth = width / frequency.length;
//
//        for (int i = 0; i < frequency.length; ++i) {
//            int barHeight = (int) ((double) frequency[i] / Arrays.stream(frequency).max().orElse(1) * height);
//            g.fillRect(i * barWidth, height - barHeight, barWidth - 1, barHeight);
//        }
//
//        g.drawLine(10, height, width, height);
//        g.drawLine(10,-100,10,height);
//    }
//}
