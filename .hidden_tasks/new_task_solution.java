```java
class Indamon {
    // copy your previous class and modify

    public int attackOponnent(Indamon target) {
        // method to deal damage and returns the battle result
        int damage = attack / target.getDefense();
        target.setHp(target.getHp() - damage);
        if (target.getHp() <= 0) {
            target.setFainted(true);
            target.setHp(100); // revive the Indamon for the next round
            return 1; // the enemy lost
        }
        return 0; // the enemy did not lose
    }
}

class Game {
    // attributes
    private Indamon player1;
    private Indamon player2;
    private int player1Score;
    private int player2Score;

    public Game(Indamon player1, Indamon player2) {
        this.player1 = player1;
        this.player2 = player2;
        this.player1Score = 0;
        this.player2Score = 0;
    }

    public void playRound() {
        player1Score += player1.attack(player2);
        player2Score += player2.attack(player1);
    }

    public int getPlayer1Score() {
        return player1Score;
    }

    public int getPlayer2Score() {
        return player2Score;
    }
}
```