import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        int number = year - 2002;
        float proc_izi = 0;
        final double[] nacho_sum = Constants.MOEX_RATE;
        final double[] INFLATION = Constants.INFLATION_RATE;

        if (year >= 2002 && year < 2022) {
            while (true) {
                double intialCapital = nacho_sum[number];
                proc_izi += 0.5;
                double cash = nacho_sum[number] * proc_izi * 0.01;
                for (int y = 0; y < 2022 - year; y++) {
                    intialCapital -= cash;
                    intialCapital = intialCapital * (nacho_sum[number + y + 1] / nacho_sum[number + y]);
                    cash = cash * (100 + INFLATION[number + y]) / 100;
                }
                if (intialCapital < 0) {
                    System.out.println(proc_izi - 0.5);
                    break;
                }
                if (proc_izi > 100) {
                    System.out.println(proc_izi);
                    break;

                }
            }

        } else {
            System.out.println("throws Exception…");

        }

    }

}

