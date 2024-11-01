package org.echoes_of_eden.Simulation.Game.Building.Workplace;

public class AnimalFarm extends Workplace {    
    // keep track of all the animals
    
    public AnimalFarm() {
        this.stoneRequired = 10;
        this.woodRequired = 10;
        this.ironRequired = 10;

        this.stoneDelivered = 0;
        this.woodDelivered = 0;
        this.ironDelivered = 0;

        this.numberOfWorkers = 0;
        this.maxWorkers = 100;

        this.isUsable = false;
    }

    public void disaster() {
        // implement disaster
    }
}