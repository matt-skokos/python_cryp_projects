package youttube_tutorials;


public class VigenereArrayList {
    public static void main(String[] args) {
        int rows = 26;
        int cols = 26;
        int[][] vigList = new int[rows][cols];

        for (int i = 0; i < rows; i++){
            for (int k = 0; k < cols; k++ ) {
                vigList[i][k] = i + k;
            }
        }
        
        for (int i = 0; i < 26; i++){
            for (int k = 0; k < 26; k++) {
                int x = (vigList[i][k]) % 26;

                System.out.print((char)(x + 65) + "    ");
            }
            System.out.println();
    }
    }
}
