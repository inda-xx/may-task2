```java
import java.util.Random;

public class WhackAMole {
    int score, molesLeft;
    char[][] moleGrid;

    public WhackAMole() {
        moleGrid = new char[5][5];
        score = 0;
        molesLeft = 3;
        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++) {
                moleGrid[i][j] = '*';
            }
        }
    }

    public void place() {
        Random rand = new Random();
        int x = rand.nextInt(5);
        int y = rand.nextInt(5);
        moleGrid[x][y] = 'M';
    }

    public void whack(int x, int y) {
        if(moleGrid[x][y] == 'M') {
            moleGrid[x][y] = 'W';
            score++;
            molesLeft--;
        }
    }

    public void printGrid() {
        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++) {
                if(moleGrid[i][j] == 'M') {
                    System.out.print('*');
                } else {
                    System.out.print(moleGrid[i][j]);
                }
            }
            System.out.println();
        }
    }

    public void printGridToUser() {
        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++) {
                System.out.print(moleGrid[i][j]);
            }
            System.out.println();
        }
    }
}
```