package org.echoes_of_eden.Simulation.Game.Building.Workplace;

public class Cemetery extends Workplace {
    protected int emptyGraves;
    protected int filledGraves;
    
    public Cemetery() {
        this.stoneRequired = 10;
        this.woodRequired = 10;
        this.ironRequired = 10;

        this.stoneDelivered = 0;
        this.woodDelivered = 0;
        this.ironDelivered = 0;

        this.emptyGraves = 100;
        this.filledGraves = 0;

        this.numberOfWorkers = 0;
        this.maxWorkers = 10;

        this.isUsable = false;
    }

    @Override
    public void disaster() {
        // implement disaster
    }
}
