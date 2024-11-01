package main.java.org.echoes_of_eden.buildings.workplace;

public class Tavern extends Workplace {        
    public Tavern() {
        this.stoneRequired = 10;
        this.woodRequired = 10;
        this.ironRequired = 10;

        this.stoneDelivered = 0;
        this.woodDelivered = 0;
        this.ironDelivered = 0;

        this.numberOfWorkers = 0;
        this.maxWorkers = 2;

        this.isUsable = false;
    }

    public void disaster() {
        // implement disaster
    }
}